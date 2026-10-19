# vault-b/UP-001 «No long dashes» needs the replacement spelled out

- **Kind:** bug
- **Target:** `skills/client-docs/SKILL.md` § Terms and formatting
- **Plugin version:** 1.0.7
- **Seen:** 2×, one session (2026-10-20), a client brief written in Ukrainian

## What happened
The skill says «Plain sentences. Short, active, no long dashes». It doesn't say what replaces the dash.
The agent rewrote every «X — Y» sentence into a different construction («the table shows…», «X looks
the same: it is…»). The operator: «I said not to use long dashes, but - dashes was ok.» Only the
character had to change.

A second correction narrowed it: where the dash stands in for a missing verb inside a longer
instruction («for course forms — "Show message", for tariff forms — go to payment»), the verb
reads better («for course forms choose "Show message", for tariff forms choose go to payment»).

## Proposed fix
Replace the formatting line with:

> - **Dashes.** Replace a long dash («—», «–») with a hyphen «-» and keep the sentence as it is,
>   ranges included («steps 1-3», «P1-P10»). Two exceptions: where the dash stands in for a missing
>   verb inside a longer sentence, write the verb; before a closing summary label («how fields are
>   ordered — question Q2») the long dash stays. Quoted UI text keeps its own punctuation.
