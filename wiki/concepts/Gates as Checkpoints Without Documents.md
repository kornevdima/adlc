---
type: concept
title: "Gates as Checkpoints Without Documents"
created: 2026-11-08
updated: 2026-11-08
tags: [concept, gates, definition-of-done, stage-gate]
confidence: medium
sources: ["[[cooper-stage-gate-systems-1990]]", "[[scrum-guide-2020]]"]
---

# Gates as checkpoints without documents

A gate is a decision made against stated criteria and evidence. It owns no document. The documents belong to the stages on either side; the gate only reads them and writes down a verdict.

## The parts

Cooper's Stage-Gate gives the shape: deliverables in, criteria applied, a decision out (go, kill, hold, recycle), with must-meet and should-meet criteria (Source: [[cooper-stage-gate-systems-1990]], medium confidence, 1990, secondhand text). The Scrum Guide's Definition of Done is the same shape inside a sprint: a shared, formal description of the quality an Increment must reach before it counts as done (Source: [[scrum-guide-2020]]). A delivery-pipeline quality gate is the automated form: a threshold on test, coverage or scan results that blocks promotion (medium confidence; stated from general practice, not from a source fetched this session).

## Rules that keep a gate from becoming paperwork

1. Criteria are written before the work, in the stage that feeds the gate (the Definition of Done is the model).
2. Evidence is a pointer to an existing artifact (a test run, a review verdict, a spec section), never a new report.
3. The output is one decision line: gate name, verdict, date, deciding role, evidence pointers, and any conditions. A conditional go names the condition.
4. Kill, hold and recycle must be real outcomes. A gate that only ever says go is a ritual (a failure mode relayed by secondary sources; low confidence).
5. Resources, here the next story or stage, are released only by the decision.

## Record forms, lightest first

A decision line in a log; a checked checklist embedded in the story; an approval by a named role (a review or pull-request approval). Pick the lightest that a later reader can audit.

See also [[Software Lifecycle Inputs and Handoffs]] and [[Lifecycle Artifacts and Decision Levels]] for what each stage hands over, and [[Disciplines Bodies of Knowledge and Boundaries]] for who sits at each gate.
