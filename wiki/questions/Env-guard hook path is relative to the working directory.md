---
type: synthesis
title: "Env-guard hook path is relative to the working directory"
created: 2026-10-21
updated: 2026-10-21
tags:
  - adlc
  - permissions
  - hooks
  - upstream
status: resolved
upstream: [vault-e/UP-001]
related:
  - "[[Workers print secrets from env files]]"
  - "[[Upstream channel from vaults to the plugin]]"
---

# Env-guard hook path is relative to the working directory

**Opened from** the report in `.raw/upstream/` (hand-delivered 2026-10-21). Kind: bug, one occurrence is enough.

**Outcome:** the env-guard hook runs wherever the session's working directory is, and a missing hook file degrades to a warning instead of blocking every tool.

## What happened

The 1.0.8 settings template wired the PreToolUse hook as `python3 .claude/hooks/guard_env.py`. In the session that upgraded a vault to 1.0.8, the working directory moved into a subdirectory of the vault; Python could not find the file and exited 2, which Claude Code reads as "block". Every Bash, Read, Edit and Write call was refused, including the edit that would have fixed the settings. The operator fixed `.claude/settings.json` by hand, using `$CLAUDE_PROJECT_DIR`.

## Resolution (2026-10-21, unreleased)

- **`permissions.md`** template, both hook entries: `if [ -f "$CLAUDE_PROJECT_DIR/.claude/hooks/guard_env.py" ]; then python3 "$CLAUDE_PROJECT_DIR/.claude/hooks/guard_env.py"; else echo 'guard_env.py missing; env guard off' >&2; fi`. The `if` returns the status of the last command it ran, so a real block (exit 2 from the hook) still blocks and a missing file passes with a warning; the hook payload on stdin reaches Python unchanged. A note under the template says why.
- **`guard_env.py`** docstring shows the same command; the **`wiki`** skill's scaffold step 8 says the entry is anchored on `$CLAUDE_PROJECT_DIR`, never a cwd-relative path.
- Checked with the hook in a scratch project directory: a read of `.env.local` through the new command exits 2 with the rule on stderr; with the hook file removed, exit 0 and the warning; a read of `.env.example` exits 0.

## Open

- Vault-side after 1.0.9: vaults that already use the bare `$CLAUDE_PROJECT_DIR` form keep working; the `if … fi` form is the template's, taken at the next settings refresh.
