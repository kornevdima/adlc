---
type: meta
title: "Sources Index"
updated: 2026-11-08
tags:
  - meta
  - index
  - source
status: evergreen
related:
  - "[[index]]"
  - "[[log]]"
  - "[[entities/_index]]"
  - "[[Andrej Karpathy]]"
---

# Sources Index

Navigation: [[index]] | [[concepts/_index|Concepts]] | [[entities/_index|Entities]]

All source pages — summaries of ingested documents, transcripts, articles, and data.

---

## Transcripts

- [[yt-pocock-ai-coding-workflow]] — 2026-04-24 | Matt Pocock @ AI Engineer | full AI coding workflow: grilling → PRD → vertical-slice Kanban → AFK Ralph loop → TDD → fresh-context review → manual QA
- [[campbell-after-ai-hype]] — 2026-06-18 | Richard Campbell, NDC 2026 keynote | skeptic's AI landscape assessment: trough of disillusionment, agentic coding as the first real product, GPT-5 LLM-judge failure, vendor churn
- [[yt-schroeder-domain-specific-agents]] — 2026-06-29 | Justin Schroeder (StandardAgents), AI Engineer | domain-specific agents: composition over inheritance
- [[yt-alvoeiro-multi-agent-architecture]] — 2026-05-06 | Luke Alvoeiro (Factory), AI Engineer | five multi-agent primitives; missions: validation contracts, structured handoffs, serial execution, per-role models
- [[orlov-rag-wiki-llm-graphify]] — 2026-06-27 | Orlov (YouTube, uk) | three waves of agent memory: RAG → Wiki LLM → graphify; auto-transcript, figures low-confidence

---

## Articles

- [[agent-sdk-comparisons-2026]] — 2026 | Composio, TURION.AI, Morph, Sau Sheong (aggregated) | Claude Agent SDK vs Google ADK landscape; medium confidence (vendor-adjacent blogs)
- [[claude-ai-native-sdlc-playbook]] — 2026-08-21 | Louis Claxton (Anthropic Applied AI) | the AI-native SDLC playbook: six stages as a loop, committed-artifact chain, governance + leading/lagging indicators per play, Stage 6 closing the loop; filed as the external vocabulary for ADLC
- [[google-cloud-okf-announcement]] — 2026-06-12 | McVeety, Hormati (Google Cloud) | OKF launch post; Knowledge Catalog is the hosted, IAM-gated, agent-facing consumer
- [[obsidian-static-publishers-comparison]] — 2026-09-03 | web synthesis | five Obsidian publishers; split by publish trigger (repo-rebuild vs app-push vs live-render)
- [[obsidian-vault-site-generators]] — 2026-09-03 | web synthesis | MkDocs / Docusaurus / Starlight / Hugo Obsidian bridges; rewrite cost for this vault shape
- [[git-backed-wiki-platforms-comparison]] — 2026-09-03 | web synthesis | git-fed team wikis + Confluence routes; one-way vs round-trip; dialect survival
- [[github-docs-markdown-wikis-pages]] — 2026-09-03 | GitHub Docs | markdown rendering, repository Wiki, Pages as vault-sharing surfaces
- [[claude-code-large-codebases-docs]] — 2026-09-03 | Claude Code Docs | additional directories, add-dir, sparse worktrees for cross-repo access

- [[fowler-bounded-context]] — 2014-01-15 | Martin Fowler | bounded context and context map
- [[nygard-documenting-architecture-decisions]] — 2011-11-15 | Michael Nygard | the original ADR post
- [[shape-up-basecamp]] — 2019 | Ryan Singer, Basecamp | Shape Up, from search excerpts
- [[getdx-flow-metrics]] — 2025-09-09 | DX after Mik Kersten | the five flow metrics
- [[aws-ai-dlc-workflows]] — 2025-11-29 | AWS DevOps blog | AI-DLC open-sourced workflows
- [[anthropic-building-effective-agents]] — 2024-12-19 | Anthropic | building effective agents
- [[raci-responsibility-assignment-matrix]] — undated | search results | RACI
- [[writethedocs-docs-as-code]] — undated | Write the Docs | docs as code
- [[productplan-product-requirements-document]] — undated | ProductPlan | the PRD
- [[redhat-golden-paths]] — undated | Red Hat | golden paths
- [[dora-2025-ai-assisted-report]] — 2025-09-23 | DORA | the 2025 report page
---

## Code Repositories

- [[openmanus-repo]] — 2025 | FoundationAgents (MetaGPT team) | PlanningFlow per-step statuses, is_stuck(), max_steps, MCP both directions; semi-dormant since 2025-04
- [[okf-spec-and-reference-repo]] — 2026-06 | GoogleCloudPlatform/open-knowledge-format | OKF v0.2 spec + reference visualizer; the knowledge-catalog copy is frozen
- [[kovetskiy-mark-readme]] — 2026 | kovetskiy/mark | one-way markdown → Confluence publisher README

- [[backlog-md-readme]] — undated | MrLesk and contributors | Backlog.md, a Markdown-native task manager in the repo
---

## Papers

- [[vibe-coding-new-sdlc-day1]] — 2026-05 | Osmani, Saboo, Kartakis (Google) | Day 1, vibe-coding course | syntax→intent thesis; vibe/structured/agentic spectrum; Agent = Model + Harness; factory model; CapEx/OpEx economics; eval-not-demo checklists

- [[cooper-stage-gate-systems-1990]] — 1990 | Robert G. Cooper | Stage-Gate systems; read via a third-party mirror
- [[google-sre-book-introduction-playbooks]] — 2016 | Beyer and others, Google | SRE book Introduction
- [[space-developer-productivity]] — 2021-02 | Forsgren and others | SPACE, via the Microsoft Research record
- [[sei-attribute-driven-design-method-collection]] — 2006-10-31 | SEI | Attribute-Driven Design
---

## Documentation and standards

- [[scrum-guide-2020]] — 2020-11 | Schwaber and Sutherland | the Scrum Guide: accountabilities, events, artifacts, Definition of Done
- [[atlassian-what-is-an-epic]] — undated | Atlassian | epic, sprint and board definitions; linking pages to work items
- [[madr-markdown-decision-records]] — 2024-09-17 | MADR project | MADR 4.0.0 template and rules
- [[backstage-system-model]] — undated | Backstage project | the software catalog system model
- [[claude-code-common-workflows-worktrees]] — fetched 2026-11-08 | Anthropic | parallel Claude Code sessions with git worktrees
- [[github-code-owners-and-push-protection]] — fetched 2026-11-08 | GitHub | code owners, required review, push protection
- [[dora-metrics-guide]] — 2026-01-05 | Nathen Harvey, DORA | the five DORA measures

- [[team-topologies-key-concepts]] — undated | Team Topologies | team types and interaction modes
- [[safe-product-management]] — 2024-10-15 | Scaled Agile | the Product Management role page
- [[obsidian-bases-help]] — undated | Obsidian | Bases, with a Kanban view
- [[atlassian-link-confluence-page-to-work-item]] — undated | Atlassian | page-to-work-item links
- [[atlassian-control-chart]] — undated | Atlassian | the control chart, cycle and lead time
- [[backstage-descriptor-format]] — undated | Backstage project | the catalog descriptor format
- [[contextmapper-context-map]] — undated | Context Mapper project | context maps
- [[claude-code-settings-files-and-precedence]] — fetched 2026-11-08 | Anthropic | settings files and precedence
- [[claude-code-worktrees-page]] — fetched 2026-11-08 | Anthropic | worktrees
- [[gitleaks-readme]] — fetched 2026-11-08 | Gitleaks maintainers | secret scanning hook
- [[kiro-specs-docs]] — fetched 2026-11-08 | Kiro (AWS) | specs
- [[bmad-method-docs]] — fetched 2026-11-08 | BMad Code organization | the method docs home
- [[aws-ai-dlc-phases-and-stages]] — fetched 2026-11-08 | AWS Labs | AI-DLC phases and stages
---

## Add new sources here after each ingest.
