---
type: source
source_type: documentation
title: "ProductPlan, product requirements document"
author: ProductPlan
date_published: unknown
url: https://www.productplan.com/glossary/product-requirements-document/
confidence: high
key_claims:
  - "A PRD is the document of record for a release: what is not in it is not in the release."
  - "It must include every explicit capability required, each with a use case that informs testing."
  - "It also holds an overview of release goals, non-functional requirements, assumptions, constraints and dependencies."
  - "It describes needs, not solutions, and may not dictate a specific implementation."
  - "Engineering writes the functional specification; UX design and QA test plans follow after the PRD is accepted."
tags:
  - source
  - requirements
created: 2026-11-08
updated: 2026-11-08
---

# ProductPlan, product requirements document

Fetched in full. The Atlassian PRD guide returned only navigation text, so this glossary entry stands in as the primary for the PRD row. Confidence: high for what a PRD contains and where it stops.

## What it says

The PRD is the record of what a release must deliver. Each capability carries a use case, so testers know what to check. It adds non-functional requirements (supported environments, usability), assumptions, constraints and dependencies.

The PRD leaves the how to engineering. It may suggest an approach to illustrate a use case but does not prescribe one. Engineering then writes the functional specification, which describes how each PRD item will be implemented. UX design and QA test plans are made by other teams once the PRD is accepted.

## Use in the wiki

It backs the Discover row of [[Lifecycle Artifacts and Decision Levels]] and the split between product decisions (PRD) and engineering decisions (ADRs). It also shows that the test plan is downstream of the PRD, not part of it.
