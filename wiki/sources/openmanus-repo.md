---
type: source
title: "FoundationAgents/OpenManus (GitHub)"
source_type: code-repo
author: "Xinbin Liang, Jinyu Xiang et al. (MetaGPT team)"
date_published: 2025
url: "https://github.com/FoundationAgents/OpenManus"
created: 2026-07-08
updated: 2026-07-08
confidence: high
tags:
  - source
  - agents
  - planning
status: current
related:
  - "[[OpenManus]]"
  - "[[Plan-Driven Research Loop]]"
  - "[[Research OpenManus for claude-mem]]"
key_claims:
  - "PlanningFlow persists a plan with per-step statuses (not_started / in_progress / completed / blocked) + notes; executor loop always picks the first non-completed step"
  - "Step-typed executor routing: [TYPE] tag in step text selects the executor agent"
  - "BaseAgent.is_stuck(): duplicate assistant-output detection (threshold 2) injects a change-strategy prompt"
  - "max_steps hard budget (default 10) with graceful termination report"
  - "MCP both directions: run_mcp.py (agent consumes MCP tools), run_mcp_server.py (exposes itself as MCP server)"
  - "Multi-agent run_flow.py marked unstable by the authors"
  - "MIT license; 56.4k stars / 9.8k forks; last release v0.3.0 (2025-04-10); ~343 open issues, ~200 open PRs as of 2026-07"
---

# Source: FoundationAgents/OpenManus (GitHub)

**URL**: https://github.com/FoundationAgents/OpenManus

## Summary

Open-source general agent framework (Python, MIT) from the MetaGPT team, born as a 3-hour prototype during the 2025 Manus hype. ReAct loop + tool collection (browser-use, Python exec, file ops, search, chart visualization), works with any OpenAI-compatible LLM API via `config.toml`.

## Architecture notes (from source, `main` @ 2026-07-08)

- `app/flow/planning.py` — **PlanningFlow**: planner LLM creates a persisted plan via a PlanningTool; each step executed in isolation with a "only execute this current step" prompt; per-step statuses `[ ] [→] [✓] [!]`, notes, progress rendering; separate finalize/summary pass at the end.
- `app/agent/base.py` — **BaseAgent**: step-based loop bounded by `max_steps`; `is_stuck()` counts identical assistant messages and prepends a "consider new strategies" prompt when threshold (2) is hit.
- Executor selection: regex `\[([A-Z_]+)\]` on step text routes the step to a matching named agent.

## Why it matters for claude-mem

The runtime itself is not adoptable (Python orchestration can't execute Agent Skills; project semi-dormant since ~2025-04). The **patterns** transfer: persisted plan artifact, question-driven loop, typed executor routing, stuck detection, and step budgets map directly onto `/autoresearch`. See [[Plan-Driven Research Loop]] and [[Research OpenManus for claude-mem]].

## Caveats

Post-hype maintenance risk: last release 2025-04-10, hundreds of open issues/PRs. Star count (56k) is a hype artifact, not a maturity signal.

## Connections

- [[OpenManus]] | [[Plan-Driven Research Loop]] | [[Research OpenManus for claude-mem]] | [[agent-sdk-comparisons-2026]]
