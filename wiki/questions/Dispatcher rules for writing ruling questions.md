---
type: synthesis
title: "Dispatcher rules for writing ruling questions"
created: 2026-10-03
updated: 2026-10-04
tags:
  - adlc
  - dispatcher
  - operator-profile
  - upstream
status: resolved
upstream: [vault-a/UP-001, vault-a/UP-002]
related:
  - "[[Review the ADLC flow against the AI-Native SDLC Playbook]]"
  - "[[Operator profile - learn engagement style from corrections]]"
---

# Dispatcher rules for writing ruling questions

**Opened from** the vault-a operator-profile cleanup (operator, 2026-10-03: "file these changes in backlog for adlc"). Two lessons came out of that vault's correction log. The dispatcher hit each one repeatedly. Both describe how the **dispatcher** writes a question for the operator, not what this particular operator prefers. So they belong in the plugin, where every vault and every operator gets them (`operator-profile.md` rule 8, target **upstream**).

**Outcome:** the operator rules once, on true facts. They don't have to catch the dispatcher's mistakes, and they aren't asked the same question twice.

## The gap

Neither `skills/adlc/SKILL.md` nor `skills/wiki/references/technical-planning.md` says how to write a ruling question: the options, the premise behind them, the recommended pick. Grepping for "outcome", "premise" and "framed" finds nothing (2026-10-03).

## Lesson 1: cite the record before stating a status (seen 5×)

When an option states a status, describes a past ruling or an approved BR/FR, or says what the product does, it must give its source:
- a link to the record page, line or code comment it was read from;
- or "I checked it just now";
- or the label "estimate, not measured" for a worker's figure.

A rollup can't be the source: `hot.md`, mission control and the run ledger all go stale.

| Date | Stated as fact | The record | Cost |
|---|---|---|---|
| 2026-09-16 | test-plan gap 3, wrong summary | US-111 owns the measurement | the operator ruled "defer", then ruled again |
| 2026-09-24 | Q-S4-1 "invites and join links" | BR-019: a join link never binds a project | ruled on a wrong premise, asked again |
| 2026-09-30 | "you already rejected widening style-src" | the rejection was `style-src-elem`, not `style-src-attr` | corrected in the next message |
| 2026-10-01 | "the admin can't read wikis" | it can (TC-120) | an invite was created then revoked; Q-005 was filed then withdrawn |
| 2026-10-02 | BUG-018 "open"; "one edit gives 4.7:1" | fixed (`f265115`); 2.58:1 when measured | wrong work proposed; a fix offered on a worker's estimate |

The 2026-09-16 row is no longer in the correction log. It was a Standing-rulings line that the 2026-10-03 cleanup moved to the page it settles: the profile before the cleanup ("Test-plan gap 3 … First answered 'defer' on a wrong summary from the agent"), and the Sprint 07 page.

Vault-a ratified this rule in its profile on 2026-10-02. Once the plugin rule ships, that line comes out of the profile.

## Lesson 2: outcome first, mechanism second (seen 2×, plus one that belongs to lesson 1)

Open a ruling question with what the user sees, what the library does, or who owns which session. Then give the options. Don't open with the mechanism.

| Date | Framed as | Operator's reply |
|---|---|---|
| 2026-09-21 | sign-out in cookie terms | "singout should call logout and session should be revoked on IDP. am i wrong?" (the IdP session and the app session had not been told apart) |
| 2026-09-30 | Mermaid CSP as nonce / template / blob / sandbox | "why not to use library to render the chart?" (the library injects the `<style>` itself) |
| 2026-10-02 | US-139 factors, from one sample's ratios | asked twice for one decision; the text-only pin went red. **Recounted 2026-10-04:** the log calls this a dispatcher error from a figure taken off one wiki composition. That is an unmeasured premise (lesson 1), not mechanism-first framing. Row 35 shows the same story asked in outcome terms, and that question went fine. |

## Proposed work

1. Add a **"Writing a ruling question"** rule to `skills/adlc/SKILL.md` Step 2, next to the interjection rule. It covers:
   - source or label every factual premise (lesson 1);
   - put the outcome before the mechanism (lesson 2);
   - one decision per question. Several questions can still share one stop: the log counts that as a saving (rows on 2026-10-01 and 10-02, "cost no extra stop").
   Name `technical-planning.md` as the reference if the text grows.
2. Point the other places that put options in front of the operator at the rule: the Gate grilling in `technical-planning.md`, the `/adlc` Step 4.4 distill proposals, and `scope-analyst`'s census and reconcile options. **Not `wrap-up`** (corrected 2026-10-04): it asks nothing, it only writes `proposed:` lines and a report.
3. Eval cases ([[Plugin eval suites for claude plugin eval]]):
   - a status question where `hot.md` contradicts the bug page. Pass: the option cites the bug page.
   - a CSP question where a library does the injecting. Pass: the question opens with what the library does.
4. Once vault-a runs the release that carries the rule, remove "Cite the record" from the Pacing and ceremony section of vault-a's profile, and delete its `proposed:` lines.

## Evidence

The correction log in vault-a `wiki/meta/operator-profile.md` (the version of 2026-10-03): the rows dated 2026-09-21, 09-24, 09-30 (×2), 10-01 and 10-02 (×3).

## Resolution (2026-10-04)

Items 1–3 shipped in the working tree. Not released yet: that needs the next version bump.
1. `skills/adlc/SKILL.md` Step 2 § **Writing a ruling question**, after the interjection rule. Three rules: source every premise (a rollup is not a source; check a worker's figure, or label it "estimate, not measured"), outcome first, and one decision per question with several questions allowed at one stop.
2. Pointers to the rule:
   - `technical-planning.md` § grilling;
   - `/adlc` Step 4.4 (each proposal also names the dates of its log rows);
   - `agents/scope-analyst.md` § Propose, never rule (outcome first, sourced premises, estimates labelled).
3. Eval cases `evals/adlc/ruling-cites-record` and `evals/adlc/ruling-outcome-first` on a new fixture layer, `adlc-vault`. In that vault, mission control is stale (BUG-018 shows "open" with the builder's 4.7:1 guess, and the CSP ruling is framed as mechanisms), and the library fact sits at the bottom of the spec. Both cases pass, **and so does the no-plugin baseline (Δ 0.00, two rounds).** A fresh model on a small vault reads the record and frames the question well anyway. The field failures happened deep into long sessions, after a rollup had already been loaded. So the cases are regression pins, not proof that the rule works. The proof is the next vault-a run's correction log: no new premise or framing rows.
4. Open: remove the profile line and the `proposed:` lines in vault-a once it runs the release.

