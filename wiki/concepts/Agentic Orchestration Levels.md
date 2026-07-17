---
type: concept
title: "Agentic Orchestration Levels"
created: 2026-07-17
updated: 2026-07-17
tags:
  - orchestration
  - adoption
  - harness
  - adlc
status: draft
produced_by: operator
related:
  - "[[Harness Engineering]]"
  - "[[Grilling Session]]"
  - "[[Context Engineering for Coding Agents]]"
sources:
  - "[[vibe-coding-new-sdlc-day1]]"
---

# Agentic Orchestration Levels

Operator's synthesis: a four-level adoption ladder for AI-assisted delivery, from a bare chat session to agent-operated delivery. The Day 1 deck ([[vibe-coding-new-sdlc-day1]]) deliberately uses a *spectrum* (vibe coding → structured AI-assisted → agentic engineering) rather than numbered levels; this page defines the ladder adlc positions itself on. Each level is distinguished by **where the human's judgment is spent** and **how much harness exists around the model**.

| Level | Name | Human role | Harness required |
|---|---|---|---|
| 0 | Chat session | Copy-paste intermediary: prompts in a ChatGPT/Claude tab, pastes results into the codebase by hand | None — no repo access, no memory, no verification |
| 1 | Assisted editing | Prompts an in-editor/terminal agent per task, reviews every change inline | Repo access; ad-hoc prompts; verification is "does it seem to work" |
| 2 | Conductor with a harness | Directs synchronously, task by task, but through a configured harness | AGENTS.md, skills, a knowledge substrate (wiki), tests as the contract |
| 3 | Orchestrator (Mode ADLC) | Refines and plans in a [[Grilling Session]], then delegates the epic to the delivery loop; reviews evidence at story boundaries | Full adlc stack: product + code wikis, verification contracts, worker pipeline, run ledger, mission control |

## Mapping to the Day 1 deck

- Levels 0–1 span the deck's **vibe coding → structured AI-assisted** positions; level 2 reaches **agentic engineering** in its **conductor** mode; level 3 is its **orchestrator** mode plus the **factory model** ("the developer's primary output is the system that produces code").
- The deck's single biggest differentiator — *how outputs get verified* — is what gates each promotion: level 2 requires tests-before-generation; level 3 requires verification contracts a worker can execute and a human can audit.
- The [[Grilling Session]] gate is adlc's addition; the deck has no equivalent plan-interrogation ritual. It is what makes level-3 delegation safe: shared understanding is established *before* autonomy, not reconstructed after a failure.

> [!gap] Levels 1 and 2 are interpolated by the assistant from the deck's spectrum; the operator has only pinned the endpoints (0 = chat session, 3 = refine/plan/delegate after grilling). Definitions may shift as the ladder gets used in adoption conversations.

## Why a ladder and not a spectrum

A spectrum describes practice; a ladder prescribes investment. Each level names the harness assets a team must build to climb ([[Harness Engineering]]): level 1 costs nothing and caps quickly; level 2 is where AGENTS.md, skills, and the wiki pay for themselves; level 3 is high-CapEx/low-OpEx delivery (the deck's economics framing) — the harness is built once and every epic after rides it. Teams choose a level per task by stakes, exactly as the deck prescribes for its spectrum — level 3 for production epics does not forbid level 1 for a throwaway script.
