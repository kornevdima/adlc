---
type: source
title: "AWS AI-DLC (blog and open-source workflows)"
created: 2026-11-08
updated: 2026-11-08
source_type: article-and-repository
author: "Will Matos, Raj Jain, Siddhesh Jog, Raja SP (AWS); repository awslabs/aidlc-workflows"
date_published: 2025-11-29
url: https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/
confidence: medium
tags:
  - ai-dlc
  - orchestration
  - governance
status: mature
key_claims:
  - "AI-DLC has three phases, Inception, Construction and Operations; each phase decides how deep to run (high, blog dated 2025-11-29)."
  - "Human approval is embedded at every decision gate, and the workflow records every human action and approval (high)."
  - "Inception and construction use team rituals called Mob Elaboration and Mob Construction; the unit of delivery is a short cycle called a bolt (medium, secondary sources)."
  - "The repository keeps a state file for progress and an append-only audit log of raw user input, AI response and approval; newer layouts shard the audit per intent (medium, from search summaries of the repo)."
  - "An open issue reports the audit records that someone approved, not what was approved (low, single issue)."
---

# AWS AI-DLC

AI-DLC lets the AI propose and the humans validate at gates. It is delivered as rules files (Amazon Q Rules, Kiro steering files, and equivalents for other agents), so the orchestration lives in prose rules read by one agent, not in code. (Source: [[aws-ai-dlc-workflows]])

## Steps and who runs them
- Three phases: Inception (intent, requirements, stories, units of work), Construction (design, code, test per unit), Operations. Each stage evaluates how deep to go, so small changes skip stages. Confidence high.
- Bolts replace sprints: hours or days, one per unit of work. Confidence medium (secondary sources, not the fetched blog excerpt).
- The blog excerpt did not describe sub-agents. The rules run in one main agent thread that asks questions and drafts; no worker split is prescribed there. Confidence medium.

## Human approval and its record
- Gates sit after Units Generation and after each Construction stage. The reply is Approve, Edit or Reject. High for gates, medium for the three options.
- Older layout: `aidlc-state.md` holds progress and `audit.md` is append-only, with raw user input unsummarized. Newer layout: per-intent records, a sharded `audit/` directory, and a report command that stores the exact reply. Medium.
- Weakness: one issue says the audit shows that approval happened, not the approved content. Low.

## Spikes, research, setup
Not covered in the sources read. The only hook is the "depth" decision per stage, so a spike is not a named step. Gap.

## Bookkeeping required
A state file and an audit log, per intent; stage artifacts under inception and per-unit construction folders.

Related: [[Agentic Lifecycle Methods Compared]], [[claude-ai-native-sdlc-playbook]].
