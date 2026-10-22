---
type: concept
title: "Use cases and modes"
created: 2026-10-22
updated: 2026-10-22
tags:
  - architecture
  - use-cases
  - modes
status: active
related:
  - "[[Plugin architecture overview]]"
  - "[[Skills and routing]]"
  - "[[SDLC Wiki Concerns]]"
  - "[[Agentic Orchestration Levels]]"
  - "[[Wiki Sharing Patterns]]"
  - "[[AI-Native SDLC Playbook vs ADLC]]"
---

# Use cases and modes

What the plugin is used for, from the lightest case to the heaviest. A vault has one base mode and zero or more concerns; the delivery loop is an additive mode on top. The folder maps and frontmatter for each live in the shared `modes.md` reference ([[Shared references]]).

## 1. A knowledge base that compounds

The base case, any mode: drop sources into `.raw/`, ingest them, ask questions, save answers, lint. The hot cache gives every new session the recent context for a few hundred tokens; the index and the per-folder indexes give it the map. This repo's own wiki is this case ([[LLM Wiki Pattern]], [[Compounding Knowledge]]). The autoresearch loop extends it to research that runs without the operator ([[Plan-Driven Research Loop]]).

## 2. A code wiki for a repository (Mode B)

"Map my codebase": modules, flows, decision records, dependencies, seeded from the tree by the wiki skill's initial repository pass, and optionally the structural code graph from graphify with summaries in `wiki/code/` ([[graphify-integration]]). `/project-profile` writes the repo's `AGENTS.md` so that any agent, and later the workers, know the commands and conventions ([[Project Profile Skill Suite]], [[AGENTS.md]]).

## 3. A product or project wiki (Mode C, or B plus C)

Stakeholders, decisions, deliverables, communications. The bundled business-analysis method turns meeting notes, tracker exports and Confluence pages into registers with stable ids; `ba-export` renders them back to Office files when a client wants a document. The glossary and the per-folder changelogs come from this case: hundreds of ids and seven weeks of edits in one vault ([[Identifiers with no glossary]], [[Pages carry their history inline]]).

## 4. Concerns for the other roles

Opt-in folder kits for `ops`, `qa`, `sec`, `design` and `writing`, each with an "add when" rule so a vault only carries the structure it produces artifacts for ([[SDLC Wiki Concerns]]). ADLC vaults almost always add `qa`.

## 5. The agentic development life cycle (Mode ADLC)

One product wiki plus one code wiki per service, linked through `services/` symlinks. Agents cover the BA, QA and PM roles; humans operate and gate. Three pipelines: ingest (raw context into requirements, stories and per-service specs), build (the story loop of [[Workers and the dispatch pipeline]], resumable from its run ledger), and sync (`wrap-up` propagates down into the code wikis and up into the product wiki). The operator profile records the engagement pole, business-input or fully-managed, and the standing rulings the loop obeys ([[Operator profile - learn engagement style from corrections]]). Gate 0 governance sits above it in the product-management layer ([[Product Management Layer Skill]]). This is the top rung of [[Agentic Orchestration Levels]]; the field reviews are [[ADLC Field Review Findings]] and [[Skills Field Eval 2026-10]].

## 6. Manual work with the wiki as context

An engineer implements a story by hand and wants the context, not the loop: "`/adlc:wiki implement US-042`" loads the hot cache, the story, its spec and the conventions, and stops. The wrap-up then records what shipped like any other session. This is a routine use, not a misroute.

## 7. Intake for non-engineers

A product owner drops one five-heading note (problem, outcome, who is affected, constraints, open questions) into `.raw/intake/`; the next ingest turns it into requirements and stories. Nobody outside engineering touches the wiki directly.

## 8. Sharing, interop and other hosts

- **Cross-project access**: another repo's `AGENTS.md` points at the vault and reads the hot cache, then the index.
- **Other hosts**: Claude Code, Cursor and GitHub Copilot through their manifests; Codex CLI and OpenCode through a symlink to `skills/` ([[Hooks and host adapters]]).
- **People without Obsidian**: the vault is Markdown and YAML in git; `okf_export.py` renders an Open Knowledge Format bundle, and the publishing options are mapped in [[Wiki Sharing Patterns]] and [[Vault Publishing Topologies]].
- **Teams**: git is the state bus; session wiki branches and code-only PRs are the flow (`team-sync.md`, `git-flow.md`).

## 9. Feeding the plugin itself

Every vault keeps a ledger of what the plugin got wrong; the ratified entries travel to this repo as redacted reports and come back as a version ([[Release and upstream flow]]).

## Coming from the AI-Native SDLC Playbook

Same lifecycle, different substrate: the playbook's intent, spec, plan and review files map to typed wiki records with stable ids. The map is in [[AI-Native SDLC Playbook vs ADLC]]; the gaps it found (a Stage 6 trigger, evals on configuration change) are open threads in the hot cache.
