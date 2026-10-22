---
type: synthesis
title: "Env guard blocks commands that only mention env files"
created: 2026-10-22
updated: 2026-10-22
tags:
  - adlc
  - permissions
  - hooks
  - upstream
status: resolved
upstream: [vault-a/UP-024]
related:
  - "[[Workers print secrets from env files]]"
  - "[[Env-guard hook path is relative to the working directory]]"
  - "[[Upstream channel from vaults to the plugin]]"
---

# Env guard blocks commands that only mention env files

**Opened from** the report in `.raw/upstream/` (hand-delivered 2026-10-22). Kind: bug, seen twice in one session.

**Outcome:** a commit message, PR title or PR body may name an env file or the resolved-config command; the hook still blocks every real read and every real print of resolved config.

## What happened

The env guard (`guard_env.py`, the PreToolUse hook from [[Workers print secrets from env files]]) matched its patterns anywhere in a Bash command, quoted text included. Two routine commits in one session were refused: the first message named an env file as a word in a sentence, the retry named the compose command that prints resolved config. Nothing was read or printed. The same applied to issue bodies, PR titles and `echo`.

## Resolution (2026-10-22, shipped in 1.0.9)

- **`guard_env.py`** splits the command with `shlex` before matching and leaves out the prose: the value of `git -m` / `--message` (also the `-am` cluster and `--message=`), the value of `gh -t` / `--title` / `-b` / `--body`, and the body of a quoted heredoc (`<<'EOF'`) fed to `cat`, `tee`, `git` or `gh`. Everything else in the command is checked as before, including what follows the message (`git commit -m "…" && cat .env` blocks).
- **Two holes the report's proposal left open are closed.** A skipped value that holds `$(` or a backtick runs, so it is checked (`git commit -m "$(cat .env)"` blocks). A heredoc body is skipped only when the line has no pipe and no process substitution, and only for the four consumers above, so `bash <<'EOF'` and `cat <<'EOF' | sh` still block. An unquoted heredoc can expand, so its body is always checked.
- **Fails closed:** when `shlex` cannot split the command (unbalanced quotes), the whole string is checked as before.
- **`test_guard_env.py`** beside the hook: 11 payload groups. Blocks: `cat` / `sed` / `grep` / `bash -c` on env files, Read and Edit on env files, the resolved-config commands, command substitution inside a message, a message followed by a real read, heredocs fed to a shell, unbalanced quotes. Passes: the two reported commit messages, the standard `git commit -m "$(cat <<'EOF' … EOF)"` form, `gh pr create --title/--body`, `gh issue create --body-file -` with a heredoc, a heredoc written to a file, `.env.example`. All green.
- Not covered: `echo` arguments (the report names them but proposes no fix; an unquoted `echo $(cat .env)` cannot be told from prose after splitting), and a message option on a later line of a multi-line command whose first command is not `git` or `gh` (it is still checked, so the failure is a false block, not a leak). The workaround stays `git commit -F <file>`.

## Open

- Vault-side after 1.0.9: the vault flips its `sent` entry to `shipped (1.0.9)`. Vaults pick up the new hook by copying `guard_env.py` into `.claude/hooks/` again; the settings entry does not change.
