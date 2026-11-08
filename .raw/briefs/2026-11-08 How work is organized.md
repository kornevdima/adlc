<!--
Source: research brief from the plugin's operator, written 2026-11-08 in a vault that runs adlc 1.2.0.
The case study is described in general terms: no project names, paths, people or prompts.
Immutable source: do not edit. A changed brief is a new dated file.
-->

# How work is organized: research brief

## Goal

adlc runs a delivery loop: one operator directs agents through stories in one vault. This research asks how the work around that loop should be organized, so that adlc can carry a whole software lifecycle for a project with any mix of contributors.

The model to research has these parts:

- Inputs, not team size. People bring inputs to a project: product, design, development, QA, DevOps. One person can bring every input, and a team can grow around a project that one person started. Every contributor runs adlc.
- Two layers. The wiki is the knowledge layer, in the role Confluence plays for a team: product documentation, decisions, domain knowledge. The backlog is the work layer, in the role Jira plays: epics, stories, sprints, a board.
- One source of truth. The work goes to one git remote, where everyone can see it and update it.
- A bigger system. The project is one part of a larger system, with other teams and shared standards.

The plugin's creator raised this after reviewing, as product owner, a project run through adlc. The creator knows the plugin well enough to see these gaps; other people who use it would run into the same gaps without seeing why.

## Expected result

One synthesis page, filed after the questions are answered, that describes a target operating model:

1. the kinds of input, the artifacts each one produces and consumes, and the handoffs between them
2. the artifacts at each stage of the lifecycle, where each one lives (knowledge layer, work layer, code wiki, `.raw/`), and who owns it
3. the levels of decision (system, team, product, service), and the kinds of record that are not decisions
4. how people and their agents work together over one remote, and how a project grows
5. how delivery is measured, and which data comes from git and which from frontmatter
6. how agent work is governed: what runs in a worker, what runs in the main session, and who approves what
7. a table that maps each case-study finding below to the part of the model that answers it, and a list of the gaps between the model and adlc as built

The synthesis compares alternatives and states the trade-offs for each part of the model. It does not settle a choice by taking the cheapest option. The operator decides on the changes to adlc later, in a separate planning step. The research proposes no changes to the plugin's code.

## The case study

The project is a small local web app with two services, a backend and a frontend, kept on separate branches of one repository. It was run through adlc 1.2.0 over four sessions by one operator. The vault holds requirements, features, stories, one epic and eight decision records. No code for the epic has been written yet. The operator reviewed the work as product owner and found these gaps.

| # | Finding |
|---|---|
| F1 | The decision register mixes product decisions with a team decision (how the repository and worktrees are organized), a skill selected in the toolset (not a decision at all), and the setup of one machine |
| F2 | There are no deliverables. An epic exists, but nothing says what a release hands to the user or which epics make it up |
| F3 | There are no product domains. The code wikis describe the services, but the split of responsibilities (for example media conversion and text extraction) is not recorded anywhere |
| F4 | There is no PRD. Feature pages exist, but no single page describes the application |
| F5 | The product side is missing. The product owner cannot find what is being built, the deliverables, what the user gets when the work is done, the progress, the estimates, or the progress of the current epic and sprint. The wiki is neither user documentation nor a project package |
| F6 | There is no framework to measure the work against the DORA metrics. Stories and epics record no start, finish or release |
| F7 | There is no product board for stakeholders. Story frontmatter already holds the fields a card needs (status, feature, epic, services, dependencies, size, priority). The pages in `meta/`, mission control among them, serve the agents and are not meant to be shared |
| F8 | Spike work is not recorded. The main session checked the GPU toolkit, built a native speech engine from source, downloaded a model and test-ran a server, in several attempts. Only the conclusions reached the wiki, spread over six pages. The commands, versions, failed attempts and machine changes were lost, and they are what a later move to infrastructure as code would need |
| F9 | adlc lacks orchestration governance. Across four sessions workers ran twice. Research, the spike, an architecture design and a plugin change all ran in the main session. The agent invented its own process where adlc defines no step. Records were filed with `decided_by: operator` after one-line replies, and a broad reply was taken as acceptance of rulings it did not mention. Bookkeeping was done by throwaway scripts, and one session ran no wrap-up. The operator's answers did not reach the operator profile. Changes that affect every project on the machine have no record |
| F10 | Operator prompts are logged verbatim in committed pages. The correction log asks for each correction as typed. That helps debugging, and the "What it exposed" column shows how the agent processed the input, but nothing reviews the quotes for sensitive content before they are committed. The operator suggests material of this kind belongs in `.raw/`, with a review at wrap-up |
| F11 | Epics are filed inside `sprints/`. A sprint is a time box and can carry several epics, for example backend and frontend work in parallel |
| F12 | The shift-left gates produce gate documents (`GATE-1`, `GATE-1.5`). A gate is a checkpoint, not a document. The architecture worker's Gate 1 writes functional and non-functional requirements, which is the business analyst's work. Each input works within its own body of knowledge (BABOK for business analysis, TOGAF for architecture), and an architect adds architecture drivers rather than requirements |

## Questions

Q0 runs first, from this repository, before any web research. Q1 to Q8 are web research, one research worker each.

| # | Question | Findings it answers |
|---|---|---|
| Q0 | What does adlc already provide for each part of the model? Read `wiki/architecture/`, the skills (`product-management-layer`, `ba-export`, the BA methods for scrum events and planning, `adlc`, `wrap-up`), the shift-left reference, and the sources already in `.raw/` (the AI-native SDLC playbook, the plan for the product management layer). Record what exists, what is partial and what is missing | all |
| Q1 | What kinds of input does a software lifecycle have, which artifacts does each one produce and consume, and where are the handoffs? Sources: Scrum, SAFe, Shape Up, Team Topologies, RACI practice | F5, F9 |
| Q2 | How do a knowledge layer and a work tracker divide the work, and how do their pages link? Covers Confluence with Jira, docs as code, trackers kept as Markdown files, boards built from frontmatter, and how epics relate to sprints when one sprint carries several epics | F7, F11 |
| Q3 | Which artifacts belong to each stage of the lifecycle: PRD, release and deliverable, domain model, spike record, decision record, test plan, runbook, infrastructure as code? What levels of decision are there, and which records are not decisions? | F1, F2, F3, F4, F8 |
| Q4 | How does a project fit into a bigger system: system architecture (for example C4), dependencies between teams, shared standards, links across projects? | F3 |
| Q5 | How do several people, each running agents, work over one git remote? Covers review of documentation through pull requests, concurrent agents, which state is personal and which is shared, sensitive input, and how a project grows when someone joins it | F9, F10 |
| Q6 | How is delivery measured: DORA, SPACE, flow metrics, estimation? Which data comes from git and which from frontmatter? | F5, F6 |
| Q7 | What do existing agentic lifecycle methods prescribe for orchestration and governance? For example AWS AI-DLC, GitHub Spec Kit, Kiro, BMAD, and Anthropic's guidance on agents | F9 |
| Q8 | How does each kind of input map to its body of knowledge (BABOK, TOGAF and the others), where does one discipline's work end and the next begin, and how does a gate work as a checkpoint with no document of its own? | F1, F12 |

## How to run it

- Run `/autoresearch` in this repository, with this brief as the topic. The plan holds Q0 to Q8.
- `references/program.md` allows at most 7 questions per plan. This brief needs 8 web questions, so raise `max_questions` to 8 for this run and note it in the plan.
- Q0 is answered in the session from the repository, not by a research worker, and its result goes into the plan before the workers start.
- The research is filed in this repository's `wiki/`, which is public. Nothing filed may name the case-study project, its people, its paths, or quote its operator. Run `skills/wiki/scripts/upstream_redact_check.py` on every page before filing.
- The session may read the case-study vault's review notes and session reviews on this machine for context. Nothing from them is filed here except what this brief already states.
- Nothing is committed or pushed without the operator's word.
