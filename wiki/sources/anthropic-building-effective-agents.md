---
type: source
title: "Anthropic: Building effective agents"
created: 2026-11-08
updated: 2026-11-08
source_type: article
author: "Erik S., Barry Zhang (Anthropic)"
date_published: 2024-12-19
url: https://www.anthropic.com/engineering/building-effective-agents
confidence: high
tags:
  - orchestration
  - agents
  - governance
status: mature
key_claims:
  - "Workflows run LLMs through predefined code paths; agents direct their own process and tools (high)."
  - "Start with the simplest solution and add complexity only when it measurably helps (high)."
  - "Orchestrator-workers: a central LLM splits the task at run time, delegates to workers and synthesizes; suited to multi-file code changes and multi-source research (high)."
  - "Agents pause for human feedback at checkpoints or blockers; stop conditions such as an iteration cap keep control (high)."
---

# Building effective agents

The page is dated December 2024 (about two years old) and notes the tooling has since changed; the principles remain the reference most methods cite. (Source: [[anthropic-building-effective-agents]])

- Use a workflow when the steps are known and consistency matters. Use an agent when the step count cannot be predicted. Agents cost more and compound errors, so sandbox them and add guardrails.
- Orchestrator-workers differs from parallelization because the subtasks are not fixed in advance; the orchestrator derives them from the input.
- Human review stays essential for coding agents, to confirm a solution fits the wider system.
- The article prescribes no log or status file. Recording is left to the builder. It says nothing on spikes or environment setup.

Related: [[Agentic Lifecycle Methods Compared]], [[anthropic-harness-design]].
