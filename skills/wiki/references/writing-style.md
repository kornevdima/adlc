# Writing for a human reader

One method for every document a person reads, whoever they are: a client, a user of the app (help pages, tutorials), a reader of BA deliverables (stories, requirements, test plans), or the operator reading a report or a reply in chat. It was written down after two vaults rebuilt the same rules by hand from their operators' corrections. The `technical-writer` skill applies it to documents; `doc-writer` and `ba-suite-subagent` apply it to their pages; the `/adlc` and `wrap-up` reports and every reply to the operator follow it too.

The operator profile's **§ Writing** names the vault's reference document (one the operator called good) and any local exceptions. Read it first; it beats this page where they differ.

## Audience

- **One audience per document.** A client document holds only what the client reads or decides. Implementation (scripts, fields, requirement IDs, test scope, build checks, our delivery plan, internal wikilinks) goes to a separate internal page, linked from frontmatter only. A help page holds what the user does, not how the feature is built.
- **Address the reader directly** ("you", "on your side"); we are "we". Never the reader's organisation in the third person.
- **Ask only for what the reader can find themselves** (the editor link of a form, not its embed id). The technical step is ours and is not explained to them.
- **Never tell the reader what they don't need to do, or why.** State our part in one plain line, or leave it out.

## Sentences

- Short sentences, one idea each. No nested "the same as…" constructions: "P6, P7 and P8 look the same", not "P6 and P8 open the same window as P7".
- No sentence that repeats the previous one or explains the obvious. If deleting a sentence loses nothing, delete it.
- Natural domain terms, the way the reader says them. Identifiers in Latin script and consistent (Q1, P1, G1), never mixed with another alphabet.
- **One word, one meaning per document.** If a word could mean two things (our internal record and a product concept), describe what it does instead of using the word.
- **No internal names in prose.** Table names, state names, internal IDs (gap, requirement, work-package codes) and engineer names stay out of text for a client or a user. Talk in workstreams.
- **Code identifiers in backticks** (files, functions, endpoints, tables, event or webhook names); a product's UI labels in quotes.
- **Dashes.** Replace a long dash (—, –) with a hyphen (-) and keep the sentence as it is, ranges included ("steps 1-3", "P1-P10"). Two exceptions: where the dash stands in for a missing verb inside a longer sentence, write the verb ("for course forms choose 'Show message'"); before a closing summary label ("how fields are ordered - question Q2") the dash may stay. Quoted UI text keeps its own punctuation. The rule is a character swap, not a rewrite: in one session an agent rewrote every dashed sentence into a different construction, and the operator had to undo it.

## Identifiers and codes

This is the rule that keeps the reader's head free. Stories, sprints, epics, bugs and requirements have IDs so records can link; a reader should never have to translate them.

- **An identifier never stands alone.** The first time, write what the thing is in plain words, then the id in brackets: "the sprint that closed the permissions work (S26)", "the bug where a removed app still shows in the launcher (BUG-075)". After that, the plain name again, or the id where a table column needs it.
- **A string of ids is not a sentence.** "S25-S26 of EPIC-005, bug ASD-123" asks the reader to hold three lookups in their head. Say what happened: "In the last two sprints of the permissions epic, one bug was found and fixed."
- **Every code or label is explained where it first appears.** Codes a reader must carry across a document (G1, P5, Q3) get a legend at their first table.
- **In introductory text, plain words over codes** ("the partner request form", not "G2"). A sentence that needs several codes points to an example instead.
- **On a wiki page, the first mention of an identifier links to its definition:** `[[glossary#OQ-001|OQ-001]]` for an id defined in a register, `[[FR-012]]` for one that has its own page. See § Pages that stay current for the glossary.

## Structure

- **Every table gets a short lead-in:** what the rows are, what the non-obvious columns mean, and the one takeaway the reader must not miss ("looking the same doesn't mean the same form").
- **A count that a section lists in full links to that section** instead of repeating its range.
- **Cross-link consistently.** Places, records and systems named in a table link to them, in every table, not only the first.
- **Warn about gaps before the reader meets them** (missing screenshots, skipped numbers), not after.
- **Totals and ranges as numbers** ("from 10 to 21 forms", "15 forms instead of 5"). Never leave the reader to multiply.
- **Proposals are labelled as proposals** ("proposed plan", "we propose…").

## Facts

- **Check claims against the live system before writing them** (open the CRM, the site, the repo); say what was checked and when ("as of 19.10.2026").
- **Links are claims.** Every link points at the thing its text names. Before reporting, open each link target as the reader will (the deployed page, not the source) and confirm the anchor and the named element exist. When a row generalises across pages, check every page it covers and name the exceptions. A statement about what is live ("already on the site") is checked on the live system, with the date.
- **Scope every statement exactly** and name the exceptions (the field order applies to the three request forms; the contact form has only Email).
- **Examples must be true for the point they illustrate;** if an example fits only partly, pick another.
- **Every statement has a source:** the requirements register, a client source, a code read, or an operator statement. Anything else is our inference: mark it as an assumption or leave it out.
- **Screenshots of third-party tools:** hide personal names and photos before capturing.

## Pages that stay current

A wiki page is read for what is true now. History kept inside the page makes every reader do the reconciliation the writer skipped. The operator of one vault put it as: the content of the page should be up to date; dated update blocks look like meta. Checked by `skills/wiki/scripts/page_history_check.py`.

- **A page holds the current state only.** No "Update YYYY-MM-DD", "Correction", "Revision" or "as filed" sections, no "superseded" sentences, no "was X, now Y" wording, no strikethrough of an old value. When a fact changes, rewrite the page so it reads as if written today.
- **History goes to the folder's `_changelog.md`:** one table, newest first, columns `Date | Page | Change`, each change as one plain sentence with the pages it touched as wikilinks. Every folder with authored pages has one, linked from the folder's `_index.md`; the scaffold creates both. `sources/` is exempt (a summary describes its source as of its date), as are `log.md` and the ledgers and boards in `meta/`: those are records by design.
- **The only in-page history is frontmatter:** `status: superseded` with `superseded_by: "[[New page]]"` (or `status: delivered` for a plan that shipped). The body still reads as current, with a changelog row for the flip.
- **An unresolved conflict is current state**, so a `[!contradiction]` callout stays until it is resolved; then it is removed and the resolution becomes a changelog row.
- **Every identifier has a glossary entry.** `wiki/glossary.md` holds the project terms by hand and one `### ID` entry per identifier, generated from the registers by `skills/wiki/scripts/glossary.py build`. A new id gets its entry in the same edit that creates it (run `build` after a register changes), and `link --apply` links the first mention of each id on every page (`\|` inside a table cell). Identifiers with their own pages (requirements, features, bugs, stories) link to those pages, not to the glossary.

## Questions to the reader

- Shape: what is there now → our proposal → what each choice costs → the one thing to decide. "What is there now" is complete: it states every consequence the choice depends on.
- Questions go in a table with an empty "Your answer" column, so the reader answers in place. One row, one question; a row with two questions says so and leaves two answer slots.
- A task is not a question: it goes in "What we need from you".
- Cut a question the reader already answered, or that code access or documentation will answer. Propose an answer and let them confirm.

## Tasks for the reader

- **The least that unblocks us.** Split the reader's steps into "blocks our work" and "can run in parallel with us". Ask only for what blocks us, in the smallest form (a link pasted into a table row beats a naming convention). Any step we can do with the access we have is ours. Say which steps run in parallel.

## Change reports and replies to the operator

A report after a change, and every reply to the operator, reads like a client brief, not like a board. The reader should understand it without opening the board, the ledger or a ticket.

Shape, in this order, headings optional for a short reply:

1. **What there was.** One or two lines, only when the change is not obvious without it.
2. **What changed, and where.** Plain words first, the id in brackets, the place (file, page, section) after. One line per change; a table with a lead-in when there are more than five.
3. **What it means for you / what we need from you.** Decisions, checks, approvals, in the shape of § Questions and § Tasks.
4. **Assumed or unverified.** One line, or "nothing".

Rules: lead with the answer; say what changed and where; no recap of the request, no filler, no restating what was just said; concrete numbers; an id is attached to its plain description, never the other way round. A reply that is one answer stays one paragraph.

## Corrections

- **A correction is a pattern, not a line.** When the operator corrects one spot (a missing link, an unexplained code, a wording), search the whole document, and its translation, for the same pattern and fix every instance in the same edit. Report how many places changed. If an instance needs a judgement call, list it and ask instead of leaving it silently.
- Log each correction in the operator profile's correction log, verbatim and classified. A correction becomes a standing rule in § Writing only when the operator says it is standing, or ratifies a distill proposal after it repeats.

## Translation

Rules for a document kept in two languages are in the `technical-writer` skill, § Translating: source first, both files in one edit, meaning not words, a glossary in the profile, local typography.
