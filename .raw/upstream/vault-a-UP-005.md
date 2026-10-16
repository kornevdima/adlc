---
report: vault-a/UP-005
title: "The footprint check flags dispatcher- and verifier-owned code-wiki records"
kind: bug
plugin_version: 1.0.7
status: ratified (2026-10-07)
exported: 2026-10-16
---

# vault-a/UP-005 The footprint check flags dispatcher- and verifier-owned code-wiki records

- **Key:** `vault-a/UP-005`
- **Kind:** bug
- **Target:** `skills/adlc/scripts/build_snapshot.py footprint` and `/adlc` Step 2.4a
- **Plugin version seen:** 1.0.7
- **Ratified by the vault's operator:** 2026-10-07

## What happened
The footprint check treats every non-test path that differs from the build snapshot as a tester violation. That includes the service's own code-wiki tree (`wiki/contracts/`, `wiki/verification/`, `wiki/reviews/`), which the dispatcher, the reviewer and the verifier write during a story by design. Each time, the dispatcher had to read the diff by hand to clear the flag.

## Evidence
Seen 6 times in one vault between 2026-10-05 and 2026-10-06:
- the dispatcher's own contract edit after the snapshot, not re-snapshotted (twice);
- a parallel verifier's baseline record;
- the reviewer's record written between the snapshot and the tester round (twice);
- the dispatcher's as-built edit to a contract.

## Proposed fix
- Exempt the service's code-wiki tree from the footprint, or take an `--exempt` glob list from the service AGENTS.md (like `--globs` for tests); or attribute paths by worker.
- Re-snapshot automatically after a dispatcher contract edit.

## Workaround in the reporting vault
The dispatcher re-snapshots after editing a contract and reads any flagged `wiki/` path by hand.
