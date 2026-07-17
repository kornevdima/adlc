---
type: concept
title: "Harness Engineering"
complexity: intermediate
domain: ai-agents
aliases:
  - "Agent Harness"
  - "Agent = Model + Harness"
created: 2026-07-17
updated: 2026-07-17
tags:
  - concept
  - harness
  - agentic-engineering
  - context-engineering
  - evals
status: current
related:
  - "[[vibe-coding-new-sdlc-day1]]"
  - "[[Context Engineering for Coding Agents]]"
  - "[[Context Rot]]"
  - "[[Generator-Evaluator Pattern]]"
  - "[[Agentic Orchestration Levels]]"
  - "[[AGENTS.md]]"
  - "[[LLM Wiki Pattern]]"
sources:
  - "[[vibe-coding-new-sdlc-day1]]"
  - "[[anthropic-harness-design]]"
---

# Harness Engineering

The discipline of designing and owning the scaffolding wrapped around an AI model — prompts and rule files, tools, context policies, hooks, sandboxes, sub-agents, and observability — that turns a raw model into an agent that can actually finish something. **Agent = Model + Harness.** The behaviour developers experience with any coding agent is dominated by what the harness does, not just by which model is underneath. (Source: [[vibe-coding-new-sdlc-day1]])

The counter-intuition it corrects: treating the model as the system ("new model, agent gets smarter") leads to the wrong investments. The model is one input into a running agent. And crucially, the harness is **the team's surface area, not the model provider's** — it can be reviewed, versioned, evaluated, and improved like any other engineering asset.

## What's in the harness

- **Instructions and rule files** — who the agent is, what it cares about, what it is forbidden from doing: [[AGENTS.md]], CLAUDE.md, skill files, sub-agent prompts.
- **Tools** — functions, MCP servers, APIs, *plus the prose that tells the model when and how to call them*.
- **Sandboxes / execution environments** — where the agent's code actually runs and what it cannot reach.
- **Orchestration logic** — sub-agent spawning, model routing, hand-offs between specialists, and the rules governing when each fires.
- **Guardrails / hooks** — deterministic code at lifecycle points (before a tool call, after an edit, before a commit); "the place for things the agent should never forget but often does."
- **Observability** — logs, traces, evaluations, cost and latency metering; without it there is no way to tell whether the agent is doing well or quietly drifting.

## Why it matters: the harness effect is measurable

- Terminal Bench 2.0: one team moved a coding agent **from outside the Top 30 to the Top 5 by changing only the harness** — no model change.
- LangChain: **+13.7 points** on the same benchmark by tweaking only the system prompt, tools, and middleware around a fixed model.
- The everyday corollary: when an agent misbehaves, the first instinct is to blame the model, but the failure usually traces to a missing tool, a vague rule, an absent guardrail, or a context window stuffed with noise (see [[Context Rot]]). **"Most agent failures, examined honestly, are configuration failures."**

This is also what separates the ends of the vibe-coding-to-agentic-engineering spectrum: the same agent, vibe coded or engineered, differs only in how deliberately the harness is configured. Vibe coding runs on minimal, implicit scaffolding; agentic engineering on explicit harness abstractions from planning through production monitoring.

## The harness in the SDLC lifecycle

The harness must be present in every phase where an agent operates; different phases exercise different components:

1. **Configure** (requirements, planning, architecture) — set up rule files and architectural constraints, define the tool surface, fix the rules the agent cannot break. In this vault's practice, a [[Grilling Session]] belongs here: it turns unknown unknowns into decisions *before* the harness is pointed at implementation.
2. **Run** (implementation) — sandboxes, execution environments, and tools keep the model focused, secure, and productive while it generates and executes code.
3. **Feedback loop** (testing & QA) — orchestration + guardrails: the harness executes the tests, captures failures, and routes error output back to the model. The harness *is* the automated think → act → observe loop.
4. **Observe** (review, deployment, maintenance) — hooks (e.g., block a commit containing a hard-coded password) and observability (token cost, latency, drift, decision audit trails).

## Relations

- **[[Context Engineering for Coding Agents]]** — context policy is one harness layer (the static/dynamic boundary, skill loading, sub-agent context hygiene). Context engineering optimizes what the model sees; harness engineering owns that *plus* everything the model can do and everything that checks it.
- **[[Generator-Evaluator Pattern]]** / [[anthropic-harness-design]] — the trust-boundary split between producing and judging agents is a harness-architecture decision.
- **[[Agentic Orchestration Levels]]** — how much harness you need scales with how far the operator moves from conductor to orchestrator: async multi-agent delegation is only safe when verification and observability are harness-borne rather than human-borne.
- **[[Context Rot]]** — a noise-stuffed context window is a canonical harness (configuration) failure, not a model failure.
- **Evals as harness surface** — tests verify the deterministic parts, evals the non-deterministic (trajectory, tool choice, quality); the leaders' rule from [[vibe-coding-new-sdlc-day1]] is to treat AGENTS.md, system prompts, eval suites, and skill libraries as code: reviewed, versioned, owned.

## adlc as an instance

This project is harness engineering practiced end-to-end — each harness component has a concrete artifact here:

| Harness component | adlc artifact |
|---|---|
| Instructions / rule files | AGENTS.md via `/project-profile`, per-skill SKILL.md, sub-agent prompts (`agents/*.md`) |
| Tools | graphify CLI, vault scripts, MCP interop path (planned vault MCP server) |
| Orchestration logic | ADLC dispatcher: feature-builder → tester → reviewer → verifier; autoresearch's plan-driven loop; model tiering per role |
| Guardrails / hooks | verification contracts, commit gates, backup-before-write rules (e.g., the DEFECT-001 fix) |
| Memory | the wiki itself — the [[LLM Wiki Pattern]] gives agents persistent, compounding state instead of a blank slate per session |
| Observability | `log.md`, `_run` ledgers, review/verification records, `wiki/meta/usage.md` token rollups |
| Evals | per-skill eval suites (`skills/*/evals/`), golden cases, benchmark runs |

The vault's own eval experience corroborates the "configuration failures" claim: the graphify G5 eval failures traced to script/harness defects (edge destruction, path anchoring), not model weakness — and were fixed without touching the model.
