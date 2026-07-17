---
type: concept
title: "Context Engineering for Coding Agents"
complexity: intermediate
domain: ai-agents
aliases:
  - "Agent Context Engineering"
  - "Coding Agent Context"
created: 2026-05-09
updated: 2026-07-17
tags:
  - concept
  - context-engineering
  - coding-agents
  - llm
status: developing
related:
  - "[[AGENTS.md]]"
  - "[[Repo Map]]"
  - "[[Contextual Retrieval]]"
  - "[[Project Profile]]"
  - "[[anthropic-context-engineering]]"
  - "[[evaluating-agents-md-eth]]"
sources:
  - "[[anthropic-context-engineering]]"
  - "[[anthropic-contextual-retrieval]]"
  - "[[evaluating-agents-md-eth]]"
  - "[[racg-survey-2025]]"
  - "[[yt-pocock-ai-coding-workflow]]"
  - "[[yt-schroeder-domain-specific-agents]]"
  - "[[yt-alvoeiro-multi-agent-architecture]]"
  - "[[vibe-coding-new-sdlc-day1]]"
---

# Context Engineering for Coding Agents

The set of strategies for choosing what tokens an LLM-backed coding agent sees during inference. Distinguished from prompt engineering: prompt engineering crafts an instruction; context engineering manages the whole token state across many turns including tools, system prompt, retrieved data, and message history (Source: [[anthropic-context-engineering]]).

## The Core Problem

Context windows are finite, and every token the model sees has to earn its place. Anthropic's framing:

> "The smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome." (Source: [[anthropic-context-engineering]])

For coding agents specifically, the question is: of all the things you *could* tell the agent about a project (conventions, structure, domain, decisions, history, recent work), what should be **upfront**, what should be **retrievable**, and what should be **excluded entirely**?

## The hybrid model is the consensus answer

Both Anthropic's Claude Code design and the broader ecosystem converge on the same architecture:

- **Upfront**: a small, curated artifact (CLAUDE.md / AGENTS.md) carrying conventions and load-bearing facts that apply to most tasks.
- **Just-in-time**: tools (glob, grep, read) that retrieve specific files when relevant.
- **Cached**: long-lived content that benefits from prompt caching.

> "Claude Code is an agent that employs a hybrid model where CLAUDE.md files are naively dropped into context up front, while primitives like glob and grep allow it to navigate its environment and retrieve files just-in-time." (Source: [[anthropic-context-engineering]])

## The empirical surprise

The strongest evaluation of pre-computed context files (ETH Zurich AGENTbench, 2026) found:

- Human-written context files: **+4%** task success.
- LLM-generated context files: **-2% to -3%** (worse than no file).
- Both options cost +20-23% inference and +3-4 steps regardless of accuracy.

(Source: [[evaluating-agents-md-eth]])

The implication is sharp: **automatic project summarization is net-negative**. Curation is unavoidable. Even good context files clear the bar by a small margin.

## What helps vs what doesn't

From the AGENTbench data:

| Content type | Effect |
|---|---|
| Repository overview | Negligible / no improvement |
| Concrete commands ("run `pytest -k unit`") | When mentioned, used 1.6× more often |
| Conventions ("use ruff, not flake8") | Specific actionable directives outperform descriptive prose |
| LLM-generated summary | Net-negative — duplicates README |
| "Tribal" / hidden knowledge (only in human heads) | The only category that consistently helps |

Pair this with [[racg-survey-2025]] which lists context types most useful for repo-level tasks: cross-file dependencies, structural information (class hierarchies, types), API signatures, naming conventions, module relationships.

## Three Patterns for Long-Horizon Tasks

From [[anthropic-context-engineering]]:

1. **Compaction** — summarize history before context limits. Claude Code keeps the compressed summary plus the **5 most recently accessed files**.
2. **Structured note-taking** — agents write to durable scratchpads (NOTES.md, todo list, memory tool) and re-read on demand.
3. **Sub-agent architectures** — specialized sub-agents return condensed summaries (typically 1-2K tokens) to a coordinator. claude-mem's `graphify-extract-subagent` and `wiki-ingest-subagent` already follow this pattern.

Factory's missions system ([[yt-alvoeiro-multi-agent-architecture]]) pushes the third pattern furthest for multi-day runs: each feature gets a worker with **clean context** ("no accumulated baggage, no degraded attention"), state travels only via [[Structured Handoff]]s and Git commits, and features run **serially** with parallelism reserved for read-only operations (search, research, code review) — naive parallel writers "step on each other's changes" and coordination overhead eats the throughput gains.

## Composition as the limit case of sub-agent architectures

[[yt-schroeder-domain-specific-agents]] pushes pattern 3 to its logical end: the skills/MCP/system-prompt stack is **inheritance** (inflating one agent's context), and past some skill count returns go negative — "if you use very many of these, it actually makes your agent substantially worse". The alternative is **composition**: many small complete agents, each with a domain-written system prompt, minimal toolset, and own message history, coordinated in plain English. A sub-agent's total context can be just its system prompt + tools + the one incoming ask, claimed to yield >80% token efficiency per task and make far cheaper models viable. See [[Domain-Specific Agents]]. This converges with the ETH finding above from a different direction: more upfront context is not free, and scoping beats stacking.

## Quantitative bounds for retrieval

From [[anthropic-contextual-retrieval]]:

- Adding contextual prefixes to chunks before embedding: **35%** failure-rate reduction.
- Plus contextual BM25: **49%** reduction.
- Plus reranking: **67%** reduction.
- One-time preprocessing cost: ~$1.02 per million document tokens.

Critically: below 200K tokens of "important context" (~500 pages), Anthropic recommends **skip RAG entirely** — drop the whole corpus into the prompt and use prompt caching. Most projects' load-bearing context fits this bound.

## Implications for Tool Design

- **Both layers needed.** Narrative-style conventions (AGENTS.md / wiki) AND structural code maps (graphify / repo-map) target different question types ([[racg-survey-2025]]).
- **Cap the upfront budget.** Aider's repo-map defaults to 1K tokens. AGENTS.md spec doesn't define a cap but evaluations suggest brevity wins.
- **Specific over general.** Concrete commands and named tools beat overview prose.
- **Hand-curated tribal knowledge is the only consistent positive.** This is the part agents can't extract for you.

## A full practitioner instantiation (Pocock, 2026)

[[yt-pocock-ai-coding-workflow]] shows what these principles look like as a working end-to-end workflow, and adds practitioner rules the papers don't state:

- **Push vs pull for standards.** Coding standards should be *pull* for the implementer (skills the agent loads on demand) but *push* for the automated reviewer (inject the standards next to the diff so the reviewer has both). This refines the "cap the upfront budget" rule: the budget depends on the role in the pipeline.
- **Review in a fresh context.** Never review in the session that implemented — the reviewer inherits a degraded (dumb-zone) context. Clear first. See [[Context Rot]] and [[Generator-Evaluator Pattern]].
- **Model tiering by role**: cheaper model (Sonnet) for implementation, stronger model (Opus) for review and merging.
- **Feedback loops as the ceiling**: "the quality of your feedback loops influences how good your AI can code" — tests and typecheckers are context the agent *earns at runtime*, and improving them (see [[Deep Modules]]) beats adding more upfront prose.
- **Doc rot as anti-context**: stale planning docs (old PRDs) left in the repo are *negative* context — agents find and trust them after the code has diverged. Pocock deletes/closes them post-implementation. This is the practitioner echo of the ETH finding that wrong/duplicative context files are net-negative.
- **Token visibility**: a status line showing exact token usage in every session, so the operator knows distance to the dumb zone.

## The six-types and static/dynamic framing (Google, 2026)

[[vibe-coding-new-sdlc-day1]] contributes a vocabulary that complements the hybrid model above. Six context types every agent needs: **instructions, knowledge, memory, examples, tools, guardrails**. The design decision is which of these sit in **static context** (always loaded — rule files, personas; every token paid on every interaction) vs **dynamic context** (loaded on demand — skills via progressive disclosure, tool results, RAG, windowed history), and the paper's rule matches this vault's practice: treat that boundary as a first-class architectural decision, reviewed and versioned like configuration.

Two additions worth keeping:

- **Context engineering as a financial lever.** In the token economy, a dense high-signal payload raises first-pass success and avoids the trial-and-error prompting loops that dominate vibe-coding OpEx; passing a 100K-token repo into every prompt is financially unviable at scale. Context quality is a TCO line item, not just an accuracy one.
- Context engineering is "the bridge between vibe coding and agentic engineering" — the same question as the ETH curation finding, asked from the discipline side: *what would a new team member need to know, and how do you encode it in a form the AI can use?* The wider scaffolding this bridge belongs to is [[Harness Engineering]] — context policy is one harness layer among tools, hooks, sandboxes, and observability.

## Connections

- [[AGENTS.md]] — the convention layer
- [[Repo Map]] — the structural layer
- [[Contextual Retrieval]] — the retrieval-side complement
- [[Project Profile]] — claude-mem's planned design that synthesizes these findings
- [[Hot Cache]] — claude-mem's existing always-loaded context, which is itself a context-engineering choice
- [[Structured Handoff]] — the artifact that makes clean-context worker resets viable ([[yt-alvoeiro-multi-agent-architecture]])
- [[Harness Engineering]] — the superset discipline: context policy plus tools, hooks, sandboxes, orchestration, observability
