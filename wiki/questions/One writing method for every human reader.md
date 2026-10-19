---
type: synthesis
title: "One writing method for every human reader"
created: 2026-10-20
updated: 2026-10-20
tags:
  - adlc
  - writing
  - technical-writer
  - operator-profile
  - upstream
status: resolved
upstream: [vault-b/UP-001, vault-b/UP-002, vault-b/UP-003, vault-b/UP-004, vault-b/UP-005, vault-c/UP-001]
related:
  - "[[Operator profile - learn engagement style from corrections]]"
  - "[[Dispatcher rules for writing ruling questions]]"
  - "[[Upstream channel from vaults to the plugin]]"
---

# One writing method for every human reader

**Opened from** six upstream reports from two vaults, both about text a person reads, and from the operator's instruction of 2026-10-20: the method must be neutral (client briefs, the help documentation two other vaults keep, BA stories and requirements, and the agent's own replies), and a change report must read like a client brief, not like a list of sprint and ticket codes.

**Outcome:** one style reference that every writer in the plugin reads, one skill for documents and their translations, and reports to the operator that are understood without the board open.

## What the two vaults reported

| Report | What happened | Seen |
|---|---|---|
| vault-c/UP-001 | The vault produced client question packs in a second language. The first read as a dump of the agent's notes ("looks like AI slop"); the translation was written first and the source reconstructed from it; a term with two meanings made a question unreadable. The operator ruled that translation is a deliverable. The method was rebuilt by hand in the vault's operator profile over two days, then written as a `client-docs` skill straight into this repo's working tree | 3× |
| vault-b/UP-001 | "No long dashes" didn't say what replaces the dash. The agent rewrote every dashed sentence into another construction; the operator wanted only the character swapped | 2× |
| vault-b/UP-002 | A correction was applied only to the line the operator quoted; the same pattern (an unlinked count, an unlinked code, a bare domain) stayed elsewhere in the document | 3× |
| vault-b/UP-003 | Links written from the source repo pointed at anchors the deployed site didn't have yet; a row linked a block that had no such button on that page | 2× |
| vault-b/UP-004 | The client's task list asked them to build ~29 forms to a spec. The operator cut it to "create any form, paste its link; we configure the rest while you work" | 1×, operator-approved |
| vault-b/UP-005 | The operator wrote a "Writing style" section in the vault's AGENTS.md (audience, sentences, structure, questions, facts, talking to the operator), most of it generic | the section itself |

**Key collision.** Both vaults chose `vault_key: vault-b`. The five-report vault's files were already in `.raw/upstream/` under that key, so it keeps `vault-b`; the other vault is `vault-c` here and should re-key its ledger and export.

## Resolution (2026-10-20, unreleased)

- **`skills/wiki/references/writing-style.md`**, new. Audience, sentences (with the dash rule spelled out), identifiers and codes (an identifier never stands alone: plain words first, the id in brackets; a string of ids is not a sentence), structure (a lead-in before every table, codes explained where they first appear, consistent cross-links, totals as numbers), facts (checked live and dated; links are claims), questions to the reader (a table with "Your answer"), tasks for the reader (the least that unblocks us), change reports and replies to the operator (what there was, what changed and where, what it means for you, assumed or unverified), corrections (a pattern, not a line).
- **`skills/technical-writer/SKILL.md`** replaces the `client-docs` draft. Four kinds of document with what the skill may change in each: client documents (everything), help pages (wording, never an unconfirmed claim), BA deliverables (wording only, IDs and acceptance criteria untouched), change reports. The question-pack shape now has "what there is now", "what we propose" and "what we need from you" before the assumptions, as the reference brief does. Translation rules unchanged.
- **Who reads the reference:** `doc-writer` (help pages), `ba-suite-subagent` (stories, requirements, test plans), the `/adlc` Report to User (rewritten: outcomes in words, ids in brackets, "Needs you" as decisions), `wrap-up` step 8, the vault AGENTS.md template (a § Writing), and this repo's AGENTS.md (§ Writing for the operator).
- **Operator profile template:** § Client documents is § Writing (the reference document, the pack shape, exceptions); the skill reads either heading.

## Open

- Vault-side after 1.0.8: the five-report vault's AGENTS.md § Writing can shrink to its own-language examples and the reference document; the other vault's profile keeps its glossary and shape and drops the generic rules.
- The second vault re-keys to `vault-c` (ledger frontmatter and `.raw/exports/upstream/`).
- No eval case yet. A candidate: a change report graded on "no id without its plain description".
