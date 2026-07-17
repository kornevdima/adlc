---
type: source
title: "The New SDLC With Vibe Coding — From Ad-hoc Prompting to Agentic Engineering (Day 1)"
source_type: whitepaper
author: "Addy Osmani, Shubham Saboo, Sokratis Kartakis (Google)"
date_published: 2026-05
created: 2026-07-17
updated: 2026-07-17
confidence: high
tags:
  - source
  - whitepaper
  - agentic-engineering
  - vibe-coding
  - harness
  - sdlc
  - economics
status: current
related:
  - "[[Harness Engineering]]"
  - "[[Agentic Orchestration Levels]]"
  - "[[Context Engineering for Coding Agents]]"
  - "[[Andrej Karpathy]]"
  - "[[Generator-Evaluator Pattern]]"
  - "[[AGENTS.md]]"
key_claims:
  - "The core shift is from writing syntax to expressing intent; the machine handles implementation, the human provides intent, architecture, and judgment"
  - "Agent = Model + Harness; agent behaviour is dominated by the harness, not just the model underneath"
  - "Most agent failures, examined honestly, are configuration failures — a missing tool, a vague rule, an absent guardrail, a noise-stuffed context window"
  - "Without both tests (deterministic parts) and evals (non-deterministic parts), the practice is always vibe coding, regardless of prompt sophistication"
  - "Vibe coding is low CapEx / high OpEx; agentic engineering is high CapEx / low OpEx — context engineering is a financial lever, not just a technical skill"
  - "Set the bar at the eval, not the demo: a demo proves an agent can succeed once, a passing eval suite proves it succeeds reliably"
---

# Source: The New SDLC With Vibe Coding (Day 1)

**Authors**: Addy Osmani, Shubham Saboo, Sokratis Kartakis | **Provenance**: Google (contributors incl. Elia Secchi, Julia Wiesinger, Anant Nawalgaria) | **Date**: May 2026
**Raw**: `.raw/Day_1_v3.pdf` (51 pp., image-heavy) | Day 1 of a multi-day course — Day 3: *Context Engineering: Sessions, Skills & Memory*; Day 5: *Spec-Driven Production Grade Development*.

## Summary

Framework paper for the AI-era SDLC. The most profound shift in software engineering is the transition **from writing code to expressing intent** — the developer supplies intent, architecture, and judgment; intelligent systems translate intent into working software. As of early 2026: 85% of professional developers regularly use AI coding agents, 51% daily, ~41% of all new code is AI-generated. The paper's central move is to replace the vibe-coding-vs-not binary with a **spectrum**, and to argue that what separates its ends is not the model or the tool but how deliberately you configure the **harness** around the model (see [[Harness Engineering]]). Closing line: "Generation is solved. Verification, judgment, and direction are the new craft."

Terminology history: [[Andrej Karpathy]] coined "vibe coding" in February 2025 ("fully give in to the vibes... forget that the code even exists"); by early 2026 he acknowledged the framing was too narrow and introduced **"agentic engineering"** for the disciplined end of the spectrum.

## The spectrum: vibe coding → agentic engineering

The key differentiator is not whether you use AI, but how much structure, verification, and human judgment surrounds the AI's output.

| Dimension | Vibe Coding | Structured AI-Assisted Coding | Agentic Engineering |
|---|---|---|---|
| Intent specification | Casual natural-language prompts | Detailed prompts with examples and constraints | Formal specs, architecture docs, memory files |
| Verification | "Does it seem to work?" | Manual testing, spot-checking | Automated test suites, CI/CD gates, LM judges |
| Codebase understanding | Minimal; may not read generated code | Selective review of critical paths | Comprehensive review of architecture; AI handles implementation details |
| Error handling | Copy-paste errors back to the AI | Developer diagnoses root cause, AI implements fix | Agents self-diagnose within defined bounds; humans handle architectural issues |
| Appropriate scope | Prototypes, scripts, personal projects, hackathons | Features within established codebases | Production systems, team-scale development |
| Risk profile | High; acceptable for disposable code | Moderate; human judgment at key checkpoints | Low; systematic verification at every stage |

The right position depends on the stakes: a weekend prototype can be pure vibe coding; a production API handling financial transactions demands agentic engineering. Teams that keep the boundary blurry "produce prototypes that ship by accident."

## Tests vs evals; trajectory evaluation

The single biggest differentiator between the ends of the spectrum is **how outputs get verified**, and two mechanisms must work together:

- **Tests** verify the deterministic parts: given this input, that output. Checked by code.
- **Evals** verify the non-deterministic parts: did the agent take the right *trajectory* of steps, choose the right tools, and meet the quality bar. Checked by labelled datasets, scoring rubrics, and LM judges.

"Without both, the practice is always vibe coding, regardless of how sophisticated the prompts are." Testing AI-generated code requires both **output evaluation** (does it compile, do tests pass) and **trajectory evaluation** (the full sequence of tool calls and intermediate reasoning) — a fluent output that skipped its verification steps is a *more* dangerous failure than one with a visible error. These wire into a continuous quality flywheel: evaluate → diagnose (cluster root causes) → optimize (prompts/tools) → verify against a regression suite → monitor production.

## Context engineering: the real skill

Quality of AI-generated code depends less on prompt cleverness and more on context quality. Six context types: **instructions, knowledge, memory, examples, tools, guardrails**. The key engineering trade-off is **static context** (always loaded: rule files like AGENTS.md/CLAUDE.md, personas — every token paid on every interaction) vs **dynamic context** (loaded on demand: skills, tool results, RAG, windowed history). The best systems treat this boundary as a first-class architectural decision, reviewed and versioned. **Agent Skills** (progressive disclosure: metadata at startup → full instructions on task match → deep references only when needed) are named the most powerful dynamic-context pattern, solving four problems: [[Context Rot]] from overloaded prompts, absence of procedural memory, operational overhead of multi-agent architectures, and portability across vendors. Consistent with the vault's existing synthesis in [[Context Engineering for Coding Agents]] — including the ETH finding that only curated, high-signal files help.

## The new SDLC and the factory model

AI compresses the SDLC dramatically but *unevenly*: implementation collapses from weeks to hours while requirements, architecture, and verification remain human-paced. Per phase: requirements become a human-AI conversation producing spec + prototype simultaneously; architecture stays the most human-centric phase (trade-offs need business context); implementation shifts from writing to reviewing/guiding/verifying (industry surveys: 25–39% productivity gains, but METR found experienced developers **19% slower** on certain tasks due to verify/debug overhead); review gets an AI first-pass; maintenance is the most underestimated win — "too risky to touch" legacy code becomes safely refactorable.

The **factory model** ties it together: the developer's primary output is not code but **the system that produces code** — specifications and context, agents, tests and quality gates, feedback loops, guardrails. A factory manager doesn't assemble every widget; they design the assembly line and ensure quality control. Give agents success criteria, not step-by-step instructions. The central machine in that factory is the harnessed agent.

## Harness engineering

The model is one input into a running agent; everything else — prompts, tools, context policies, hooks, sandboxes, sub-agents, observability — is the **harness**. **Agent = Model + Harness**, and it is *the team's* surface area, not the model provider's. Evidence that the harness dominates: on Terminal Bench 2.0 one team moved a coding agent **from outside the Top 30 to the Top 5 by changing only the harness** (no model change); a LangChain study raised a coding agent's score **13.7 points by tweaking only the system prompt, tools, and middleware** around a fixed model. "Most agent failures, examined honestly, are configuration failures." A developer can vibe code or apply agentic engineering *with the exact same agent* — the difference is how deliberately the harness is configured. Full treatment: [[Harness Engineering]] (including the configure → run → feedback loop → observe lifecycle mapping onto SDLC phases).

## Conductor and orchestrator modes

Two modes developers move between fluidly (see [[Agentic Orchestration Levels]]):

- **Conductor**: hands-on, real-time direction in the IDE; watching code appear, correcting live. Natural for complex logic, debugging, unfamiliar codebases. Preserves control but caps throughput — the human directs every movement.
- **Orchestrator**: async, multi-agent delegation. Define goals, assign to agents (often background/sandboxed), review results, course-correct periodically. Demands a different skill set: **specification, decomposition, evaluation, system design**.

Coding agents show up in three places, and the same developer often uses all three in one day: **in the editor** (inline completion, chat panels), **in the terminal** (goal-driven agents with filesystem access — "where serious vibe coding happens today"), and **in the background** (autonomous cloud sandboxes producing PRs). The right starting point depends on the task, not on autonomy-ladder position.

## The 80% problem

Agents rapidly generate ~80% of a feature; the remaining 20% — edge cases, error handling, integration points, subtle correctness — demands contextual knowledge models lack. AI errors have evolved from syntax mistakes to **insidious conceptual failures**: wrong business-logic assumptions, no clarification-seeking on ambiguity, missed edge cases, architecture that creates long-term maintenance burden — harder to detect precisely because the code "looks right" and may pass basic tests. Effective posture: use AI for rapid implementation of well-specified tasks; reserve human attention for ambiguity, trade-offs, and correctness verification.

## The economics: CapEx vs OpEx

For engineering leaders the metric is TCO, and OpEx in the AI era is dictated by the **token economy**:

- **Vibe coding = low CapEx, high OpEx.** Near-zero entry cost hides a compounding burden: the token burn rate of the fix-your-own-unverified-mistakes prompting loop, a maintenance tax on structurally inconsistent "spaghetti", and security remediation without an eval harness.
- **Agentic engineering = high CapEx, low OpEx.** Upfront investment in API schemas, deterministic test suites, and structured context drops the marginal cost of shipping/maintaining a feature dramatically.
- **Context engineering is a financial lever**: a dense, high-signal payload (precise AGENTS.md + architectural guardrails) raises first-pass success and avoids trial-and-error loops. Passing a 100K-token repo into every prompt is financially unviable.
- **Intelligent model routing**: frontier models for requirements/architecture/initial implementation; smaller, cheaper models for test generation, code review, CI/CD monitoring.

## Adoption checklists

**Individuals**: (1) set up AGENTS.md — start with ten lines, add a rule every time the agent misbehaves; (2) install skills for your coding agent; (3) make one repetitive workflow your first agent; (4) **write tests and evals before generating code** — together they are the contract with the AI; (5) review every line that ships, skeptical of anything clever; (6) keep foundational skills sharp.

**Leaders**: (1) make context engineering a first-class practice — **treat AGENTS.md, system prompts, eval suites, and skill libraries as code: reviewed in PRs, versioned, owned by named engineers** (otherwise the harness drifts and agent behaviour becomes irreproducible); (2) **set the bar at the eval, not the demo** — require eval coverage with explicit rubrics (task success, tool-use quality, trajectory compliance, hallucination, response quality) as a shipping precondition, like test coverage gates a deploy; (3) re-shape code review for generated code's failure modes (hallucinated dependencies, plausible-but-wrong); (4) make the prototype/production boundary explicit; (5) invest in harness components as shared infrastructure — build the harness once, refine it many times.

**Organizations**: (1) treat AI-assisted development as an engineering investment, not a productivity feature — tooling without eval coverage/observability/standards produces "speed without quality"; (2) build the production substrate (trajectory + final-response evals in CI, traces, scoped permissions, tuned security review) *before* the first production agent ships; (3) adopt open standards (MCP for tools, A2A for cross-agent delegation); (4) plan for hybrid human-agent teams — agents are participants, not just tools; (5) hire for judgment (specification, evaluation, architecture, review), not implementation volume.

Durable principles: **structure scales, vibes don't**; **AI amplifies your engineering culture** (it multiplies strengths *and* weaknesses); **the human role is evolving, not diminishing**.

## Other notable claims

- Building *production agents* (agent-as-product) now happens in the same terminal workflow: Google's Agents CLI adds seven skills covering the full ADK lifecycle (scaffold, code, eval, deploy, observe) to whatever coding agent the developer already uses (see [[Google ADK]]).
- Anthropic experiment, early 2026: agent teams built a working C compiler in Rust over two weeks — humans set direction and reviewed, wrote no implementation. The bottleneck moved to specifying and verifying.
- Agent anatomy refresher (from Google's Nov 2025 *Introduction to Agents*): model, tools, memory, orchestration, deployment, running a perceive → plan → act → observe → iterate loop.

## Relevance to adlc

The paper is effectively an external validation of adlc's architecture: the vault + skills + subagents + evals stack *is* a harness ([[Harness Engineering]] maps each component), the ADLC dispatcher's build → test → review → verify pipeline is the factory model's assembly line, and "set the bar at the eval, not the demo" matches the project's per-skill eval suites. The leaders' checklist item — AGENTS.md/evals/skills as reviewed, versioned team assets — is what `/project-profile` and the plugin repo already practice.

**Provenance caveat**: Google paper; tool recommendations (Agents CLI, Jules, ADK, Gemini Code Assist) are vendor-aligned. Framework content (spectrum, harness, factory model, economics) draws heavily on Addy Osmani's independent writing and is corroborated by non-Google sources in the endnotes.

## Connections

- [[Harness Engineering]] — the concept page extracted from this source
- [[Agentic Orchestration Levels]] — conductor/orchestrator maturity framing
- [[Context Engineering for Coding Agents]] — the vault's deeper synthesis; this source adds the six-types and static/dynamic framing
- [[Context Rot]] — named here as one of four problems Agent Skills solve
- [[Generator-Evaluator Pattern]] — LM judges + trajectory evals are this pattern institutionalized
- [[Andrej Karpathy]] — coined both endpoint terms of the spectrum
- [[Validation Contract]] — "tests and evals before code as the contract with the AI" is the same move
