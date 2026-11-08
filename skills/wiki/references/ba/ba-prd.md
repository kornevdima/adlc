---
name: ba-prd
description: >
  Writes and maintains the product requirements document (PRD) of a Mode ADLC vault at
  wiki/product/prd.md: purpose, users, what the user can do when the work is done, scope and
  non-goals, the feature list with links, open questions. Keeps the document at the why and the
  what; the how belongs to the architecture artifacts in the code wikis. Trigger this method
  when the user says "write the PRD", "product requirements", "what are we building", "update
  the PRD", "the PRD is stale", or after the requirements register exists and no PRD does. Runs
  after ba-elicitation-synthesizer and ba-requirements-lifecycle; feeds ba-user-story-factory
  (the feature list is the epic list) and the architecture worker (the quality requirements it
  turns into drivers).
---

# BA PRD

Writes the one page that says what the product is for and what it will do, for a reader who decides or builds. It sits above the requirements register (which lists every requirement with an id) and below nothing: a vault has one PRD.

## Reference files

Read before processing input:
- `skills/wiki/references/ba/ba-suite-orientation.md` for the id schemes and the writing standards
- `skills/wiki/references/ba/ba-elicitation-synthesizer.md` for where the requirements register and its sources live
- `skills/wiki/references/writing-style.md` for the sentences; the PRD is read by people who did not write it

## Scope boundaries

**This method covers:** `wiki/product/prd.md`, created in the initial ADLC pass after the requirements register and kept current by `wrap-up` as features ship.

**This method does not cover:**
- the requirements register and the RTM (ba-requirements-lifecycle)
- epics and stories (ba-user-story-factory; the PRD's feature list is the input to its Step 1)
- the C4 context and the team dependencies (`wiki/product/context.md`, from the records reference)
- architecture: drivers, domain model, ADRs (the architecture worker, in each service's code wiki)
- business cases and solution assessments (`deliverables/`)

## Input handling

Minimum viable input: the requirements register (`wiki/requirements/`) with stable ids, or the sources in `wiki/sources/` when the register does not exist yet (then the PRD's open questions list what the register will need).

Optimal input, and what each adds:

| Input | Effect |
|---|---|
| Requirements register with MoSCoW | Scope and non-goals come from the Must / Won't split, not from guessing |
| Stakeholder analysis | The users section names roles, not an undifferentiated "user" |
| Feature notes (`wiki/features/`) | The feature list links instead of describing |
| Gap register | Open questions include what is known to be missing |
| Intake notes (`.raw/intake/`) | Purpose and outcome in the product owner's words, cited |

Clarification rule: if the sources disagree on who the product is for, ask one question naming the two readings; otherwise proceed and list the disagreement under open questions.

## Processing steps

### Step 1: Purpose

One paragraph: the problem, for whom, and how one would notice it is solved. Every sentence cites a source or a requirement id. No mechanism, no technology.

### Step 2: Users

One line per role: who they are, what they come to the product for, roughly how many when a source says. Roles, never names. Link the stakeholder page when one exists.

### Step 3: What the user can do when the work is done

The outcomes, in the user's terms, one line each, grouped by role. Each line traces to one or more requirement ids in brackets. This section is what a release record's "What the user gets" is cut from later.

### Step 4: Scope and non-goals

Scope: the Must and Should requirements, named in plain words with the ids. Non-goals: the Won't requirements and anything a source asked for that the product will not do, each with the reason in one line. A non-goal with no reason is a question, not a non-goal.

### Step 5: Feature list

One row per feature, linking the feature page in `wiki/features/` and the epic in `wiki/epics/` when they exist, with the release it is planned for. This list is the input to the story factory's epic step; the two must agree, so when the factory names an epic the PRD lacks, the PRD gets the row.

### Step 6: Open questions

What the sources do not settle, one per line, each naming who can answer it and what it blocks. Answers land on the requirement pages, and the question is removed from the PRD; the removal is a changelog row.

### Step 7: Quality requirements for the architecture worker

A short table of the non-functional requirements by id with the measurable threshold each carries. The architecture worker restates these as quality attribute scenarios in `architecture-drivers.md`; the PRD only lists them so the worker and the reader see the same set.

## Output specification

The page `wiki/product/prd.md`:

```markdown
---
type: prd
title: "Product requirements"
status: developing          # developing | current | delivered
created: YYYY-MM-DD
updated: YYYY-MM-DD
produced_by: ba-prd
sources:
  - "[[<source page>]]"
tags:
  - product
  - prd
---

# Product requirements

## Purpose
## Users
## What the user can do when the work is done
## Scope and non-goals
## Features
## Open questions
## Quality requirements
```

Rules:
- The page holds the current state only. When a feature ships, `wrap-up` rewrites its row (status, the release it shipped in) and adds a row to `product/_changelog.md`; no dated update blocks.
- The how stays out: no component names, no technology choices, no data model. A reader who wants the how follows the links to the code wikis.
- Every id links on first mention (`glossary.py link --apply` does the mechanical part); every table has a lead-in; totals as numbers.
- Office export (`ba-export`) renders the page as the BRD's product section; the wiki page is the source of truth.

## Quality checklist

- [ ] Every sentence in Purpose and Outcomes cites a source or a requirement id
- [ ] Users are roles; no person is named
- [ ] Each non-goal has a reason
- [ ] The feature list and the epics in `wiki/epics/` name the same set
- [ ] No mechanism, component or technology appears outside the links
- [ ] Open questions name who answers and what each blocks
- [ ] The page passes `tells_check.py` with no `fix` finding
