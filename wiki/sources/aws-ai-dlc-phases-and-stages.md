---
type: source
source_type: documentation
title: "AI-DLC phases and stages guide"
author: AWS Labs
date_published: 2026-11-08
url: https://awslabs.github.io/aidlc-workflows/guide/04-phases-and-stages
confidence: medium
key_claims:
  - "The lifecycle has 33 stages across five phases: Initialization, Ideation, Inception, Construction, Operation."
  - "Phase 0 runs automatically with no gate; every in-scope stage in phases 1, 2 and 4 ends with an approval gate."
  - "Construction stages 3.1 to 3.5 are approved per Unit (Approve or Request Changes) unless the user chose automatic continuation; build and test and the CI pipeline gate once after the last Unit."
  - "Verification gates run at each phase boundary; on failure the user chooses to proceed or go back."
  - "The delivery planning stage produces a bolt plan that groups Units for delivery; it does not replace the dependency graph that orders Units."
  - "Audit is an append-only event log in per-clone shards, separate from the overwritten state file (from a search result of the state-and-audit chapter)."
created: 2026-11-08
updated: 2026-11-08
tags:
  - ai-dlc
  - governance
---

# AI-DLC phases and stages guide

## Stages by phase

- Initialization (0.1 to 0.3): workspace scaffold, workspace detection, state initialization. No gate.
- Ideation (1.1 to 1.7): intent capture, market research, feasibility, scope definition, team formation, rough mockups, approval and handoff. Several are conditional.
- Inception (2.1 to 2.9): reverse engineering (brownfield only), practices discovery, requirements analysis, user stories, refined mockups, domain design, units generation, contract design, delivery planning.
- Construction (3.1 to 3.7): per Unit functional design, NFR requirements, NFR design, infrastructure design and code generation; then build and test once, and a CI pipeline once.
- Operation (4.1 to 4.7): deployment pipeline, environment provisioning, deployment, observability, incident response, performance validation, feedback and optimization.

Skipped stages are marked and carry no gate.

## Human gates

Phase 0 has none. Every in-scope stage of phases 1, 2 and 4 ends in an approval. In Construction the per-Unit stages share one checkpoint, which can run automatically if the user opts in; plan approval, verification-command selection, skeleton approval and failures still need the user. Phase boundaries add a verification gate.

## Bolts

The page does not define a bolt. It shows that delivery planning writes a bolt plan recording the delivery grouping and its rationale, and that bolt-started and bolt-completed events appear on the swarm and worktree path. A bolt is a delivery grouping of Units, an inference the page does not confirm.

## Audit log

The state initialization stage creates the audit directory beside the state file. Construction writes ordered receipts, one per verified checkpoint, including checkpoints the user let run automatically. Bypass settings are recorded. A search result for the state-and-audit chapter adds that the log is append-only, split into per-clone shards so parallel worktrees do not conflict, and that routing does not read it. A community article reports timestamped, typed entries; the field list was not read.

(Source: [[aws-ai-dlc-phases-and-stages]])
