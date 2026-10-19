---
type: synthesis
title: "Parallel builder and tester revert each other's edits"
created: 2026-10-02
updated: 2026-10-02
tags:
  - adlc
  - plugin
  - workers
  - dispatch
  - distill
status: resolved
related:
  - "[[Upstream channel from vaults to the plugin]]"
  - "[[Wiki maintenance edits blocked in ADLC vaults]]"
  - "[[Integrate the wiki toolset into the ADLC workers]]"
---

# Parallel builder and tester revert each other's edits

**Opened from live use** (vault-a, one story of one sprint, 2026-10-02). It is a lost-edit bug: a worker's change disappeared and no worker reported it.

## What happened

1. The dispatcher ran `feature-builder` and `feature-tester` for the same story **at the same time**.
2. The tester saved a copy of a source file before mutating it, to check that a test catches the break.
3. The builder then edited the same file (a comment rewrap).
4. The tester restored the file by copying its saved copy back. That silently undid the builder's edit.
5. Neither worker reported it. The dispatcher noticed the missing change and re-applied it.

## Where the fix landed: one service only

- The vault recorded it as a dispatch lesson on the epic's as-built page.
- The epic-close distill wrote the rule into three of the service's local worker bindings under `<service>/.claude/agents/` (tester, verifier, reviewer). The rule: restore by undoing your own edit, then check `git diff`; never copy back a snapshot taken before the run.
- **The plugin has none of it:**
  - `skills/adlc/SKILL.md` Step 2 lists build (3), then test (4). It never says whether they may run at the same time, so the dispatcher chose to.
  - The generic `agents/feature-tester.md`, `feature-verifier.md` and `feature-reviewer.md` say nothing about how to restore a temporary change.

## Root causes

- **A. The dispatch order is not stated.** Step 2 does not say that workers on the same story must not edit the same files at the same time. That covers build → test and also the fix loop in step 5 (builder and tester both get findings).
- **B. Snapshot restore is unsafe whenever someone else can write.** Copying back a saved file reverts every change made since, not just your own.
- **C. Distill only goes down, never up.** Step 4.4 folds lessons into the repo-local workers and nowhere else. A lesson that applies to every service has no route back to the plugin's generic workers, so every other vault can hit it again. This is why the fix stayed in one service.

## Proposed fix (to rule on before building)

1. **adlc Step 2:** run a builder and a tester for the same story one after the other. Parallel is allowed only when their file sets don't overlap. The same applies to the step 5 fix rounds.
2. **Generic tester, verifier and reviewer:** a temporary change (a mutation to check a test bites, a debug edit) is undone by reverting your own edit and confirmed with `git diff`. Never restore from a copy taken earlier.
3. **Distill (Step 4.4):** mark each lesson service-specific or general. General lessons go into a plugin follow-up (an open task here, or a proposed edit to the generic worker), not only into the local file.

## Done when

- Step 2 states the ordering rule, including for fix rounds;
- the three generic workers carry the restore rule;
- Step 4.4 has an upstream route for general lessons.

## Resolution (2026-10-02)

All three proposals built as written:
- `skills/adlc/SKILL.md` Step 2.4: builder and tester take turns on shared files, also in the step 5 fix rounds. Step 2.7: the dispatcher's mutation spot-check follows the same restore rule.
- `agents/feature-tester.md`, `feature-verifier.md`, `feature-reviewer.md`: a strict rule to undo your own temporary edit and check `git diff`, never restore a snapshot. The tester's "never modify app code" now names the temporary mutation as its one exception.
- Step 4.4: each distilled lesson is marked service-specific or general; general ones go to the operator as proposed plugin text.

Not yet field-tested. Ships with the next plugin version bump.

**Gap C reopened (2026-10-04).** "Tell the operator" was a conversation, not a route: the next general lesson waited in a vault's ledger until the operator pointed at it. The route is now [[Upstream channel from vaults to the plugin]].

## Evidence

- Vault-a: the epic's as-built page, the "Dispatch lesson" entry of 2026-10-02.
- The service's local worker bindings for the tester, verifier and reviewer.
