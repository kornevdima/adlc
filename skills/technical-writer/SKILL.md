---
name: technical-writer
description: >
  Write, edit and translate documents for a human reader in a wiki vault: client briefs,
  question packs and scope notes sent outside the team; help pages and tutorials; the wording
  of BA stories, requirements and test plans; change reports to the operator. One writing
  method for all of them (skills/wiki/references/writing-style.md), a source-language file and
  its translation kept in step, terms held stable through a vault glossary, and the operator's
  corrections recorded in the operator profile.
  Triggers on: "write this for the client", "client questions", "question pack", "client brief",
  "scope of work", "write the help page", "user guide", "rewrite this story", "make the
  requirement readable", "change report", "translate this", "sync the translation",
  "make it readable", "/technical-writer".
---

# technical-writer: documents for a human reader, and their translations

A document a person reads is where the vault meets its readers: a client who decides, a user who follows a help page, a stakeholder who reads a story or a requirement, the operator who reads a change report. Two things go wrong with such documents most: they read like a dump of the agent's notes, and a translation drifts from its source. This skill covers both. Translation counts as a deliverable here, not a last step.

The style is in `skills/wiki/references/writing-style.md`: audience, sentences, identifiers, structure, facts, questions, tasks, change reports, corrections. This skill is the procedure around it.

## Before writing

1. **Read the operator profile.** `wiki/meta/operator-profile.md`, § Writing (older vaults: § Client documents) and § Translation (template: `wiki/references/operator-profile.md`). If the profile names a reference document, read it: it is the best guide to the operator's taste, and it beats the generic style where they differ.
2. **Read the style reference**, `skills/wiki/references/writing-style.md`. Resolve the plugin root first (`$CLAUDE_PLUGIN_ROOT`, or the installed plugin under `~/.claude/plugins/cache/`); the path is inside the plugin, not the vault.
3. **Find the sources.** Every statement comes from the requirements register (`wiki/requirements/`), a client source (spec, contract, message), a code read, or an operator statement. A statement with none of these is our inference: mark it as an assumption or leave it out.
4. **Find the kind of document**, which sets the folder and what you may change:

| Kind | Where it lives | What this skill changes |
|---|---|---|
| Client document (brief, question pack, scope of work, status note) | `client-briefs/` or `client-pack/`, or the folder the vault's AGENTS.md names | everything; the document is yours |
| Help page, tutorial | `user-docs/`, `tutorials/` (the `writing` concern). `doc-writer` authors them from a code read; this skill reshapes wording and structure | wording, structure, links; never a claim about the app that the code read did not confirm |
| BA deliverable (story, requirement, test plan, gap) | `user-stories/`, `requirements/`, `test-plans/`, `gaps/` | wording only. IDs, frontmatter, acceptance criteria and traceability links stay; a change of meaning is a BA task, not an edit |
| Change report, reply to the operator | the chat reply, the `/adlc` or `wrap-up` report, a `comms/` note | the whole text, per § Change reports in the style reference |

5. **Find the pair.** A document kept in two languages comes as a source-language file and a translation, for example `x.md` (source) and `x.ru.md`. Check which one the operator treats as the source of truth (a ruling in the profile). If there is no ruling, the source language is the one the wiki is written in.

## Writing

### Shape of a question pack

Unless the profile sets another shape, use this one:

1. **What we build**, with no heading: 3-5 lines and, if one exists, the high-level diagram from the architecture page. Diagram and text use the same part names and the same number of parts.
2. **What there is now**: the current state, with links to every place it names, checked live and dated.
3. **What we propose**: labelled as a proposal.
4. **What we need from you**: tasks, split into "blocks our work" and "can run in parallel" (style reference § Tasks).
5. **Assumptions**: what we take as given unless the client objects. Things the client has already answered go here, not in the questions.
6. **Blockers** and **Processes** (how the two teams work together: deploy, review, data handling, access), when they apply.
7. **Questions to you**: a table with an empty "Your answer" column (style reference § Questions).

Sections are `##` headings. Numbering runs through all question sections and is redone after any change.

### Each statement

- One question, then one or two sentences on what it affects and why the answer matters.
- Say exactly what the source says. Don't make a component bigger or smaller than the source does.
- Links are claims: open each target as the reader will, on the deployed page, and confirm the anchor and the named element exist before reporting (style reference § Facts).
- An identifier never stands alone (style reference § Identifiers): plain words first, the id in brackets.

### A help page

Follow `doc-writer`'s document-as-built rule: only built and verified behaviour, nothing the code read did not confirm. Second person, task first ("Your job", then "In the app"). The style reference's § Audience applies in full: the user never reads how the feature is built.

### A story or a requirement

Keep the ID, the frontmatter, the acceptance criteria and the links untouched. Rewrite the prose for the reader who has to build or accept it: one idea per sentence, the user-visible outcome before the mechanism, every code explained where it first appears. If the rewrite changes what the story means, stop and report it as a BA finding instead of editing.

## Translating

1. **Change the source first, then the translation.** If the operator edits the translation directly (common), port the change back to the source in the same turn.
2. **Both files in the same edit.** Use one exact-match replace per file, each asserting its old text occurs once. After the edit, compare both files' section headings and question numbers. They must match.
3. **Meaning, not words.** The translation must read as if it were written in that language: rewrite the sentence, don't map it word for word.
4. **Glossary.** Keep a two-column glossary in the operator profile's § Translation, or in `wiki/meta/glossary.md` when it grows past about 30 rows. Add every domain term the first time it is translated, and reuse it after that. Also list what stays untranslated: code identifiers, product names, and technical words the client uses as is.
5. **Local typography.** Decimal separators, units, and page references in the target language's form (for example `0,1-1 с` and `стр. 8` in Russian, `0.1-1 s` and `p.8` in English). Dashes per the style reference: a hyphen, the sentence unchanged.

## After the edit

- **A correction is a pattern, not a line.** When the operator corrects one spot, search the whole document and its translation for the same pattern and fix every instance in the same edit; report how many places changed. A judgement call is listed and asked, never left silently. (Seen 3× in one session: a count linked in one table and left bare in the others; a code unlinked in one column; a domain left as plain text.)
- **Report** in the shape of the style reference § Change reports: what changed and where, in plain words, one line per change; what is assumed or unverified. Don't restate the document.
- **Log** each operator correction in the operator profile's correction log, verbatim and classified (`wiki/references/operator-profile.md`). A correction that changes how any future document is written goes into § Writing or § Translation only when the operator says it is standing, or ratifies a distill proposal after it repeats.
- A dated file that has been sent is never edited. A change after sending means a new dated file.
- Sending to a client is an outward action: only on the operator's word.
