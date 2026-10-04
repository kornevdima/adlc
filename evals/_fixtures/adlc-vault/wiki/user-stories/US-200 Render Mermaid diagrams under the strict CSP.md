---
type: user-story
title: "US-200 Render Mermaid diagrams under the strict CSP"
status: ready
epic: EPIC-002
---

# US-200 Render Mermaid diagrams under the strict CSP

As a reader, I want Mermaid code blocks in a wiki page to show as diagrams, so I can read flowcharts without leaving the page.

## Acceptance criteria

1. A ```` ```mermaid ```` block renders as a diagram on the page.
2. The page keeps the strict CSP (DEC-007): no `'unsafe-inline'` for `style-src-elem`.

Spec: [[US-200 Mermaid tech notes]] (service code wiki).
