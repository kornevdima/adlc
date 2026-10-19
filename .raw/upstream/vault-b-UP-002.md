# vault-b/UP-002 Apply an operator's correction to the whole document, not the one line named

- **Kind:** improvement
- **Target:** `skills/client-docs/SKILL.md` § After the edit
- **Plugin version:** 1.0.7
- **Seen:** 3×, one session (2026-10-19/20), a client brief

## What happened
The operator quoted one line and asked for a change (a raw count → a link to the section that lists
the items; a code → a link to its row; a bare domain → a link). Each time the agent changed only
that line. The same pattern stayed in other tables. The operator: «why this table not cross
linked? We have already linked data in [the first section]. What's the problem with updating this
page?»

## Proposed fix
Add to § After the edit:

> - **A correction is a pattern, not a line.** When the operator corrects one spot (a missing link,
>   an unexplained code, a wording), search the whole document — and its translation — for the same
>   pattern and fix every instance in the same edit. Report how many places changed. If an instance
>   needs a judgement call, list it and ask instead of leaving it silently.
