#!/usr/bin/env python3
"""PreToolUse guard: no tool reads an env file or prints resolved config.

A prose rule in a dispatch packet did not stop workers from reading `.env*` files
(a `sed` over `web/.env.local`, a `docker compose config`) and their output, private
keys included, went into the transcript. This hook makes the rule mechanical. Hook it
into the vault's `.claude/settings.json` (see `skills/wiki/references/permissions.md`):

    "hooks": {"PreToolUse": [{"matcher": "Bash|Read|Edit|Write|NotebookEdit",
      "hooks": [{"type": "command", "command": "if [ -f \"$CLAUDE_PROJECT_DIR/.claude/hooks/guard_env.py\" ]; then python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/guard_env.py\"; else echo 'guard_env.py missing; env guard off' >&2; fi"}]}]}

The command is anchored on `$CLAUDE_PROJECT_DIR`, never on the working directory: a cwd-relative
path broke once the session moved into a subdirectory, Python exited 2 ("can't open file") and
every tool was blocked. The `if` keeps a block (exit 2) and lets a missing hook file pass with a
warning, since `if` returns the status of the last command it ran.

It blocks (exit 2, reason on stderr):
- Read / Edit / Write / NotebookEdit on a file named `.env` or `.env.<anything>`;
- a Bash command that names such a file;
- a Bash command that prints resolved config: `docker compose config`, `docker inspect`,
  a bare `env` / `printenv` / `set` / `export -p`.

It allows `.env.example`, `.env.sample`, `.env.template` and `.env.dist`: variable names
come from there, and a value's presence is checked with `test -n "$VAR"`.
Everything else passes (exit 0). It reads the hook payload from stdin and never prints
the command or the path it blocked in full: the reason names the rule, not the secret.

Prose is not a command. A commit message or PR body that names an env file or the
resolved-config command is text, not a read, so the Bash check skips it: the value of
`git -m` / `--message` and `gh -t` / `--title` / `-b` / `--body`, and the body of a quoted
heredoc (`<<'EOF'`) fed to `cat`, `tee`, `git` or `gh` on a line with no pipe or process
substitution. A value that holds `$(` or a backtick is checked anyway, since it runs. If the command does not split (unbalanced
quotes), the whole string is checked as before, so the hook fails closed.
"""
import json
import re
import shlex
import sys

ALLOWED_SUFFIX = re.compile(r"\.(example|sample|template|dist)$")
# `.env`, `.env.local`, `.env.development.local`, as a whole token or a path segment.
ENV_TOKEN = re.compile(r"""(?:^|[\s"'`=:/(])(\.env(?:\.[\w-]+)*)(?=$|[\s"'`;|&)<>])""")
RESOLVED_CONFIG = [
    re.compile(r"\bdocker\s+compose\b(?:\s+-\S+(?:\s+[^-\s]\S*)?)*\s+config\b"),
    re.compile(r"\bdocker(?:\s+container)?\s+inspect\b"),
    re.compile(r"(?:^|[;&|]\s*|\bsudo\s+)(?:printenv|env|set|export\s+-p)\s*(?=$|[;&|>])"),
]
# Options whose value is prose, per command.
MESSAGE_OPTS = {"git": {"-m", "--message"}, "gh": {"-t", "--title", "-b", "--body"}}
# Consumers that only print, write or store a literal heredoc body; never a shell.
HEREDOC_CONSUMERS = {"cat", "tee", "git", "gh"}
HEREDOC = re.compile(r"""<<(-?)[ \t]*(['"])([A-Za-z_][\w-]*)\2[^\n]*\n""")
SEPARATORS = {";", "&", "&&", "|", "||", "(", ")", "$", "$(", "\n"}


def env_file(name):
    base = name.rsplit("/", 1)[-1]
    if base != ".env" and not base.startswith(".env."):
        return False
    return not ALLOWED_SUFFIX.search(base)


def runs_code(value):
    return "$(" in value or "`" in value


def strip_heredocs(cmd):
    """Drop the bodies of quoted heredocs fed to a consumer that cannot execute them."""
    out, pos = [], 0
    for m in HEREDOC.finditer(cmd):
        if m.start() < pos:
            continue
        head = re.split(r"[;&|(\n]", cmd[pos:m.start()])[-1].split()
        consumer = head[0].rsplit("/", 1)[-1] if head else ""
        line = cmd[cmd.rfind("\n", 0, m.start()) + 1:m.end()]
        tabs = r"\t*" if m.group(1) else ""
        end = re.compile(rf"^{tabs}{re.escape(m.group(3))}[ \t]*$", re.M).search(cmd, m.end())
        # `cat <<'EOF' | bash` or `tee >(sh)` would run the body: check it.
        if consumer not in HEREDOC_CONSUMERS or not end or re.search(r"\||[<>]\(", line):
            continue
        out.append(cmd[pos:m.end()])
        pos = end.start()
    out.append(cmd[pos:])
    return "".join(out)


def command_text(cmd):
    """The command without its prose: message option values and literal heredoc bodies."""
    lex = shlex.shlex(strip_heredocs(cmd), posix=True, punctuation_chars=True)
    lex.whitespace_split = True
    lex.commenters = ""
    kept, head, skip = [], None, False
    for tok in lex:
        if skip:
            skip = False
            if not runs_code(tok):
                continue
        elif tok in SEPARATORS:
            head = None
        elif head is None:
            if not re.match(r"^\w+=", tok):
                head = tok.rsplit("/", 1)[-1]
        else:
            opts = MESSAGE_OPTS.get(head, ())
            name, eq, value = tok.partition("=")
            if eq and name in opts and name.startswith("--"):
                if not runs_code(value):
                    kept.append(name)
                    continue
            elif tok in opts or (head == "git" and re.fullmatch(r"-[a-zA-Z]+m", tok)):
                skip = True
        kept.append(tok)
    return " ".join(kept)


def main():
    try:
        data = json.load(sys.stdin)
    except (ValueError, OSError):
        return 0
    tool = data.get("tool_name", "")
    inp = data.get("tool_input") or {}
    if tool in ("Read", "Edit", "Write", "NotebookEdit"):
        path = inp.get("file_path") or inp.get("notebook_path") or inp.get("path") or ""
        if env_file(path):
            print(f"guard_env: {tool} of an env file is blocked. Take variable names from "
                  "`.env.example` or the compose file; check presence with `test -n \"$VAR\"`.",
                  file=sys.stderr)
            return 2
        return 0
    if tool == "Bash":
        cmd = inp.get("command", "") or ""
        try:
            cmd = command_text(cmd)
        except ValueError:
            pass
        for m in ENV_TOKEN.finditer(cmd):
            if env_file(m.group(1)):
                print("guard_env: this command names an env file. Never read `.env*` with any tool; "
                      "take variable names from `.env.example` or the compose file and check "
                      "presence with `test -n \"$VAR\"`.", file=sys.stderr)
                return 2
        for pat in RESOLVED_CONFIG:
            if pat.search(cmd):
                print("guard_env: this command prints resolved config (secrets included). "
                      "Read the compose file or `.env.example` for names; never the values.",
                      file=sys.stderr)
                return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
