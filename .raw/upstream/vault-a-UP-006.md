---
report: vault-a/UP-006
title: "Workers stay alive after their hand-back"
kind: bug
plugin_version: 1.0.7
status: ratified (2026-10-07)
exported: 2026-10-16
---

# vault-a/UP-006 Workers stay alive after their hand-back

- **Key:** `vault-a/UP-006`
- **Kind:** bug
- **Target:** the generic workers (verifier first) and `/adlc` Step 2
- **Plugin version seen:** 1.0.7
- **Ratified by the vault's operator:** 2026-10-07

## What happened
A worker hands back (the harness shows "stopped with background work of its own still running") and stays listed as live. Nothing on the dispatcher side checks. A worker listed as running looks like it is still spending tokens, and a process it left (a dev server, a wait loop) can hold ports.

## Evidence
Seen 5 times in one vault, 2026-10-04 to 2026-10-08: two verifiers, two testers (one left an idle wait-loop shell wrapper; one showed as running for about 7 hours with no live process), and two builders in one story, plus a fix-round report lost after a resume.

## Proposed fix
- Workers end every background process they started before handing back (a Don't in each generic worker).
- After every hand-back, the dispatcher checks the agent list and stops a worker that is still live once its report is filed.

## Workaround in the reporting vault
Every dispatch packet says "before handing back, make sure no process or browser you started is still running"; the dispatcher checks the agent list after hand-backs.
