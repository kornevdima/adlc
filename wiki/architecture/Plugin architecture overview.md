---
type: overview
title: "Plugin architecture overview"
created: 2026-10-22
updated: 2026-10-22
tags:
  - architecture
  - plugin
  - overview
status: active
related:
  - "[[architecture/_index]]"
  - "[[Skills and routing]]"
  - "[[Shared references]]"
  - "[[Workers and the dispatch pipeline]]"
  - "[[Hooks and host adapters]]"
  - "[[Scripts]]"
  - "[[Evals]]"
  - "[[Use cases and modes]]"
  - "[[Release and upstream flow]]"
  - "[[LLM Wiki Pattern]]"
  - "[[Harness Engineering]]"
---

# Plugin architecture overview

adlc is a harness for agentic delivery: a persistent Obsidian wiki as the knowledge substrate, role skills that read and write it, a plan-driven loop that dispatches workers story by story, and the hooks, scripts and evals that keep all of that honest. Version 1.0.9. This page is the map; each part has its own page.

## One folder, three roles

The repository root is at the same time the plugin source, an Obsidian vault and a working git repo. Nothing is copied between the three.

| Role | What lives there |
|---|---|
| Plugin source | `.claude-plugin/`, `.cursor-plugin/`, `.github/plugin/`, `agents/`, `hooks/`, `skills/`, `bin/`, `evals/` |
| Obsidian vault | `wiki/` (this knowledge base), `.raw/` (immutable sources, including the upstream reports), `_attachments/` |
| Working repo | git history, `README.md`, `AGENTS.md`, `LICENSE`, `ATTRIBUTION.md` |

The vault here is the plugin's own design wiki: research sources, concept pages, the questions that became fixes, and now this folder. Vaults that use the plugin have the same three layers (`.raw/`, `wiki/`, `AGENTS.md`) and are scaffolded by the wiki skill.

## The layers

From the outside in:

1. **Host adapters.** A manifest per host (Claude Code, Cursor, GitHub Copilot) points at the same `skills/` and `agents/` folders; Codex CLI and OpenCode reach the skills through a symlink. Each host gets its own hook file with the same two hooks: print the hot cache at session start, nudge for a hot-cache update at stop. See [[Hooks and host adapters]].
2. **Skills.** Twenty Agent Skills, each a `SKILL.md` with a trigger phrase in its description. They are the only entry points a person uses. Three families: the knowledge substrate, the code graph, roles and delivery. See [[Skills and routing]].
3. **Shared references.** Sixty-one documents under the wiki skill's `references/` folder that other skills and the workers read at run time: the bundled business-analysis method, the shift-left method, the vault modes and concerns, the writing method, the permission profile, the templates. A skill folder of its own holds a reference only when no one else needs it. See [[Shared references]].
4. **Workers.** Fifteen subagents in `agents/`, dispatched by skills through the Agent tool with a packet of inputs, never invoked by a person. They run in their own context and return one report. See [[Workers and the dispatch pipeline]].
5. **Scripts.** Fifteen standard-library Python scripts beside the skills that own them, plus one shell installer. They do the deterministic work a prompt should not: lint checks, the glossary, the tester footprint, the upstream redaction check, the OKF export. See [[Scripts]].
6. **Evals.** Cases for `claude plugin eval` under `evals/`, run locally before each version bump, with layered fixtures and deterministic graders. See [[Evals]].

## How a request moves through the layers

A session starts: the host's SessionStart hook prints `wiki/hot.md`, so the agent has the vault's recent context before the first prompt. The person types a trigger phrase or a slash command, and the matching skill loads. The skill reads the references it names (the writing method, the mode's folder map, the operator profile), does the orchestration itself, and dispatches a worker where the work should run in isolation or in parallel: one ingest subagent per source, one research subagent per question, the build, test, review and verify workers per story. Workers write their record into the wiki and report its path; the dispatching skill writes the logs, the board and the hot cache. Scripts run inside skills and workers as the routine path for anything mechanical, so the permission profile can allow-list them. At stop, the hook checks whether `wiki/` changed and asks for the hot cache to be refreshed, or for the wrap-up skill when the vault has service checkouts.

## Where the knowledge lives

- **Hot cache** (`wiki/hot.md`): about 500 words of recent context, read at session start, rewritten at session end. [[Hot Cache]].
- **Index and log** (`wiki/index.md`, `wiki/log.md`): the catalog and the chronological record. Pages hold the current state; history goes to each folder's `_changelog.md`; every identifier has a glossary entry ([[Pages carry their history inline]], [[Identifiers with no glossary]]).
- **Sources** (`.raw/`): immutable; agents never edit them. `.raw/.manifest.json` tracks what has been ingested.
- **Code graph** (optional, `graphify-out/` and `wiki/code/`): the structural layer for code projects. [[graphify-integration]].
- **Per-vault instruments** (`wiki/meta/`): mission control, the operator profile, the upstream ledger, lint reports, the usage rollup.

## Design principles the parts follow

- **The wiki is canonical.** Office exports, boards and tracker items are generated views.
- **Skills orchestrate, workers do isolated work, scripts do mechanical work.** A worker never writes the dispatcher's logs; a prompt never does what a script can check ([[Workers write to logs the dispatcher owns]]).
- **Every harness rule traces to a real failure.** Rules enter through the upstream channel from the vaults, with a question page here and a shipped row in the plugin ([[Release and upstream flow]]).
- **No hardcoded stack.** Workers read the service's own `AGENTS.md` for commands and conventions; `/project-profile` writes that file.
- **Writing for a human reader is one method everywhere**: skills, worker reports and the wiki pages they produce follow the writing-style reference ([[One writing method for every human reader]]).

## Related design pages

[[Harness Engineering]] (the agent is the model plus its harness), [[Generator-Evaluator Pattern]] (why build and verify are separate workers), [[Structured Handoff]] and [[Validation Contract]] (the shape of a worker report and a verification contract), [[Agentic Orchestration Levels]] (where Mode ADLC sits on the adoption ladder), [[AI-Native SDLC Playbook vs ADLC]] (the vocabulary map).
