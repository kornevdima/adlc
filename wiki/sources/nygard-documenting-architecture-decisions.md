---
type: source
source_type: article
title: "Documenting Architecture Decisions (Nygard, 2011)"
author: Michael Nygard
date_published: 2011-11-15
url: https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions
confidence: high
stale: true
key_claims:
  - "An architecture decision record is a short text file capturing one significant decision, its forces and its consequences."
  - "Sections are title, context, decision, status, consequences."
  - "Architecturally significant means structure, non-functional characteristics, dependencies, interfaces or construction techniques."
  - "Records live in the repository, are numbered sequentially, never reused and never deleted; a reversed decision is marked superseded."
tags:
  - source
  - decision-records
created: 2026-11-08
updated: 2026-11-08
---

# Documenting architecture decisions (Nygard, 2011)

The original post that named the architecture decision record (ADR). Published 2011-11-15, so older than three years and potentially stale as a date, but it is the foundational definition and later templates still follow it. Confidence: high for the definition, since it is the primary source.

## What it says

- An ADR is a short text file for one significant decision. It keeps the forces behind the choice so a later developer can judge whether it still applies, instead of accepting or reversing it blindly. (high)
- Five parts: title (a short noun phrase), context (technical, political, social and project-local forces, stated as facts), decision (full sentences, "We will ..."), status (proposed, accepted, deprecated, superseded), consequences (positive, negative and neutral results). (high)
- Scope test: a decision is architecturally significant when it affects structure, non-functional characteristics, dependencies, interfaces or construction techniques. (high)
- Format: Markdown or similar, kept in the project repository, numbered sequentially, numbers never reused. A reversed decision stays in place and is marked superseded, with a pointer to its replacement. (high)

## Use in this wiki

The test of "significant" and the rule "never delete, supersede" are the basis of [[Lifecycle Artifacts and Decision Levels]]. Successor template: [[madr-markdown-decision-records]].
