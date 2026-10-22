---
type: module
title: "Shared references"
path: "skills/wiki/references/"
created: 2026-10-22
updated: 2026-10-22
tags:
  - architecture
  - module
  - references
status: active
related:
  - "[[Plugin architecture overview]]"
  - "[[Skills and routing]]"
  - "[[Workers and the dispatch pipeline]]"
  - "[[SDLC Wiki Concerns]]"
  - "[[One writing method for every human reader]]"
---

# Shared references

The wiki skill's `references/` folder holds 61 documents that are read at run time by other skills, by the workers, and by the repo's own `AGENTS.md`. They are the plugin's method library: a skill prompt says what to do, a reference says how, and one reference serves every skill that needs it. The rule for placement: a document lives under the wiki skill when more than one skill or worker reads it; a skill keeps a private `references/` folder only for what nobody else needs (the adlc skill's shipped-reports table, the autoresearch program, the product-management layer's reference, the four help documents of `wiki-faq`).

## The conventions every writer reads

| Reference | What it fixes | Read by |
|---|---|---|
| `writing-style.md` | The writing method for every human reader: lead with the answer, identifiers explained where they first appear, pages that stay current, change reports | `adlc`, `save`, `technical-writer`, `wiki`, `wiki-ingest`, `wiki-lint`, `wrap-up`; `ba-suite-subagent`, `doc-writer`; this repo's `AGENTS.md` |
| `glossary.md` | The glossary page template, its Registers table, the linking rules | `adlc`, `technical-writer`, `wiki`, `wiki-ingest`, `wiki-lint`; `wiki-lint-subagent` |
| `frontmatter.md` | The page types and their required fields, OKF-compatible | `wiki-ingest` (and the scaffold) |
| `modes.md` | The vault modes (B, C, B plus C, ADLC): folder maps, frontmatter, pipelines, the intake note | `wiki`, `wiki-faq`, README |
| `concerns/` (five files) | Opt-in folder kits per role: `ops`, `qa`, `sec`, `design`, `writing`, each with its "add when" rule | `wiki` (scaffold) |
| `operator-profile.md` | The operator's engagement pole, standing rulings, corrections, translation pointer | `adlc`, `technical-writer`, `wiki`, `wiki-faq`, `wrap-up` |
| `permissions.md` | The `.claude/settings.json` profile for ADLC vaults: allow-listed scripts, denied env reads, the guard hooks | `adlc`, `wiki` (scaffold) |
| `mission-control.md` | The board and the activity ledger: the metrics seam | `adlc`, `wiki`, `wiki-lint`, `wrap-up`; `wiki-lint-subagent` |
| `adlc-upstream.md` | The per-vault ledger of plugin lessons and the export rules | `adlc`, `wiki`, `wiki-faq`, `wrap-up`; `AGENTS.md` |
| `review-policy.md` | The per-service review policy page | `project-profile`; `feature-reviewer` |
| `git-setup.md`, `git-flow.md`, `team-sync.md` | Vault git init; session wiki branches and code-only PRs; git as the team's state bus | `wiki`, `adlc`, `wrap-up`, README |
| `mcp-setup.md` | Obsidian and tracker MCP configuration | `ba-export`, `wiki-faq`, `AGENTS.md` |
| `technical-planning.md`, `ba-suite-pipeline.md` | The two ADLC pipelines: requirements into per-service specs; raw context into BA deliverables | `adlc`, `wiki`, `wiki-ingest`, `wiki-lint`, `wrap-up`, `ba-export`; `ba-suite-subagent` |
| `rest-api.md` | Obsidian REST API notes | kept for the MCP work; no skill reads it today |

## The two method libraries

**Business analysis** (`ba/`, 14 method documents and 24 supporting references): orientation, elicitation synthesis, stakeholder analysis, workshops, process modelling, gap analysis, user-story factory, business case, RFI and RFP analysis, solution assessment, test-case generation, scrum events, requirements lifecycle, planning and monitoring. The supporting references are the rubrics and templates those methods cite: INVEST criteria, MoSCoW language triggers, gap severity, story splitting, traceability matrix, BPMN elements, financial formulas, governance templates. The `ba-suite-subagent` runs one method per dispatch with these documents as its only method source; `ba-export-subagent` applies the matching method's export shape. No external BA plugin is needed.

**Shift-left engineering** (`shift-left/`, 2 documents): the four-gate method (requirements, domain model, decision records, engineering workflow) that `architecture-subagent` applies when it turns requirements into a per-service spec. The product-management layer reads the same method for its Gate 0.

## How a reference is used at run time

A skill names the reference and the section ("`writing-style.md` § Change reports"), and the agent reads that file from the plugin root: `$CLAUDE_PLUGIN_ROOT` when the host sets it, otherwise the newest `~/.claude/plugins/cache/*/adlc/*/`. Workers get the same path in their dispatch packet. Vault-side copies are never made, with one exception: the scaffold copies `guard_env.py` into the vault's `.claude/hooks/` because a hook has to run before the plugin is loaded.

## Why this shape

A method in one place changes in one place: the writing method moved every report and page at once when it shipped ([[One writing method for every human reader]]), and the current-state rule reached seven skills and three workers in one release ([[Pages carry their history inline]]). The cost is that a reference is read in full; the long ones (`modes.md`, `permissions.md`) are organised by section so a skill can name the part it needs.
