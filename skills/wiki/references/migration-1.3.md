# Migrating a vault to 1.3.0

Version 1.3.0 gives a Mode ADLC vault the layers around the story loop: a product layer (`product/`, `domains/`), work records with plugin-owned frontmatter (`epics/`, `releases/`, the story fields), a generated board, decision levels, spikes, routes for non-story work, and the architecture worker's artifact pages in place of gate pages. A vault created under 1.2.0 or earlier keeps working without this migration; the loop and the lint will ask for the missing pieces one at a time. Running the migration once is cheaper.

## The script

```bash
PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(ls -d "$HOME"/.claude/plugins/cache/*/adlc/*/ 2>/dev/null | sort -V | tail -1 | sed 's:/$::')}"
python3 "$PLUGIN_ROOT/skills/wiki/scripts/migrate_1_3.py" --vault .            # dry run: prints every change
python3 "$PLUGIN_ROOT/skills/wiki/scripts/migrate_1_3.py" --vault . --apply    # writes
```

Run it from the vault root on a clean working tree, read the dry run, then apply and review the diff before committing. It is idempotent: a second run reports only the board regeneration. What it does, in order:

| Step | Change | Why |
|---|---|---|
| 1 | Creates `wiki/product/`, `wiki/domains/`, `wiki/epics/`, `wiki/releases/`, each with `_index.md` and `_changelog.md`; `.raw/spikes/` (with a `.gitkeep`) and `.raw/reflection/` | the folder map in `modes.md` |
| 2 | Adds `*.local.md`, `.raw/reflection/` and `.claude/settings.local.json` to `.gitignore` when missing | `git-setup.md`; the operator's words as typed and machine setup never travel |
| 3 | Moves epic pages (`type: epic`, or a name starting with `EPIC-`) from `wiki/sprints/` to `wiki/epics/` | item 5 of the plan; wikilinks resolve by basename, so no link changes |
| 4 | Renames gate pages in every code wiki and repoints their links with `relink.py`: `GATE-1-<SVC>` to `architecture-drivers.md`, `GATE-1.5` to `domain-model.md`, `GATE-2` to `adrs/decisions.md`, `GATE-3` to `engineering-workflow.md` | gates are checkpoints, not documents (`technical-planning.md` § Gates as checkpoints) |
| 5 | Adds `kind: feature` and `history: []` to story pages that lack them; touches no other story field | `frontmatter.md` § Work records; the dates are the loop's |
| 6 | Appends a `## How we work` section with the defaults to `AGENTS.md` when it has none; writes `catalog-info.yaml` from `Owner:` and `Purpose:` when absent | `records.md` § Team choices and § The project in a bigger system |
| 7 | Generates `wiki/board.md` (and `board.base` under `reader: obsidian`) | the team's board, `mission-control.md` |

## What the script leaves to you

- **The renamed gate pages still hold their old content.** A former `GATE-1` page holds requirements the worker wrote; the 1.3.0 worker writes drivers and scenarios instead. Dispatch `architecture-subagent` once per service ("refresh the artifacts from the register") so the pages become what their names say, and so `adrs/decisions.md` is split into one ADR per page. Until then the pages are correct history under a new name.
- **Gates tables on the epic pages.** Write one Gates table per active epic (`technical-planning.md` § Gates as checkpoints) from what was approved: the approval pack of the register is gate 1's evidence, the old gate pages' approvals are gates 1.5 to 3.
- **The release records.** Create `wiki/releases/<RELEASE-ID>.md` for each release in flight (`frontmatter.md` § release) and set `release:` on each epic page; an epic cannot close under 1.3.0 without one.
- **Story fields.** The script sets only `kind` and `history`. Set `epic`, `release`, `size`, `priority` and `services` on the stories you will work next; the BA worker sets them on new stories, and the loop refuses to open a story without `epic` and `kind`.
- **The PRD and the domains.** Run the initial pass's steps 2a and 2b (wiki skill, Mode ADLC initial BA pass): the BA worker writes `product/prd.md` from the register, and the domain pages with `context-map.md`.
- **`product/context.md`** and the bounded-context notes: the scaffold's placeholders come from the vault description; the architecture worker writes each service's bounded-context note on its next run.
- **The correction log.** Existing rows keep their Quote column as history. New rows use the five columns of `operator-profile.md` § Correction log (no quote, a Session column); `wrap-up` adds the header the first time it writes one. Nothing already committed is rewritten.
- **Team choices filed as decisions.** `wiki-lint` check 6a lists decision pages that hold a tool or team choice; move each line to `AGENTS.md` (`Toolset:` or `## How we work`) and delete the page with a changelog row.
- **Permissions.** Add `Task(spike)` and `Bash(python3 *skills/wiki/scripts/board.py *)` to `.claude/settings.json` (`permissions.md`).
- **The glossary.** Add `## Registers` rows for `epics/` and `releases/`, then `glossary.py build` and `link --apply`.

## By hand, without the script

The same seven steps as the table, in that order; the script is a convenience, not a requirement. The one step that needs care is the gate rename: move the file, then `relink.py --from "GATE-2-WEB" --to "decisions" --vault wiki --apply` for the product wiki and once more for each code wiki, so no page links a name that no longer exists.
