# vault-b/UP-005 Client-facing writing style: generic rules

- **Kind:** improvement
- **Target:** `skills/client-docs/SKILL.md` (new § Style); operator-profile template, «Client documents»
- **Plugin version:** 1.0.7
- **Seen:** a vault's AGENTS.md «Writing style» section, built from a session of operator
  corrections on a client brief (2026-10-19/20)

## What happened
The operator wrote down a style for every client-facing document and for how agents talk to them.
Most of it is not specific to the vault. The skill covers question packs and translation but not
these rules.

## Proposed fix
Add a § Style to the skill (examples generalised; the vault's own examples were in Ukrainian):

**Audience**
- One audience per document. A client document holds only what the client reads or decides.
  Implementation (scripts, CMS fields, requirement IDs, test scope, build checks, our delivery
  plan, internal wikilinks) goes to a separate internal page, linked from frontmatter only.
- Address the client directly («you», «on your side»); we are «we». Never the client in the third
  person.
- Ask the client only for what they can find themselves (the editor link of a form, not its embed
  id). The technical step is ours and is not explained to them.
- Never tell the client what they don't need to do or why. State our part in one plain line, or
  leave it out.

**Sentences**
- Short sentences, one idea each. No nested «the same as…» constructions: «P6, P7 and P8 look the
  same», not «P6 and P8 open the same window as P7».
- No sentence that repeats the previous one or explains the obvious. If deleting a sentence loses
  nothing, delete it.
- Natural domain terms. IDs in Latin script and consistent (Q1, P1, G1).
- In introductory text, plain words over codes («the B2B request form», not «G2»). A sentence that
  needs several codes points to an example instead.

**Structure**
- Every table gets a short lead-in: what the rows are, what the non-obvious columns mean, and the
  one takeaway the reader must not miss («looking the same doesn't mean the same form»).
- Every code or label is explained where it first appears.
- A count that a section lists in full links to that section instead of repeating its range.
- Cross-link: places, records and systems named in a table link to them, consistently across all
  tables.
- Warn about gaps (missing screenshots, skipped numbers) before the reader meets them.
- Totals and ranges as numbers; never leave the reader to multiply.
- Proposals are labelled as proposals.

**Questions to the client**
- Shape: what is there now → our proposal → what each choice costs → the one thing to decide.
  «What is there now» is complete: it states every consequence the choice depends on.
- Questions go in a table with an empty «Your answer» column, so the client answers in place.
- A task is not a question: it goes in «What we need from you».

**Facts**
- Check claims against the live system before writing them; say what was checked and when.
- Scope every statement exactly and name the exceptions.
- Examples must be true for the point they illustrate.
- Screenshots of third-party tools: hide personal names and photos before capturing.

**Talking to the operator**
- Same rules: plain, short, concrete numbers, no recap or filler. Lead with the answer; say what
  changed and where; flag anything assumed or unverified in one line.
