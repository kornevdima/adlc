---
type: synthesis
title: "Hand-backs without the gates that cover the change"
created: 2026-10-20
updated: 2026-10-20
tags:
  - adlc
  - dispatcher
  - feature-builder
  - feature-tester
  - upstream
status: resolved
upstream: [vault-a/UP-015, vault-a/UP-016]
related:
  - "[[Structured Handoff]]"
  - "[[Tester edits app code to prove a test bites]]"
---

# Hand-backs without the gates that cover the change

**Opened from** vault-a UP-015 and UP-016 (proposed 2026-10-20, one sprint's evidence), plus three vault-d occurrence rows of the same family. The operator asked for fixes on 2026-10-20.

**Outcome:** a worker's green means the gates that cover its change ran and exited 0, and a defect a one-minute run can see never waits for a fifteen-minute verify.

## What happened

- **UP-016, 4× in one sprint.** A tester reported "full e2e 144/0" while a unit guard was red (it never ran unit). The same tester left an unused import, and the verify failed at lint. Another tester skipped typecheck (the test runner doesn't typecheck), and a wrong type in its new spec reached the verify. A builder changed how the server reads a test-only config file, ran `build` but no e2e, and seven e2e specs failed in the verify. Each worker ran the checks it thought of, not the gates that cover the files it touched. The generic workers said "run the service's gates" without tying the gate to the change.
- **UP-015, 3× in the same sprint.** Each of those defects was visible to lint + typecheck + unit in about a minute and surfaced only in the verify (15 to 18 minutes) or in review. Under `on_fail: stop`, two of them ended the run.
- **vault-d occurrences (2026-10-09 and 2026-10-16):** builders reported "exit 0" read from `cmd | tail`, which is tail's exit code; a tester's whole final report was the word "placeholder" (its work was in the tree, with no evidence), and the dispatcher re-ran the spec itself; a mutation spot-check reverted with a `sed` that matched a second, legitimate line, caught only by the snapshot diff.

## Resolution (2026-10-20, unreleased)

- **`feature-builder` step 6 and `feature-tester` step 6:** run every gate that covers a file you changed: lint and typecheck for any source or test file, the unit suite for any unit or guard test in the repo, and (builder) the one existing e2e spec that exercises a change to runtime configuration, a server file read or test setup, through the wired runner. The builder may run an existing e2e spec as that gate; it still never authors one. Reports carry each exit code captured without a pipe; a report without them is incomplete and comes back.
- **`/adlc` Step 2 § Accepting a hand-back:** the dispatcher accepts a hand-back only with the covering gates' exit codes; an empty or placeholder report goes back to the worker and the gap is never filled by trusting the tree.
- **`/adlc` Step 2.6:** the dispatcher runs lint, typecheck and unit itself for every package the story touched before dispatching the verifier; a non-zero exit goes back to the owning worker, and the verify waits. Same command set as the Step 2.7 re-verify.
- **`/adlc` Step 2.7:** for a file the branch doesn't have yet, compare with `git show refs/adlc/<ID>/build-<n>:<path> | diff - <path>`; prefer line-addressed edits for the mutation.
- **`technical-planning.md`:** the "Handoffs carry evidence" rule now names the covering gates and the no-pipe capture; a new "Run the cheap gates before the verify" rule.

## Open

- Vault-side after 1.0.8: the gate table in the local worker bindings stays (it names the service's commands); the packet lines that list the gates can come out.
- No eval case; the rule is in worker and dispatcher text.
