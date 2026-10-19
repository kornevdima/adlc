#!/usr/bin/env python3
"""PreToolUse guard: no tool reads an env file or prints resolved config.

A prose rule in a dispatch packet did not stop workers from reading `.env*` files
(a `sed` over `web/.env.local`, a `docker compose config`) and their output, private
keys included, went into the transcript. This hook makes the rule mechanical. Hook it
into the vault's `.claude/settings.json` (see `skills/wiki/references/permissions.md`):

    "hooks": {"PreToolUse": [{"matcher": "Bash|Read|Edit|Write|NotebookEdit",
      "hooks": [{"type": "command", "command": "python3 .claude/hooks/guard_env.py"}]}]}

It blocks (exit 2, reason on stderr):
- Read / Edit / Write / NotebookEdit on a file named `.env` or `.env.<anything>`;
- a Bash command that names such a file;
- a Bash command that prints resolved config: `docker compose config`, `docker inspect`,
  a bare `env` / `printenv` / `set` / `export -p`.

It allows `.env.example`, `.env.sample`, `.env.template` and `.env.dist`: variable names
come from there, and a value's presence is checked with `test -n "$VAR"`.
Everything else passes (exit 0). It reads the hook payload from stdin and never prints
the command or the path it blocked in full: the reason names the rule, not the secret.
"""
import json
import re
import sys

ALLOWED_SUFFIX = re.compile(r"\.(example|sample|template|dist)$")
# `.env`, `.env.local`, `.env.development.local`, as a whole token or a path segment.
ENV_TOKEN = re.compile(r"""(?:^|[\s"'`=:/(])(\.env(?:\.[\w-]+)*)(?=$|[\s"'`;|&)<>])""")
RESOLVED_CONFIG = [
    re.compile(r"\bdocker\s+compose\b(?:\s+-\S+(?:\s+[^-\s]\S*)?)*\s+config\b"),
    re.compile(r"\bdocker(?:\s+container)?\s+inspect\b"),
    re.compile(r"(?:^|[;&|]\s*|\bsudo\s+)(?:printenv|env|set|export\s+-p)\s*(?=$|[;&|>])"),
]


def env_file(name):
    base = name.rsplit("/", 1)[-1]
    if base != ".env" and not base.startswith(".env."):
        return False
    return not ALLOWED_SUFFIX.search(base)


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
