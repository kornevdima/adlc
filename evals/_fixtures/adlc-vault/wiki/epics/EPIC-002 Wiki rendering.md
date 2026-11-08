---
type: epic
title: "EPIC-002 Wiki rendering"
status: active
release: "[[R-1.0]]"
feature: "[[FEAT-002 Diagrams in pages]]"
created: 2026-09-20
started: 2026-09-25
done: ""
tags:
  - epic
---

# EPIC-002 Wiki rendering

Readers see a wiki page with its diagrams and code rendered, under the strict content security policy the site already enforces.

## Rulings

Rulings from the grilling session, one row each; the story column says where each one is built.

| Date | Ruling | Story | Decided by | Evidence |
|---|---|---|---|---|
| 2026-09-25 | The strict CSP stays; no `'unsafe-inline'` for styles or scripts | [[US-200 Render Mermaid diagrams under the strict CSP]] | product owner | DEC-007 |

## Gates

One decision line per checkpoint; the artifacts are in the service code wiki.

| Gate | Verdict | Date | Decided by | Evidence | Conditions |
|---|---|---|---|---|---|
| 1 Requirements | go | 2026-09-22 | product owner | the requirements register approval pack | none |
| 1.5 Domain | go | 2026-09-24 | architect | [[US-200 Mermaid tech notes]] | none |
| 2 Decisions | hold | 2026-09-25 | architect | | the rendering mechanism (nonce, template, blob or sandbox) is not decided; a ruling or a spike settles it |
| 3 Workflow | | | | | |
