---
type: synthesis
title: "Tester edits app code to prove a test bites"
created: 2026-10-04
updated: 2026-10-04
tags:
  - adlc
  - workers
  - feature-tester
  - dispatcher
  - upstream
status: resolved
upstream: [vault-a/UP-003, vault-a/UP-004]
related:
  - "[[Parallel builder and tester revert each other's edits]]"
  - "[[Dispatcher rules for writing ruling questions]]"
  - "[[Plugin eval suites for claude plugin eval]]"
---

# Tester edits app code to prove a test bites

**Opened from** the vault-a EPIC-002 run (operator, 2026-10-04: "Good", on the shaped proposal). The source is the run ledger's Carry-forward (`wiki/sprints/_run EPIC-002.md:157-160`, uncommitted) and correction-log row 2026-10-04 in `wiki/meta/operator-profile.md`. It was staged "for the EPIC-002 distill", so it reached this backlog only on 2026-10-04 when the operator pointed at it. It was missed the first time because the review of new proposals only looked in this repo. That miss is the evidence for [[Upstream channel from vaults to the plugin]].

**Outcome:** an app edit by the tester can't slip through, even one it reverts byte for byte. The builder's work stays attributable to the builder.

## What happened (seen 2× in one epic)

| Story | What the tester did | The record |
|---|---|---|
| US-175 | a one-line app fix; the edit was blocked | `_run EPIC-002.md:130` |
| US-179 | dropped `expires_at` from `pendingInviteCountFilter` to make a new itest fail, then reverted that line by hand; the dispatcher confirmed the filter intact (`src/db/invites.ts:344`) | `_run EPIC-002.md:130` |

Both broke the service's own "never modify app code" rule, plus the operator's ruling from S08: "in-run mutation, not file edits to uncommitted code" (BUG-027, US-199). Neither the reviewer nor the verifier could catch it: the reviewer sees only the final diff, and the verifier checks outcomes. **The plugin's own tester allowed it:** `agents/feature-tester.md` said "a temporary mutation to prove a spec bites is the one exception".

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
    - the US-179 edit-then-revert: caught as "rewritten";
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

## Open

- **Field test:** the next `/adlc` run in vault-a, after the release. A false "rewritten" may come from files the suite regenerates (for example `next-env.d.ts`); list them in the service's Test globs line.
- **Vault-side:**
  - redeploy `feature-tester.md` to `<service>/.claude/agents/`. The local copy already has the plain rule, which didn't hold; the check is what's new;
  - add the `build_snapshot.py` allow rule;
  - drop the ledger's distill item once it is shipped.
- No eval case yet. A case would need a worker dispatch (slow). The script is checked directly.
