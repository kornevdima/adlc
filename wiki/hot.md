---
type: meta
title: "Hot Cache"
updated: 2026-07-04T16:30:00
tags:
  - meta
  - hot-cache
status: evergreen
related:
  - "[[index]]"
  - "[[log]]"
  - "[[Grilling Session]]"
  - "[[Validation Contract]]"
---

# Recent Context

Navigation: [[index]] | [[log]]

## Last Updated

**2026-07-04 (tier 3 metrics seam + graphify grounding for workers, committed)**: Two harness increments this session — the metrics seam / mission-control spec, then (pre-redeploy) all ADLC workers taught to leverage graphify data. Wrapped up and committed on `adlc`.

## Key Recent Facts

- **Graphify grounding (new, motivated by the pending agent redeploy):** `technical-planning.md` § Code graph grounding — where a service has `graphify-out/graph.json` + `wiki/code/`, workers orient there before grep. Doctrine: **the graph finds; the code asserts** — claims in specs/reviews/tests still need code confirmation; on disagreement the code wins and staleness is reported. **Freshness is the dispatcher's job**: `/graphify-update` post-verify pre-commit; `wrap-up` step 3 refreshes changed repos' graphs. Bash workers use the CLI (self-contained pinned-python snippet): `feature-builder` (orient), `feature-reviewer` (blast radius — callers outside the diff), `feature-tester` (routes + neighboring specs). Bash-less workers use the readable layer (`wiki/code/_COMMUNITY_*.md`, `GRAPH_REPORT.md`): `architecture-subagent`, `doc-writer`. `feature-verifier` untouched (runtime).
- **Metrics seam / mission-control (`references/mission-control.md`, new):** two derived pages in ADLC `meta/` — `mission-control.md` (operator's async board: in-flight stages `spec→grilling→build→test→review→verify→docs→shipped`, readiness vs the literal bar, defect-route table, milestone status, open human gates; dispatcher updates a row per stage transition, wrap-up reconciles) and `ba-activity.md` (cost rollup from `produced_by`/`feature`/`effort_estimate` frontmatter, grep-first, wrap-up-refreshed; "Not counted" = seam health check). Derived-view rule: records always win; team-sync merge rule = regenerate-don't-merge. `wiki-lint` check 13 (missing `produced_by`, board contradictions, board staleness). ADLC scaffold seeds both pages.
- Earlier same day (committed `91934de`): tier 2 — grilling gate, milestone holistic verify, FAILs→backlog, vertical slices, coverage ledger, ingest video path + canonical language.

## Recent Changes

- Created: `skills/wiki/references/mission-control.md`.
- Edited (metrics seam): `technical-planning.md`, `skills/wrap-up/SKILL.md`, `agents/wiki-lint-subagent.md`, `team-sync.md`, `modes.md`, `ba-suite-pipeline.md`, `skills/wiki/SKILL.md`.
- Edited (graphify grounding): `technical-planning.md` (new section), `agents/feature-builder.md`, `agents/feature-reviewer.md`, `agents/feature-tester.md`, `agents/architecture-subagent.md`, `agents/doc-writer.md`, `skills/wrap-up/SKILL.md` (step 3).
- Logged: [[log]] entries `impl | Workers ground in the graphify layer` and `impl | Harness tier 3: metrics seam / mission-control`.

## Active Threads

- **Both increments committed** — next: **redeploy `agents/*.md` snapshots to service repos** (now carrying graphify grounding; one repo lacks feature-reviewer entirely). Service repos without a graph need `/graphify-ingest` once for workers to benefit.
- Other human follow-ups: `.gitattributes` two-liner in existing project vaults; seed the two `meta/` pages in existing ADLC vaults; `plugin.json` 0.3.0→0.4.0.
- Remaining planned: pm-layer evals E1–E8; RLM → wiki-query ([[RLM-Optimized Wiki Querying]]).
