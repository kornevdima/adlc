---
type: synthesis
title: "Review the ADLC flow against the AI-Native SDLC Playbook"
created: 2026-09-03
updated: 2026-09-03
tags:
  - adlc
  - sdlc
  - review
  - open-task
status: open
related:
  - "[[AI-Native SDLC Playbook vs ADLC]]"
  - "[[claude-ai-native-sdlc-playbook]]"
  - "[[Agentic Orchestration Levels]]"
  - "[[Integrate the wiki toolset into the ADLC workers]]"
  - "[[Operator profile - learn engagement style from corrections]]"
  - "[[Research OpenManus for claude-mem]]"
---

# Review the ADLC flow against the AI-Native SDLC Playbook

**Requested by the operator, 2026-09-03**: *"I want to review the adlc flow later — https://claude.com/blog/the-ai-native-sdlc-playbook#sd-s6. I don't like the idea to keep one file with common name; the current workflow with wiki files looks better to me. But it is the explanation for AI SDLC — what we have as ADLC."*

Source filed as [[claude-ai-native-sdlc-playbook]] (raw: `.raw/claude-ai-native-sdlc-playbook.md`, anchors kept). Stage-by-stage mapping and the vocabulary map: [[AI-Native SDLC Playbook vs ADLC]].

## Standing ruling (taken, not to be measured)

- Substrate stays **typed wiki records with stable IDs**; no `intent.md` / `spec.md` / `plan.md` common-name files. The playbook is the *external vocabulary* for ADLC, not a template to adopt.

## Review checklist — grilling style, one question at a time, each with a recommended answer

The anchor the operator pointed at is **Stage 6 (Maintain — closing the loop)**; it is first.

1. **Stage 6 — do we want a headless entry into ADLC?** Today every run starts from an operator session; the FAIL → `bugs/` + backlog mechanic already is the "finding re-enters the pipeline" seam. *Recommended*: design the seam only — a trigger (schedule / webhook / channel) that runs a bounded, read-only diagnosis and files a `bugs/` page + backlog item, with detection kept deterministic and outside the model; build it when a project has a metrics store, on the deferred Agent SDK branch. Do **not** generate `intent.md`; the backlog item *is* the intent.
2. **Stage 1 — a non-engineer intent route.** *Recommended*: doc-only — "drop it in `.raw/` with this five-heading template (problem, outcome, affected, constraints, open questions); `wiki-ingest` + the BA pass do the rest." Same content as the playbook's `intent.md`, filed as a source with a stable ID downstream.
3. **Stage 5 — a review policy page per service.** The reviewer's standards are currently re-assembled into each dispatch packet. *Recommended*: yes — `services/<svc>/wiki/reviews/_policy.md` (passes, what "Important" means, nit cap, exclusions), pushed verbatim by the dispatcher; a typed record, not a root-level `REVIEW.md`.
4. **Stage 4 — evals on config change.** *Recommended*: yes, cheap — run the plugin's `claude plugin eval` suites in CI on changes under `agents/` or `skills/`; add "every verifier FAIL that reached production becomes an eval case" to the defect route.
5. **Stage 5 — "mistake twice → CLAUDE.md".** ADLC distils into repo-local workers and AGENTS.md Don'ts. *Recommended*: keep both targets; make `/adlc distill` say which it chose and why (Don'ts → AGENTS.md; worker mechanics → `.claude/agents/`).
6. **Measurement — time-based indicators.** The playbook's metrics are two-commit deltas (intent→spec, spec→first plan, first-pass merge share). *Recommended*: defer; `meta/ba-activity.md` tracks cost, `mission-control.md` tracks state. Add only if an operator asks for cycle-time.
7. **Deploy stage — keep it out?** *Recommended*: yes, and say so explicitly in `technical-planning.md`: ADLC ends at a verified commit; push / PR / deploy are the operator's, with the playbook's hooks-as-gates as the documented next step for teams that want it.
8. **Vocabulary in the README.** *Recommended*: one paragraph mapping playbook terms to ADLC (the vocabulary map), so a reader arriving from the playbook finds their footing.

## Not in scope of this review

- Enterprise managed-settings / sandbox floor (small-team plugin; note as a pointer only).
- Claude Tag / Slack on-call (product-specific; belongs to the Stage 6 seam if ever built).

## Done when

Each item above has a ruling recorded here (adopt / defer / reject with one line), and the adopted ones have landed in the skill / reference they name. Then flip `status: closed` and move the summary into [[AI-Native SDLC Playbook vs ADLC]].
