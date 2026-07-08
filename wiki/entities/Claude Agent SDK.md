---
type: entity
title: "Claude Agent SDK"
entity_type: product
created: 2026-07-08
updated: 2026-07-08
tags:
  - entity
  - tool
  - sdk
status: current
related:
  - "[[agent-sdk-comparisons-2026]]"
  - "[[Research OpenManus for claude-mem]]"
---

# Claude Agent SDK

Anthropic's open-source framework for building agents on the "give the agent a computer" paradigm — shell, filesystem, web. Same engine that powers Claude Code; executes Agent Skills natively and has the deepest MCP integration of the 2026 SDK field (Source: [[agent-sdk-comparisons-2026]]).

**Relevance to claude-mem**: recommended runtime for the future headless branch (`feat/headless-agent`) — reuses `skills/*` as-is with zero port, enabling cron/CI-driven ingest and autoresearch via the Anthropic API. Decision record: [[Research OpenManus for claude-mem]].

## Connections

- [[Google ADK]] | [[agent-sdk-comparisons-2026]] | [[Research OpenManus for claude-mem]]
