---
type: meta
title: "Hot Cache"
updated: 2026-10-02T00:00:00
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
  - "[[Configurable subagent models per host]]"
  - "[[Skills Field Eval 2026-10]]"
---

# Recent Context

Navigation: [[index]] | [[log]]

## Last Updated

**2026-10-02 (Cursor plugin + model-selection question)**: Fixed the Cursor marketplace: `source` is now `"./"`; the old value resolved to a missing `./adlc/`. Cursor manifests are at 1.0.3. Cursor plugin hooks now live in `hooks/cursor-hooks.json` and print the JSON Cursor reads; the stop hook fires only on the first stop of a turn, so its auto-submitted follow-up cannot loop. `.cursor/hooks.json` is removed. Opened [[Configurable subagent models per host]]: a hardcoded `model: sonnet` broke worker dispatch in a Copilot org without Claude models. Proposed design: agents ship with no model; `adlc:setup` writes per-host model tiers to a per-machine file; dispatchers pass `model`; on a model error, retry the same worker without one. Nothing built. Then [[Skills Field Eval 2026-10]]: three operator sessions confirm K8 (strong), handoff drift, and main-thread marathons. Top new findings: the SessionStart `type: "prompt"` hook errors at every startup; manual work (an engineer implements a story using `/adlc:wiki` only for context) is a valid mode with no defined behaviour, so add a context-load row; the verifier is compose-only; graphify regenerate overwrites hot.md.

**2026-09-16 (fix: plugin 1.0.3, c811f3e)**: bundled the 23 BA reference tables the method docs depend on; all pointers resolve. See [[log]].

**2026-09-03 (autoresearch: Sharing the Wiki with People)**: 14 pages, synthesis [[Research Sharing the Wiki with People]]. Recommendation: pilot [[Quartz]] v5 on a 20-page slice; CI-mirrored GitHub Wiki as the free-private fallback; one-way Confluence publish only where readers already live; avoid round-trip sync. See [[Vault Publishing Topologies]], [[Cross-Repo Wiki Access]].

## Key Recent Facts

- **Plugin follow-up**: `skills/wiki/scripts/okf_export.py` targets `knowledge-catalog/okf`, now a frozen snapshot; OKF is v0.2 in `GoogleCloudPlatform/open-knowledge-format` (`generated` / `verified` / `status` / `stale_after`; per-folder `index.md` reserved). Retarget before relying on the export.
- Obsidian Publish is $8/mo annual, $10 monthly ([[Wiki Sharing Patterns]] refined).
- 14 agents; per-story pipeline (census →) build → test → review → verify (→ reconcile) → document. Plugin reinstall under the new name is done; repo + dir still `claude-mem`.

## Active Threads

- **Open tasks** (index § Open tasks): field-eval priorities (prompt hook → model steps 1–4 → wiki context-load row for manual work → worker portability → graphify); subagent model selection (steps 1–4 first, then verify Copilot/Cursor dispatch `model`); playbook review (Stage 6 first); filing-clause field test; scope-analyst offload test (four candidate changes parked); cheap-worker escalation.
- **Human follow-ups**: `claude plugin marketplace update adlc-marketplace`; install the Cursor plugin and confirm it loads; decide the sharing pilot (Quartz slice vs GitHub Wiki mirror); retarget the OKF exporter; rename repo + dir; redeploy `agents/*.md` to service repos.
- Research gaps, one fetch each: Flowershow pricing; Quartz v5 changelog; `markdown-confluence` wikilink + callout support.
- Deferred: vault MCP server; `/project-profile --refresh`; Stage 6 trigger seam.
