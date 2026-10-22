---
type: module
title: "Scripts"
path: "skills/*/scripts/, bin/"
created: 2026-10-22
updated: 2026-10-22
tags:
  - architecture
  - module
  - scripts
status: active
related:
  - "[[Plugin architecture overview]]"
  - "[[Skills and routing]]"
  - "[[Wiki maintenance edits blocked in ADLC vaults]]"
---

# Scripts

Fifteen Python scripts, standard library only, each beside the skill that owns it, plus one shell installer. A script exists wherever a check or a rewrite has to be deterministic: a prompt may miss a dead link, a script does not. The scripts are also the reason the permission profile works in auto mode: `permissions.md` allow-lists each script by path, so the routine operation never needs an ad-hoc `sed` that the profile would deny ([[Wiki maintenance edits blocked in ADLC vaults]]).

## Inventory

| Script | Owner | Does | Run by |
|---|---|---|---|
| `glossary.py` | `wiki` | `build` regenerates the glossary's id entries from the Registers table in the page; `link --apply` links first mentions; `build --check` is the lint | the scaffold, the ADLC and Mode B passes, `wrap-up`, `wiki-lint` 8d |
| `page_history_check.py` | `wiki` | Lists history kept inside pages and folders without a linked changelog; writes nothing | `wiki-lint` 8b and 8c, `wrap-up` 6a, the epic close |
| `relink.py` | `wiki` | Repoints wikilinks from one page to another across a vault, aliases and anchors kept | the epic close (ledger into as-built page), `wrap-up` |
| `upstream_redact_check.py` | `wiki` | Flags tracker ids, sprint tokens, ledger names, hashes, URLs, source paths and vault names in an upstream report or a plugin page | `/adlc upstream` before an export; this repo before a commit |
| `guard_env.py` | `wiki` | PreToolUse hook: blocks any tool call that reads an env file or prints resolved configuration; `.env.example` and commit / PR message text stay allowed. Payload tests in `test_guard_env.py` | the vault's `.claude/settings.json`, copied there by the scaffold |
| `okf_export.py` | `wiki` | Renders the vault as an Open Knowledge Format bundle | by hand, for sharing ([[Open Knowledge Format]]) |
| `build_snapshot.py` | `adlc` | Snapshots the build as a git ref and checks the tester's footprint against it | the story loop, after builder and after tester |
| `lint_graph.py` | `wiki-lint` | Graph-layer checks: label and title drift, stale labels, orphan community pages, graph staleness against the source files | `wiki-lint` |
| `build_index_json.py` | `wiki-query` | Writes `wiki/index.json`, the machine-readable locator for large vaults | `wiki-query` large-vault mode, `wrap-up` |
| `chunks.py`, `merge.py`, `regenerate.py` | `graphify-ingest` | Plan the extraction chunks; merge AST and semantic JSON and re-cluster; regenerate the report, `wiki/code/` and the hot-cache snapshot from the labels | `graphify-ingest` |
| `detect.py`, `update.py` | `graphify-update` | Detect what changed since the last run; apply the incremental update with labels preserved | `graphify-update` |
| `usage_report.py` | `wrap-up` | Rolls token usage up from the host's session transcripts into `wiki/meta/usage.md` | `wrap-up` |
| `bin/setup-graphify.sh` | plugin | Installs the graphify library into a compatible Python and pins the path for a project | the operator, once |

## Conventions

- **Standard library only, exit codes fixed**: 0 clean, 1 findings, 2 bad input. A skill reads the code, not the prose.
- **Dry run by default** for anything that writes (`glossary.py link`, `relink.py`); `--apply` writes.
- **The vault is an argument** (`--vault .`), never the current directory by assumption; the one hook that runs before the plugin loads is anchored on `$CLAUDE_PROJECT_DIR` ([[Env-guard hook path is relative to the working directory]]).
- **A script's docstring is its documentation.** The reference that introduces a rule points at the script; the script's header repeats the usage.
- **Field-checked before release** on a copy of a reporting vault when a script answers an upstream report; the question page records the numbers.
