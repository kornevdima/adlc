---
type: meta
title: "Hot Cache"
updated: 2026-10-20T01:30:00
tags:
  - meta
  - hot-cache
status: evergreen
related:
  - "[[index]]"
  - "[[log]]"
  - "[[Upstream channel from vaults to the plugin]]"
  - "[[Workers print secrets from env files]]"
  - "[[Contracts that prescribe mechanisms or skip the code]]"
  - "[[Hand-backs without the gates that cover the change]]"
  - "[[Workers write to logs the dispatcher owns]]"
---

# Recent Context

Navigation: [[index]] | [[log]]

## Last Updated

**2026-10-20 (session: release 1.0.8)**. Committed as `chore(plugin): 1.0.8`. Nineteen reports fixed on top of the 2026-10-17 batch, all listed under 1.0.8 in `upstream-shipped.md`:
- [[One writing method for every human reader]] (vault-b/UP-001 to UP-005, vault-c/UP-001): new `skills/wiki/references/writing-style.md`, the `technical-writer` skill in place of the `client-docs` draft, the `/adlc` and `wrap-up` reports reshaped, § Writing in the vault AGENTS.md template, the operator profile and this repo's AGENTS.md. Replies to the operator follow it: an identifier never alone, plain words first.
- [[Workers print secrets from env files]] (UP-013): worker Don'ts, deny rules, and the new `skills/wiki/scripts/guard_env.py` PreToolUse hook (blocks env-file reads by any tool; `.env.example` stays readable). The ADLC scaffold copies it to `.claude/hooks/`.
- [[Contracts that prescribe mechanisms or skip the code]] (UP-014, UP-017, UP-018, vault-d/UP-003): `/adlc` Step 2.2 is a rule list now; census items 7 and 8; reviewer dimension 8.
- [[Hand-backs without the gates that cover the change]] (UP-015, UP-016): covering gates with no-pipe exit codes; `/adlc` § Accepting a hand-back; Step 2.6 cheap gates before the verify.
- [[Workers write to logs the dispatcher owns]] (UP-021): workers never write `log.md`, `hot.md` or the board.
- Joined existing pages: UP-019 and UP-020 (ruling questions), vault-d/UP-001 and the shared-environment rules (left running), vault-d/UP-002 (footprint), the UP-007 recurrence (instruments).

## Key Recent Facts

- **Read both co-located vaults' `wiki/meta/adlc-upstream.md`**, not only `.raw/upstream/`: this batch had no export files at all. vault-a is at UP-021, vault-d at UP-003.
- vault-a/UP-011 (visual review at sprint close) is declined by the operator; leave it.
- Two vaults chose the key `vault-b`. The one with five reports in `.raw/upstream/` keeps it; the other is `vault-c` in the plugin and should re-key.
- The third co-located vault's ledger uses its directory name as the key (ledger created 2026-10-10, before the opaque-key template). The plugin lists it as `vault-d`; the vault should re-key. Never copy a vault's key verbatim when it is not opaque: alias it, and note the alias on its first shipped row.
- **Upstream pages carry no pointers into a vault's private repo:** no story, epic, sprint, bug or test-case ids, no ledger page names or line numbers, no commit hashes, no source paths or symbols, no product nouns. Say "a later story", "the run ledger", "a database filter". Audited and cleaned 2026-10-20; the two vault-b raw reports still name the client's form kinds (operator's call).
- **Run `skills/wiki/scripts/upstream_redact_check.py` on every upstream page, log line and reference before a commit** (`--names "<vault dirs>"`, or `--vault <co-located vault>`; never `--vault .` in this repo). Vaults run it with `--vault .` at `/adlc upstream`; a non-opaque key stops the export. Built 2026-10-20, unreleased.
- The `guard_env.py` hook also blocks the main session (`cp .env.example .env` is the operator's step).
- `gh` can't reach GitHub from this machine. Auto-mode's Bash classifier failed transiently this session; reads went through the Read tool.
- `claude plugin eval` takes only the last `--case`; run cases one at a time.

## Active Threads

- **After 1.0.8 is installed in the vaults:** flip vault-a UP-013 to UP-021, vault-d UP-001 to UP-003 and the two writing-method vaults' entries from `proposed` or `sent` to `shipped (1.0.8)`, and remove the workarounds each page's Open section names (packet lines, local-binding bullets, the re-snapshot habit, the generic writing rules in the profile and AGENTS.md). Fast evals at the bump: 9 of 10, the callout case still failing.
- **Not addressed from the ledgers:** the public-repo records occurrence (vault-a, 2026-10-18: records with local paths committed to a public service repo; proposed `Records: public-repo` flag); the UP-002 "simplest shape first" gap; UP-011 (declined).
- **In vault-a:** copy the current worker files into `<service>/.claude/agents/`; add `guard_env.py` and its settings entry; field-test the footprint check with `--exempt`.
- **Evals backlog** ([[Plugin eval suites for claude plugin eval]]): the 12 slow cases; the `[!contradiction]` callout; graphify and pm-layer; `adlc` worker cases on `adlc-vault`.
- **Open tasks:** [[Integrate the wiki toolset into the ADLC workers]]; [[Operator profile - learn engagement style from corrections]].
- **Deferred:** vault MCP server; `/project-profile --refresh`; the Stage 6 trigger; K8; the Cursor plugin load check; the sharing pilot; the OKF exporter; renaming the repo.
