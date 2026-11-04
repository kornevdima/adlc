---
type: meta
title: "Hot Cache"
updated: 2026-11-04T12:00:00
tags:
  - meta
  - hot-cache
status: evergreen
related:
  - "[[index]]"
  - "[[log]]"
  - "[[Plugin architecture overview]]"
  - "[[Configurable toolset for reader, code navigation and design]]"
  - "[[Upstream channel from vaults to the plugin]]"
  - "[[Glossary links ids to work pages that share them]]"
---

# Recent Context

Navigation: [[index]] | [[log]]

## Last Updated

**2026-11-04 (session: configurable toolset, 1.1.0)**. [[Configurable toolset for reader, code navigation and design]]: a vault's `AGENTS.md` now carries a `Toolset:` block (`reader`, `code-nav`, `design`, `design-system`); Obsidian and graphify are defaults the skills read, not requirements. New `skills/wiki/references/toolset.md`, `skills/wiki/scripts/toolset.py` (`show` / `check` / `detect`, 8 tests green) and the sixteenth worker `agents/feature-designer.md` (`shape` before the build, `review` after the code review, on impeccable and taste-skill against a design-system folder; never edits code). Seven code-touching workers orient with the toolset's tool and list `mcp__semble__*`, `mcp__serena__*`. The scaffold asks the toolset (step 3a); `/adlc` reads it at Step 0 and dispatches the designer at 2.2b and 2.5a; `graphify-ingest` runs the installer only when no pinned interpreter imports graphify and refuses when the block names another tool; `wiki-lint` writes a Markdown dashboard outside Obsidian. Four manifests at 1.1.0. **Not committed.** Eval case `evals/wiki/scaffold-toolset` written, not run.

**2026-10-23 (session: vault-d/UP-004)**. [[Glossary links ids to work pages that share them]]: `glossary.py` settles an id that two filenames start with by the family's folder and `type:`; 5 tests green; shipped under 1.0.9. Committed as `fix(glossary)`.

**2026-10-22 (session: architecture folder)**. `wiki/architecture/` created (9 pages) and 1.0.9 committed as `chore(plugin): 1.0.9`; the three vault-e reports (changelogs, glossary, hook path) and vault-a/UP-024 shipped under 1.0.9.

## Key Recent Facts

- **The toolset's defaults keep old vaults working**: no block means `reader: obsidian`, graphify when `graphify-out/graph.json` exists, no design tool. `toolset.py detect` on this machine proposes wiki-renderer, Semble and Serena, impeccable and taste-skill; `check` finds every tool plus the design-system folder.
- **Documented, not tested:** a worker whose `tools:` names an MCP server the session lacks. The docs say a launch fails only when no entry resolves; the built-ins always resolve.
- **Field models for the generic text**: a co-located vault's repo-local Semble and Serena bindings (operator ruling 2026-11-01) and a design-system repo built with impeccable whose `AGENTS.md` ranks dated rulings above tool heuristics. Neither is named in plugin pages (redaction rule).
- `.raw/upstream/vault-f-UP-001.md` is still unfiled: `glossary.py`'s `OWN_PAGE_ID` misses two-part prefixes (`ADR-XX-05`), and the "Plugin issues" section lands in a shared glossary when `meta/` is untracked.
- `gh` can't reach GitHub from this machine. `claude plugin eval` takes only the last `--case`.

## Active Threads

- **Release 1.1.0:** run the eval fast set (and the new `wiki/scaffold-toolset` case), commit, then set the `Toolset:` block in the co-located vaults (`toolset.py detect`), add the Semble and Serena allow lines and `Task(feature-designer)` to their settings, and give each service `AGENTS.md` a `## Code navigation` section (`/project-profile`).
- **Follow-ups from the toolset work:** `/project-profile` does not yet write the `## Code navigation` section itself (the reference describes it); `impeccable critique` runs degraded inside the designer (no sub-agents); a `wiki/code/` graph of this repo was never built.
- **vault-f/UP-001** (glossary two-part prefixes): confirm on a scratch copy, fix `OWN_PAGE_ID`, add a test, decide the "Plugin issues" opt-in.
- **Not addressed from the ledgers:** the public-repo records occurrence (vault-a, 2026-10-18); the UP-002 "simplest shape first" gap; vault-a UP-011 (declined).
- **Evals backlog** ([[Plugin eval suites for claude plugin eval]]): the 12 slow cases; graphify and pm-layer; `adlc` worker cases.
- **Open tasks:** [[Integrate the wiki toolset into the ADLC workers]]; [[Operator profile - learn engagement style from corrections]]; [[Configurable subagent models per host]] (postponed).
- **Deferred:** vault MCP server; `/project-profile --refresh`; the Stage 6 trigger; K8; the Cursor plugin load check; the sharing pilot; the OKF exporter; renaming the repo.
