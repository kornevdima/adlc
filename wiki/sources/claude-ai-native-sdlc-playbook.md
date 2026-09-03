---
type: source
title: "The AI-Native SDLC Playbook"
source_type: playbook
author: "Louis Claxton (Anthropic Applied AI)"
date_published: 2026-08-21
created: 2026-09-03
updated: 2026-09-03
confidence: high
tags:
  - source
  - playbook
  - sdlc
  - ai-native-sdlc
  - governance
  - claude-code
  - artifact-chain
status: current
related:
  - "[[AI-Native SDLC Playbook vs ADLC]]"
  - "[[Review the ADLC flow against the AI-Native SDLC Playbook]]"
  - "[[vibe-coding-new-sdlc-day1]]"
  - "[[Harness Engineering]]"
  - "[[Agentic Orchestration Levels]]"
  - "[[Grilling Session]]"
  - "[[AGENTS.md]]"
  - "[[Generator-Evaluator Pattern]]"
key_claims:
  - "Build is no longer the constraint; the human-speed steps around it are (plan, review/test, deploy), and controls designed for human-written diffs stop matching reality once agents write most of them"
  - "The AI-native SDLC is a loop, not a line: each stage commits an artifact the next stage reads (intent.md, spec.md, plan.md, the diff and its tests, the PR review findings, the incident record); the chain of commits is the audit trail"
  - "Humans remain accountable for every decision that requires judgment; human attention concentrates at the gates, reviewing what the agent flagged rather than starting each stage from scratch"
  - "A skill is an advisory control; a policy that must always hold needs something deterministic behind it (a hook, or a review pass that re-checks it at the PR)"
  - "Stage 6 closes the loop: a deterministic detection script watches production, invokes Claude on a control-band breach (diagnose at 2σ, propose at 3σ through the review gate), and the finding re-enters the pipeline as intent.md with no person in the invocation path"
  - "Name one system as the source of truth per artifact; linkage (record ID in the artifact, commit SHA in the legacy record) is the minimum bar"
---

# Source: The AI-Native SDLC Playbook

**Author**: Louis Claxton (Anthropic Applied AI; credits Jim Blackhurst, Will Steuk, Jamal Arif) | **Published**: 2026-08-21 | **Raw**: `.raw/claude-ai-native-sdlc-playbook.md` (HTML-to-Markdown capture, section anchors `sd-s1`…`sd-s6` preserved) | **URL**: https://claude.com/blog/the-ai-native-sdlc-playbook

Filed at the operator's request as the reference explanation of the *AI-native SDLC* — the industry name for what this plugin calls ADLC. Comparison and the operator's stance: [[AI-Native SDLC Playbook vs ADLC]]; the pending review is tracked in [[Review the ADLC flow against the AI-Native SDLC Playbook]].

## Summary

The playbook's thesis is that code generation collapsed the build phase, so the bottleneck moved to the human-speed stages on either side of it — plan, review/test, deploy — and the controls built for human-written diffs (line-by-line review, weekly committees) no longer match reality. The answer is not fewer controls but **the same control objectives with new enforcement**: the lifecycle becomes a loop with an agent embedded at every stage, humans keep decision authority at gates, and each stage ends by **committing an artifact the next stage reads**. The vocabulary — *AI-native SDLC*, *agentic SDLC*, *AI SDLC* — is declared interchangeable.

It is organised as **plays** grouped under six non-linear stages. Each play has a Traditional / AI-native contrast, prerequisites, execution steps, a "what it looks like" file, governance considerations, and leading / lagging indicators.

## The six stages and their artifacts

| Stage | Artifact committed | Trigger for the next stage | Key practice |
|---|---|---|---|
| 1 Plan | `intent.md` — problem, proposed outcome, affected users/systems, constraints, open questions, in the originator's own words | product owner accepts (merge / closed review) | "Ideas stop waiting for someone to write them up." Non-engineers write intent via claude.ai / Cowork with a VCS connector; an `intent/` folder in the product repo is the simplest home |
| 2 Design | `spec.md` — requirements + design in one session, constrained by org skills (brand, security, compliance, UX), concerns flagged | product owner accepts, consults a tech lead for higher-risk work | "Policy is applied while the spec is written, not discovered in a review weeks later" |
| 3 Build | `plan.md` (files that change, order, risks, proof) + `CLAUDE.md` + skills + hooks + subagents | engineer accepts the plan; plan mode blocks edits until then | "Nothing is implemented without an accepted plan." When implementation departs from the plan, update `plan.md` in the same commit. Auto mode + worktrees for parallel sessions; subagents for recurring jobs (a `verifier` with `Bash, Read` that reports and never fixes) |
| 4 Test | the diff + its tests; eval suite results | checks pass | "Every session checks its own work before a human sees it." Failing test first for bug fixes; a hook blocks test edits during a fix; **continuous evals in CI on any change to `CLAUDE.md`, skills, or hooks** — configuration regression-tested like code; every incident becomes an eval |
| 5 Deploy | PR with ranked review findings | code-owner approval via branch protection; production hook needs a named release authorization | "Review runs in both directions." `REVIEW.md` defines passes (bugs / security / compliance vs `spec.md` + `plan.md`), what "Important" means, nit caps, exclusions. Second occurrence of a mistake goes into `CLAUDE.md` as part of the review. Agent acts up to the production gate and never past it; deploy / rollback exposed through MCP, tiered by environment |
| 6 Maintain | new `intent.md` from a breach, scan finding, or channel message; incident record | intent re-enters Stage 1 | "The loop closes." Deterministic detection (rolling mean / σ, Western Electric rules) invokes Claude: log at 1σ, read-only diagnose at 2σ, propose at 3σ via PR or pre-approved runbook. Scheduled security scans and Claude Tag on-call feed the same route |

## Cross-cutting patterns

- **The committed-artifact chain is the audit trail.** Who asked for what, what the agent produced, who approved — read from git timestamps. Most metrics are two-commit deltas (intent→spec elapsed, spec commits dated after the first plan commit, first-pass merge share).
- **Advisory vs deterministic controls.** Skills make violations rare; hooks make them close to impossible; review passes re-check at the PR. Managed settings (deny lists, sandbox, `allowManagedHooksOnly`, marketplace allowlists) are the enterprise floor.
- **Source of truth per artifact.** Repo-as-truth, legacy-system-as-truth (Jira / ServiceNow with MCP write-back), or linkage as the minimum bar. Both can coexist if linked.
- **Separation of duties.** The agent that wrote the code cannot approve it; approvals are human, through branch protection.
- **Feedback loop ≠ verifier subagent.** The loop runs throughout the task; the verifier is a fresh context that checks once at the end so the verdict is not coloured by the assumptions that produced the code (the [[Generator-Evaluator Pattern]]).

## Relationship to other sources

- [[vibe-coding-new-sdlc-day1]] gives the *why* (harness engineering, CapEx/OpEx); this playbook gives the *stage-by-stage what*, with governance and measurement per play. Both treat `CLAUDE.md` / skills / hooks as the harness — [[Harness Engineering]].
- The plan-mode play (interrogate the plan, iterate until a stranger could implement it) is the [[Grilling Session]] with a committed output.
- `CLAUDE.md` plays the role [[AGENTS.md]] plays in this plugin ("what a new joiner needs on day one; under a page; the mistake made twice goes in").
- Stage 6 is the level above the operator-authored [[Agentic Orchestration Levels]] ladder: an orchestrator that nobody starts.

## Assessment

High confidence as a description of Anthropic's recommended practice; it is prescriptive, enterprise-oriented (regulated orgs, managed settings), and Claude-product-specific in tooling. The artifact chain is the transferable idea; the *single common-name file per stage* is a packaging choice, not a requirement — the text itself says "for the early stages, .md files are the predominant artifact" and "from Build onward, the artifact is code and its records." See [[AI-Native SDLC Playbook vs ADLC]] for what transfers.
