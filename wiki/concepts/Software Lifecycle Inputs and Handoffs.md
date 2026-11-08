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
  - "[[Structured Handoff]]"
---

# Software lifecycle inputs and handoffs

Every framework names the same few inputs under different titles. A small team folds several inputs into one person; a large organization splits them into groups. The inputs are the stable part, the job titles are not.

## The inputs and what each produces

| Input | Produces | Consumes | Scrum | Shape Up | SAFe (medium, secondary sources) |
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

- SAFe splits product work across Product Management (program backlog), Product Owner (team backlog), System Architect (technical direction) and Release Train Engineer (coordination), with Business Owners agreeing objectives. Confidence medium: the official page fetched covered only Agile Teams, so the split rests on secondary summaries.
- Team Topologies organizes teams, not individuals: stream-aligned, platform, enabling and complicated-subsystem teams, linked by collaboration, X-as-a-Service and facilitating interaction modes. Its handoff is a service boundary between teams. Confidence medium: seen through search excerpts of the official site, including a February 2025 post.
- RACI was not researched in this pass. It assigns Responsible, Accountable, Consulted and Informed per artifact and is the usual way to record the table above.

## Implication

People bring inputs, not headcount. One person can hold Product and Design; the handoffs still exist and are still recorded, so an agent can pick up whichever input is missing. See [[Structured Handoff]] for the handoff format.
