---
type: synthesis
title: "Verification instruments that miss what they measure"
created: 2026-10-17
updated: 2026-10-20
tags:
  - adlc
  - workers
  - feature-tester
  - feature-verifier
  - upstream
status: resolved
upstream: [vault-a/UP-007, vault-a/UP-008, vault-a/UP-009]
related:
  - "[[Tester edits app code to prove a test bites]]"
  - "[[Dispatcher rules for writing ruling questions]]"
---

# Verification instruments that miss what they measure

**Opened from** three upstream reports from vault-a, all ratified 2026-10-07 (`.raw/upstream/vault-a-UP-007.md`, `-008.md`, `-009.md`). Each one is a check that passed or failed for a reason the instrument couldn't see. The vault had fixed them only in its local worker bindings.

**Outcome:** a tester's or verifier's verdict rests on an instrument that can see the property, and an environment failure is never filed as a code failure.

## The three lessons

| Report | What happened | Seen |
|---|---|---|
| UP-007 | UI measurements: an ancestor clipped overflow, so page scroll hid a box that didn't wrap; `elementFromPoint` skips `inert` subtrees, so an overlap check passed; an accessibility checker's "incomplete" on gradient text (152 nodes) was read as a pass; an element screenshot at a fractional x showed a page-coloured column 0; the computed size of a collapsed `::before` returned its declared size | 5× in one epic |
| UP-008 | A long full e2e run exhausted a Next.js dev server. Many unrelated files failed with connection errors (one round: 21 failures in 10 files, all green after one restart). Workers re-ran everything or filed each failure as a new flake. The verifier's step 6 allowed only one restart for one scenario | 15+ in one epic |
| UP-009 | A contract named a wrapper script as the instrument; `npm run <script> -- -g <pattern>` lost `-g` through a nested `npm run`, so the whole suite ran | 2× |

## Resolution (2026-10-17, unreleased)

- `agents/feature-tester.md` and `agents/feature-verifier.md`:
  - a section **"Check the instrument can see the property"** with the five traps;
  - the connection-failure rule: read the dev server's log, restart it once, rerun only the failed files and record both runs; assertion failures are never retried into green (in the verifier, under step 6);
  - run a filtered suite with the direct runner and the environment it needs, and check the test count matches the filter.
- `/adlc` Step 2.2 (name the instrument): when the instrument takes flags, the contract names the direct runner command, not a wrapper script.

## Recurrence: three more forms (vault-a, 2026-10-17)

An occurrence row, not an entry, folded in on 2026-10-20 because it extends the same list: jsdom DOM tests "passed" a CSS outline override that lost to an unlayered theme rule in a real browser; previews used short columns, so a full-height readout went off-screen only on real pages; e2e printed in fresh pages (`emulateMedia`, `page.pdf`) and never print-then-return in one page. Added to the tester's and verifier's § Check the instrument can see the property: prove styling in a real browser, measure on content as tall as real pages, drive the app's own controls and round trips.

## Open

- Vault-side: remove the measurement-traps and terrain bullets from the local bindings once 1.0.8 is installed. Keep the service-specific details (which dev server, which port).
- No eval case. These are worker rules; a case would need a worker dispatch.
