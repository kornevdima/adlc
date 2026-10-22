---
type: module
title: "Skills and routing"
path: "skills/"
created: 2026-10-22
updated: 2026-10-22
tags:
  - architecture
  - module
  - skills
status: active
related:
  - "[[Plugin architecture overview]]"
  - "[[Workers and the dispatch pipeline]]"
  - "[[Shared references]]"
  - "[[Evals]]"
  - "[[maintenance-triggers]]"
---

# Skills and routing

Twenty skills in `skills/<name>/SKILL.md`, following the cross-platform Agent Skills spec: frontmatter with `name` and `description` only, the trigger phrases inside the description. The host matches a person's words against the descriptions, so the description is the routing table. Skills are the only user-facing entry points; workers are dispatched from inside them.

## The three families

**Knowledge substrate**, the wiki itself:

| Skill | Does | Dispatches | Own references or scripts |
|---|---|---|---|
| `wiki` | Set up and scaffold a vault (modes, concerns, ADLC topology); load context for work done by hand; route to the sub-skills | `architecture-subagent` (ADLC initial pass) | `references/` (61 docs, shared), `scripts/` (6) |
| `wiki-ingest` | File one source or a batch into pages, cross-reference, log | `wiki-ingest-subagent` (3+ sources) | none |
| `wiki-query` | Answer from the wiki, hot cache first; large-vault mode with `index.json`; routes structural questions to the code graph | none | `build_index_json.py` |
| `wiki-lint` | Health check: 28 numbered checks, from orphans and dead links to history markers, changelog and glossary drift, graph staleness | `wiki-lint-subagent` (vaults of 20+ pages) | `lint_graph.py` |
| `save` | File the current conversation as a typed note | none | none |
| `autoresearch` | Plan-driven research loop, one subagent per question, resumable plan | `research-subagent` | `program.md` |
| `wiki-faq` | In-session help: requirements, workflow, troubleshooting, terminology | none | four help documents |
| `obsidian-markdown`, `obsidian-bases` | Obsidian-flavoured Markdown and `.base` database files, from the Obsidian creator's skills | none | none |

**Code graph**, the optional structural layer for code projects:

| Skill | Does | Dispatches | Scripts |
|---|---|---|---|
| `graphify-ingest` | Build the code graph (AST plus semantic extraction in chunks), file summaries into `wiki/code/` | `graphify-extract-subagent` (one per chunk) | `chunks.py`, `merge.py`, `regenerate.py` |
| `graphify-update` | Incremental rebuild after a change, labels preserved | `graphify-extract-subagent` (changed docs only) | `detect.py`, `update.py` |
| `graphify-query`, `graphify-path`, `graphify-explain` | Traverse, shortest path, node with neighbours; no LLM cost | none | the graphify CLI |

**Roles and delivery**, the agentic development life cycle:

| Skill | Does | Dispatches | Own references or scripts |
|---|---|---|---|
| `adlc` | The delivery loop: readiness gate, run ledger, story loop, epic close, distill, upstream export | `scope-analyst`, `feature-builder`, `feature-tester`, `feature-reviewer`, `feature-verifier`, `doc-writer`, `devops` | `upstream-shipped.md`, `build_snapshot.py` |
| `wrap-up` | Session sync across the product wiki and the code wikis, boards reconciled, caches refreshed | `ba-suite-subagent` for BA catch-up | `usage_report.py` |
| `product-management-layer` | Gate 0 governance: tool approval, buy-versus-build, compliance scoping | none | `reference.md`, its own eval runner |
| `ba-export` | Render wiki deliverables to Office files and PlantUML | `ba-export-subagent` (one per deliverable) | none |
| `technical-writer` | Documents for a human reader, translations kept in step, operator corrections recorded | none | none (method in the shared `writing-style.md`) |
| `project-profile` | Build or refresh a repo's `AGENTS.md` from a config scan plus a short interview | `mechanical-scanner-subagent` | none |

## Routing rules worth knowing

- **The wiki skill is also a context loader.** "`/adlc:wiki implement US-042`" reads the hot cache, the story and its spec and stops; it does not start a run. That is the manual mode, used when an engineer implements a story by hand ([[Use cases and modes]]).
- **Mode decides the ingest path.** In a Mode ADLC vault, `wiki-ingest` writes the source summary and then routes the structured deliverables to the BA and architecture workers instead of flattening them into entities and concepts.
- **Skills own the logs.** Only the dispatching skill writes `log.md`, `hot.md` and the board; workers report paths.
- **Orchestration never leaves the skill.** A skill that needs parallel or isolated work dispatches a worker; it does not call another skill's worker through a side channel.
- **When to run which skill** is the subject of [[maintenance-triggers]].

## Where the tests are

Thirteen of the twenty skills have cases under `evals/<skill>/`; the five graphify skills and the product-management layer keep older local runners. See [[Evals]].
