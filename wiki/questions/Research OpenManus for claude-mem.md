---
type: synthesis
title: "Research: OpenManus for claude-mem"
created: 2026-07-08
updated: 2026-07-08
tags:
  - research
  - agents
  - runtime
status: developing
related:
  - "[[OpenManus]]"
  - "[[Claude Agent SDK]]"
  - "[[Google ADK]]"
  - "[[Plan-Driven Research Loop]]"
sources:
  - "[[openmanus-repo]]"
  - "[[agent-sdk-comparisons-2026]]"
---

# Research: OpenManus for claude-mem

## Overview

Evaluated OpenManus as a foundation for running claude-mem as an autonomous agent over APIs. Verdict: reject as runtime, adopt as pattern source. The headless runtime question resolves to the Claude Agent SDK; interop with other frameworks resolves to a future vault MCP server.

## Key Findings

- OpenManus is a capable but semi-dormant hype-era framework: last release v0.3.0 (2025-04-10), ~343 open issues (Source: [[openmanus-repo]])
- claude-mem's orchestration lives in Agent Skills (markdown); no external Python framework can execute it — any runtime adoption means a full port and permanent divergence (Source: [[openmanus-repo]])
- Claude Agent SDK executes the existing skills natively; it is the zero-rewrite path to cron/CI-driven ingest and autoresearch (Source: [[agent-sdk-comparisons-2026]])
- Google ADK 2.0 is the stronger explicit multi-agent framework but offers no skills reuse; its interop is reachable via MCP instead (Source: [[agent-sdk-comparisons-2026]])
- Five OpenManus patterns transfer to `/autoresearch`: persisted plan, question-driven loop, typed executor routing, stuck detection, step budgets → [[Plan-Driven Research Loop]]

## Options Considered (2026-07-08)

| Option | Verdict |
|---|---|
| A: Claude Agent SDK headless branch | **Recommended**; pending FRs + ADR |
| B: Vault MCP server | Deferred — "good option later"; AGENTS.md will declare the MCP tools |
| C: Adopt OpenManus as runtime | Rejected — rewrite cost + framework risk |
| D: Patterns only | **Implemented** — autoresearch v2 |

## Key Entities

- [[OpenManus]]: pattern source, rejected runtime, potential future MCP consumer
- [[Claude Agent SDK]]: chosen runtime for the future headless branch
- [[Google ADK]]: rejected for headless branch; MCP interop path instead

## Key Concepts

- [[Plan-Driven Research Loop]]: the five adapted patterns, implemented in autoresearch v2

## Contradictions

- Star count vs maturity: 56k stars suggests a healthy project; release/issue data says semi-dormant. Maintenance data is more credible than stars (Source: [[openmanus-repo]])

## Open Questions

- FRs + ADR for the headless branch (`feat/headless-agent`) — not yet written
- Vault MCP server tool surface (read/write/query granularity) — deferred
- Eval coverage for autoresearch v2 via skill-creator — pending

## Sources

- [[openmanus-repo]]: FoundationAgents/OpenManus, main @ 2026-07-08
- [[agent-sdk-comparisons-2026]]: 2026 SDK comparison articles (medium confidence)
