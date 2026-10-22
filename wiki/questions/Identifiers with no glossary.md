---
type: synthesis
title: "Identifiers with no glossary"
created: 2026-10-21
updated: 2026-10-21
tags:
  - adlc
  - wiki
  - writing
  - upstream
status: resolved
upstream: [vault-e/UP-003]
related:
  - "[[Pages carry their history inline]]"
  - "[[One writing method for every human reader]]"
  - "[[Upstream channel from vaults to the plugin]]"
---

# Identifiers with no glossary

**Opened from** a vault's operator request ("we need a glossary page; an id in text can link to the global glossary"), read from its co-located ledger and filed here in redacted form. Kind: design the operator approved.

**Outcome:** every vault has `wiki/glossary.md`, with one entry per identifier generated from the registers, and the first mention of an id on any page links to its definition.

## What happened

- The writing method already said that every code is explained where it first appears, but a BA vault mints hundreds of ids (stakeholders, open questions, gaps, readiness items, trial checks, jobs) that have no page of their own, so pages either repeated the explanation or left the code bare.
- The vault built its own page: hand-written project terms, one `### ID` entry per identifier generated from five register tables, lookup tables for requirements and features, and a script that links the first mention per page (about 630 links across 73 pages, tables escaped with `\|`). The script hardcoded the register paths, the id regexes and the column positions, and did not bump the page's date.
- The plugin knew one glossary: the translation list in the operator profile, with `wiki/meta/glossary.md` as its overflow location.

## Resolution (2026-10-21, unreleased)

- **`skills/wiki/scripts/glossary.py`** (new, stdlib): `build [--check]` regenerates the id entries from a `## Registers` table inside the glossary page (`Section | Lead-in | Owner | ID pattern | Entry`, owners resolved by wikilink, entry templates with `{1}`, `{-1:status}`, `{2:lower}`), adds a plugin-issues section from the upstream ledger and lookup tables for pages that carry their id in the filename, and bumps `updated:` on change. `link [--apply]` links first mentions to `[[glossary#ID|ID]]` or to the id's own page, skipping frontmatter, headings, code, existing links, records, `sources/`, the register's own id cell, a page's own id and the folders in `link_skip:`.
- **`skills/wiki/references/glossary.md`** (new): the page template, the Registers table, the linking rules, the translation column. **`frontmatter.md`** adds the `glossary` type.
- **`wiki` skill:** the scaffold creates the page and links it from `index.md`; the Mode B and ADLC passes run `build` then `link --apply`; the AGENTS.md template carries the rule. **`wiki-ingest`, `ba-suite-subagent`, `architecture-subagent`, `doc-writer`, `/adlc` step 8:** a new id gets its entry in the same edit; workers report new ids, the dispatcher rebuilds. **`technical-writer`** and the operator profile: translation terms live on the glossary page. **`writing-style.md`** § Identifiers: the first mention on a wiki page is a link. **`wiki-lint`** check 8d: `build --check`, the link dry run, dead glossary anchors. **`permissions.md`** allows the script.
- Checked on a copy of the reporting vault with its registers moved into the table: the same 82 entries as its own script, 0 first mentions left to link, every anchor resolving.

## Open

- Vault-side after 1.0.9: add the `## Registers` table and `link_skip:` to the glossary page, delete the local script and the AGENTS.md line that names it, run `build --check` to confirm the page is in step.
- The Registers row pattern is the vault's: a pattern narrower than the register (`ER-0\d` against a tenth row) is a config error the `build --check` in lint will not see. Entry templates read cells by position, so a register that gains a column needs its row edited.
