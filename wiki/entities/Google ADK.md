---
type: entity
title: "Google ADK"
entity_type: product
created: 2026-07-08
updated: 2026-07-17
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

**Agents CLI** (May 2026): Google now ships `google-agents-cli`, a small CLI that adds seven skills covering the full ADK lifecycle (scaffold, write agent code, evaluate, deploy to Agent Runtime, wire observability) to whichever coding agent the developer already uses — Claude Code, Codex, or another. Notably this embraces the skills-on-top-of-any-agent distribution model rather than requiring the ADK SDK as entry point. (Source: [[vibe-coding-new-sdlc-day1]])

## Connections

- [[Claude Agent SDK]] | [[agent-sdk-comparisons-2026]] | [[Research OpenManus for claude-mem]] | [[vibe-coding-new-sdlc-day1]]
