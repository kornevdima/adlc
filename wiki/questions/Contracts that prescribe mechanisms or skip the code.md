---
type: synthesis
title: "Contracts that prescribe mechanisms or skip the code"
created: 2026-10-20
updated: 2026-10-20
tags:
  - adlc
  - dispatcher
  - scope-analyst
  - feature-reviewer
  - upstream
status: resolved
upstream: [vault-a/UP-014, vault-a/UP-017, vault-a/UP-018, vault-d/UP-003]
related:
  - "[[Dispatcher rules for writing ruling questions]]"
  - "[[Verification instruments that miss what they measure]]"
---

# Contracts that prescribe mechanisms or skip the code

**Opened from** four upstream entries about the same artefact, the verification contract the dispatcher writes in `/adlc` Step 2.2 and the packets built from it: vault-a UP-014, UP-017 and UP-018 (proposed 2026-10-17 to 2026-10-20) and vault-d UP-003 (proposed 2026-10-16). The operator asked for fixes on 2026-10-20.

**Outcome:** a contract says what must be true afterwards, every fact it names has been read in the code, every reader of a source the story moves is accounted for, and every grilling ruling has a row that builds it.

## The four lessons

| Report | What happened | Seen |
|---|---|---|
| vault-a/UP-014 | Packets prescribed a mechanism, not an outcome. "Blur the grip at drag end" also blurred after a click, and keyboard resizing stopped (the operator: "now i can't resize using keyboard"). The ruling "print should always render A4" became "`@page size` on every print", which hid the browser's orientation control. Three more rounds followed the first | 2× in one session |
| vault-d/UP-003 | Scenarios named UI states, keys and lists nobody had checked: a disabled button on a page the role's scope hides, six refusal reasons where the server has seven, a label the catalogue spells differently. Workers caught all three, one test round each | 3× in one run |
| vault-a/UP-018 | A source migration split across three stories. The first story's contract named the editor and the save check, not the other readers of the old source. Review found a role that could be saved but not assigned; after the fix, a role was assignable but did not open the app, and a test title claimed it did | 1× |
| vault-a/UP-017 | A grilling ruling sat on the epic page with no story or contract row. It shipped unbuilt and was found two stories later by a builder who happened to look | 1× |

The single occurrences are in because the operator asked for the batch; each is a defect in how the contract is written, not a pattern that needs a second sighting.

## Resolution (2026-10-20, unreleased)

- **`/adlc` Step 2.2** is now a rule list. The three shipped rules stay (name the instrument, state the done-condition, effort where the claim is irreversible). Four new ones:
  - **State the outcome, not the mechanism**, including what must keep working; a ruling that turns into a mechanism with a side effect gets the side effect into the ruling question first.
  - **Check every named fact against the code** (the loader's scope, the message catalogue, the action's reasons), or mark it `[UNVERIFIED]` for the tester.
  - **List every reader of a moved source**, each `moved here` or `deferred to <story>` with the user-visible effect until then.
  - **Carry the grilling rulings**: map each to the story and contract row that builds it before an epic's first build; an unmapped ruling stops the loop.
- **`/adlc` Step 0.3** (grilling): every ruling gets a row, written on the epic page with the story it lands in. **Step 2.1a:** the census packet carries the rulings on an epic's first story.
- **`scope-analyst`** census items 7 (the ruling map, unmapped first in the report) and 8 (the readers of a moved source, by file and symbol).
- **`feature-reviewer`** dimension 8: checks the readers list against the diff, and flags a test title or record that claims a deferred reader moved.
- **`technical-planning.md`:** the grilling gate says every ruling gets a row; a dispatcher rule "A contract states outcomes, checked against the code".

## Open

- Vault-side after 1.0.8: the local tester's reachability check (vault-d) and the epic ledger's "readers left on the catalogue" carry-forward (vault-a) can come out.
- An eval case for "outcome, not mechanism" would need a packet grader; none yet.
