---
report: vault-a/UP-007
title: "UI measurements trust instruments that can't see the property"
kind: improvement
plugin_version: 1.0.7
status: ratified (2026-10-07)
exported: 2026-10-16
---

# vault-a/UP-007 UI measurements trust instruments that can't see the property

- **Key:** `vault-a/UP-007`
- **Kind:** improvement
- **Target:** `agents/feature-tester.md` and `agents/feature-verifier.md` (a measurement-traps rule)
- **Plugin version seen:** 1.0.7
- **Ratified by the vault's operator:** 2026-10-07

## What happened
Each time, a worker's first UI measurement passed or failed for a reason the instrument could not see; a later probe found it.

## Evidence
Seen 5 times in one epic:
- an ancestor clipped overflow, so page scroll hid a box that didn't wrap;
- `document.elementFromPoint` skips `inert` subtrees, so an overlap check passed;
- an accessibility checker reported "incomplete" on gradient text (152 nodes) and it was read as a pass;
- an element screenshot at a fractional x showed a page-coloured column 0;
- the computed size of a `::before` returned the declared size for a collapsed box.

## Proposed fix
Generic rule in the tester and verifier: "Before trusting a UI measurement, check the instrument can see the property: clip screenshots to the snapped box, measure pseudo-elements by layout, measure overlap by boxes (hit-tests skip `inert`), assert an element's own overflow, and treat an accessibility tool's 'incomplete' as unmeasured, never as a pass."

## Workaround in the reporting vault
A measurement-traps bullet in the service's local tester and verifier bindings.
