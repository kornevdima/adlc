---
type: user-story
title: "US-200 Render Mermaid diagrams under the strict CSP"
kind: feature
feature: "[[FEAT-002 Diagrams in pages]]"
epic: "[[EPIC-002 Wiki rendering]]"
sprint: "[[S07]]"
release: "[[R-1.0]]"
status: ready
created: 2026-09-22
ready: 2026-09-26
started: ""
done: ""
history:
  - "2026-09-22 draft"
  - "2026-09-26 ready"
size: M
priority: must
services:
  - web
depends_on: []
caused_by: ""
updated: 2026-09-26
---

# US-200 Render Mermaid diagrams under the strict CSP

As a reader, I want Mermaid code blocks in a wiki page to show as diagrams, so I can read flowcharts without leaving the page.

## Acceptance criteria

1. A ```` ```mermaid ```` block renders as a diagram on the page.
2. The page keeps the strict CSP (DEC-007): no `'unsafe-inline'` for `style-src-elem`.

Spec: [[US-200 Mermaid tech notes]] (service code wiki).
