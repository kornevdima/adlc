# vault-e/UP-001 Env-guard hook command is relative to the working directory and blocks every tool

- **Kind:** bug
- **Plugin version:** 1.0.8
- **Target:** `skills/wiki/references/permissions.md` § Template (the `hooks` block); `skills/wiki/SKILL.md` step 8; the `guard_env.py` docstring

## What happened

The settings template wires the PreToolUse env-guard hook as `python3 .claude/hooks/guard_env.py`,
a path relative to the session's working directory. After the session's working directory moved
into a subdirectory of the vault, Python could not find the file and exited with code 2. Claude
Code reads exit code 2 from a PreToolUse hook as "block", so every Bash, Read, Edit and Write call
was refused, including the edit that would have fixed the settings. The operator had to fix the
project's `.claude/settings.json` by hand.

Seen once, on 2026-10-20, in the session that upgraded a vault to 1.0.8. As a plugin bug, one
occurrence is enough.

## Proposed fix

1. Use an absolute path in the template and the docstring:
   `python3 "$CLAUDE_PROJECT_DIR"/.claude/hooks/guard_env.py`.
2. A missing hook file should fail open with a warning rather than block. That needs a small
   wrapper, because Python's own "can't open file" exit code is also 2.

## Workaround in use

The vault's `.claude/settings.json` already uses the `$CLAUDE_PROJECT_DIR` form.
