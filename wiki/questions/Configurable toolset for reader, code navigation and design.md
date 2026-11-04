---
type: synthesis
title: "Configurable toolset for reader, code navigation and design"
created: 2026-11-04
updated: 2026-11-04
tags:
  - plugin
  - toolset
  - agents
  - design
  - code-graph
status: resolved
related:
  - "[[Plugin architecture overview]]"
  - "[[Workers and the dispatch pipeline]]"
  - "[[Shared references]]"
  - "[[Scripts]]"
  - "[[graphify-integration]]"
  - "[[Integrate the wiki toolset into the ADLC workers]]"
  - "[[Configurable subagent models per host]]"
---

# Configurable toolset for reader, code navigation and design

**Resolved 2026-11-04 (plugin 1.1.0, unreleased).** A vault now declares its tools in a `Toolset:` block in its `AGENTS.md`, beside `Mode:` and `Concerns:`. Obsidian and graphify stay the defaults for vaults without the block; nothing requires them.

## The problem

Two tools were written into the plugin as if every vault used them. Obsidian appeared in 34 plugin files and graphify in 40 (skills, workers, the installer, the README and the manifests, counted 2026-11-04 before the change). The operator's own practice had moved on:

- The vaults are read in the operator's own renderer, a local web app for Obsidian-flavoured Markdown (wiki-renderer, MIT), so "open the folder in Obsidian", the Obsidian MCP notes, the `.obsidian/app.json` the graph build wrote, and the Bases, Canvas and Dataview artefacts were instructions for a tool nobody ran.
- Code navigation in the delivery vaults had moved to two MCP servers, Semble (search by meaning, file and line back) and Serena (symbol-level reads and edits through the language server). The operator's repo-local worker bindings carried the playbook (operator ruling 2026-11-01), but the generic workers, `wiki-query`, `wiki-lint`, the epic close and the planning reference knew only graphify, and `graphify-ingest` ran its installer on every build.
- A design system had been built with impeccable (a `DESIGN.md` summary, tokens, a brand book with dated owner rulings) and reviewed with impeccable's detector, audit and critique, and taste-skill's tell list. The loop had no worker for design: the builder decided the look and the verifier checked behaviour.

## The design

One block, four keys, read by every skill and worker that used to assume a tool:

```markdown
Toolset:
  reader: wiki-renderer             # obsidian | wiki-renderer | none
  code-nav: semble, serena          # graphify | semble | serena | none
  design: impeccable, taste-skill   # impeccable | taste-skill | none
  design-system: ~/work/design-system
```

Defaults when the block is absent reproduce the previous behaviour: `obsidian`, graphify when `graphify-out/graph.json` exists, no design tool. The reference `skills/wiki/references/toolset.md` names the options, what each one changes in which skill, the Semble and Serena playbook the workers follow, the install and permission lines. The script `skills/wiki/scripts/toolset.py` resolves the block (`show`), checks what is installed (`check`, with the install line per missing tool) and proposes a block from the machine (`detect`); eight parser tests in `test_toolset.py`.

Why the vault `AGENTS.md` and not a settings file or the operator profile: every skill and worker already reads that file first, the `Mode:` and `Concerns:` lines set the precedent, and the dispatcher inlines sections of it into packets. A per-machine file ([[Configurable subagent models per host]]) answers a different question, which model a host has; the toolset is a property of the vault and travels with it.

## What changed

- **Scaffold** (`wiki` skill step 3a): proposes the block from `toolset.py detect`, asks the three choices and the design-system folder, writes the block and runs `check`; the AGENTS.md template carries the block and two filing rows for design briefs and design reviews; the open-the-vault instruction follows the reader.
- **Reader-specific artefacts** are written only for `reader: obsidian`: the `.obsidian/app.json` default and the canvas note in `graphify-ingest`, the Dataview dashboard and the canvas map in `wiki-lint` (a Markdown dashboard otherwise), the Bases suggestion in `mission-control.md`, the Obsidian MCP notes in `mcp-setup.md`. The dialect itself does not change: pages stay Obsidian-flavoured Markdown, which both readers render.
- **Code navigation**: the seven code-touching workers (`feature-builder`, `feature-tester`, `feature-reviewer`, `feature-verifier`, `scope-analyst`, `doc-writer`, `architecture-subagent`) orient with the tool the packet names, with three branches (graphify, Semble and Serena, none) and the rule that the tool finds and the code asserts, and list `mcp__semble__*` and `mcp__serena__*` in their tools. `wiki-query` routes structural questions to Semble when the block names it. `/adlc` reads the block at Step 0, puts the `code-nav` line and the service's `## Code navigation` section into every packet, and refreshes a graph at the epic close only for graphify; `wrap-up` the same. `graphify-ingest` and `graphify-update` refuse when the block names another tool, and the ingest reuses the pinned interpreter instead of running the installer every time. `technical-planning.md` § Code navigation grounding and `permissions.md` carry the generic text and the allow lines.
- **Design**: a sixteenth worker, `feature-designer`, with two modes. `shape` runs after the contract and before the build: a brief from the design system (surface and mode, components and tokens to reuse, every state, copy pending acceptance, the accessibility floor, the contract's visual rows, open questions for the operator). `review` runs after the code review and before the verifier: impeccable `detect`, `audit` and `critique`, taste-skill's redesign audit and tell list, judged under the design system's dated rulings; a review record with a verdict that loops to the builder. It never edits code and never rules on taste; a tool that disagrees with a ruling is reported, not filed. `/adlc` dispatches it at Steps 2.2b and 2.5a only when the block names a design tool and the story changes a user-facing surface. The `design` concern reference gains the two record shapes.
- **Documentation**: the README's install section, the FAQ's requirements, workflow, troubleshooting and glossary, this repo's `AGENTS.md`, the four manifests (1.1.0, "Markdown wiki" in the descriptions, new keywords), and the architecture pages.

## Field evidence

- A co-located delivery vault's repo-local bindings for five workers carried the Semble and Serena playbook since the operator's ruling of 2026-11-01: find with Semble, read and edit TypeScript symbols with Serena, Grep for literal sweeps, say which instrument found each claim. The generic text in `toolset.md` is that playbook without the repo's specifics (which file types Semble indexes, which language Serena's server parses), which stay in the binding and in the service `AGENTS.md`.
- A design-system repository built with impeccable: `DESIGN.md` generated from the brand book, a `.impeccable/design.json` sidecar, five critique snapshots, an `AGENTS.md` that ranks the brand book's dated rulings above the tool's heuristics ("when a tool disagrees with a ruling, report the disagreement; don't fix the ruling"). The designer's rules are that repository's practice made generic.
- The operator's renderer renders wikilinks, embeds, callouts, Mermaid, frontmatter and highlighted code, searches the wiki and saves edits back; it does not render `.base` or `.canvas` files, which is the line between dialect and reader-only artefacts.

## Assumed or unverified

- A worker whose `tools:` lists an MCP server the session has not configured: the Claude Code documentation says a subagent fails to launch only when **no** entry resolves, and does not describe the partial case. The built-in tools always resolve, so the workers are expected to launch with the MCP entries dropped. Not tested on a machine without the servers.
- The new eval case `evals/wiki/scaffold-toolset` was written, not run; the fast set is the operator's pre-release check.
- `impeccable critique` asks for two isolated sub-agents; the designer has no Agent tool and runs the two assessments inline with the degraded banner the reference prescribes.

## Resolution log

- 2026-11-04: requested by the operator ("instead of obsidian I have my own wiki reader"; "we don't need to install graphify every time, I'm testing serena + semble"; "create a design sub-agent that uses impeccable and tasteskill"); designed and built in one session; version 1.1.0, not committed.
