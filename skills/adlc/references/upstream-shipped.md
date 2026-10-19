# Upstream reports shipped

Consumer vaults read this from the installed plugin to close their `sent` entries in `wiki/meta/adlc-upstream.md` (format: `skills/wiki/references/adlc-upstream.md` § Closing the loop). A release adds one row per report it resolves. Rows are never removed.

| Report key | Shipped in | What changed |
|---|---|---|
| vault-a/UP-001 | 1.0.7 | `/adlc` Step 2 § Writing a ruling question: source every premise |
| vault-a/UP-002 | 1.0.7 | the same section: outcome first, one decision per question |
| vault-a/UP-003 | 1.0.7 | `feature-tester`: never edits app code, not even temporarily; proves a bite in-run |
| vault-a/UP-004 | 1.0.7 | `/adlc` Step 2.3a / 2.4a: `build_snapshot.py` snapshot and footprint check |
| vault-a/UP-005 | 1.0.8 | `build_snapshot.py footprint --exempt` (default `wiki/**`): code-wiki records never count as violations; `/adlc` Step 2.4a |
| vault-a/UP-006 | 1.0.8 | workers: leave nothing running (stop by PID, never `pkill`), `Left running:` in the report; `/adlc` Step 2 § After every hand-back |
| vault-a/UP-007 | 1.0.8 | `feature-tester`, `feature-verifier`: § Check the instrument can see the property |
| vault-a/UP-008 | 1.0.8 | `feature-tester`, `feature-verifier` step 6: connection failures across files mean the dev server; restart once, rerun the failed files |
| vault-a/UP-009 | 1.0.8 | `/adlc` Step 2.2, `feature-tester`, `feature-verifier`: name the direct runner when an instrument takes flags |
| vault-a/UP-010 | 1.0.8 | `/adlc` Step 2 § Claiming a cause or a fix |
| vault-a/UP-012 | 1.0.8 | `wrap-up` step 7c: leave nothing running |
| vault-a/UP-013 | 1.0.8 | workers never read `.env*` or resolved config; `permissions.md` deny rules plus the `guard_env.py` PreToolUse hook (`skills/wiki/scripts/`) |
| vault-a/UP-014 | 1.0.8 | `/adlc` Step 2.2: state the outcome, not the mechanism; side effects of a ruling go into the ruling question |
| vault-a/UP-015 | 1.0.8 | `/adlc` Step 2.6: the dispatcher runs lint, typecheck and unit before dispatching the verifier |
| vault-a/UP-016 | 1.0.8 | `feature-builder`, `feature-tester`: run every gate that covers a changed file, exit codes without a pipe; `/adlc` Step 2 § Accepting a hand-back |
| vault-a/UP-017 | 1.0.8 | `scope-analyst` census item 7, `/adlc` Step 0.3 and 2.2: every grilling ruling maps to a contract row; unmapped stops the loop |
| vault-a/UP-018 | 1.0.8 | `/adlc` Step 2.2 and `scope-analyst` item 8: the contract lists every reader of a moved source; `feature-reviewer` dimension 8 checks it |
| vault-a/UP-019 | 1.0.8 | `/adlc` Step 2 § Findings rule: a bug page only after the cause is read in the code or reproduced |
| vault-a/UP-020 | 1.0.8 | `/adlc` Before Starting 2: the run's state is read from the ledgers and `git log`, never remembered; re-read after a resume, compaction or rewind |
| vault-a/UP-021 | 1.0.8 | all workers: never write `log.md`, `hot.md` or mission control; the dispatcher logs the record path from the report |
| vault-d/UP-001 | 1.0.8 | `feature-tester`, `feature-verifier` § Shared environment: no long-lived service as a background child; compose, detached, or `ENV_MISMATCH`. The reporting vault's ledger still carries its directory name as the key (created under the pre-1.0.7 template); it is listed here as `vault-d` and should re-key |
| vault-d/UP-002 | 1.0.8 | the same change as vault-a/UP-005: `footprint --exempt`, default `wiki/**` (covers the coverage ledger and the run ledger in a co-located wiki) |
| vault-d/UP-003 | 1.0.8 | `/adlc` Step 2.2: every named UI state, key, label or list is checked against the code before dispatch, or marked `[UNVERIFIED]` |
| vault-b/UP-001 | 1.0.8 | `writing-style.md` § Sentences, Dashes: replace the character, keep the sentence; the two exceptions spelled out |
| vault-b/UP-002 | 1.0.8 | `writing-style.md` § Corrections and `technical-writer` § After the edit: a correction is a pattern, not a line |
| vault-b/UP-003 | 1.0.8 | `writing-style.md` § Facts: links are claims, checked on the deployed target with the date |
| vault-b/UP-004 | 1.0.8 | `writing-style.md` § Tasks for the reader: the least that unblocks us, the rest in parallel |
| vault-b/UP-005 | 1.0.8 | new `skills/wiki/references/writing-style.md` (audience, sentences, identifiers, structure, facts, questions, change reports), read by `technical-writer`, `doc-writer`, `ba-suite-subagent`, the `/adlc` and `wrap-up` reports and the vault AGENTS.md § Writing |
| vault-c/UP-001 | 1.0.8 | `technical-writer` skill (first drafted as `client-docs`): documents for a human reader and their translations; operator profile § Writing (was "Client documents") and § Translation. The reporting vault's ledger uses the key `vault-b`, already taken by another vault; it is listed here as `vault-c` and should re-key |
