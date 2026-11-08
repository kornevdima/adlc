---
type: concept
title: "Software Lifecycle Inputs and Handoffs"
status: draft
confidence: medium
created: 2026-11-08
updated: 2026-11-08
tags: [concept, roles, handoff, workflow]
related:
  - "[[scrum-guide-2020]]"
  - "[[shape-up-basecamp]]"
  - "[[team-topologies-key-concepts]]"
  - "[[safe-product-management]]"
  - "[[raci-responsibility-assignment-matrix]]"
  - "[[Structured Handoff]]"
---

# Software lifecycle inputs and handoffs

Every framework names the same few inputs under different titles. A small team folds several inputs into one person; a large organization splits them into groups. The inputs are the stable part, the job titles are not.

## The inputs and what each produces

| Input | Produces | Consumes | Scrum | Shape Up | SAFe (medium) |
|---|---|---|---|---|---|
| Product | Goal, ordered backlog or pitch | Feedback, stakeholder needs | Product Owner | Shaper, betting table | Product Management, Product Owner, Business Owners |
| Design | Interface and flow decisions | Problem and appetite | inside Developers | Designer on the build team | inside Agile Teams |
| Development | Increment, tests | Backlog items | Developers | Programmers | Agile Teams; System Architect sets technical direction |
| QA | Verified Increment | Definition of Done | inside Developers | QA joins late for integration testing | inside Agile Teams |
| DevOps | Running, observable release | Verified Increment | not named | not named | not named in the role pages checked |
| Facilitation | Removed impediments | Team friction | Scrum Master | none | Scrum Master, Release Train Engineer |

(Sources: [[scrum-guide-2020]], [[shape-up-basecamp]])

## Where the handoffs sit

1. Product to build. Scrum hands over an ordered backlog item; Shape Up hands over a pitch with problem, appetite and solution. In both the receiver can renegotiate scope but not the goal or the time budget.
2. Build to verify. Scrum folds this into the Definition of Done; Shape Up puts QA late in the cycle.
3. Verify to release. Neither primary source names an owner for deployment. This is the gap an agentic loop has to fill explicitly.
4. Release to product. Scrum closes the loop at Sprint Review; Shape Up closes it at the next betting table.

## Other frameworks

- SAFe names Product Management as owner of strategy, vision, roadmap and the ART backlog (the backlog of the Agile Release Train, the group of teams that ships together). System Architect, Release Train Engineer and Business Owners are named as fellow ART leaders (Source: [[safe-product-management]]). Confidence medium: the page is official and dated October 2024, but part of it is behind a login. The Product Owner link, the System Architect's duties and the "program backlog" label come from secondary summaries and stay unconfirmed.
- Team Topologies organizes teams, not individuals. Four team types: stream-aligned, enabling, complicated subsystem, platform. Three interaction modes: collaboration, X-as-a-Service, facilitation. A handoff is therefore a service boundary between teams (Source: [[team-topologies-key-concepts]]). Confidence high for the definitions, taken from the authors' own site; the page is undated.
- RACI records who does what per artifact. Four letters: Responsible (does the work, several allowed), Accountable (signs off, exactly one), Consulted (input before), Informed (told after). The one-A rule is the useful part: an artifact with no Accountable has no owner, and with two the decision stalls. A person can hold A and R on a small team, which fits the "inputs not headcount" point below (Source: [[raci-responsibility-assignment-matrix]]). Confidence medium: reference and community pages, not the PMBOK text.

## Implication

People bring inputs, not headcount. One person can hold Product and Design; the handoffs still exist and are still recorded, so an agent can pick up whichever input is missing. See [[Structured Handoff]] for the handoff format.
