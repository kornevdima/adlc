---
type: meta
title: "Questions Index"
created: 2026-10-22
updated: 2026-10-22
tags:
  - meta
  - index
  - question
status: evergreen
related:
  - "[[index]]"
  - "[[questions/_changelog]]"
---

# Questions Index

Navigation: [[index]] | [[concepts/_index|Concepts]] | [[entities/_index|Entities]] | [[sources/_index|Sources]] | [[questions/_changelog|Changelog]]

Filed answers and the pages behind plugin fixes: each one opened from a question, a field finding or an upstream report, and closed by a release. Changes to these pages are recorded in [[questions/_changelog]].

---

## Open

- [[Integrate the wiki toolset into the ADLC workers]] — workers write into a vault they have no toolset for; three reinvention instances measured in one session (status: open)
- [[Operator profile - learn engagement style from corrections]] — `project-profile` covers the codebase, nothing covers the human running it; business-input vs fully-managed as the axis (status: open — smallest useful version shipped 2026-09-03, see its resolution log)
- [[Configurable subagent models per host]] — a hardcoded `model: sonnet` broke worker dispatch in a Copilot org without Claude models; design: no model in agents, `adlc:setup` writes per-host tiers to a user file, dispatchers pass `model` (status: postponed — low priority, operator 2026-10-02)
- [[Plugin eval suites for claude plugin eval]] — ruling 4: local evals before each version bump; 22 skill cases converted to `evals/` with fixtures (fast set green); graphify, pm-layer and new `adlc` / worker cases left (status: open)

## Resolved

- [[One writing method for every human reader]] — vault-b/UP-001 to UP-005 and vault-c/UP-001: client packs that read as note dumps, drifting translations, dashes rewritten instead of swapped, corrections applied to one line, links that missed the deployed page. Fix: `writing-style.md` for every writer (identifiers never alone, change reports that read without the board), the `technical-writer` skill in place of `client-docs`, the `/adlc` and `wrap-up` reports reshaped. Unreleased (status: resolved 2026-10-20)
- [[Workers print secrets from env files]] — vault-a/UP-013: a `docker compose config` and a `sed` over `.env.local` put a dev private key into transcripts despite a packet rule. Fix: a worker Don't, `permissions.md` deny rules, and the `guard_env.py` PreToolUse hook that blocks env-file reads by any tool. Unreleased (status: resolved 2026-10-20)
- [[Contracts that prescribe mechanisms or skip the code]] — vault-a/UP-014, UP-017, UP-018 and vault-d/UP-003: packets that prescribe a mechanism, scenarios naming states and labels nobody checked, a moved source with unlisted readers, a grilling ruling with no row. Fix: four contract rules in `/adlc` Step 2.2, census items 7 and 8, reviewer dimension 8. Unreleased (status: resolved 2026-10-20)
- [[Hand-backs without the gates that cover the change]] — vault-a/UP-015 and UP-016: workers reported green without lint, typecheck, unit or the e2e that covered their change; a one-minute defect surfaced in a fifteen-minute verify. Fix: covering gates with no-pipe exit codes in builder and tester, `/adlc` § Accepting a hand-back, and the dispatcher's cheap gates before every verify. Unreleased (status: resolved 2026-10-20)
- [[Workers write to logs the dispatcher owns]] — vault-a/UP-021: a reviewer created `log.md` in a code wiki that keeps none, a verifier wrote the product log. Fix: workers write their record and report its path; the dispatcher logs it. Unreleased (status: resolved 2026-10-20)
- [[Pages carry their history inline]] — vault-e/UP-002: dated update and correction blocks, as-filed markers and "was X, now Y" wording inside pages; the plugin's own wrap-up told agents to write them. Fix: `writing-style.md` § Pages that stay current, per-folder `_changelog.md` from the scaffold, wrap-up and every page-writing skill and worker rewritten, `page_history_check.py` in lint. Unreleased (status: resolved 2026-10-21)
- [[Identifiers with no glossary]] — vault-e/UP-003: hundreds of register ids with no page to explain them. Fix: `wiki/glossary.md` per vault, `glossary.py build` from a Registers table in the page and `link --apply` for first mentions, template in `references/glossary.md`, lint check 8d. Unreleased (status: resolved 2026-10-21)
- [[Env-guard hook path is relative to the working directory]] — vault-e/UP-001: the cwd-relative hook command blocked every tool once the session's directory moved. Fix: `$CLAUDE_PROJECT_DIR` in an `if … fi` that fails open on a missing file, in the template and the docstring. Unreleased (status: resolved 2026-10-21)
- [[Workers and processes left running after hand-back]] — vault-a/UP-006 and UP-012: workers stay listed as live after handing back, and stray servers hold the e2e port. Fix: a "leave nothing running" rule in every Bash worker, a dispatcher check after each hand-back, and `wrap-up` step 7c. Follow-up vault-d/UP-001 and the shared-environment rules (no long-lived service as a background child, never recreate a container you didn't start). Unreleased (status: resolved 2026-10-17)
- [[Verification instruments that miss what they measure]] — vault-a/UP-007 to UP-009: UI measurement traps, dev-server connection failures read as code failures, wrapper scripts that drop runner flags. Fix: tester and verifier rules, plus `/adlc` Step 2.2. Unreleased (status: resolved 2026-10-17)
- [[Upstream channel from vaults to the plugin]] — lessons about the plugin had no route out of a vault (gap C, "tell the operator", was a conversation). Now `wiki/meta/adlc-upstream.md` per vault: entries are exported by `/adlc upstream` (a GitHub issue, or a manual hand-off) and closed by `upstream-shipped.md`. Vault-a seeded with UP-001 to UP-004. Unreleased (status: resolved 2026-10-04)
- [[Tester edits app code to prove a test bites]] — vault-a EPIC-002, seen 2× (US-175, US-179): the tester edited app code and reverted it, which neither the reviewer nor the verifier can see. Fix: the dispatcher's build snapshot (`refs/adlc/<story>/build-<n>`) plus a tester footprint check (`build_snapshot.py`); the tester never edits app code, not even temporarily. Follow-up UP-005 (1.0.8): code-wiki records are exempt from the footprint. Unreleased (status: resolved 2026-10-04)
- [[Dispatcher rules for writing ruling questions]] — two dispatcher lessons from vault-a's profile: cite the record (5×), outcome first (2×). Shipped as `/adlc` Step 2 § Writing a ruling question, with pointers from grilling, distill and `scope-analyst`, plus two `evals/adlc/` cases (they pass, and so does the no-plugin baseline). Follow-ups UP-010, UP-019 and UP-020 (1.0.8): § Claiming a cause or a fix, a bug page only after the cause is read, the run's state read from the ledgers after a resume or rewind. Unreleased (status: resolved 2026-10-04)
- [[Review the ADLC flow against the AI-Native SDLC Playbook]] — stage-by-stage review of `/adlc` against Anthropic's playbook; 8 rulings: 6 adopted, deploy as an optional `devops` worker, time metrics deferred (status: closed 2026-10-02)
- [[Wiki maintenance edits blocked in ADLC vaults]] — the epic close deletes the run ledger but leaves 20+ dead `[[_run …]]` links, and the permissions profile has no path for bulk wiki rewrites (auto mode denied a `sed -i` relink). Fix: relink at the epic close, a scripted relink tool to allow-list, auto-mode guidance, and `Write(path)` rules corrected to `Edit(path)` (status: resolved 2026-10-02 — field test pending)
- [[Parallel builder and tester revert each other's edits]] — the dispatcher ran builder and tester at once; the tester restored a pre-run copy of a source file and silently undid the builder's edit. Fixed only in one service's local workers. Fix: sequential dispatch on overlapping files, undo-own-edit + `git diff` restore in the generic workers, an upstream route in distill (status: resolved 2026-10-02)

## Architecture

How the plugin is built, as-built at 1.0.9. Full catalog: [[architecture/_index]].

- [[Plugin architecture overview]] — one folder as plugin, vault and repo; the six layers and the path a request takes through them (status: active)
- [[Skills and routing]] — the 20 skills in three families, triggers, what each dispatches (status: active)
- [[Shared references]] — the 61 reference documents other skills and workers read; the BA and shift-left method libraries (status: active)
- [[Workers and the dispatch pipeline]] — the 15 subagents, the per-story pipeline, the rules every worker follows (status: active)
- [[Hooks and host adapters]] — manifests and hooks for Claude Code, Cursor, Copilot; the vault-side guard hooks (status: active)
- [[Scripts]] — the 15 Python scripts and the installer, who runs each (status: active)
- [[Evals]] — 25 plugin eval cases, fixtures, graders, what is not covered yet (status: active)
- [[Use cases and modes]] — the nine things the plugin is used for, lightest to heaviest (status: active)
- [[Release and upstream flow]] — from a vault's lesson to a question page, a fix, a version, a closed entry (status: active)
