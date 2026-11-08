---
type: concept
title: "Lifecycle Artifacts and Decision Levels"
confidence: medium
created: 2026-11-08
updated: 2026-11-08
tags:
  - concept
  - lifecycle
  - decision-records
related:
  - "[[nygard-documenting-architecture-decisions]]"
  - "[[madr-markdown-decision-records]]"
  - "[[productplan-product-requirements-document]]"
  - "[[google-sre-book-introduction-playbooks]]"
status: draft
---

# Lifecycle artifacts and decision levels

Answer first: each lifecycle stage leaves one kind of record, and only some records are decisions. A decision record is for a choice that is costly to reverse and has real alternatives. Conventions, tool selections, machine setup and design briefs are other kinds of record and should not sit in the decision log.

## Artifact by stage

The table gives the stage, the record it leaves, and how well the claim is sourced.

| Stage | Record | Notes | Confidence |
|---|---|---|---|
| Discover | PRD (product requirements document) | The record of what a release must deliver: every capability with a use case, goals, non-functional requirements, assumptions, constraints, dependencies; it describes needs and may not dictate an implementation, which engineering specifies afterwards (Source: [[productplan-product-requirements-document]]) | high |
| Discover | Spike record | A time-boxed investigation that produces knowledge, not working software, to cut risk or sharpen an estimate; the term comes from Extreme Programming (Mountain Goat Software and Scrum.org, via search results; the Agile Alliance glossary page returned 404) | medium |
| Design | Domain model | Entities, relations and vocabulary the code uses; owned by the service that holds the data | low (practice judgment) |
| Design | ADR | One significant engineering decision (Source: [[nygard-documenting-architecture-decisions]], [[madr-markdown-decision-records]]) | high |
| Build and verify | Test plan | What is checked, where, against which requirement | low (practice judgment) |
| Release | Release and deliverable records | What shipped, which version, which requirements it closes | low (practice judgment) |
| Operate | Infrastructure as code | The environment itself, versioned; the code is the record | low (practice judgment) |
| Operate | Runbook (Google says playbook) | Steps for a known alert; recorded ahead of time it gave roughly 3x better time to repair than winging it, per Google's own experience (Source: [[google-sre-book-introduction-playbooks]]) | high |
| Operate | Postmortem | Blameless; fixes target the system, not people; written for every significant incident (Google SRE materials, search summary; the postmortem chapter was not fetched) | medium |

## What a spike should leave behind

The sources define the spike as a time-boxed activity whose output is knowledge. Recommended boxes run from under four hours (Scrum.org) to one to three days. At the end the team decides; if more research is needed, that becomes a new, separately prioritised spike. The record contents below are practice judgment (low): the question, the time box, the commands run, tool and library versions, failed attempts with why they failed, and the result. Failed attempts matter most, because they stop the next person repeating them. If the result changes the design, it feeds an ADR; the spike record is evidence, not a decision.

## Levels of decision

Four levels, widest first (practice judgment, low confidence on the naming):

- System or organisation: shared platforms, security posture, how services talk. Owned outside the project and referenced from it.
- Team: how the team works, branching, review rules.
- Product: what to build, for whom, what to cut. Lives with the PRD.
- Service: structure, data, dependencies and interfaces of one service. Lives in that service's ADRs.

A lower level does not overrule a higher one; it records a deviation and asks. Keep product and engineering decisions in separate logs. MADR's format allows both, but mixing them buries the engineering ones. InfoQ's ADR purpose article (search summary, medium) warns that teams with no other place for significant decisions dump everything into the ADR log, and the real ones get lost; its remedy is a separate record type.

## What is not a decision

- Conventions (naming, formatting): syntax-level, not architecturally significant (InfoQ, search summary; medium). They belong in project instructions or lint config.
- Tool selections: record one only when it is costly to reverse; otherwise a list entry is enough.
- Machine setup: a procedure; it belongs in a setup guide.
- Design briefs: an input to a build, tied to one story.

Test for a record (practice judgment, low): would a future developer without context break something or lose days rebuilding the reasoning? If yes, write the ADR.

## Gaps

The Atlassian PRD page returned only navigation, so ProductPlan stands in. The Agile Alliance spike glossary page returned 404, so spike claims rest on search results from Mountain Goat Software and Scrum.org. The SRE postmortem chapter was not read. No primary source was read for the domain model, test plan, release record or infrastructure as code.
