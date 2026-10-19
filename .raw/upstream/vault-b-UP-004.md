# vault-b/UP-004 Ask the client for the least work that unblocks us; do the rest in parallel

- **Kind:** improvement
- **Target:** `skills/client-docs/SKILL.md` § Writing
- **Plugin version:** 1.0.7
- **Seen:** 1×, operator-approved (2026-10-20)

## What happened
The client's task list asked them to build each of ~29 forms in their SaaS tool to a field spec
and to name each form by a key. The operator: «This is too hard. Change it so the client needs to
create any forms and put links in the table. We will update fields, so we can start integration
while they work on connecting [payments].» We have access to the tool, so the field setup was ours
to do.

## Proposed fix
Add to § Writing:

> - **Client tasks: the least that unblocks us.** Split the client's steps into «blocks our work»
>   and «can run in parallel with us». Ask only for what blocks us, in the smallest form (a link
>   pasted into a table row beats a naming convention). Any step we can do with the access we have
>   is ours. Say which steps run in parallel.
