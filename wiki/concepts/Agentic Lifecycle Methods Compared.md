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
  - "[[claude-ai-native-sdlc-playbook]]"
---

# Agentic lifecycle methods compared

Every method puts a human gate between artifacts, keeps the main thread as the one that talks to the human, and records approval as a file in the repo. They differ on whether workers exist and how much bookkeeping they demand. Kiro and BMAD facts below come from search summaries and release notes, not a full read of their docs, so they are medium or low confidence.

## Comparison

The table has one row per method.

| Method | Steps | Worker vs main thread | Human approval and record | Spikes and setup | Bookkeeping |
|---|---|---|---|---|---|
| AWS AI-DLC | Inception, Construction, Operations; bolts per unit | Single agent following rules; no worker split in the sources read (medium) | Gate after each stage, Approve, Edit or Reject; logged in an append-only audit file (medium) | Not named (gap) | State file plus audit log (medium) |
| GitHub Spec Kit | Constitution, specify, plan, tasks, implement | Slash commands in one agent session (medium) | Human reviews and edits each spec file before the next command; the file in git is the record (medium) | A constitution of project rules; no spike step (medium) | Per-feature spec folder; no log (medium) |
| Kiro | Requirements in EARS form, design, tasks | IDE agent; hooks fire on file events; steering files give standing context (medium) | Approve each of the three files in turn; Quick Spec skips the gates (medium) | Steering files carry setup knowledge; no spike step (low) | Three markdown files per feature under the spec folder (medium) |
| BMAD | Analysis, planning (brief, PRD, architecture, epics), then per-story create, dev, review | One persona per role, switched in a session; v6.11 folds the story pair into a single build chain (low to medium; sources conflict on whether scrum master and QA remain separate) | PRD and architecture are reviewed before stories; story status moves in a status file (medium) | Analyst role covers research; no environment step (low) | Sprint status file; an open issue reports it drifting when review skips it (low) |
| Anthropic guidance | Workflow or agent; orchestrator-workers | Orchestrator splits and workers run subtasks; main thread synthesizes (high) | Pause at checkpoints and blockers (high) | Not covered | None prescribed (high) |

(Sources: [[aws-ai-dlc-workflows]], [[anthropic-building-effective-agents]], [[spec-kit-research]])

## What this means for a single-plugin lifecycle
- Workers suit bounded, measurable work such as research, build and review. Gates and decisions stay in the main thread. This matches Anthropic's orchestrator-workers pattern. Confidence high.
- No surveyed method handles spikes or environment setup as a first-class step. A plugin that does fills a gap. Confidence medium.
- Approval records are weak when they capture only that approval happened. Record the approved artifact version beside the approval. Confidence medium (one reported AI-DLC issue).
- Status files drift when a stage skips updating them; make one stage own the update. Confidence low (one BMAD issue).
- Depth-adaptive stages (AI-DLC) and right-sized paths (BMAD) both let small changes skip planning. Confidence medium.
