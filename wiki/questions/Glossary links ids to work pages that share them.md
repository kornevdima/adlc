---
type: synthesis
title: "Glossary links ids to work pages that share them"
created: 2026-10-23
updated: 2026-10-23
tags:
  - adlc
  - wiki
  - glossary
  - upstream
status: resolved
upstream: [vault-d/UP-004]
related:
  - "[[Identifiers with no glossary]]"
  - "[[Scripts]]"
  - "[[Upstream channel from vaults to the plugin]]"
---

# Glossary links ids to work pages that share them

**Opened from** the co-located vault's ledger (ratified 2026-10-23), with its redacted export copied to `.raw/upstream/`. Kind: plugin bug, found on the vault's first glossary run after the 1.0.9 sync.

**Outcome:** a story, epic or decision id links to the page it belongs to, even when census, copy-table or plan pages start their filenames with the same id; decision filenames in the scaffold's `ADR-NNN-slug` form count as own pages; a register owner written with a folder resolves to that folder's page.

## What happened

`glossary.py` (from [[Identifiers with no glossary]]) looked clean on `build` and on the `link` dry run, but its lookup tables pointed several ids at the wrong pages. A scratch `link --apply` would have written 355 links in 88 pages, most story and epic links to the wrong target. Three faults:

1. **Silent first match.** The script kept the first page, in path order, whose filename started with an id and a space. The vault names work pages `<story id> Census <date>` in a planning folder that sorts before the stories, so the census page took the id for 6 of 20 stories, both epics and one decision. Nothing was printed.
2. **Slug filenames ignored.** The filename regex needed a space or the end of the name after the id, so `ADR-005-short-title.md`, the scaffold's own decision naming, never counted.
3. **Owners resolved by basename.** `[[decisions/_index]]` dropped its folder and read the first `_index.md` in the vault; an owner written `[[folder/_index\|alias]]` inside a table cell kept the backslash.

## Resolution (2026-10-23, shipped in 1.0.9)

- **Shared ids are settled by the family, not by path order.** Every page whose filename starts with an id claims it; when several do, the id goes to the page in the same folder and with the same frontmatter `type:` as most pages of that id family (stories in `user-stories/` with `type: user-story`). Each shared id prints an `id-clash` line naming the owner and the other pages. When no single page fits, the id is left out of the lookup table and not linked, and `build` and `link` exit 1. A work page's own first mention of its story id now links to the story too, instead of being treated as the page's own id.
- **`ID-NNN-slug` filenames count** as own pages (`ADR-005-short-title.md`).
- **Owners resolve by path** when the link has a folder; the backslash before `|` is dropped; a bare name that matches two pages stops `build` with exit 2 and names both, instead of picking one.
- Checked on a scratch copy of the reporting vault: all 9 shared ids (6 stories, 2 epics, 1 decision) went to the right page, including an epic shared with its as-built page in the same folder (settled by `type:`). The decisions now get their lookup table. `link --apply` wrote 541 first mentions in 157 pages, none of them to a census, copy-table or plan page; the few links to those pages that remain were hand-written before the run.
- **`test_glossary.py`** beside the script, 5 vault tests: a work page does not take the id, an unresolved clash is not linked and exits 1, slug filenames link, an owner with a folder and an alias resolves, a bare ambiguous owner fails. All green.
- Docs: `references/glossary.md` § When two pages start with the same id (the rule and the naming that never clashes); `wiki-lint` 8d reports `id-clash` lines as WARN; the `scope-analyst` census naming keeps `type: census` and never names a census `<STORY-ID> <Title>.md` beside the stories.

The report proposed refusing every shared id or preferring a home folder; the family rule does the second without a per-vault folder list, and still refuses when it cannot tell.

## Open

- Vault-side: the reporting vault already synced 1.0.9 before this fix, so it re-syncs the plugin, runs `build`, reads the `id-clash` lines, then `link --apply`, and flips its entry to `shipped (1.0.9)`. Renaming its work pages is now optional.
- The family rule needs a family: an id whose only claimant is a work page (a census for a story with no page yet) still links to that work page.
