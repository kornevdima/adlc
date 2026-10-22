---
type: meta
title: "Hot Cache"
updated: 2026-10-21T22:00:00
tags:
  - meta
  - hot-cache
status: evergreen
related:
  - "[[index]]"
  - "[[log]]"
  - "[[Upstream channel from vaults to the plugin]]"
  - "[[Pages carry their history inline]]"
  - "[[Identifiers with no glossary]]"
  - "[[Env-guard hook path is relative to the working directory]]"
  - "[[Workers print secrets from env files]]"
---

# Recent Context

Navigation: [[index]] | [[log]]

## Last Updated

**2026-10-21 (session: release 1.0.9)**. Three vault-e reports fixed, rows under 1.0.9 in `upstream-shipped.md`:
- [[Pages carry their history inline]] (UP-002): pages hold the current state only, history in per-folder `_changelog.md` linked from `_index.md`. `writing-style.md` § Pages that stay current; the scaffold creates the changelogs; `wrap-up` steps 5 / 6 / 6a no longer write "as-built diverges" notes or pointer sentences into pages (frontmatter `status: superseded` + `superseded_by:` instead); ingest, save and the BA / architecture / doc workers rewrite and add a changelog row. New `skills/wiki/scripts/page_history_check.py`, run by `wiki-lint` 8b / 8c and `wrap-up` 6a.
- [[Identifiers with no glossary]] (UP-003): `wiki/glossary.md` in every vault. New `skills/wiki/scripts/glossary.py`: `build [--check]` from a `## Registers` table inside the page (owner wikilink, id regex, entry template), `link [--apply]` for first mentions; template `references/glossary.md`; translation terms move to the same page; `wiki-lint` 8d.
- [[Env-guard hook path is relative to the working directory]] (UP-001): the hook entry is `if [ -f "$CLAUDE_PROJECT_DIR/.claude/hooks/guard_env.py" ]; then …; else echo … >&2; fi`, a block still blocks, a missing file warns.

## Key Recent Facts

- **Two of the three were filed from the co-located vault's ledger and standing ruling, not from an export.** The vault has to add UP-002 and UP-003 to its own `adlc-upstream.md` before it can close them; UP-001 came through `.raw/upstream/` and is already `sent` there.
- `glossary.py` was checked on a scratch copy of the reporting vault: 82 entries identical to the vault's own script, 0 first mentions left, every anchor resolving. `page_history_check.py` on the same copy: 0 history hits, the two structural gaps (a client-documents folder without a changelog, a changelog with no index to link it). On this repo's wiki it reports 2 prose hits on concept pages about rule supersession; left.
- **Read both co-located vaults' `wiki/meta/adlc-upstream.md`**, and now the third vault's, not only `.raw/upstream/`. Keys in use: vault-a to vault-e (plus vault-g, -m, -r, -s, -v, -w reserved by the vaults).
- Upstream pages carry no pointers into a vault's private repo; run `skills/wiki/scripts/upstream_redact_check.py --vault <vault>` on every touched page, log line and reference before a commit (never `--vault .` here).
- `gh` can't reach GitHub from this machine. `claude plugin eval` takes only the last `--case`.

## Active Threads

- **After 1.0.9 is installed in the vaults:** vault-e adds `_changelog.md` where folders lack one and an `_index.md` for its technical folder, moves its register config into the glossary's `## Registers` table and deletes its local script, keeps its `$CLAUDE_PROJECT_DIR` hook form; all vaults flip their `sent` entries to `shipped (1.0.9)` and remove the workarounds each page's Open section names. Other vaults gain changelogs and a glossary at their next lint or wrap-up.
- **Not addressed from the ledgers:** the public-repo records occurrence (vault-a, 2026-10-18); the UP-002 "simplest shape first" gap; vault-a UP-011 (declined).
- **Evals backlog** ([[Plugin eval suites for claude plugin eval]]): the 12 slow cases; the `[!contradiction]` callout case; graphify and pm-layer; `adlc` worker cases.
- **Open tasks:** [[Integrate the wiki toolset into the ADLC workers]]; [[Operator profile - learn engagement style from corrections]].
- **Deferred:** vault MCP server; `/project-profile --refresh`; the Stage 6 trigger; K8; the Cursor plugin load check; the sharing pilot; the OKF exporter; renaming the repo.
