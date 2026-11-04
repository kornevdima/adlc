---
type: module
title: "Workers and the dispatch pipeline"
path: "agents/"
created: 2026-10-22
updated: 2026-11-04
tags:
  - architecture
  - module
  - agents
  - workers
status: active
related:
  - "[[Plugin architecture overview]]"
  - "[[Skills and routing]]"
  - "[[Generator-Evaluator Pattern]]"
  - "[[Structured Handoff]]"
  - "[[Validation Contract]]"
  - "[[Workers write to logs the dispatcher owns]]"
  - "[[Tester edits app code to prove a test bites]]"
---

# Workers and the dispatch pipeline

Sixteen subagents in `agents/<name>.md`. A skill dispatches one through the Agent tool with `subagent_type: "<name>"` and a packet of inputs; the worker runs in its own context, writes its record into the wiki, and returns one report. Nobody invokes a worker directly, and the description of each one says so. The agent files carry no model name: the host's default applies, and a per-host tier file is a postponed design ([[Configurable subagent models per host]]).

## The per-story pipeline

The `adlc` skill is the dispatcher. For one story in one service it runs, in order:

1. **`scope-analyst` in census mode**, when the story's scope is not yet measured against the code: it checks the story's claims, sweeps for the defect family, computes the blast radius, and proposes. It never rules and never writes feature code.
2. **The dispatcher writes the verification contract** (scenarios, preconditions, data hygiene, target fingerprint) before any code exists ([[Validation Contract]]).
   - **`feature-designer` in shape mode**, when the vault's toolset names a design tool and the story changes a user-facing surface: a design brief from the design-system folder (components and tokens to reuse, every state, copy pending acceptance, the accessibility floor, the visual rows the contract takes). It never writes code.
3. **`feature-builder`**: implements the code and unit tests from the spec, runs the service's own typecheck, lint and unit commands green. No e2e, no wiki, no commit.
4. **`feature-tester`**: writes the end-to-end specs from the contract in the service's own framework. Never edits app code, not even temporarily; the dispatcher's build snapshot and footprint check make that visible ([[Tester edits app code to prove a test bites]]). Builder and tester take turns on shared files ([[Parallel builder and tester revert each other's edits]]).
5. **`feature-reviewer`**: reviews the diff for correctness and quality against the service's conventions, files a review record, returns approved or changes requested. On changes requested the dispatcher loops back to builder and tester, then re-reviews.
   - **`feature-designer` in review mode**, same condition as above: impeccable detect, audit and critique and taste-skill's tell list, judged under the design system's dated rulings; a design review record whose verdict loops to the builder like a code finding. A tool that disagrees with a ruling is reported, not filed; visual acceptance stays the operator's.
6. **Cheap gates, then `feature-verifier`**: the dispatcher runs lint, typecheck and unit tests itself, then the verifier runs the contract against a local stack through docker compose and the chrome-devtools MCP, asserts data invariants, and writes one pass or fail record. It never fixes.
7. **The dispatcher re-verifies the evidence and commits** with trace ids; on fail it files the bug page and the backlog item.
8. **`scope-analyst` in reconcile mode**: folds the outcome into the remaining plan rows.

At the epic close: `doc-writer` writes end-user documentation from the as-built code when the service has the writing concern; `devops` pushes, opens the PR, deploys through the service's documented path and verifies the deployed revision, only when the operator says so and never touching infrastructure or secrets.

## The other workers

| Worker | Dispatched by | Does |
|---|---|---|
| `wiki-ingest-subagent` | `wiki-ingest` (batches of three or more) | Reads one source fully, files its pages, updates the index, reports |
| `wiki-lint-subagent` | `wiki-lint` (vaults of 20+ pages) | Reads the whole vault, runs the scripts, writes the structured lint report |
| `graphify-extract-subagent` | `graphify-ingest`, `graphify-update` | Extracts entities, edges and hyperedges from one chunk of files into JSON |
| `research-subagent` | `autoresearch` | Answers one plan question: searches, fetches, files source and concept pages |
| `mechanical-scanner-subagent` | `project-profile` | Scans a repo's build, test and lint configuration into the mechanical sections of `AGENTS.md` |
| `ba-suite-subagent` | the ADLC ingest pass, `wrap-up` | Runs one business-analysis method from the bundled library and files the deliverable with stable ids |
| `architecture-subagent` | the ADLC technical-planning pass | Refines requirements into a per-service shift-left spec in that service's code wiki |
| `ba-export-subagent` | `ba-export` | Renders one deliverable to Office or PlantUML under `.raw/exports/` |

## Rules every worker follows

- **Tool sets are the smallest that do the job.** Writers of pages get Read, Grep, Glob, Write, Edit; builders and testers add Bash; the verifier and devops add the chrome-devtools MCP. The code-touching workers also list the Semble and Serena servers (`mcp__semble__*`, `mcp__serena__*`) and the JetBrains IDE server's nine read tools (`mcp__idea__search_symbol` to `lint_files`; the builder adds `rename_refactoring`, nobody the terminal, run, patch or database tools), all of which resolve to nothing in a vault that has not configured them; the designer adds Skill for the impeccable and taste-skill skills.
- **Code navigation follows the vault's toolset.** graphify, or Semble to find and Serena or the JetBrains IDE server to read symbols and callers ([[JetBrains MCP server vs Serena for code navigation]]), or Grep; the dispatch packet carries the `code-nav` line and the service's `## Code navigation` section, and reports say which instrument found each claim ([[Configurable toolset for reader, code navigation and design]]).
- **Workers write their record and report its path.** `log.md`, `hot.md` and the board belong to the dispatcher ([[Workers write to logs the dispatcher owns]]).
- **A page a worker changes is rewritten to its current state** with one row in that folder's changelog; a new id is reported so the dispatcher can rebuild the glossary.
- **Hand-backs carry evidence**: the commands run and their exit codes, under the covering gates for the change; the dispatcher re-runs them before accepting ([[Hand-backs without the gates that cover the change]], [[Structured Handoff]]).
- **Nothing is left running** after a hand-back; the dispatcher checks ([[Workers and processes left running after hand-back]]).
- **No secrets in transcripts**: never print resolved configuration or env files; the permission profile and the env-guard hook enforce it ([[Workers print secrets from env files]]).
- **No hardcoded stack.** Commands and conventions come from the service's `AGENTS.md`; a missing file sends the dispatcher to `/project-profile` first.

## Why build and verify are different workers

The generator and the evaluator sit on opposite sides of a trust boundary ([[Generator-Evaluator Pattern]]): the worker that wrote the code cannot be the one that says it works, and the one that found the defect does not fix it. The same split puts the scope analyst's measurements and the dispatcher's rulings in different hands.
