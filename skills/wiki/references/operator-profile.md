# Operator profile: the human counterpart of the project profile

`project-profile` builds `AGENTS.md` — the **codebase's** conventions, commands, and tribal knowledge. Nothing equivalent exists for the **human running the delivery**: how much they want to be in the loop, what they rule on versus delegate, what they consider ceremony, which verification instruments they trust, and how they correct. Without a record all of it is re-learned every session, or not at all.

> `project-profile` : the codebase :: operator profile : the human running it.

The seed already existed: the `adlc` run ledger carries `checkpoint` / `on_fail` / `verification_mode`, set once at Step 0 and never revisited. The profile is where those knobs become *revisable by evidence* rather than only declared.

## Where it lives

`wiki/meta/operator-profile.md` in the product wiki — **per project**, because the engagement pole is a property of the project, not of the person (the same operator runs a content site as business-input and an internal tool as fully-managed, and each would be harmed by the other's settings). Seeded at ADLC scaffold (`wiki` skill step 8) and by `/adlc` Step 0 when absent. Git-tracked like the rest of `meta/`. No PII beyond the operator's role; quotes are their own words *about the work*.

## The axis: business-input vs fully-managed

| | **business-input** | **fully-managed** |
|---|---|---|
| Product / design decisions | operator rules, always | agent rules within stated principles |
| Checkpoints | at story boundaries | at epic boundaries |
| Ambiguity | stop and ask | assume, state the assumption, continue |
| Content / copy | never authored without acceptance | authored to a brief |
| Visual acceptance | the operator's eyes are the gate | screenshots archived, not blocking |

The pole sets the **defaults** for the run policy (`checkpoint`, `on_fail`); the operator can still override per run.

## Template

```markdown
---
type: operator-profile
title: "Operator profile"
engagement: business-input     # business-input | fully-managed
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - meta
  - operator
status: evergreen
---

# Operator profile

## Engagement
- Pole: business-input
- Checkpoints: story boundaries
- Ambiguity: stop and ask
- Content / copy: never authored without acceptance

## Decision rights
<!-- what the operator rules on BY NAME. A ruling is taken, not measured. -->
- Product and design decisions; content removal; whether an asset is fit to publish

## Standing rulings
<!-- one line each, dated, verbatim where possible; these ride in every dispatch packet -->
- YYYY-MM-DD — "re-use the shared component, no per-route rules" (design)

## Preferred instruments
- Visual acceptance: a screenshot in front of the operator is the gate
- Regression pins: the e2e suite — never a throwaway script

## Pacing and ceremony
- Reads worker progress lines and scratchpad filenames: narrate instrument choices up front
- Snapshot / diff pipelines for changes that cannot alter the artefact: ceremony

## Proposed changes
<!-- written by /adlc distill; the operator ratifies by editing the section above and deleting the line -->
<!-- proposed: YYYY-MM-DD — checkpoints → epic boundaries (pattern seen in 2 epics: EPIC-A, EPIC-B) -->

## Correction log
| Date | Quote (verbatim, short) | Class | What it exposed | Outcome |
|---|---|---|---|---|
| YYYY-MM-DD | "why run a dev server if it's runnable from npm" | instrument | worker rebuilt the wired preview server, worse | contract now names the instrument |
```

## Correction classes

`data` (a missed instance the sweep should have found) · `instrument` (the wrong tool, or a rebuilt one) · `pacing` (gold-plating, an hour past value) · `product` (a defect the operator saw on the page) · `delegation` (a worker that should have been dispatched) · `ruling` (a direct decision, to be taken) · `meta` (a correction of an over-correction).

The **distribution is the finding**: in the session that motivated this reference, six of eight corrections were about *how* the work was being done — instruments, pacing, delegation, ceremony — and only two about the work product. A profile that records only product preferences captures almost nothing of value.

## Rules

1. **Log per correction; distil on a schedule.** Every intervention becomes one row, with its context. Settings change only at `/adlc distill` (Step 4.4), on evidence that repeats. Per-correction updating over-fits a loud session — eight corrections in one epic is a small sample from one mood.
2. **A pattern must repeat before it becomes a setting.** Record the correction with its context first; require it across sessions or epics before it is a rule.
3. **Never encode "less rigour".** The operator who cut a dist-diff as ceremony demanded, in the same session, the e2e pin that was missing. They asked for rigour in the instrument that *persists*, not for less of it. A naive learner would have recorded "wants less checking" and been badly wrong — the line between the two is exactly this fine.
4. **Proposals, not silent hardening.** Distill writes `proposed:` lines; the operator ratifies by editing. A silently learned profile that gets it wrong is hard to notice; a ratification prompt is friction of the kind the operator objects to. A proposal line in a file they already read is neither.
5. **Observable working preferences with the evidence attached — not inferred traits.** The log is the evidence; the profile is the distillation. Keep both: a profile without its log cannot be audited or argued with.
6. **Standing rulings are a different weight from preferences.** A one-off and a standing law look identical in a transcript. The explicit "Standing rulings" block is the manual solution; anything not in it is a preference.

## How the loop uses it

- **`/adlc` Step 0** reads it; the pole sets the run-policy defaults; **standing rulings** and **preferred instruments** ride in every dispatch packet next to the Carry-forward, so a worker that knows "this operator's eyes are the acceptance gate" reaches for a screenshot early rather than a harness late.
- **Story loop** — every operator interjection is classified and appended to the correction log. A `ruling` is taken; dispatching a census against it is a category error.
- **Step 4.4 distill** — reads the run's rows, writes `proposed:` changes.
- **`wrap-up`** — appends interjections the loop did not log (non-`/adlc` sessions), lists open proposals in its report.

## Effort: the unit is the claim, not the task

Both `Agent` and `Workflow` accept an `effort` parameter; nothing in the loop sets it, and a single per-task dial would be wrong anyway. One CSS declaration consumed a 6,034-pair census sweep, a 9-scenario contract, an hour of builder time, 21 e2e tests and 7 mutation proofs. Auditing which of that earned its keep:

| Spend | Verdict |
|---|---|
| Census blast-radius pass | earned it — found the systemic fix would move 16 other instances |
| Tester's specs + reorder mutation | earned it — exposed a shipped fix with no e2e pin at all |
| Builder's final hour on a throwaway harness | waste — the operator could already see the fix working |
| Dist snapshot/diff for a CSS-only edit | waste — true by construction |
| Census against a settled ruling | waste, and a category error |

> **The rule is not "spend less". Effort tracks irreversibility and blast radius, never how interesting the problem is.** "The button now has a gap" is settled by one screenshot (effort near zero); "nothing else moved" is invisible if wrong and deserves a mutation pin that survives in the suite. Same change, two claims, opposite correct efforts.

Practical consequences, already wired into the dispatcher rules (`technical-planning.md`): every contract names its instrument and states a done-condition; effort goes to the artefact with a future; a visible, operator-confirmable outcome is shown to the operator, not proven to a harness. If effort must vary per dispatch, **split the dispatch** (cheap builder, expensive tester) rather than tuning one dial — and a cheap worker must still be able to escalate: the most valuable single result of the motivating session came from a builder that refused an ordered fix after measuring it red.
