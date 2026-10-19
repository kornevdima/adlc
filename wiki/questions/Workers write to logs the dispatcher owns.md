---
type: synthesis
title: "Workers write to logs the dispatcher owns"
created: 2026-10-20
updated: 2026-10-20
tags:
  - adlc
  - workers
  - feature-reviewer
  - feature-verifier
  - upstream
status: resolved
upstream: [vault-a/UP-021]
related:
  - "[[Integrate the wiki toolset into the ADLC workers]]"
  - "[[Workers and processes left running after hand-back]]"
---

# Workers write to logs the dispatcher owns

**Opened from** vault-a UP-021 (proposed 2026-10-20; three occurrence rows from 2026-10-17 and 2026-10-19). The operator asked for fixes on 2026-10-20.

**Outcome:** a worker's output is its record page and the path in its report; every `log.md`, `hot.md` and board line is written by the dispatcher.

## What happened (seen 3×)

- 2026-10-17 and 2026-10-19: a reviewer appended a pointer to `wiki/log.md` in a code wiki that keeps no log, and so created the file. The dispatcher removed it both times.
- 2026-10-19: a verifier added a line to the product wiki's `wiki/log.md`.

The generic reviewer and verifier said "append a one-line pointer to the wiki log". That rule was written for a single-wiki vault. In a multi-repo vault the log belongs to the dispatcher (product wiki) or doesn't exist (code wiki). The vault's workaround was a packet line, "do not create or write `wiki/log.md`", in every dispatch.

## Resolution (2026-10-20, unreleased)

- **`feature-reviewer`** § Register in the wiki and **`feature-verifier`** step 9: write the record, report its path; the dispatcher writes the log pointer. Never create or write `log.md`, `hot.md` or mission control in either wiki. The reviewer's tool line no longer mentions a log pointer.
- **`feature-tester`, `devops`, `scope-analyst`:** the same Don't (the tester's coverage ledger and the devops deploy record are their records; `doc-writer` and `feature-builder` already had it).
- **`/adlc` Step 2 § After every hand-back:** the dispatcher logs what the worker reported, the pointer line and the board row.
- **`technical-planning.md`** "Records are pages; log entries are pointers" now ends with "and the dispatcher writes them".

## Open

- Vault-side after 1.0.8: the packet line and the local bindings' copy of it come out.
