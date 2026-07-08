---
type: entity
title: "Google ADK"
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

# Google ADK (Agent Development Kit)

Google's code-first multi-agent framework. ADK 2.0 (April 2026) added graph-based workflows and collaborative agent teams; SDKs in Python, TypeScript, Java, Go; native A2A protocol; model-agnostic via LiteLLM (Gemini, Claude, Ollama, vLLM) while optimized for Gemini (Source: [[agent-sdk-comparisons-2026]]).

**Relevance to claude-mem**: not chosen for the headless branch — it treats Agent Skills as plain markdown, forcing an orchestration rewrite. Interop path instead: ADK agents (like any MCP client) consume a future claude-mem vault MCP server. Decision record: [[Research OpenManus for claude-mem]].

## Connections

- [[Claude Agent SDK]] | [[agent-sdk-comparisons-2026]] | [[Research OpenManus for claude-mem]]
