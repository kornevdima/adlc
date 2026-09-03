---
type: synthesis
title: "Operator profile: learn engagement style from corrections"
created: 2026-08-25
updated: 2026-09-03
tags:
  - agents
  - adlc
  - personalization
  - operator
  - workflow
status: open
related:
  - "[[Project Profile]]"
  - "[[AGENTS.md]]"
  - "[[Hot Cache]]"
  - "[[Compounding Knowledge]]"
  - "[[Context Engineering for Coding Agents]]"
  - "[[Integrate the wiki toolset into the ADLC workers]]"
---

# Operator profile: learn engagement style from corrections

**Requested by the operator, 2026-08-25**, mid-delivery-session: *"capture user input in personalized
settings … during the conversation my behavior and changes were evaluated, you know when I corrected
and how … some project might have business input, some can be fully managed."*

## The gap, stated precisely

`project-profile` builds `AGENTS.md` — the **codebase's** conventions, commands, and tribal knowledge.
**There is no equivalent for the operator.** How much they want to be in the loop, what they rule on
versus delegate, what they consider ceremony, and how they correct — all of it is re-learned from
scratch every session, or not at all.

> **`project-profile` : the codebase :: this task : the human running it.**

## The seed already exists and has not been grown

The ADLC run ledger's frontmatter already carries three engagement knobs:

```yaml
checkpoint: auto            # auto | ask
on_fail: stop               # stop | file-and-continue
verification_mode: "build-first, verify in batches"
```

They are **set once at Step 0 and never revisited.** Nothing updates them from what actually happens,
nothing generalises them across epics, and nothing carries them to the next project. That is the whole
opportunity: the schema is there, the learning loop is not.

## Evidence — one session's correction log, and what it reveals

Recorded because it is the ground truth this feature would learn from. Ten operator interventions in a
single delivery session:

| # | Intervention | Class | What it exposed |
|---|---|---|---|
| 1 | Second defect instance, unprompted | **data** | Sweep must find both unaided or the instrument is untrustworthy |
| 2 | *"what is `measure.mjs`? what can't be checked using chrome mcp or e2e?"* | **instrument** | A shipped fix had **no e2e guard at all** |
| 3 | *"why do we need to run some dev server if it's runnable from npm … why keep track all dist files?"* | **instrument** | A worker had reimplemented `astro preview`, worse; dist-diff was ceremony |
| 4 | *"what builder is doing? I already see it works … still adding settle floor to `measure.mjs`"* | **pacing** | Worker gold-plating a throwaway an hour past value |
| 5 | *"why don't they use shared design component?"* | **product** | Two routes, one component, one per-route flag |
| 6 | *"why you don't run ba agent for this work?"* | **delegation** | **67% of story pages untraced** in their own feature note |
| 7 | *"we need to make it as dress, to re-use component without rules"* | **ruling** | Direct design decision, to be taken not measured |
| 8 | *"it was no census to define, but it was my observation and direct consensus"* | **meta-correction** | The assistant had **over-corrected**, abandoning a call that was right |

**The distribution is the finding.** Only two of eight are about the work product. **Six are about how
the work is being done** — instruments, pacing, delegation, ceremony. An operator profile that only
recorded product preferences would have captured almost nothing of value here.

Three further patterns, each directly actionable:

- **Every product defect this session came from the operator LOOKING AT THE PAGE.** Zero came from a
  gate. In the previous session, three of four shipped fixes had the same origin. **For this operator,
  on this project, a screenshot in front of them is the highest-yield verification step available** —
  and it was repeatedly reached for last.
- **They give rulings and expect them taken, not measured.** #7 is a decision; dispatching a census
  against it (#8) was a category error. **A profile should record which operators rule versus which
  ask for options.**
- **They read scratchpad filenames and worker progress lines.** #2 and #4 both originate there. This
  operator inspects the *how*, not only the output — so narrating instrument choices up front is
  cheaper than being caught.

## The two poles they named

> *"some project might have business input, some can be fully managed"*

This is the axis the profile exists to place a project on:

| | **business-input** | **fully-managed** |
|---|---|---|
| Product/design decisions | operator rules, always | agent rules within stated principles |
| Checkpoints | at story boundaries | at epic boundaries |
| Ambiguity | stop and ask | assume, state the assumption, continue |
| Content/copy | never authored without acceptance | authored to a brief |
| Visual acceptance | operator's eyes are the gate | screenshots archived, not blocking |

The motivating project (a content site) is emphatically the **left column** — content subtraction requires acceptance case by case,
parity is not a product ruling, and every ship this session traces to the operator's own eyes. **A
project on the right column would be actively harmed by the same settings**, which is why this must be
per-project and not a global preference.

## Proposed mechanism

1. **A profile artefact per project** — `operator-profile.md` beside `AGENTS.md`, or a section within
   it. Records the engagement pole, decision rights (what the operator rules on by name), pacing
   preferences, ceremony tolerance, and preferred verification instruments.
2. **A correction log that feeds it.** Every operator intervention gets classified — data · instrument
   · pacing · product · delegation · ruling · meta — and appended with the outcome. **The log is the
   evidence; the profile is the distillation.** Keep both: a profile without its log cannot be audited
   or argued with.
3. **Distil on a schedule, not per-correction.** The ADLC skill already has a `distill` step that folds
   session learnings into repo-local workers. Same cadence, same place. ⚠ **Per-correction updating
   would over-fit** — see the risk below.
4. **Seed from the existing knobs.** `checkpoint` / `on_fail` / `verification_mode` become the first
   three fields rather than a parallel system, and gain the ability to be *revised by evidence* rather
   than only declared.
5. **Surface it at dispatch.** The profile belongs in the worker packet the same way carry-forward
   already is — a worker that knows "this operator's eyes are the acceptance gate" reaches for a
   screenshot earlier.

## Risks, and the one that worries me most

- ⚠ **Over-fitting to a loud session.** Eight corrections in one session is a small sample from one
  epic in one mood. A profile that hardens on it will mis-serve the next epic. **Prefer recording the
  correction with its context over inferring a rule from it**, and require a pattern to repeat before
  it becomes a setting.
- ⚠⚠ **A profile that suppresses useful checks is worse than no profile.** An operator who says
  "less ceremony" three times could plausibly get "skip verification" encoded. **This session shows
  exactly how fine that line is:** the same operator who cut the dist-diff as ceremony (#3) also
  exposed a missing e2e guard as a serious defect (#2). **They were not asking for less rigour — they
  were asking for rigour in the instrument that persists rather than the one that gets deleted.**
  A naive learner would have recorded "wants less checking" and been badly wrong.
- **Corrections are not uniform in weight.** A one-off preference and a standing law look identical in
  a transcript. The existing vault convention — an explicit "⚠ OPERATOR PROCESS RULINGS — standing"
  block — is a manual solution to this and probably the right shape to formalise.
- **Reading correction patterns shades into modelling the person.** Keep it to observable working
  preferences with the evidence attached, not inferred traits.

## Open questions

- **Who writes it — the wrap-up skill, a dedicated pass, or the operator directly?** Auto-derived is
  cheap but risks the over-fit above; operator-authored is accurate but is one more thing to maintain,
  and this session's evidence is that maintenance-by-intention does not hold (10 of 12 feature notes
  in the sibling vault were stale, and the 2 current ones were current only because exactly one story
  claimed each).
- **Does it live per-project, per-operator, or both?** The two poles are per-project; correction style
  is probably per-person and worth carrying between projects.
- **Should the profile be shown to the operator for ratification?** Arguments both ways: a silently
  learned profile that gets it wrong is hard to notice; a ratification step is friction of exactly the
  kind this operator objects to.
- **What is the smallest useful version?** Possibly just: engagement pole + a standing-rulings list +
  the correction log. Items 1 and 5 could ship without 2 and 3 and still help.

## Effort calibration — a second dimension, operator-raised 2026-08-25

> *"I think that sometime effort level affects the output. Some tasks should not be overthinked."*

`Agent` and `Workflow` both already accept an `effort` parameter, and neither the ADLC skill nor any
worker ever sets it. Like `checkpoint`/`on_fail`, the knob exists and nothing drives it.

### The evidence, and it does NOT say "less effort"

One CSS declaration — `margin-top: var(--space-7)` on an existing rule — consumed: a census sweeping
6034 sibling pairs over 38 page loads, a 9-scenario contract, a builder running an hour, 21 e2e tests,
and 7 mutation proofs.

**Auditing which of that earned its keep is the whole lesson:**

| Spend | Verdict |
|---|---|
| Census blast-radius pass | **Earned it.** Found the systemic fix would move `a8912ef`'s 16 instances −32px |
| Tester's 21 specs + reorder mutation | **Earned it.** Exposed a shipped fix with no e2e pin at all |
| Builder's final hour on a throwaway harness | **Waste.** Operator could already see the fix working |
| S8's dist snapshot/diff pipeline | **Waste.** Proved HTML unchanged for a CSS-only edit — true by construction |
| Census dispatched against a settled ruling | **Waste, and a category error** |

> [!important] **THE RULE IS NOT "SPEND LESS". It is: effort tracks IRREVERSIBILITY and BLAST RADIUS,
> never how interesting the problem is.**
> The trivial dimension (does the button move down) was confirmable in one screenshot and the operator
> did it themselves in seconds. The subtle dimension (does this silently revert another fix, decided
> by nothing but stylesheet source order at equal specificity) was invisible and genuinely deserved
> the mutation work. **Same change, same commit, two dimensions, opposite correct efforts.**

### Why a per-task effort setting is not enough

A single dial set on "this is a small CSS change" would have skipped the mutation proof and shipped an
unguarded regression path. A dial set on "spacing has burned us before" produced the wasted hour.
**Neither reading of the task is wrong; the task simply is not the right unit.**

Candidate unit instead — **the claim**. Each assertion carries its own cost-of-being-wrong:

- *"the button now has a gap"* — cheap to check, instantly visible, **low effort, and a screenshot
  beats any harness**
- *"nothing else moved"* — invisible if wrong, discovered months later, **high effort, and it must
  end up in `npm test` rather than in a deleted script**

### Observable heuristics from this session

- **A visible, operator-confirmable outcome needs verification effort near zero.** Show them; they
  answer in seconds. Effort spent proving what a screenshot settles is pure waste — and this operator
  reads worker progress lines, so the waste is *visible* to them, which compounds the cost.
- **Effort belongs on what SURVIVES.** The throwaway harness and the permanent spec cost similar
  effort; only one is still checking anything tomorrow. **Spend on the artefact with a future.**
- **Gold-plating has no natural stop.** The builder kept refining a harness an hour past the point of
  value because nothing told it the value had been reached. **A worker needs a stated done-condition,
  not just a task** — "stop when X is measured", not "measure X".
- **Ceremony that proves things true by construction is always waste**, at any effort level. No amount
  of care makes "did a CSS edit change the HTML" worth a pipeline.

### Open questions

- Is `effort` settable **per claim** in practice, or only per dispatch? If only per dispatch, the
  practical move is **splitting the dispatch** — cheap builder, expensive tester — rather than tuning
  one dial.
- Does a low-effort worker **know** when it has hit something that deserves escalation? The
  most valuable single result this session came from a builder that **refused an ordered fix after
  measuring it red**. **A cheap worker that cannot escalate is a different, worse thing from a cheap
  worker.**
- Should the done-condition be a contract field? The contract already carries scenarios; **it does not
  carry "and then stop".**

## Resolution log — 2026-09-03: the smallest useful version shipped

Shipped as `skills/wiki/references/operator-profile.md` (template + rules + effort section) and wired in:

| Piece | Where |
|---|---|
| Profile artefact, per project | `wiki/meta/operator-profile.md` — seeded by the `wiki` skill's ADLC scaffold step 8 (one engagement question) and by `/adlc` Step 0 when absent; listed in `mission-control.md` § Scaffold as the third `meta/` page |
| Engagement pole → run-policy defaults | `/adlc` Step 0.5–0.6; ledger frontmatter gained `engagement:` |
| Standing rulings + preferred instruments in every dispatch packet | `/adlc` Step 0.5 |
| Correction log, classified per interjection | `/adlc` "Operator interjections" rule; `wrap-up` step 7a for non-loop sessions |
| Distil on a schedule, proposals only | `/adlc` Step 4.4 writes `proposed:` lines; the operator ratifies by editing. Rule 3 ("never encode less rigour") is in the reference verbatim |
| Effort: per claim, done-condition, name the instrument | dispatcher rules in `technical-planning.md`; `/adlc` Step 2.2 contract rules |

**Decisions on the open questions**
- *Who writes it*: the loop logs, distill proposes, the operator ratifies — none of the three is "maintenance by intention", which the sibling-vault evidence (10 of 12 stale feature notes) says does not hold.
- *Per-project or per-person*: per-project only, for now. The poles are project properties; carrying correction *style* between projects shades into modelling the person and is deferred until two projects show the same rows.
- *Ratification*: `proposed:` lines in a file the operator already reads — no interruption, no silent hardening.
- *Smallest version*: pole + decision rights + standing rulings + preferred instruments + the log. Shipped exactly that.

**Effort calibration**: the done-condition is now a contract rule; per-claim effort is a dispatcher rule; the unused `effort` parameter on `Agent` / `Workflow` stays unused — the recommendation in the reference is to **split the dispatch** (cheap builder, expensive tester) rather than tune one dial.

**Remaining (open)**
- Can a low-effort worker escalate? The builder that refused a red fix is the existence proof; nothing in the workers names escalation as a duty beyond "STOP and report". Consider a one-line "escalate when your measurement contradicts the packet" rule if a cheap worker ever ships a wrong fix silently.
- `effort` per dispatch untested in the loop; try it on a builder-only story before making it a rule.
- Over-fit guard is procedural (rule 2: repeat before setting). No mechanism counts repeats across epics yet; the `proposed:` line must cite the epics it saw.

