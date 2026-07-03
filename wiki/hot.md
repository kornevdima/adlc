---
type: meta
title: "Hot Cache"
updated: 2026-07-04T12:00:00
tags:
  - meta
  - hot-cache
status: evergreen
related:
  - "[[index]]"
  - "[[log]]"
  - "[[Grilling Session]]"
  - "[[Vertical Slices for Agent Tasks]]"
  - "[[Validation Contract]]"
---

# Recent Context

Navigation: [[index]] | [[log]]

## Last Updated

**2026-07-04 (harness tier 2 + ingest tier 3, committed)**: Implemented the full tier 2 harness backlog (grilling gate, milestone holistic verification, verifier-FAILs→backlog, vertical-slice rule, assertion-coverage ledger) plus the wiki-ingest tier 3 items (YouTube capture path, canonical-language rule) and the `merge=union` scaffold. Wrapped up and committed on `adlc`.

## Key Recent Facts

- **Tier 2 shipped (uncommitted):** `technical-planning.md` gained a **grilling gate** (dispatcher interviews the human question-by-question with recommended answers before Gate 1 approval; grounded by an Explore pass; never delegated/unattended), a **milestone holistic verification** section (cross-feature seam journeys, fresh-target re-verify of shipped contracts, unscoped e2e suite; `conditional — milestone verify pending` otherwise), and the **FAILs→backlog** dispatcher rule (every FAIL = bug page + backlog item + `conditional — fix pending`; ENV_MISMATCH / NEEDS_SIGN_IN are operational, never defects).
- **Vertical slices:** `ba-user-story-factory` Step 2.5 tracer-bullet check — Functional stories must cut schema→service→API→UI and end observable; horizontal layer-stories fail and get re-split; Technical Enabler requires justification; dependency map must be a DAG of independently grabbable stories (longest chain reported, re-split if > half the stories).
- **Assertion-coverage ledger:** `feature-tester` step 7 maintains `coverage/_index.md` in the service code wiki (one row per contract scenario: feature, id, tag, test title, last result + date; derived — contract + spec always win). Documented in `concerns/qa.md`; `wiki-lint` checks ledger drift and FAILs-without-backlog-item (critical); `wrap-up` step 4 reconciles the defect route.
- **wiki-ingest:** new Video / YouTube path (yt-dlp `--skip-download --write-subs --write-auto-subs`, VTT cleaning incl. rolling-duplicate dedupe, proper-noun `(sp?)` caveat) and Canonical Language rule (wiki pages in vault language; `.raw/` never translated; `source_language:` frontmatter).
- **Model split (operator decision):** workers draft on Sonnet; judgment/orchestration/re-verification live at the dispatcher (session model). Don't fix worker quality with model upgrades.
- **Production audit findings (context for all of the above):** tester env-precondition assumptions were the largest failure class; verifier PASSes were environment-dependent; one "VERIFIED" shipped a bug via a stubbed integration; logs full of FAILs sat next to an empty backlog.

## Recent Changes

- Edited: `skills/wiki/references/technical-planning.md` (3 sections), `skills/wiki/references/ba/ba-user-story-factory.md`, `agents/feature-tester.md`, `agents/wiki-lint-subagent.md` (checks 11–12), `skills/wrap-up/SKILL.md`, `skills/wiki-ingest/SKILL.md` (2 new sections), `skills/wiki/references/concerns/qa.md`.
- Closed wrap-up follow-up: `.gitattributes` (`wiki/log.md merge=union` + `**/wiki/log.md`) created in this repo; `references/git-setup.md` now bakes it into the scaffold. Existing project vaults still need it added by hand.
- Logged: [[log]] entry `2026-07-04 impl | Harness tier 2 + wiki-ingest tier 3`.
- Prior session (committed): harness hardening `bc511a3`, team-sync `0278002`, 5-talk ingest `59449d5`.

## Active Threads

- **Tier 2 committed** — next: **redeploy agent copies to service repos** (stale `.claude/agents/` snapshots; one lacks feature-reviewer entirely), and add the two-line `.gitattributes` to existing project vaults by hand.
- **Remaining backlog (tier 3):** metrics seam / mission-control (rollups from `produced_by` frontmatter — `ba-suite-pipeline.md` § Metrics seam is the stub).
- **pm-layer evals**: E1–E8 documented but not encoded/run.
- **`plugin.json`**: 0.3.0→0.4.0 bump still uncommitted (user-managed).
- **RLM → wiki-query**: design filed ([[RLM-Optimized Wiki Querying]]), not implemented.
