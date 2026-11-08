---
type: synthesis
title: "Research: How work is organized"
created: 2026-11-08
updated: 2026-11-08
tags:
  - research
  - operating-model
  - lifecycle
  - governance
  - metrics
status: developing
related:
  - "[[Software Lifecycle Inputs and Handoffs]]"
  - "[[Knowledge Layer and Work Tracker Split]]"
  - "[[Lifecycle Artifacts and Decision Levels]]"
  - "[[Project Within a Larger System]]"
  - "[[Shared Remote Collaboration for Agent Teams]]"
  - "[[Delivery Metrics and Their Data Sources]]"
  - "[[Agentic Lifecycle Methods Compared]]"
  - "[[Gates as Checkpoints Without Documents]]"
  - "[[Disciplines Bodies of Knowledge and Boundaries]]"
  - "[[Use cases and modes]]"
  - "[[Workers and the dispatch pipeline]]"
  - "[[Product Management Layer Skill]]"
  - "[[Review the ADLC flow against the AI-Native SDLC Playbook]]"
  - "[[Structured Handoff]]"
  - "[[Grilling Session]]"
sources:
  - "[[scrum-guide-2020]]"
  - "[[shape-up-basecamp]]"
  - "[[atlassian-what-is-an-epic]]"
  - "[[backlog-md-readme]]"
  - "[[nygard-documenting-architecture-decisions]]"
  - "[[madr-markdown-decision-records]]"
  - "[[backstage-system-model]]"
  - "[[fowler-bounded-context]]"
  - "[[claude-code-common-workflows-worktrees]]"
  - "[[github-code-owners-and-push-protection]]"
  - "[[dora-metrics-guide]]"
  - "[[getdx-flow-metrics]]"
  - "[[aws-ai-dlc-workflows]]"
  - "[[anthropic-building-effective-agents]]"
  - "[[spec-kit-research]]"
  - "[[cooper-stage-gate-systems-1990]]"
  - "[[claude-ai-native-sdlc-playbook]]"
  - "[[team-topologies-key-concepts]]"
  - "[[safe-product-management]]"
  - "[[raci-responsibility-assignment-matrix]]"
  - "[[obsidian-bases-help]]"
  - "[[writethedocs-docs-as-code]]"
  - "[[atlassian-link-confluence-page-to-work-item]]"
  - "[[productplan-product-requirements-document]]"
  - "[[google-sre-book-introduction-playbooks]]"
  - "[[backstage-descriptor-format]]"
  - "[[redhat-golden-paths]]"
  - "[[contextmapper-context-map]]"
  - "[[claude-code-settings-files-and-precedence]]"
  - "[[claude-code-worktrees-page]]"
  - "[[gitleaks-readme]]"
  - "[[dora-2025-ai-assisted-report]]"
  - "[[space-developer-productivity]]"
  - "[[atlassian-control-chart]]"
  - "[[kiro-specs-docs]]"
  - "[[bmad-method-docs]]"
  - "[[aws-ai-dlc-phases-and-stages]]"
  - "[[sei-attribute-driven-design-method-collection]]"
---

# Research: How work is organized

Brief: `.raw/briefs/2026-11-08 How work is organized.md`. Run on 2026-11-08 with one inventory question answered from this repository (Q0) and eight web questions (Q1 to Q8), one research worker each. The case study is a small two-service web app run through adlc 1.2.0 by one operator; its twelve findings (F1 to F12) are stated in the brief in general terms. This page proposes no change to the plugin; the operator decides the changes in a separate planning step.

A second pass on the same day sent one worker per question after the primaries the first pass could not reach; it added 21 source pages and raised the confidence of the nine concept pages, which carry the detail. The Open Questions section lists what is still secondary.

## Overview

adlc governs the story-level delivery loop well and leaves the layers around it thin: there is no product layer (PRD, domains, deliverables, a stakeholder view), no team or machine record, no spike record, no measurement fields, and no defined step for work that is not a story. The frameworks agree on a model with a small number of stable inputs, two layers (pages for what stays true, work items for what moves through states), one git remote with reviewed pull requests, gates as decision lines rather than documents, and a main thread that talks to the human while workers do bounded work. Nine of the twelve findings map to a part of that model that adlc has only in part; three (F4, F6, F8) map to parts it does not have.

## 1. Inputs, their artifacts and handoffs

The inputs are stable across frameworks; the job titles are not (Source: [[Software Lifecycle Inputs and Handoffs]]). One person can bring several inputs, and an agent can pick up whichever input is missing, so ownership follows inputs, not headcount. The table lists each input, what it produces and consumes, and its reference body of knowledge (Source: [[Disciplines Bodies of Knowledge and Boundaries]]).

| Input | Produces | Consumes | Reference body |
|---|---|---|---|
| Product, including business analysis | PRD, product domains, requirements (business, stakeholder, solution, transition), ordered backlog, deliverables | feedback, stakeholder needs, measurements | BABOK |
| Design | design briefs, design system rulings, copy | PRD, stories | design bodies (unverified) |
| Architecture | architecture drivers, quality attribute scenarios, constraints, ADRs, domain model, context map | solution requirements, system standards | TOGAF, ISO 42010, SEI ADD |
| Development | code, unit tests, review records | stories, specs, conventions | SWEBOK |
| QA | test plans, test cases, verification records, bug records | contracts, Definition of Done | ISTQB |
| DevOps | infrastructure as code, deploy records, runbooks, postmortems | verified increment | DevOps handbook, SRE |
| Facilitation | removed impediments, sprint records | team friction | Scrum, PMBOK |

Handoffs: product to build (a backlog item or pitch; scope negotiable, goal and time budget not), build to verify (Definition of Done), verify to release, release back to product (sprint review or betting table). No surveyed framework names an owner for deploy, so the model must define that handoff itself. The business analyst owns all four requirement classes; the architect adds drivers, scenarios and constraints and records the decision that satisfies them. The handoff is a non-functional requirement in, a scenario, a ranking and a decision out.

Alternatives. Role-based (SAFe) names a person per artifact and scales to many teams but multiplies ceremony for one person. Input-based (the Developers of Scrum, Shape Up) folds roles together and suits one person or a small team but leaves deploy and architecture unowned. Team-based (Team Topologies) organizes dependencies between teams and says nothing about one team's internals. The inputs table works at every size; the cost is that each input needs an explicit owner line even when one person holds them all.

## 2. Artifacts by stage, where each lives, who owns it

Pages hold what stays true; work items hold what moves through states; link them by stable id in both directions and keep status in one place (Source: [[Knowledge Layer and Work Tracker Split]]). Each stage leaves one record type, and only ADRs and product decisions are decisions (Source: [[Lifecycle Artifacts and Decision Levels]]). The table gives the stage, the artifact, the layer it lives in and the input that owns it.

| Stage | Artifact | Layer | Owner |
|---|---|---|---|
| Discover | PRD, product domain map, intake notes | knowledge (product wiki); raw intake in `.raw/` | product |
| Discover | spike record: question, time box, commands in order, versions, failed attempts and why, result | knowledge page for the conclusion; the command log as immutable evidence in `.raw/` | whoever ran it; architecture when it feeds a design |
| Plan | epics, stories, sprints, releases (deliverables) | work layer, one file per item with typed frontmatter | product (epics, releases), facilitation (sprints) |
| Design | domain model, context map, ADRs, specs | code wiki per service; the context map in the product wiki | architecture |
| Build and verify | review records, test plans, verification records | code wiki | development, QA |
| Release | release record: version, date, which epics and stories it closes | work layer as a container, plus a knowledge page for what the user gets | product |
| Operate | infrastructure as code, deploy records, runbooks, postmortems | code repository and code wiki | DevOps |

Epics and sprints are two independent fields on a story, never nested folders: an epic spans sprints and a sprint carries stories from several epics (Source: [[Knowledge Layer and Work Tracker Split]]). A release is the container that answers what the user gets, so deliverables are releases with the epics they bundle.

Alternatives. Keep the backlog in an external tracker and the wiki in git: mature boards and reports, but two systems to keep in step and no agent-readable history. Keep both as files in git: one history, agent-readable, boards as generated views (Source: [[backlog-md-readme]]), but boards and roll-ups must be built. Put the spike record only in the wiki: readable, but the commands get summarized away; put the raw log only in `.raw/`: complete, but no reader finds the conclusion. The two-part spike record (page plus raw log) costs one extra file per spike.

## 3. Levels of decision and records that are not decisions

Four levels, widest first: system or organisation (shared platforms, standards, anything that affects every project on a machine or in a portfolio), team (how the team works: repository layout, branching, review rules), product (what to build and for whom), service (one service's structure, data and interfaces, in ADRs). A lower level records a deviation from a higher one and asks; it does not overrule it (Source: [[Lifecycle Artifacts and Decision Levels]]). Not decisions: conventions (project instructions), tool selections (a list entry unless costly to reverse), machine setup (a setup guide), design briefs (an input to one story), rulings on one story (that story's page), loop state (the run ledger). A gate verdict is a decision line, not a record of its own (Source: [[Gates as Checkpoints Without Documents]]).

Alternatives. One register with a `level` field: one place to search and filter, but engineering records bury product ones and readers must know the field. Separate logs per level: each reader finds their own kind, at the cost of four places and a rule for cross-level references. The MADR experience is that a log with no other home for significant choices collects everything (Source: [[madr-markdown-decision-records]]).

## 4. People and agents over one remote; how a project grows

Each agent works in its own worktree on its own branch; every change reaches the remote through a reviewed pull request; shared files have one writer or only grow by appending; personal state stays out of commits (Source: [[Shared Remote Collaboration for Agent Teams]]). Documentation is reviewed like code, routed by path with CODEOWNERS so that requirements pages go to the product owner and architecture pages to the lead; the required-review rule makes that binding (Source: [[github-code-owners-and-push-protection]]). Sensitive input is layered: a pre-commit secret scan, push protection at the remote, rotation of anything leaked, and for personal data and verbatim user text a reference or summary in committed pages with the text itself kept out of the shared history or reviewed before commit. The project is placed in the bigger system by four records: a C4 context and container diagram, a dependency table per team pair with an interaction mode and an end date, a catalog descriptor naming owner, system and domain, and a bounded-context note with a context map (Source: [[Project Within a Larger System]]). Growth: a one-person project already has AGENTS.md and the wiki; a second person adds CODEOWNERS, branch protection, a short contributing note and secret scanning; each newcomer brings an input and takes ownership of that input's paths.

Alternatives. Direct commits to main for one person: fastest, no review latency, but nothing to grow into and no review of what the agent filed. Pull requests from day one: a review step even when the author is the only reviewer, but the record, the hooks and the ownership rules are in place when the second person arrives.

## 5. Measuring delivery

Git gives the end of the clock (when code landed and shipped); the work item gives the start of the clock and the meaning (Source: [[Delivery Metrics and Their Data Sources]]). The five DORA measures (change lead time, deployment frequency, failed deployment recovery time, change fail rate, deployment rework rate) come mostly from commit, tag and revert timestamps (Source: [[dora-metrics-guide]]). Cycle time, flow efficiency, work in progress, flow distribution and estimation accuracy need the item: status-change timestamps, type, size, release. Cycle time and lead time in a tracker follow whichever statuses the team selects as start and stop, so the status history, not a fixed transition, is the record (Source: [[atlassian-control-chart]]). The 2025 DORA report replaces the four performance tiers with team archetypes (Source: [[dora-2025-ai-assisted-report]], medium). A story or epic record therefore carries `id`, `type`, `parent`, `created`, `ready`, `started`, `done`, a dated status history, `size`, `release` and `caused_by`, and every commit carries the item id. The dates of an epic derive from its children. SPACE adds satisfaction and collaboration, which need a survey, not a file. Ruling (operator, 2026-11-08): adlc does not generate DORA reports or collect metrics. The epics, sprints and stories in the wiki are the source of truth and carry the fields; any measurement is computed from them and from git by a tool outside the plugin.

Alternatives. Derive everything from git: zero discipline on the items, but no start of clock, no item type, no estimate, and a revert is indistinguishable from a normal fix. Full status history on every item: complete flow metrics, at the cost of one dated line per transition that a closing step must write. Story points against throughput forecasting: a coarse size costs one field and lets both methods be compared later.

## 6. Governing agent work

Every surveyed agentic method puts a human gate between artifacts, keeps the human-facing steps in the main thread, and records approval as a file in the repository (Source: [[Agentic Lifecycle Methods Compared]]). Workers suit bounded, measurable work: research, spikes, build, test, review. Gates, rulings, contracts and commits stay in the main thread (Source: [[anthropic-building-effective-agents]]). An approval record names the approved artifact version, not only that approval happened; a broad reply accepts only what it names. AI-DLC's audit log is the fullest surveyed form: a receipt per verified checkpoint, auto-approved ones included, with bypass settings recorded and skipped stages marked, append-only and kept apart from the state file (Source: [[aws-ai-dlc-phases-and-stages]]). Status files drift when a stage skips them, so one closing step owns every shared file. No surveyed method treats spikes, environment setup or changes to the tooling itself as a first-class step; a lifecycle that does fills a gap all of them leave. A gate is criteria written before the work, evidence as pointers to existing artifacts, and one decision line with verdict, date, deciding role and conditions; kill, hold and recycle must be real outcomes (Source: [[Gates as Checkpoints Without Documents]], [[cooper-stage-gate-systems-1990]]).

Alternatives. A single agent following rules (AI-DLC): simple, auditable through one log, but no context isolation and the main thread does everything. Orchestrator and workers (Anthropic): isolated context and parallel work, but the orchestrator must define a step for every kind of work or the agent invents one. Persona switching in one session (BMAD): role discipline without dispatch overhead, but no isolation and status files reported to drift.

## 7. Findings mapped to the model, and the gaps in adlc as built

The table maps each finding to the part of the model above and states what adlc has today (Q0, from the architecture pages and the skills).

| # | Finding | Model part | adlc as built |
|---|---|---|---|
| F1 | decision register mixes kinds | 3: four levels; conventions, tool selections and setup are not decisions | product decisions and ADRs are separate; no team or system record type; nothing says the toolset block is not a decision |
| F2 | no deliverables | 2: release as the container of epics | `deliverables/` holds business cases and milestones; no release record, no epic-to-release link |
| F3 | no product domains | 2 and 4: domain map and context map in the product wiki | Gate 1.5 domain model per service only |
| F4 | no PRD | 2: PRD at discover, product-owned | missing; closest are the overview page and the intake note |
| F5 | product side missing | 2 and 5: PRD, releases, progress from item fields | mission control and the activity roll-up serve agents; no product view |
| F6 | no DORA framework | 5: item fields plus commit ids; the computation stays outside the plugin (operator ruling) | no start, finish or release fields on the records; a metrics tool is not in scope |
| F7 | no stakeholder board | 2: boards as generated views over item frontmatter | Bases board (one reader only), tracker push; nothing outside `meta/` |
| F8 | spike work unrecorded | 2 and 6: two-part spike record; spikes as a defined step | missing; a spike is only a story type |
| F9 | no orchestration governance | 6: steps for every kind of work, approval records with the artifact version, one owner per shared file | strong inside the story loop; no steps for research, spikes, architecture design, scaffolding or plugin changes; no acceptance rule |
| F10 | prompts logged verbatim | 4: references in committed pages, text reviewed or kept out of shared history | the template of the plugin itself asks for a verbatim quote in a tracked page; redaction exists only for upstream exports |
| F11 | epics inside `sprints/` | 2: epic and sprint as independent fields | the filing table names only the run ledger for `sprints/` and has no row for epics |
| F12 | gate documents; architect writes requirements | 1 and 6: BA owns requirements, architect adds drivers; a gate is a decision line | the architecture worker writes `GATE-{N}` pages and its Gate 1 produces functional and non-functional requirements |

Gaps between the model and adlc as built:

- No product layer: PRD, domain map, release record, stakeholder view.
- No record type for the team and the system or machine level, and no rule naming what is not a decision.
- No epic folder or epic frontmatter; the run ledger is the only `sprints/` artifact.
- No spike record, and no step for spikes, environment setup, architecture design during delivery, or tooling changes.
- No `decided_by` or acceptance rule, so a one-line reply can stand for rulings it did not name.
- No measurement fields on stories or epics, and no commit-to-item join beyond trace ids. Collecting or reporting the metrics is not the job of adlc; the records only have to make it possible.
- Verbatim quotes in a tracked page with no review before commit, and no commit rule for `.raw/`.
- Gates written as documents, and the architecture worker doing the work of the analyst.
- No C4 context, dependency table or catalog descriptor placing the project in a portfolio.
- Mission control with no rule for several operators at once.

## Contradictions

- MADR: a search summary says the "A" means "Any" since 3.0.0; the fetched 4.0.0 page keeps "Architectural" (Source: [[madr-markdown-decision-records]]). The fetched page is the primary.
- BMAD: one guide folds the scrum master and QA agents into the developer; the current docs list them separately; release notes deprecate the story pair for a single build chain (Source: [[Agentic Lifecycle Methods Compared]]). Low confidence either way.
- AI-DLC: the blog says every approval is recorded; a repository issue says the log records that approval happened, not what was approved (Source: [[aws-ai-dlc-workflows]]). The issue is the more specific claim.
- Requirements classes: a 2022 IIBA chapter workshop argues the functional and non-functional split matters mainly to designers; the BABOK schema keeps it (Source: [[Disciplines Bodies of Knowledge and Boundaries]]).
- BABOK: version 2 treats transition requirements as a category beside solution requirements; later versions nest the functional and non-functional split under solution requirements (Source: [[Disciplines Bodies of Knowledge and Boundaries]]).
- The playbook claim of roughly three times better time to repair sits in the Introduction of the SRE book, not in the on-call chapter where secondary sources place it; the book says playbook where this wiki says runbook (Source: [[google-sre-book-introduction-playbooks]]).
- The Backstage descriptor page contradicts itself on whether a Template's owner is optional; it does not affect the catalog fields used here (Source: [[backstage-descriptor-format]]).
- ISO 25010: eight characteristics in the 2011 edition, nine in 2023. DORA 2024 tier cutoffs and the count of flow metrics (four to six) vary by secondary source (Source: [[Delivery Metrics and Their Data Sources]]).

## Open Questions

No question was blocked. Two passes ran; the second fetched 21 primaries the first pass could not reach. What is still secondary or unread:

- A RACI primary (the PMBOK wording was not seen); the SAFe Product Owner relation and System Architect page, partly behind a login; the Team Topologies page is undated (Q1).
- No current Atlassian page states the page-versus-issue rule; whether the Obsidian Kanban plugin maps lanes to a note property; the Bases views and functions detail (Q2).
- The spike glossary entry (404 at both URL forms) and the SRE postmortem chapter; domain model, test plan, release record and infrastructure as code still rest on practice judgment (Q3).
- The origin of the golden-path term rests on one vendor page; the DDD definitions of the context-map relationship types beyond customer-supplier; the SAFe dependency board, handbooks and architecture principles (Q4).
- The local CLAUDE.md variant and the memory file layout; whether worktrees isolate ports and databases (Q5).
- The 2025 DORA report PDF exceeded the fetch limit, so the reliability definition and the archetype measures are unread; the SPACE paper text (ACM returned 403; only the abstract via the Microsoft Research record) (Q6).
- Kiro hooks and steering; the BMAD planning pages, sprint status file and whether the scrum master and QA agents are still separate; the AI-DLC audit field list and the definition of a bolt; the Claude Code sub-agents page (Q7).
- TOGAF (every Open Group URL redirects to a login) and BABOK (the IIBA page is gated) remain secondary; the ADD driver and scenario definitions are in the report PDF, not the method page; ISTQB, PMBOK, SWEBOK, SRE as a body of knowledge and the design bodies are unverified (Q8).

## Sources

- [[scrum-guide-2020]]: Schwaber and Sutherland, 2020-11. [[shape-up-basecamp]]: Singer, Basecamp, 2019.
- [[atlassian-what-is-an-epic]]: Atlassian, undated. [[backlog-md-readme]]: MrLesk and contributors, undated.
- [[nygard-documenting-architecture-decisions]]: Nygard, 2011-11-15. [[madr-markdown-decision-records]]: MADR project, 2024-09-17.
- [[backstage-system-model]]: Backstage project, undated. [[fowler-bounded-context]]: Fowler, 2014-01-15.
- [[claude-code-common-workflows-worktrees]]: Anthropic, fetched 2026-11-08. [[github-code-owners-and-push-protection]]: GitHub, fetched 2026-11-08.
- [[dora-metrics-guide]]: Harvey, DORA, 2026-01-05. [[getdx-flow-metrics]]: DX after Kersten, 2025-09-09.
- [[aws-ai-dlc-workflows]]: Matos and others, AWS, 2025-11-29. [[anthropic-building-effective-agents]]: Anthropic, 2024-12-19. [[spec-kit-research]]: filed 2026-05-10.
- [[cooper-stage-gate-systems-1990]]: Cooper, 1990, via a mirror. [[claude-ai-native-sdlc-playbook]]: Claxton, Anthropic, 2026-08-21.

Second pass:

- [[team-topologies-key-concepts]]: Team Topologies, undated. [[safe-product-management]]: Scaled Agile, 2024-10-15. [[raci-responsibility-assignment-matrix]]: search results, undated.
- [[obsidian-bases-help]]: Obsidian, undated. [[writethedocs-docs-as-code]]: Write the Docs, undated. [[atlassian-link-confluence-page-to-work-item]]: Atlassian, undated.
- [[productplan-product-requirements-document]]: ProductPlan, undated. [[google-sre-book-introduction-playbooks]]: Beyer and others, Google, 2016.
- [[backstage-descriptor-format]]: Backstage project, undated. [[redhat-golden-paths]]: Red Hat, undated. [[contextmapper-context-map]]: Context Mapper project, undated.
- [[claude-code-settings-files-and-precedence]] and [[claude-code-worktrees-page]]: Anthropic, fetched 2026-11-08. [[gitleaks-readme]]: Gitleaks maintainers, fetched 2026-11-08.
- [[dora-2025-ai-assisted-report]]: DORA, 2025-09-23. [[space-developer-productivity]]: Forsgren and others, 2021-02. [[atlassian-control-chart]]: Atlassian, undated.
- [[kiro-specs-docs]]: Kiro, fetched 2026-11-08. [[bmad-method-docs]]: BMad Code organization, fetched 2026-11-08. [[aws-ai-dlc-phases-and-stages]]: AWS Labs, fetched 2026-11-08.
- [[sei-attribute-driven-design-method-collection]]: SEI, Carnegie Mellon, 2006-10-31.
