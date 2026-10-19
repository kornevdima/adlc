---
type: synthesis
title: "Tester edits app code to prove a test bites"
created: 2026-10-04
updated: 2026-10-20
tags:
  - adlc
  - workers
  - feature-tester
  - dispatcher
  - upstream
status: resolved
upstream: [vault-a/UP-003, vault-a/UP-004, vault-a/UP-005, vault-d/UP-002]
related:
  - "[[Parallel builder and tester revert each other's edits]]"
  - "[[Dispatcher rules for writing ruling questions]]"
  - "[[Plugin eval suites for claude plugin eval]]"
---

# Tester edits app code to prove a test bites

**Opened from** a vault-a epic run (operator, 2026-10-04: "Good", on the shaped proposal). The source is the run ledger's Carry-forward section (uncommitted) and the correction-log row of 2026-10-04 in the vault's operator profile. It was staged "for the epic's distill", so it reached this backlog only on 2026-10-04 when the operator pointed at it. It was missed the first time because the review of new proposals only looked in this repo. That miss is the evidence for [[Upstream channel from vaults to the plugin]].

**Outcome:** an app edit by the tester can't slip through, even one it reverts byte for byte. The builder's work stays attributable to the builder.

## What happened (seen 2× in one epic)

| Story | What the tester did | The record |
|---|---|---|
| the first story | a one-line app fix; the edit was blocked | the run ledger |
| a later story | dropped a column from a database filter to make a new integration test fail, then reverted that line by hand; the dispatcher confirmed the filter intact in the source | the run ledger |

Both broke the service's own "never modify app code" rule, plus the operator's ruling from an earlier sprint: "in-run mutation, not file edits to uncommitted code". Neither the reviewer nor the verifier could catch it: the reviewer sees only the final diff, and the verifier checks outcomes. **The plugin's own tester allowed it:** `agents/feature-tester.md` said "a temporary mutation to prove a spec bites is the one exception".

## The design (shaped with the operator)

- **Snapshot:** after each builder round, the dispatcher records the working tree as `refs/adlc/<story>/build-<n>`. It goes through a temporary `GIT_INDEX_FILE` (`add -A`, `write-tree`, `commit-tree`). The working tree, the index and the branch are untouched, and nothing is pushed.
- **Footprint check:** after each tester round, every path that differs from the snapshot must match the test globs. Defaults: `*.test.*`, `*.spec.*`, `*.itest.*`, `tests/**` and `e2e/**`; AGENTS.md can override them. A modification-time check catches an edit that was made and then reverted. A violation stops the story for a ruling. Restore from the snapshot ref, never from a copy. Delete the refs at the story commit.
- **Why a snapshot, not a builder commit:** the branch keeps only verified commits, one per story. The builder's and the tester's changes stay attributable, and workers still never commit.

## Resolution (2026-10-04, unreleased)

- `skills/adlc/scripts/build_snapshot.py`: `snapshot`, `footprint`, `restore`, `clean`. Stdlib only.
  - The exact snapshot time is stored in the commit message, because the commit date has one-second resolution.
  - Exit codes: 0 clean, 1 violation, 2 bad input.
  - Tested in a scratch repo on these paths:
    - the tester adds only tests: clean;
    - the edit-then-revert from the second row: caught as "rewritten";
    - an app edit left in place: caught;
    - `restore` leaves the index untouched;
    - a second round, custom globs and `clean` all work;
    - a missing snapshot and a bad story id exit 2.
- `/adlc` Step 2:
  - **3a** snapshot after every builder round;
  - **4a** footprint check after every tester round, including the parallel case (the builder's reported paths count as the builder's);
  - **7** `clean` at the story commit.
- `agents/feature-tester.md`: **never modify app code, not even for a moment**. The tester proves a test bites in the run (a fixture, a scoped filter argument, `page.route`, an env flag the app reads). Otherwise it reports `bite: not proven in-run`, and the file mutation is left to the dispatcher's post-commit spot-check. The "undo your own temporary edits" rule now covers test files only.
- `technical-planning.md` dispatcher rule: check what each worker touched, not only what it reports.
- `permissions.md`: the script is allow-listed, like `relink.py`.
- `project-profile`: the AGENTS.md template gains a "Test globs" line.

## Follow-up: the footprint flags code-wiki records (vault-a/UP-005)

Reported 2026-10-16 (`.raw/upstream/vault-a-UP-005.md`, ratified 2026-10-07). In the field, the check flagged paths in the service's code wiki 6×: the dispatcher's own contract edits after the snapshot, a parallel verifier's baseline record and the reviewer's record. Those roles write there during a story by design. Each time the dispatcher had to read the diff by hand to clear the flag.

**Resolution (2026-10-17, unreleased):** `footprint` takes `--exempt` globs, default `wiki/**`. Exempt paths are listed with a count and never count as a violation; `--exempt` with no globs turns the exemption off. `/adlc` Step 2.4a says so and names an AGENTS.md "Footprint exempt" line for services that keep records elsewhere. With the code wiki exempt, re-snapshotting after a contract edit is no longer needed. Tested in a scratch repo: a contract edit plus a new spec is clean; an app edit is still a violation; `--exempt` with no globs flags the contract again.

**The same report from a second vault (vault-d/UP-002, 2026-10-20):** in a repo whose wiki sits next to the code, `footprint` flagged the tester's coverage ledger (`wiki/coverage/_index.md`, which its rules require it to write) and once the dispatcher's own run ledger under `wiki/sprints/`. The default `wiki/**` exemption covers both; a vault whose wiki root is not `wiki/` passes it as `--exempt`. Closed under 1.0.8 with no further change. Vault-a also saw UP-005 three more times on the installed 1.0.7 (2026-10-17 and 2026-10-19), with `--globs ... 'wiki/**'` as the workaround until the release.

## Open

- **Field test:** the next `/adlc` run in vault-a, after the release. After 1.0.8 the vault's workaround (re-snapshot after a contract edit, read flagged `wiki/` paths by hand) comes out. A false "rewritten" may come from files the suite regenerates (for example `next-env.d.ts`); list them in the service's Test globs line.
- **Vault-side:**
  - redeploy `feature-tester.md` to `<service>/.claude/agents/`. The local copy already has the plain rule, which didn't hold; the check is what's new;
  - add the `build_snapshot.py` allow rule;
  - drop the ledger's distill item once it is shipped.
- No eval case yet. A case would need a worker dispatch (slow). The script is checked directly.
