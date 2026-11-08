---
type: concept
title: "Agentic Lifecycle Methods Compared"
created: 2026-11-08
updated: 2026-11-08
confidence: medium
tags:
  - orchestration
  - governance
  - ai-dlc
  - spec-driven
status: draft
related:
  - "[[aws-ai-dlc-workflows]]"
  - "[[anthropic-building-effective-agents]]"
  - "[[spec-kit-research]]"
  - "[[kiro-specs-docs]]"
  - "[[bmad-method-docs]]"
  - "[[aws-ai-dlc-phases-and-stages]]"
  - "[[claude-ai-native-sdlc-playbook]]"
---

# Agentic lifecycle methods compared

Every method puts a human gate between artifacts, keeps the main thread as the one that talks to the human, and records approval as a file in the repo. They differ on whether workers exist and how much bookkeeping they demand. The Kiro row rests on its specs page and the AI-DLC row on its phases guide; BMAD rests on a docs home page that omits the planning detail, so its row stays low to medium.

## Comparison

The table has one row per method.

| Method | Steps | Worker vs main thread | Human approval and record | Spikes and setup | Bookkeeping |
|---|---|---|---|---|---|
| AWS AI-DLC | Five phases, 33 stages: Initialization, Ideation, Inception, Construction, Operation; bolts group Units for delivery | Single agent following rules; no worker split in the sources read (medium) | Every in-scope stage in phases 1, 2 and 4 ends in an approval; Construction approves per Unit, optionally automatic; verification gate at each phase boundary; append-only audit log in per-clone shards, with a receipt per verified checkpoint, automatic ones included, and bypass settings (medium) | Practices discovery and reverse engineering stages for brownfield; no spike stage | State file overwritten per change, audit log append-only and not read for routing (medium) |
| GitHub Spec Kit | Constitution, specify, plan, tasks, implement | Slash commands in one agent session (medium) | Human reviews and edits each spec file before the next command; the file in git is the record (medium) | A constitution of project rules; no spike step (medium) | Per-feature spec folder; no log (medium) |
| Kiro | Requirements (user stories, acceptance criteria; EARS phrasing per site search results), design, tasks; bugfix spec swaps in a bugfix file | IDE agent; the docs page does not describe hooks or steering, so those stay unsourced (low) | Review each phase's document with passage comments sent to Kiro together; Quick Spec has no gates (medium) | No spike step on the page | Three markdown files per feature; Kiro updates task status as it works (medium) |
| BMAD | Loop of Clarify, Plan, Build and verify, Learn and adjust; planning chain analyst brief, PRD, architecture, epics, then per-story work (community guides) | Skills, with a Product Owner named on the docs home and one build skill that writes and reviews; a guide says scrum master and QA were folded into the developer agent, the docs home is consistent with that (low to medium) | PRD and architecture are reviewed before stories (community guides, low) | Entry point set by how formed the idea is, so small changes skip planning (medium) | Sprint status file with states backlog, ready-for-dev, in-progress, review, done; an open issue reports drift when review skips it (low to medium) |
| Anthropic guidance | Workflow or agent; orchestrator-workers | Orchestrator splits and workers run subtasks; main thread synthesizes (high) | Pause at checkpoints and blockers (high) | Not covered | None prescribed (high) |

(Sources: [[aws-ai-dlc-workflows]], [[aws-ai-dlc-phases-and-stages]], [[kiro-specs-docs]], [[bmad-method-docs]], [[anthropic-building-effective-agents]], [[spec-kit-research]])

## Open conflict

BMAD sources disagree on whether the scrum master and QA agents are separate. Older guides and forks list them; one guide says the current repository folded both into the developer agent. The official docs home names a single build skill that also reviews, which fits the folded reading, but the planning pages were not read. Treat it as unresolved. Confidence low.

## What this means for a single-plugin lifecycle
- Workers suit bounded, measurable work such as research, build and review. Gates and decisions stay in the main thread. This matches Anthropic's orchestrator-workers pattern. Confidence high.
- No surveyed method handles spikes or environment setup as a first-class step. A plugin that does fills a gap. Confidence medium.
- Approval records are weak when they capture only that approval happened. Record the approved artifact version beside the approval. The AI-DLC audit log records receipts per verified checkpoint, including auto-approved ones, and bypass settings, but the field list was not read. Confidence medium.
- Status files drift when a stage skips updating them; make one stage own the update. Confidence low (one BMAD issue).
- Depth-adaptive stages (AI-DLC) and right-sized paths (BMAD) both let small changes skip planning. Confidence medium.
