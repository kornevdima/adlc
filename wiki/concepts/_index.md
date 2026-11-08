---
type: meta
title: "Concepts Index"
updated: 2026-11-08
tags:
  - meta
  - index
  - concept
domain: knowledge-management
status: evergreen
related:
  - "[[concepts/_changelog]]"
  - "[[index]]"
  - "[[Hot Cache]]"
  - "[[LLM Wiki Pattern]]"
  - "[[Compounding Knowledge]]"
---

# Concepts Index

Navigation: [[index]] | [[entities/_index|Entities]] | [[sources/_index|Sources]] | [[concepts/_changelog|Changelog]]

All concept pages — ideas, patterns, and frameworks extracted from sources.

---

## Knowledge Management

- [[LLM Wiki Pattern]] — the core architecture for persistent, compounding knowledge bases
- [[Hot Cache]] — ~500-word session context file, updated after every ingest
- [[Compounding Knowledge]] — why the wiki grows more valuable over time, unlike RAG

---

## AI Agents

- [[Domain-Specific Agents]] — composition over inheritance for agents: small complete agents under a coordinator, minimal per-agent context (Source: [[yt-schroeder-domain-specific-agents]])
- [[Multi-Agent Communication Taxonomy]] — five primitives: delegation, creator-verifier, direct communication, negotiation, broadcast (Source: [[yt-alvoeiro-multi-agent-architecture]])
- [[Validation Contract]] — correctness defined at planning time, before code; assertion coverage accounted across features; validated behaviorally (Source: [[yt-alvoeiro-multi-agent-architecture]])
- [[Structured Handoff]] — schema-shaped worker report (done / undone / commands + exit codes / issues / procedure compliance) that lets clean-context agents inherit state (Sources: [[yt-alvoeiro-multi-agent-architecture]], [[anthropic-harness-design]])
- [[Plan-Driven Research Loop]] — autoresearch v2: persisted plan artifact with `[ ] [→] [✓] [!]` statuses, question-driven loop, subagent per question, stuck rule, budgets (Source: [[openmanus-repo]])
- [[Harness Engineering]] — Agent = Model + Harness: the discipline of owning the scaffolding (rules, tools, sandboxes, orchestration, hooks, observability); most agent failures are configuration failures; configure → run → feedback loop → observe lifecycle (Source: [[vibe-coding-new-sdlc-day1]])
- [[Agentic Orchestration Levels]] — operator's four-level adoption ladder: 0 chat session, 1 assisted editing, 2 conductor with a harness, 3 orchestrator (Mode ADLC, grilling gate before delegation); levels 1–2 interpolated from the Day-1 spectrum (Source: [[vibe-coding-new-sdlc-day1]], operator synthesis)

---

## Agent Workflow

- [[ADLC Field Review Findings]] — production two-wiki ADLC review: code-first inversion, handoff-seam costs (zero traceability, re-derivation), records-as-pages, duplication rates (~6–8% volume / 25–30% of the shared layer), delegation share as the efficiency lever (Source: field review, 2026-07-04)
- [[Grilling Session]] — alignment-first interview (one question at a time + recommended answer) until a shared design concept exists; precedes any plan/PRD (Source: [[yt-pocock-ai-coding-workflow]])
- [[Ralph Wiggum Loop]] — AFK implementation loop: fresh context per iteration over an issue backlog, sentinel-terminated, sandboxed; Sandcastle for the parallel version (Source: [[yt-pocock-ai-coding-workflow]])
- [[Vertical Slices for Agent Tasks]] — tracer-bullet issue decomposition; Kanban DAG of independently grabbable, all-layer slices enables parallel agents (Source: [[yt-pocock-ai-coding-workflow]])
- [[Deep Modules]] — Ousterhout's small-interface/big-functionality modules as agent enablement: feedback-loop quality is the ceiling on agent output (Source: [[yt-pocock-ai-coding-workflow]])

---

## Knowledge Sharing & Publishing

- [[Open Knowledge Format]] — Google's markdown + YAML interchange format for agent knowledge; v0.2; visualizer is a one-file graph viewer, Knowledge Catalog is agent-facing (Source: [[okf-spec-and-reference-repo]])
- [[Vault Publishing Topologies]] — rebuild-from-repo vs push-from-app vs live-render; only the first keeps agent commits live for readers (Source: [[obsidian-static-publishers-comparison]])
- [[Obsidian Vault Portability]] — portability tiers, build rules, Confluence-expectation map (Source: [[obsidian-vault-site-generators]])
- [[One-Way Publish vs Round-Trip Wiki Sync]] — lowering-step spec and decision tree for a git-canonical wiki (Source: [[git-backed-wiki-platforms-comparison]])
- [[Cross-Repo Wiki Access]] — agent routes into a sibling vault and convention breakage per GitHub surface (Source: [[claude-code-large-codebases-docs]], [[github-docs-markdown-wikis-pages]])

---

## Organizing the Work

Filed 2026-11-08 by the research [[Research How work is organized]].

- [[Software Lifecycle Inputs and Handoffs]] — the stable inputs and the four handoffs between them (Source: [[scrum-guide-2020]], [[shape-up-basecamp]])
- [[Knowledge Layer and Work Tracker Split]] — pages against work items, linked by id; epic and sprint as independent fields (Source: [[atlassian-what-is-an-epic]], [[backlog-md-readme]])
- [[Lifecycle Artifacts and Decision Levels]] — one record per stage, four decision levels, what is not a decision (Source: [[nygard-documenting-architecture-decisions]], [[madr-markdown-decision-records]])
- [[Project Within a Larger System]] — C4, interaction modes, catalog descriptor, bounded contexts (Source: [[backstage-system-model]], [[fowler-bounded-context]])
- [[Shared Remote Collaboration for Agent Teams]] — worktrees, CODEOWNERS, single-writer files, secret defences, joining (Source: [[claude-code-common-workflows-worktrees]], [[github-code-owners-and-push-protection]])
- [[Delivery Metrics and Their Data Sources]] — DORA, flow, SPACE; git against work-item data (Source: [[dora-metrics-guide]], [[getdx-flow-metrics]])
- [[Agentic Lifecycle Methods Compared]] — AI-DLC, Spec Kit, Kiro, BMAD, Anthropic guidance (Source: [[aws-ai-dlc-workflows]], [[anthropic-building-effective-agents]], [[spec-kit-research]])
- [[Gates as Checkpoints Without Documents]] — criteria in, one decision line out (Source: [[cooper-stage-gate-systems-1990]], [[scrum-guide-2020]])
- [[Disciplines Bodies of Knowledge and Boundaries]] — bodies of knowledge per input; where analysis ends and architecture begins (Source: search summaries; primaries unreachable)

---

## Add new concepts here as they are extracted from sources.
