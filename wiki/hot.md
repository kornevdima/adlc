---
type: meta
title: "Hot Cache"
updated: 2026-09-16T00:00:00
tags:
  - meta
  - hot-cache
status: evergreen
related:
  - "[[index]]"
  - "[[log]]"
  - "[[Research Sharing the Wiki with People]]"
  - "[[AI-Native SDLC Playbook vs ADLC]]"
  - "[[Integrate the wiki toolset into the ADLC workers]]"
---

# Recent Context

Navigation: [[index]] | [[log]]

## Last Updated

**2026-09-16 (fix: plugin 1.0.3, uncommitted)**: The bundled BA method docs pointed at 23 reference tables (rubrics, taxonomies, templates) that were never copied from upstream ba-suite, so BA workers had been inferring those rubrics. The tables are now bundled in `skills/wiki/references/ba/references/`, all pointers use plugin-root paths and resolve, and the shift-left `_index.md` path notes are qualified. See [[log]].

**2026-09-03 (autoresearch: Sharing the Wiki with People)**: 5 questions, 5 answered, 14 pages. Synthesis [[Research Sharing the Wiki with People]]. **The OKF "preview" is a proof-of-concept one-file graph viewer** (one HTML file: graph, rendered markdown, backlinks, search; no auth, no page tree); the only hosted consumer, Google Cloud Knowledge Catalog, is IAM-gated and agent-facing. **Publishers split by trigger** ([[Vault Publishing Topologies]]): rebuild-from-repo keeps agent commits live for readers; app-pushed routes (Digital Garden, Obsidian Publish) need a human re-publish. **Recommendation**: pilot [[Quartz]] v5 (explorer, breadcrumbs, search, backlinks, graph, repo-triggered CI, free) on a 20-page slice; keep a **CI-mirrored GitHub Wiki** as the free-private fallback (`[[Page]]` by title = the vault's basename rule); publish **one-way to Confluence** (`kovetskiy/mark`) only where readers already live there; avoid round-trip sync (GitBook / Wiki.js) unless UI editing is required — it competes with agents for writes. Every non-Obsidian route needs a lowering step (wikilinks, callouts, `_index.md`), which `okf_export.py` half-implements ([[One-Way Publish vs Round-Trip Wiki Sync]], [[Obsidian Vault Portability]]). Cross-repo agent access: sibling clone + AGENTS.md pointer + committed `permissions.additionalDirectories` ([[Cross-Repo Wiki Access]]).

**2026-09-03 (earlier)**: plugin 1.0.1/1.0.2 — `scope-analyst` wired into `/adlc`, worker filing/instrument clauses, operator profile, AI-Native SDLC Playbook ingested → [[AI-Native SDLC Playbook vs ADLC]].

## Key Recent Facts

- **Plugin follow-up**: `skills/wiki/scripts/okf_export.py` targets `knowledge-catalog/okf`, now a frozen snapshot; OKF is v0.2 in `GoogleCloudPlatform/open-knowledge-format` (`generated` / `verified` / `status` / `stale_after`; per-folder `index.md` reserved). Retarget before relying on the export.
- Obsidian Publish is $8/mo annual, $10 monthly ([[Wiki Sharing Patterns]] refined).
- 14 agents; per-story pipeline (census →) build → test → review → verify (→ reconcile) → document. Plugin reinstall under the new name is done; repo + dir still `claude-mem`.

## Active Threads

- **Open tasks** (index § Open tasks): playbook review (Stage 6 first); filing-clause field test; scope-analyst offload test (four candidate changes parked); cheap-worker escalation.
- **Human follow-ups**: commit the 1.0.3 BA reference-table fix, then `claude plugin marketplace update adlc-marketplace`; `claude plugin marketplace update adlc-marketplace`; decide the sharing pilot (Quartz slice vs GitHub Wiki mirror); retarget the OKF exporter; rename repo + dir; redeploy `agents/*.md` to service repos.
- Research gaps, one fetch each: Flowershow pricing; Quartz v5 changelog; `markdown-confluence` wikilink + callout support.
- Deferred: vault MCP server; `/project-profile --refresh`; Stage 6 trigger seam.
