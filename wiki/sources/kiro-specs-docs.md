---
type: source
source_type: documentation
title: "Kiro specs documentation"
author: Kiro (AWS)
date_published: 2026-11-08
url: https://kiro.dev/docs/specs/
confidence: medium
key_claims:
  - "A feature spec is three files: requirements.md (user stories and acceptance criteria), design.md (architecture, sequence diagrams, data flow, error handling, testing strategy) and tasks.md (trackable tasks Kiro updates as work proceeds)."
  - "A bugfix spec swaps requirements.md for bugfix.md: current, expected and unchanged behavior."
  - "The user reviews each phase in a Review view that takes comments on specific passages and sends them to Kiro together."
  - "Quick Spec generates all three files without approval gates, so the standard path has gates."
  - "The requirements file uses EARS phrasing (WHEN ... THE SYSTEM SHALL ...); this comes from the concepts and requirements-first pages seen only as search results."
created: 2026-11-08
updated: 2026-11-08
tags:
  - spec-driven
  - kiro
---

# Kiro specs documentation

The specs overview page defines a spec as three markdown files that move a feature from intent to tasks.

## The three files

- Requirements holds user stories and acceptance criteria. For a bug, a bugfix file holds the current, expected and unchanged behavior instead.
- Design holds the technical side: system and component design, sequence diagrams, data flow, error handling and the testing strategy.
- Tasks holds the implementation plan as trackable tasks that Kiro updates as it works.

## What the user does between files

The user moves through three phases and reviews the document of each phase before the next. A Review button opens a view where the user comments on specific passages and sends the comments to Kiro in one batch. Quick Spec produces all three files with no approval gates. The page does not spell out what exactly counts as approval at each step.

## Not on the page

The page does not describe EARS notation, hooks or steering files; they appear only as navigation entries. Search results from the same site's concepts page say the requirements file writes system behavior as event-driven SHALL statements, and third-party listings place a steering folder of standing context beside the spec. Treat hooks and steering as unsourced here.

(Source: [[kiro-specs-docs]])
