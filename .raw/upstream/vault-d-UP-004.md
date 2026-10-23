---
type: upstream-report
key: vault-d/UP-004
kind: bug
target: skills/wiki/scripts/glossary.py (OWN_PAGE_ID, own_page_ids, find_page); skills/wiki/references/glossary.md; agents/scope-analyst.md; skills/wiki-lint step 8d
plugin_version: 1.0.9
date: 2026-10-23
status: ratified
---

# glossary.py links ids to the wrong page when two filenames start with the same id

## What happened

On the first 1.0.9 sync of a Mode B+C vault (about 600 pages), `glossary.py build` and a `link` dry run looked clean. The generated "Pages with their own IDs" tables showed the problem: several story ids, both epic ids and one decision id pointed at dated work pages, not at the pages those ids belong to. Running `link --apply` on a scratch copy confirmed it: of 355 first-mention links in 88 pages, most of the story and epic links went to the wrong target. In a census page, the sentence "<a screen> cannot show <a part> before <story id>" was linked to that story's census page, not to the story.

Three faults:

1. **Silent first match.** `own_page_ids` keeps the first page in path order whose filename starts with an id followed by a space (`out.setdefault`). The vault names its census and copy-table pages `<story id> Census <date>.md` in a planning folder, which sorts before the stories folder, so the census page wins for 6 of 20 stories. The same happened for 2 epics (a census page, and a census page in `meta/`) and 1 decision (an implementation plan in `meta/`). No warning is printed.
2. **`ADR-NNN-short-title.md` is not an own-page id.** `OWN_PAGE_ID` needs a space or the end of the name after the id, so the scaffold's own decision filename convention never matches. The wiki skill's step "every ADR and bug id links to its page on first mention" does nothing for decisions.
3. **Register owners resolve by basename.** `find_page` drops the path, and every folder has `_index.md`, so a register owned by `[[<folder>/_index]]` reads the alphabetically first `_index.md` in the vault. A table-cell owner written `[[<folder>/_index\|alias]]` also keeps the backslash in the captured name.

Half of the first fault is vault naming: the scope-analyst default is `census/<STORY-ID>-census-YYYY-MM-DD.md` (hyphen, ignored by the regex), and this vault chose a space. But nothing in the plugin says that a space after an id in a filename claims that id, so any vault that names work pages after the story they serve hits this. A silent first match is wrong whatever the naming.

## Proposed fix

1. `build` and `link` report every id claimed by two or more pages (an `id-clash` line naming the pages) and do not link that id; or prefer the page in the id's home folder (stories, decisions, bugs) or whose frontmatter `type:` matches, and still print the clash.
2. Accept `ID-NNN-slug` filenames as own-page ids.
3. Resolve a register owner by its path when the wikilink has one; strip `\` before `|`.
4. State the naming contract in `references/glossary.md` and the scope-analyst: only the page an id belongs to starts its filename with `<ID> `; work pages use `<ID>-census-<date>` or put the id later in the name.
5. `wiki-lint` 8d runs the clash check, so a vault finds out before anyone runs `link --apply`.

## Workaround in the reporting vault

The glossary page exists with project terms and an empty Registers table; `link --apply` is not run; decision ids were already linked by page. Renaming the work pages to the hyphen form with `relink.py` is proposed locally.
