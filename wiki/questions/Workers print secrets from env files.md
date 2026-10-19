---
type: synthesis
title: "Workers print secrets from env files"
created: 2026-10-20
updated: 2026-10-20
tags:
  - adlc
  - workers
  - permissions
  - upstream
status: resolved
upstream: [vault-a/UP-013]
related:
  - "[[Workers and processes left running after hand-back]]"
  - "[[Upstream channel from vaults to the plugin]]"
---

# Workers print secrets from env files

**Opened from** vault-a's upstream log, entry UP-013 (proposed 2026-10-15; the operator asked for fixes on 2026-10-20). Kind: bug, a repeat.

**Outcome:** no tool a worker or the dispatcher runs can put an env file's values into a transcript.

## What happened (seen 2× in one day, plus one earlier form)

- A verifier ran `docker compose config`, which prints the resolved stack, and a dev private key for a third-party integration went into the transcript. No packet rule existed yet.
- A tester ran `sed` over `<service>/.env.local` and echoed fragments of the same key. The packet said "never print secrets or resolved config".
- Three days earlier (an occurrence row, 2026-10-17), a tester printed container env with `docker inspect`.

Each time the worker read the file to learn a variable's value or shape. A prose rule did not hold; the vault's workaround was to keep the packet rule and raise the key's rotation with the operator.

## Resolution (2026-10-20, unreleased)

- **Workers** (`feature-builder`, `feature-tester`, `feature-verifier`, `devops`, `scope-analyst`): a Don't. Never read `.env*` files or resolved config with any tool, not `Read`, `cat`, `sed`, `grep`, `awk`, `docker compose config` or `docker inspect`. Variable names come from the compose file or `.env.example`; presence is checked with `test -n "$VAR"` in a subshell that sources nothing.
- **`/adlc` Constraints:** the same rule, and § Accepting a hand-back: a transcript that printed a secret is reported to the operator at once (rotation is their call).
- **`permissions.md`:** `deny` rules for `Read` on `.env`, `.env.local` and `.env.*.local`, and for `docker compose config` and `docker inspect`. Bash prefix patterns cannot carve `.env.example` out of `.env*`, so the enforcement is a hook.
- **`skills/wiki/scripts/guard_env.py`:** a `PreToolUse` hook on `Bash|Read|Edit|Write|NotebookEdit`. It blocks any tool on a file named `.env` or `.env.<x>`, any Bash command that names one, and bare `env` / `printenv` / `set` / `export -p` / `docker compose config` (with options before `config`) / `docker inspect`. `.env.example`, `.sample`, `.template` and `.dist` stay readable. Exit 2 with the rule on stderr; it never echoes the blocked command or path. Stdlib only. Checked on 27 payloads (reads, edits, `sed`, `cat`, `cp .env.example .env`, compose with `-f` and `--profile`, `env FOO=1 cmd` allowed, `set -e` allowed, `config.environment.ts` allowed, a bad payload passes).
- The `wiki` skill's ADLC scaffold copies the script to `.claude/hooks/guard_env.py`, where the template's hook entry points.

## Open

- Vault-side after 1.0.8: copy the hook into each vault's `.claude/hooks/`, add the hook entry and the deny rules to `.claude/settings.json`, and drop the packet rule.
- The hook blocks the dispatcher too (a `cp .env.example .env` is the operator's step now). If that turns out to be a daily annoyance, scope the hook by `tool_input` for the main session; a worker's dispatch cannot be told apart from the main session in the hook payload today.
- The key's rotation is still the operator's call, raised twice in the vault.
