# Glossary page

Every vault carries `wiki/glossary.md`: the project's terms in plain words, and one entry per identifier so that a page can explain a code where it first appears with a link instead of a sentence (`writing-style.md` § Identifiers and § Pages that stay current). The scaffold creates the page from the template below; `skills/wiki/scripts/glossary.py` maintains it:

```bash
PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(ls -d "$HOME"/.claude/plugins/cache/*/adlc/*/ 2>/dev/null | sort -V | tail -1 | sed 's:/$::')}"
python3 "$PLUGIN_ROOT/skills/wiki/scripts/glossary.py" --vault . build            # regenerate the ID entries from the registers
python3 "$PLUGIN_ROOT/skills/wiki/scripts/glossary.py" --vault . build --check    # lint: exit 1 when the page is out of step
python3 "$PLUGIN_ROOT/skills/wiki/scripts/glossary.py" --vault . link             # dry run: first mentions that would be linked
python3 "$PLUGIN_ROOT/skills/wiki/scripts/glossary.py" --vault . link --apply     # link them
```

Run `build` after a register changes (a new open question, gap, stakeholder, trial check), then `link --apply`. Both are safe to repeat: `build` rewrites only the generated part, `link` touches only first mentions that are not yet links.

## How the page is split

Everything down to and including the `## Registers` table is written by hand: frontmatter, intro, project terms, the optional translation column. Everything after the first `## ` heading that follows the table is generated:

- one section per Registers row, with a `### ID` entry per register row (the anchor pages link to);
- `## Plugin issues`, when `meta/adlc-upstream.md` has `UP-nnn` entries;
- `## Pages with their own IDs`: lookup tables for pages whose filename starts with an id followed by a space, a hyphen or nothing (`FR-001.md`, `FEAT-003 Title.md`, `ADR-005-short-title.md`). These link to their own pages, never to the glossary.

## When two pages start with the same id

A work page named after the item it serves (`US-007 Census 2026-01-15.md` next to `US-007 Sign-in.md`) also starts with the id. The script gives the id to the page that sits in the same folder and has the same frontmatter `type:` as most pages of its family (most `US-` pages are `type: user-story` in `user-stories/`), and prints an `id-clash` line naming both. When no page fits that way (two stories in two folders, or a family split evenly), the id is left out of the lookup table and not linked, and `build` and `link` exit 1.

The naming that never clashes: only the page an id belongs to starts its filename with it. A census, copy table, plan or as-built page puts the id after a word (`Census US-007 2026-01-15.md`) or keeps its own folder and `type:` so the family rule settles it. Run `build` and read the `id-clash` lines before the first `link --apply`.

## The Registers table

One row per register the vault keeps. The `ID pattern` is a regex the first token of a table row's first cell must match in full; `Owner` is the page holding the table (text after the wikilink, such as "§ 13", is kept in the section lead). `Entry` is the template for each entry: `{id}` the id, `{0}` the rest of the first cell, `{1}`, `{2}`, `{-1}` the other cells; `{n:status}` keeps the leading status word of a cell ("Partial" from "**Partial** - API …"), `{n:lower}` lowercases it. Register pages are named by their wikilink, so renaming a page is a one-cell change here. A link with a folder (`[[decisions/_index|catalog]]`) resolves by that path; a bare name that matches two pages (every folder has an `_index`) stops `build` with exit 2 and names them.

## Linking rules `link` applies

The first mention of each id on a page becomes `[[glossary#ID|ID]]`, or `[[Page stem|ID]]` for an own-page id; inside a table cell the pipe is escaped (`\|`). Left alone: frontmatter, headings, fenced and inline code, existing links, URLs, `log.md`, log archives, lint reports, `glossary.md` itself, `sources/`, `meta/operator-profile.md` and `meta/adlc-upstream.md` (verbatim records), the id cell of a register's own row, a page's own id, and every folder listed under `link_skip:` in the glossary frontmatter. Client documents go in `link_skip:` (§ Audience: no internal names in prose for a client).

## Translation terms

The `technical-writer` skill's two-column translation glossary lives on this page too: add a `Translation` column to the Project terms table, or a `## Translation` section above `## Registers`, and point the operator profile's § Translation at it.

## Template

```markdown
---
type: glossary
title: "Glossary"
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [glossary, meta]
link_skip: []
---

# Glossary

Every identifier used in this wiki, in plain words, with the page that owns it. Pages link an id
here the first time it matters (`[[glossary#STK-001|STK-001]]`). Requirements, features and other
pages that carry their id in the filename have their own pages and link there directly.

## Project terms

The terms below have a fixed meaning in this project.

| Term | Meaning |
|---|---|
| [Term] | [What it means here, one sentence] |

## Registers

The ID entries below this table are generated from these registers by `glossary.py build`; edit the registers, not the entries.

| Section | Lead-in | Owner | ID pattern | Entry |
|---|---|---|---|---|
| Stakeholders | Roles, organisations and groups, by role only. | [[Stakeholder Register]] | STK-\d{3} | {1}. Type: {2:lower}. |
| Open questions | Each question with its current status. | [[Open questions register]] | OQ-\d{3} | {1} Status: {-1:status}. |
| Gaps | Differences between today and the target, with severity. | [[Gap register]] | G-[A-Z]{3}-\d{3} | {1}. Severity: {4:status}. |
```

Keep only the rows whose register exists; add one for every register the vault creates later (decisions, risks, trial checks, jobs). A Mode B vault with no registers keeps the table empty: `build` then writes only the own-page lookup tables, and `link` still links `[[DEC-003 …|DEC-003]]`, `[[BUG-012 …|BUG-012]]` on first mention.
