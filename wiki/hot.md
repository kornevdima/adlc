---
type: meta
title: "Hot Cache"
updated: 2026-11-09T01:30:00
tags:
  - meta
  - hot-cache
status: evergreen
related:
  - "[[index]]"
  - "[[log]]"
  - "[[Plugin architecture overview]]"
  - "[[Operating model for adlc 1.3.0]]"
  - "[[Research How work is organized]]"
  - "[[Configurable toolset for reader, code navigation and design]]"
  - "[[Upstream channel from vaults to the plugin]]"
---

# Recent Context

Navigation: [[index]] | [[log]]

## Last Updated

**2026-11-08 (late session: 1.3.0 built)**. The fifteen items of [[Operating model for adlc 1.3.0]] are implemented and the manifests read 1.3.0. New: `frontmatter.md` § Work records (story with `kind` and the loop-written dates `ready`, `started`, `done`, `history`; epic, sprint, release; decision `decided_by`, `decided_on`, `evidence`), `records.md` (four decision levels, `## How we work`, `machine.local.md`, `product/context.md`, `catalog-info.yaml`), `skills/adlc/references/routes.md` with the spike pipeline, the seventeenth worker `agents/spike.md`, `ba-prd.md`, `board.py` (6 tests), `migrate_1_3.py` (4 tests; dry run and apply checked on a copy of a co-located vault, 20 actions), `migration-1.3.md`, `bin/setup-team.sh` (run twice on a scratch vault). Rewritten: the architecture worker (artifact pages, no requirements, no gate pages; proposes spikes), `shift-left/_index.md`, `technical-planning.md` (gates as decision lines), the `/adlc` loop (Step 0 epic record and Gates table, dates at transitions, spike branch, acceptance rule, epic close into the release, board regeneration), `wrap-up`, `mission-control.md` (team board, multi-session rules), `operator-profile.md` (no quote column, `.raw/reflection/`), `team-sync.md` (joining checklist), `git-setup.md`, `modes.md`, the wiki scaffold and its AGENTS.md template, `wiki-lint` 6a/6b/10, `permissions.md`, README, the architecture pages. Four eval cases written (`wiki/scaffold-adlc`, `adlc/routes-research`, `adlc/spike-route`, `adlc/acceptance-list-back`) and the `adlc-vault` fixture extended.

**2026-11-08 (earlier)**: the operating-model research ([[Research How work is organized]], 25 pages, two passes) and the 1.3.0 plan with its rulings; the 1.2.0 branch review and merge.

## Key Recent Facts

- **Not run this session:** the eval suites (`claude plugin eval`), neither the fast set nor the four new cases. The operator runs them before the push; the 1.3.0 commit is local.
- **Settled during the build:** the work-item kind is `kind:`, not `type:` (the glossary keys on `type:`); the migration maps a former Gate 2 page to `adrs/decisions.md` and the worker splits it later; no EGM question page exists, so the 1.4.0 re-plan lives here.
- **The Bash heredoc path double-encodes non-ASCII** on this Windows machine (the section sign came out as four bytes); new files and edits with non-ASCII go through the Write and Edit tools.
- **The checker is loud on old pages by design** (about 1,500 `fix` findings on this wiki, mostly dashes); the dash sweep stays its own commit.
- `.raw/upstream/vault-f-UP-001.md` is still unfiled (glossary two-part prefixes).

## Active Threads

- **1.3.0 release steps left:** run the fast eval set and the four new cases; migrate the two co-located vaults on this machine with `migrate_1_3.py` (dry run first), then their follow-ups from `migration-1.3.md` (release records, Gates tables, PRD and domains, `Task(spike)` and `board.py` allow lines); push.
- **EGM in 1.4.0 (ruling 2026-11-08), plan agreed in outline, decisions open.** The Elephant-Goldfish Model (Google, Apache-2.0) adds fresh-context reviewers for documents. Plan: a `spec-review: egm | none` key; a `spec-reviewer` worker mirroring `feature-designer` that dispatches the `egm:egm-*` reviewers directly on each architecture artifact before its gate verdict (stages 5 to 8 on the drivers and the model, stage 9 on the workflow), record in the code wiki's `reviews/`; `egm-drift-report` in `wiki-lint`; the comprehension Goldfish on technical-writer pages. Spike first (now a spike story by the 1.3.0 rules): a worker with `Agent` in `tools:` spawning `egm:egm-comprehension`. Open: the key name and the phase 1 scope. Reviewers need Claude Code 2.1.271 or later (this machine: 2.1.319).
- **Follow-ups from 1.2.0:** set the toolset keys in the co-located vaults, their allow lines and `## Code navigation` sections; `/project-profile` writes `How we change code` on a fresh run only; `impeccable critique` runs degraded inside the designer; no `wiki/code/` graph of this repo.
- **Dash sweep** across `wiki/`, `skills/` and `agents/`, one dedicated commit.
- **Carried over unchanged:** vault-f/UP-001; the ledger items not addressed (vault-a public-repo records, UP-002, UP-011); the evals backlog ([[Plugin eval suites for claude plugin eval]]); the open tasks [[Integrate the wiki toolset into the ADLC workers]], [[Operator profile - learn engagement style from corrections]], [[Configurable subagent models per host]]; deferred: vault MCP server, `/project-profile --refresh`, Stage 6 trigger, K8, Cursor load check, sharing pilot, OKF exporter, repo rename.
