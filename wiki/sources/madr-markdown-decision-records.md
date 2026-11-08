---
type: source
source_type: documentation
title: "MADR, Markdown Decision Records (4.0.0)"
author: ADR GitHub organisation (MADR project)
date_published: 2024-09-17
url: https://adr.github.io/madr/
confidence: high
key_claims:
  - "MADR 4.0.0 was released 2024-09-17; mandatory sections are title, context and problem statement, considered options, decision outcome."
  - "Status, date, decision-makers, consulted and informed go in optional YAML front matter."
  - "Drivers, consequences, confirmation, pros and cons, and more information are optional."
  - "The project's focus is architectural decisions but it can sustain any decision; do not read architecture too strictly."
tags:
  - source
  - decision-records
created: 2026-11-08
updated: 2026-11-08
---

# MADR, markdown decision records (4.0.0)

The main successor to Nygard's form ([[nygard-documenting-architecture-decisions]]). Release 4.0.0 is dated 2024-09-17, so current. Confidence: high (the project's own page). A search snippet said that since 3.0.0 the "A" means "Any"; the fetched page still says "Architectural" and states the focus is architectural decisions.

## What it adds to Nygard

- Considered options are mandatory, so the record shows what was rejected, not only what was chosen. (high)
- Front matter carries status (proposed, rejected, accepted, deprecated, superseded), date, decision-makers, consulted and informed. This adds a who and a review trail. (high)
- Optional confirmation says how compliance with the decision will be checked. (high)
- Variants exist: full, minimal, bare, bare-minimal. No directory layout is enforced; subfolders by category are suggested for large projects. (high)

## Scope

Examples on the page include technology and library choices and feature decisions. The project says the format can record any decision but its focus is architectural ones. That leaves room for a product decision record in the same format, kept apart from engineering ADRs. (medium: this reading is an inference, not a project statement)

See [[Lifecycle Artifacts and Decision Levels]].
