---
type: module
title: "Scripts"
path: "skills/*/scripts/, bin/"
created: 2026-10-22
updated: 2026-11-08
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

Sixteen Python scripts, standard library only, each beside the skill that owns it, plus one shell installer. A script exists wherever a check or a rewrite has to be deterministic: a prompt may miss a dead link, a script does not. The scripts are also the reason the permission profile works in auto mode: `permissions.md` allow-lists each script by path, so the routine operation never needs an ad-hoc `sed` that the profile would deny ([[Wiki maintenance edits blocked in ADLC vaults]]).

## Inventory

| Script | Owner | Does | Run by |
|---|---|---|---|
| `glossary.py` | `wiki` | `build` regenerates the glossary's id entries from the Registers table in the page; `link --apply` links first mentions; `build --check` is the lint. Own-page ids take `ID Title` and `ID-slug` filenames; an id two pages start with goes to the one that matches its family's folder and `type:`, with an `id-clash` line, else it is not linked (exit 1). Vault tests in `test_glossary.py` | the scaffold, the ADLC and Mode B passes, `wrap-up`, `wiki-lint` 8d |
| `page_history_check.py` | `wiki` | Lists history kept inside pages and folders without a linked changelog; writes nothing | `wiki-lint` 8b and 8c, `wrap-up` 6a, the epic close |
| `relink.py` | `wiki` | Repoints wikilinks from one page to another across a vault, aliases and anchors kept | the epic close (ledger into as-built page), `wrap-up` |
| `upstream_redact_check.py` | `wiki` | Flags tracker ids, sprint tokens, ledger names, hashes, URLs, source paths and vault names in an upstream report or a plugin page | `/adlc upstream` before an export; this repo before a commit |
| `guard_env.py` | `wiki` | PreToolUse hook: blocks any tool call that reads an env file or prints resolved configuration; `.env.example` and commit / PR message text stay allowed. Payload tests in `test_guard_env.py` | the vault's `.claude/settings.json`, copied there by the scaffold |
| `okf_export.py` | `wiki` | Renders the vault as an Open Knowledge Format bundle | by hand, for sharing ([[Open Knowledge Format]]) |
| `toolset.py` | `wiki` | `show` resolves the vault's `Toolset:` block with its defaults (one `key=value` per line, or `--key` for one); `check` says which chosen tools are installed, each with its install line, and for the IDE server whether the IDE answers an MCP initialize; `detect` proposes a block from what the machine has; `code-wiki <svc>` prints a service's code wiki path for the vault's layout (`services/<svc>/wiki/` or `service-wikis/<svc>/`). `check` also covers the layout (`/services/` ignored, worktrees present), ub-mode (skill and three tool virtualenvs) and TokenEconomizer. Reads MCP server names and the IDE server's URL only. Parser tests in `test_toolset.py` | the scaffold (step 3a), `/adlc` Step 0, the `graphify-ingest` and `graphify-update` gates, `wiki-faq` answers |
| `build_snapshot.py` | `adlc` | Snapshots the build as a git ref and checks the tester's footprint against it | the story loop, after builder and after tester |
| `lint_graph.py` | `wiki-lint` | Graph-layer checks: label and title drift, stale labels, orphan community pages, graph staleness against the source files | `wiki-lint` |
| `build_index_json.py` | `wiki-query` | Writes `wiki/index.json`, the machine-readable locator for large vaults | `wiki-query` large-vault mode, `wrap-up` |
| `chunks.py`, `merge.py`, `regenerate.py` | `graphify-ingest` | Plan the extraction chunks; merge AST and semantic JSON and re-cluster; regenerate the report, `wiki/code/` and the hot-cache snapshot from the labels | `graphify-ingest` |
| `detect.py`, `update.py` | `graphify-update` | Detect what changed since the last run; apply the incremental update with labels preserved | `graphify-update` |
| `usage_report.py` | `wrap-up` | Rolls token usage up from the host's session transcripts into `wiki/meta/usage.md` | `wrap-up` |
| `tells_check.py` | `technical-writer` | Finds the patterns of machine-written text a regular expression can see (`references/ai-tells.md`); skips frontmatter, code and quoted text; exit 1 on a `fix` finding. Tests in `test_tells_check.py` | `technical-writer` on every page it writes, `wrap-up` 6b, `wiki-lint` writing check |
| `bin/add-service-worktree.sh` | plugin | Adds one service to a `layout: worktrees` vault: ignores `/services/`, checks the service branch out as a worktree (an orphan branch when new), seeds `service-wikis/<svc>/`; commits nothing | the operator or the scaffold, once per service |
| `bin/setup-ub-mode.sh`, `bin/ub-tool.sh` | plugin | Copy the ub-mode skill into the vault and clone crapper, dryer and mutator into `tools/` at pinned commits, each with a virtualenv; `ub-tool.sh` becomes the vault's `scripts/tool.sh`, which finds the interpreter on Windows and Unix | the operator or the scaffold, once per vault with `engineering: ub-mode` |
| `bin/setup-graphify.sh` | plugin | Installs the graphify library into a compatible Python and pins the path for a project | the operator or `graphify-ingest`, once per project; skipped while the pinned interpreter imports graphify |

## Conventions

- **Standard library only, exit codes fixed**: 0 clean, 1 findings, 2 bad input. A skill reads the code, not the prose.
- **Dry run by default** for anything that writes (`glossary.py link`, `relink.py`); `--apply` writes.
- **The vault is an argument** (`--vault .`), never the current directory by assumption; the one hook that runs before the plugin loads is anchored on `$CLAUDE_PROJECT_DIR` ([[Env-guard hook path is relative to the working directory]]).
- **A script's docstring is its documentation.** The reference that introduces a rule points at the script; the script's header repeats the usage.
- **Field-checked before release** on a copy of a reporting vault when a script answers an upstream report; the question page records the numbers.
