---
type: module
title: "Shared references"
path: "skills/wiki/references/"
created: 2026-10-22
updated: 2026-11-08
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

The wiki skill's `references/` folder holds 65 documents that are read at run time by other skills, by the workers, and by the repo's own `AGENTS.md`. They are the plugin's method library: a skill prompt says what to do, a reference says how, and one reference serves every skill that needs it. The rule for placement: a document lives under the wiki skill when more than one skill or worker reads it; a skill keeps a private `references/` folder only for what nobody else needs (the adlc skill's shipped-reports table and its routes table, the autoresearch program, the product-management layer's reference, the four help documents of `wiki-faq`).

## The conventions every writer reads

| Reference | What it fixes | Read by |
|---|---|---|
| `writing-style.md` | The writing method for every human reader: lead with the answer, identifiers explained where they first appear, pages that stay current, change reports | `adlc`, `save`, `technical-writer`, `wiki`, `wiki-ingest`, `wiki-lint`, `wrap-up`; `ba-suite-subagent`, `doc-writer`; this repo's `AGENTS.md` |
| `glossary.md` | The glossary page template, its Registers table, the linking rules | `adlc`, `technical-writer`, `wiki`, `wiki-ingest`, `wiki-lint`; `wiki-lint-subagent` |
| `frontmatter.md` | The page types and their required fields, OKF-compatible; since 1.3.0 the work records the plugin owns (story with `kind` and the loop-written dates, epic, sprint, release, decision with `decided_by`, `decided_on`, `evidence`) | `wiki-ingest`, the scaffold, `adlc`, `wiki-lint`, `board.py`; `ba-suite-subagent` |
| `records.md` | The four decision levels (product, architecture, team, machine) and their homes; what is not a decision; the `## How we work` section; `machine.local.md`; the portfolio files `product/context.md` and `catalog-info.yaml` | `wiki` (scaffold), `adlc`, `wiki-lint`, `project-profile`, `technical-writer`; `ba-suite-subagent` |
| `migration-1.3.md` | What `migrate_1_3.py` does to a 1.2.0 vault and what it leaves to the operator | the operator, `wiki-lint` 10 |
| `modes.md` | The vault modes (B, C, B plus C, ADLC): folder maps (with `product/`, `domains/`, `epics/`, `releases/`, `board.md`), frontmatter, pipelines, the intake note | `wiki`, `wiki-faq`, README |
| `concerns/` (five files) | Opt-in folder kits per role: `ops`, `qa`, `sec`, `design`, `writing`, each with its "add when" rule | `wiki` (scaffold) |
| `operator-profile.md` | The operator's engagement pole, standing rulings, the correction log (class, what it exposed, outcome, session; the words as typed in the gitignored `.raw/reflection/`), translation pointer | `adlc`, `technical-writer`, `wiki`, `wiki-faq`, `wrap-up` |
| `permissions.md` | The `.claude/settings.json` profile for ADLC vaults: allow-listed scripts, denied env reads, the guard hooks, the optional toolset lines | `adlc`, `wiki` (scaffold) |
| `toolset.md` | The vault's `Toolset:` block: reader, code navigation, design tools, design-system folder, layout, engineering method, cost plugin; what each option changes in which skill, the Semble, Serena and JetBrains IDE server playbooks workers follow, install and permission lines | `wiki` (scaffold), `adlc`, `wiki-query`, `wiki-lint`, `wrap-up`, `graphify-ingest`, `graphify-update`, `wiki-faq`; every code-touching worker and `feature-designer` |
| `service-worktrees.md` | The `layout: worktrees` topology: a branch per service checked out at `services/<svc>`, code wikis in `service-wikis/` on the main branch, the two-commit rule, line endings | `wiki` (scaffold), `adlc`, `project-profile`; `architecture-subagent`, `feature-reviewer`, `feature-verifier` |
| `engineering-ub-mode.md` | The `engineering: ub-mode` method: the three tool gates, the service `AGENTS.md` template, where an ADLC rule overrides the skill | `wiki` (scaffold), `project-profile`; `feature-builder`, `feature-reviewer` |
| `mission-control.md` | The agents' board and the activity ledger (the metrics seam), the team's generated `board.md`, and the rules for more than one session (pull before reading, one dispatcher per epic, regenerate rather than merge) | `adlc`, `wiki`, `wiki-lint`, `wrap-up`, `team-sync.md`; `wiki-lint-subagent` |
| `adlc-upstream.md` | The per-vault ledger of plugin lessons and the export rules | `adlc`, `wiki`, `wiki-faq`, `wrap-up`; `AGENTS.md` |
| `review-policy.md` | The per-service review policy page | `project-profile`; `feature-reviewer` |
| `git-setup.md`, `git-flow.md`, `team-sync.md` | Vault git init with the ignore lines for `*.local.md` and `.raw/reflection/`; session wiki branches and code-only PRs; git as the team's state bus, the role ownership table and the joining checklist (`CODEOWNERS`, `CONTRIBUTING.md`, the gitleaks hook, `bin/setup-team.sh`) | `wiki`, `adlc`, `wrap-up`, README |
| `mcp-setup.md` | Obsidian MCP configuration (`reader: obsidian` only) and tracker MCP notes | `ba-export`, `wiki-faq`, `AGENTS.md` |
| `technical-planning.md`, `ba-suite-pipeline.md` | The two ADLC pipelines: requirements into per-service architecture artifacts with gates as decision lines on the epic page; raw context into BA deliverables | `adlc`, `wiki`, `wiki-ingest`, `wiki-lint`, `wrap-up`, `ba-export`; `ba-suite-subagent`, `architecture-subagent` |
| `rest-api.md` | Obsidian REST API notes | kept for the MCP work; no skill reads it today |

## The two method libraries

**Business analysis** (`ba/`, 15 method documents and 24 supporting references): orientation, elicitation synthesis, stakeholder analysis, workshops, process modelling, gap analysis, user-story factory (which also files the epic records and the story frontmatter), the PRD (`ba-prd.md`, since 1.3.0), business case, RFI and RFP analysis, solution assessment, test-case generation, scrum events (with the sprint record), requirements lifecycle, planning and monitoring. The supporting references are the rubrics and templates those methods cite: INVEST criteria, MoSCoW language triggers, gap severity, story splitting, traceability matrix, BPMN elements, financial formulas, governance templates. The `ba-suite-subagent` runs one method per dispatch with these documents as its only method source; `ba-export-subagent` applies the matching method's export shape. No external BA plugin is needed.

**Shift-left engineering** (`shift-left/`, 2 documents): the advisor's four checkpoints (requirements understood, domain modelled, decisions taken, workflow agreed), read through the ADLC overrides: the gates are decision lines on the epic page, the worker writes architecture artifacts (drivers with quality attribute scenarios, the domain model, ADRs, the workflow) and never a requirement, and a decision without evidence becomes a spike. The product-management layer reads the same method for its Gate 0.

## How a reference is used at run time

A skill names the reference and the section ("`writing-style.md` § Change reports"), and the agent reads that file from the plugin root: `$CLAUDE_PLUGIN_ROOT` when the host sets it, otherwise the newest `~/.claude/plugins/cache/*/adlc/*/`. Workers get the same path in their dispatch packet. Vault-side copies are never made, with one exception: the scaffold copies `guard_env.py` into the vault's `.claude/hooks/` because a hook has to run before the plugin is loaded.

## Why this shape

A method in one place changes in one place: the writing method moved every report and page at once when it shipped ([[One writing method for every human reader]]), and the current-state rule reached seven skills and three workers in one release ([[Pages carry their history inline]]). The cost is that a reference is read in full; the long ones (`modes.md`, `permissions.md`) are organised by section so a skill can name the part it needs.
