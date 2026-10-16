---
report: vault-a/UP-012
title: "Wrap-up doesn't check for workers or processes left alive"
kind: design (operator-approved)
plugin_version: 1.0.7
status: ratified (2026-10-10; the operator: 'we need to have a check in wrap-up for this')
exported: 2026-10-16
---

# vault-a/UP-012 Wrap-up doesn't check for workers or processes left alive

- **Key:** `vault-a/UP-012`
- **Kind:** design (operator-approved)
- **Target:** `skills/wrap-up/SKILL.md` (a new step before the Report), with a pointer from the `adlc` skill's Step 2 hand-back handling
- **Plugin version seen:** 1.0.7
- **Ratified by the vault's operator:** 2026-10-10; the operator: 'we need to have a check in wrap-up for this'

## What happened
- Every hand-back says "no background processes running", but nothing checks that claim at the session's end.
- A worker listed as running looks like it is still spending tokens.
- A live dev server, emulator or container holds ports, and the next session's e2e silently reuses it.

## Evidence
- 2026-10-09: a stray production server left on the e2e port made local e2e test an old build for a whole story.
- 2026-10-10: a builder's task stayed open in the panel for about 6 hours after its hand-back.
- The same family as vault-a/UP-006 (2026-10-04, 2026-10-05).
- 2026-10-16, plugin 1.0.7: the wrap-up skill still has no such step; the dispatcher ran the check by hand (it found only another session's processes, correctly left alone).

## Proposed fix
Add a wrap-up step, "Leave nothing running", before the Report:
1. List the agents and stop every subagent of this session that is listed as running but has already handed back. Report each one.
2. List the processes listening on the run's ports (the service AGENTS.md's dev, e2e and emulator ports, plus any recorded in the run ledger). Report each with its owner (cwd or command). Stop only processes this session started, by PID; anything else belongs to the operator or another session, so ask first.
3. List the containers of the service's compose project and stop the ones this session started. Never remove volumes.
4. One line in the wrap-up report: "Left running: none", or the list of what was left and why.

## Workaround in the reporting vault
The dispatcher runs these checks by hand at each hand-back and at wrap-up.
