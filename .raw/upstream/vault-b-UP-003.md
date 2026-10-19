# vault-b/UP-003 Every link must land on what it names, checked on the deployed target

- **Kind:** improvement
- **Target:** `skills/client-docs/SKILL.md` § Writing
- **Plugin version:** 1.0.7
- **Seen:** 2×, one session (2026-10-19/20), a client brief that links into a test site and a SaaS admin

## What happened
1. The brief linked three section anchors on the test site. They existed in the source repo but
   not on the deployed site (the deploy was older). The brief also said a form was «already on the
   site»; the deployed site didn't have it yet.
2. A table row described buttons «in other blocks» and linked one block on one example page. That
   block had no such button there; the buttons existed only on 3 of 8 pages. The operator: «why do
   we have link to … if there is no form in this block?»

## Proposed fix
Add to § Writing:

> - **Links are claims.** Every link points at the thing its text names. Before reporting, open
>   each link target as the client will (the deployed page, not the source) and confirm the anchor
>   and the named element exist. When a row generalises across pages, check every page it covers
>   and name the exceptions. A statement about what is live («already on the site») is checked on
>   the live system, with the date.
