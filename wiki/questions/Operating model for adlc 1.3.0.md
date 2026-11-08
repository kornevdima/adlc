---
type: synthesis
title: "Operating model for adlc 1.3.0"
created: 2026-11-08
updated: 2026-11-08
tags:
  - adlc
  - plan
  - operating-model
  - release
status: open
related:
  - "[[Research How work is organized]]"
  - "[[Use cases and modes]]"
  - "[[Workers and the dispatch pipeline]]"
  - "[[Shared references]]"
  - "[[Knowledge Layer and Work Tracker Split]]"
  - "[[Lifecycle Artifacts and Decision Levels]]"
  - "[[Gates as Checkpoints Without Documents]]"
  - "[[Disciplines Bodies of Knowledge and Boundaries]]"
  - "[[Delivery Metrics and Their Data Sources]]"
  - "[[Shared Remote Collaboration for Agent Teams]]"
  - "[[Project Within a Larger System]]"
  - "[[Agentic Lifecycle Methods Compared]]"
---

# Operating model for adlc 1.3.0

The work plan for the gaps that [[Research How work is organized]] lists in its section 7. The operator ruled on 2026-11-08: everything ships in one release, 1.3.0; the agreed EGM spec-review work moves to 1.4.0. The board is a generated Markdown page; decision levels get separate record kinds; gate pages become artifact pages and the architecture worker writes drivers, never requirements; adlc collects no metrics, the records only carry the fields.

Fifteen work items in seven blocks, with the files each one touches and how its completion is checked. The order of work is at the end. The product wiki means a Mode ADLC vault's `wiki/`; the code wiki means a service's own wiki under `services/<svc>/wiki/` or `service-wikis/<svc>/`.

## A. The product layer

**Item 1, a PRD page.** The product wiki gets `product/prd.md`: purpose, users, what the user can do when the work is done, scope and non-goals, the feature list with links, open questions. The BA worker writes it in the initial pass after the requirements register, from a new method doc `skills/wiki/references/ba/ba-prd.md` that keeps the PRD at the why and the what and leaves the how to the specs. Wrap-up step 5 already names PRD-like pages; it now names this one and keeps it current when features ship. Touches: `skills/wiki/references/modes.md` (folder map, filing table), `skills/wiki/SKILL.md` (scaffold), `agents/ba-suite-subagent.md`, `skills/wiki/references/ba/_index.md`, `skills/wrap-up/SKILL.md`. Done when a scaffolded vault has the page, the initial pass fills it, and the scaffold eval checks for it.

**Item 2, product domains.** `domains/` in a Mode ADLC vault holds product domains, not research topics: one page per domain with its responsibility, the services that implement it and a link to each service's bounded-context note, plus `domains/context-map.md` with the relations between domains. The Gate 1.5 domain model per service links up to its domain. Touches: `modes.md`, `skills/wiki/SKILL.md`, `agents/architecture-subagent.md`, `skills/wiki/references/frontmatter.md` (the `domain` type). Done when the architecture worker reads the domain page before writing a service's model and the scaffold creates the folder with its index.

**Item 3, releases as the container.** A `releases/` folder; a release record carries id, version, status (planned, released), date, the epics it bundles, what the user gets, and the stories it closed. Epics carry `release:`; the test plan's `release:` and the story's `release:` point at the record. `deliverables/` keeps business cases and milestones. Touches: `modes.md`, `frontmatter.md`, `skills/wiki/references/concerns/qa.md`, `skills/adlc/SKILL.md` (epic close links the release), `skills/wrap-up/SKILL.md` (step 4 reflects shipped stories into the release). Done when an epic cannot close without a release link and the release page lists what the user gets.

**Item 4, the board.** `skills/wiki/scripts/board.py` renders `wiki/board.md` from story frontmatter: one column per status, one card per story with its feature, epic, services, size and priority, and per epic and per release the count of stories done against total. It is a view and holds no data of its own; the loop regenerates it at every story close and wrap-up step 6 regenerates it with the other roll-ups. With `reader: obsidian` in the toolset the script also writes `board.base` beside it. The page lives outside `meta/`, so it can be shared. Touches: the new script and its tests, `skills/adlc/SKILL.md`, `skills/wrap-up/SKILL.md`, `skills/wiki/references/toolset.md`, `skills/wiki/references/mission-control.md` (mission control stays the agents' board). Done when the script is idempotent on a fixture vault and the eval for the loop checks the page after a story close.

## B. The work layer

**Item 5, epics and sprints as separate things.** An `epics/` folder with an epic record: id, title, status, release, feature, created, started, done, the rulings table (moved from wherever the epic page lived), and its stories listed by query, not by hand. The filing table gets an epics row; `sprints/` keeps the run ledger and gains a sprint record `sprints/<SPRINT-ID>.md`: a time box with goal, start and end dates, the epics worked and the stories planned. One sprint carries stories from several epics; a story names its sprint and its epic as two fields. Touches: `modes.md`, `skills/wiki/SKILL.md`, `frontmatter.md`, `skills/adlc/SKILL.md` (Step 0 reads the epic from `epics/`), `skills/wiki/references/technical-planning.md`, the BA scrum-events method. Migration: `relink.py` moves an epic page out of `sprints/` and rewrites links. Done when the scaffold has both folders, the loop finds the epic in `epics/`, and the filing table has no epic in `sprints/`.

**Item 6, story frontmatter owned by the plugin.** `frontmatter.md` defines the story record: id, type (feature, defect, risk, debt, spike), feature, epic, sprint, release, status, created, ready, started, done, a dated status history (one line per transition), size, priority, services, depends_on, caused_by. The loop writes the dates at the transitions it already makes: ready at the contract, started at the builder dispatch, done at the verified commit. Commits already carry the item id. No roll-up, no computation; the ruling that metrics are computed outside adlc is written on the page. Touches: `frontmatter.md`, `skills/adlc/SKILL.md`, the BA user-story method, `skills/wiki/references/glossary` conventions if ids change (they do not). Done when a story created by the BA worker and advanced by the loop has every date filled without a human editing frontmatter.

## C. Decisions

**Item 7, decision levels as separate record kinds.** `decisions/` holds product decisions only; its index text is narrowed back. Team choices are not wiki records: the tools are the `Toolset:` block in the vault's AGENTS.md (reader, code navigation, design, layout, engineering, cost), and the rest (branching, review rules, the definition of done) is a `## How we work` section beside it, which `project-profile` already starts as "How we change code". A change to a team choice is a row in the vault's changelog, not a decision record. Machine setup goes to `meta/machine.local.md`, which the vault's gitignore already excludes through `*.local.md`. ADRs stay in the code wiki. A short reference page, `skills/wiki/references/records.md`, names the four levels and what is not a decision: the toolset block, the How we work section, design briefs, rulings on one story, the run ledger, a tool selection unless costly to reverse. The decision record gains `decided_by`, `decided_on` and `evidence` (a pointer to the message, page, spike or artifact version that carried the decision). Touches: `modes.md`, `frontmatter.md`, `skills/wiki/SKILL.md`, `skills/wiki/references/toolset.md`, `skills/project-profile/SKILL.md`, `skills/wiki/references/team-sync.md`, `skills/wiki/references/git-setup.md`. Done when the initial pass files a team choice in AGENTS.md and refuses it in `decisions/`, and the lint flags a decision with no `decided_by`.

## D. Spikes and the work that is not a story

**Item 8, the spike as a work item.** A spike is a backlog item of type spike, sized by its time box, in an epic and a sprint like any story; the BA story factory already has the type and its two-day limit. It opens when a decision has no evidence: the architecture worker, or the operator, proposes a spike story that names the question and the decision it feeds (an ADR, a product decision, a PRD section); the worker proposes, the backlog accepts. Its pipeline differs from a story's: the contract states the question, the time box, what counts as answered and what the result feeds; the run has two modes, chosen in the contract: autonomous, where a spike worker (Bash, Read, Write, Edit) runs the commands in its own context and returns the structured record, and operator-run, where the person runs the commands and the plugin's job is to document the outcome, capturing the commands, versions, failed attempts and result from the session into the same record and log, so a spike run at the keyboard leaves the same evidence as one run by the worker; the record lives on the story page itself (commands in order, tool and library versions, failed attempts and why, result), and the raw command log goes to `.raw/spikes/<id>.log`, committed, because a later move to infrastructure as code needs it and secret scanning covers it; the close writes the decision with the spike as its `evidence` and marks the spike done. Touches: new `agents/spike.md`, `skills/adlc/SKILL.md` (the per-story pipeline branches on `type: spike`), `skills/wiki/SKILL.md` (manual mode), `agents/architecture-subagent.md` (proposes spikes, never runs them), the BA user-story method, `frontmatter.md`, `wiki/architecture/Workers and the dispatch pipeline.md`. Done when a spike story in each mode leaves its record on the page, its log in `.raw/spikes/`, and an ADR whose evidence points at it; in autonomous mode no spike command runs in the main session.

**Item 9, routes for every kind of work.** A reference `skills/adlc/references/routes.md` with one row per kind of work that is not a feature story: research during delivery goes to `/autoresearch`; discovery to a spike story (item 8); architecture design to the architecture worker dispatched from the loop (Step 0 dispatches instead of stopping); scaffolding and environment setup to AGENTS.md's How we work section or `machine.local.md`; a plugin change to the upstream route, never a pull request from inside a vault session; bookkeeping to wrap-up, never a throwaway script. The adlc skill reads the table at Step 0 and whenever the operator asks for work the loop has no step for. Touches: the new reference, `skills/adlc/SKILL.md`, `skills/wiki/references/technical-planning.md`, `agents/architecture-subagent.md` (its dispatcher list), `skills/wiki/references/adlc-upstream.md`. Done when the eval gives the loop a research request, a discovery question and a plugin complaint and each lands on its route with a record.

## E. Approvals

**Item 10, acceptance names what it accepts.** A dispatcher rule in the adlc skill and the technical-planning reference: a reply accepts only the rulings it names; after a broad reply the agent lists the items it takes as accepted and asks once. Rulings and decisions carry `decided_by`, `decided_on` and `evidence`. `skills/wiki/references/mission-control.md` gains the multi-session rule in one place: pull before reading, one dispatcher per epic, regenerate rather than merge, and what to do when two sessions touched the board. Touches: `skills/adlc/SKILL.md` (Step 2 ruling questions), `technical-planning.md`, `mission-control.md`, `operator-profile.md` (the engagement pole does not override this). Done when the eval's one-line reply to a five-item ruling list produces a list-back, not five accepted records.

## F. Operator quotes

**Item 11, quotes out of committed pages.** `meta/` is the agent-facing state of the project and holds no prompt as typed. The correction log in `meta/operator-profile.md` drops the verbatim column and keeps the date, the classification, "what it exposed" and a session reference; the text as typed lives in `.raw/reflection/<session>.md`, which the vault's gitignore excludes. Nothing in it is reviewed for commit because nothing in it is committed; the distilled rulings in the operator profile are what travels with the vault, and a new machine starts without the raw material. The writing-style and technical-writer rules that say "verbatim" are rewritten, and `git-setup.md` adds the ignore line. Touches: `operator-profile.md`, `skills/wrap-up/SKILL.md` (step 7a writes the reference, no review step), `skills/wiki/references/writing-style.md`, `skills/technical-writer/SKILL.md`, `skills/wiki/references/git-setup.md`. Done when a correction logged in the eval vault leaves no quoted prompt in a tracked page and the reflection file is untracked.

## G. Gates and the roles at them

**Item 12, artifact pages and drivers.** The architecture worker stops writing requirements. It reads `requirements/` (functional and non-functional, by the BA) and writes, in the code wiki: `architecture-drivers.md` (the drivers it selected, each quality requirement restated as a quality attribute scenario, the constraints), `domain-model.md`, `adrs/`, and `engineering-workflow.md`. No file is named after a gate. Each gate is one decision line in a `Gates` table on the epic page: gate, verdict (go, hold, recycle), date, deciding role, evidence pointers, conditions. The shift-left reference is rewritten around gates as checkpoints, the technical-planning table and `team-sync.md`'s architect row follow, and `relink.py` renames existing gate pages. Touches: `agents/architecture-subagent.md`, `skills/wiki/references/shift-left/` (all), `technical-planning.md`, `team-sync.md`, `skills/adlc/SKILL.md` (Step 0 reads the Gates table), `wiki/architecture/Workers and the dispatch pipeline.md`. Done when a run of the worker on a fixture produces no FR or NFR line and the four artifact pages, and the epic page carries the gate lines.

## H. The project in a bigger system, and growth

**Item 13, the portfolio records.** The scaffold adds `product/context.md`: a C4 context and container description (text and, with `reader: obsidian`, a canvas), a dependency table per team pair with interaction mode and end date, and a `catalog-info.yaml` template at the repository root naming owner, system and domain. Each service's code wiki gets a bounded-context note that the domain page links. Touches: `skills/wiki/SKILL.md`, `modes.md`, `agents/architecture-subagent.md`, `skills/project-profile/SKILL.md` (the descriptor from the scanned repo). Done when the scaffold eval finds the three files with placeholders filled from the vault description.

**Item 14, when a second person joins.** `team-sync.md` gets a joining checklist, and the wiki setup can run it: a `CODEOWNERS` written from the `Roles:` block so each input owns its paths, a short `CONTRIBUTING.md` (branch naming, pull-request flow, who reviews what), a `gitleaks` pre-commit entry, branch protection noted as the operator's step, and the rule that personal settings stay in the local settings file. Touches: `team-sync.md`, `skills/wiki/SKILL.md`, `skills/wiki/references/git-setup.md`, `bin/` (a setup script for the hook). Done when a one-person fixture vault passes through the checklist and the files exist with the roles mapped.

## I. Release mechanics

**Item 15, shipping 1.3.0.** Version bump in the manifest; the migration note for existing vaults (new folders, the epic move, the gate rename, the `How we work.md` seed) as a `toolset.py migrate` step or a documented hand procedure; evals for the scaffold's new folders and files, the board script, the routes table and the acceptance rule; the AI-tells pass on every touched page; README, `wiki/architecture/` pages and the changelog updated; EGM re-planned as 1.4.0 in the hot cache and its question page. Done when the fast eval set is green, the migration ran on one co-located vault, and the release row is written.

## Order of work

1. Items 6, 5, 3, 4 in that order: the frontmatter first, then the folders that use it, then the release container, then the board that reads all three.
2. Items 1 and 2 beside them: the PRD and the domains do not depend on the frontmatter.
3. Item 7, then 12: the record kinds first, then the gates that write decision lines into them.
4. Items 8 and 9: the spike record and the routes, once the loop's Step 0 knows the epic folder and the Gates table.
5. Items 10 and 11: the approval rule and the quotes, independent of the rest.
6. Items 13 and 14: the portfolio and growth records last.
7. Item 15 closes the release.

## Still open for the operator

None. Closed on 2026-11-08: `.raw/reflection/` is gitignored, not committed after review; team choices live in the vault's AGENTS.md (the Toolset block and a How we work section), not in a wiki page; a spike is a work item in the backlog, not a record type of its own; the spike worker ships in 1.3.0, and a spike also runs in operator-run mode, where the plugin documents the outcome.

## Assumptions

The co-located vaults migrate when 1.3.0 ships, not before. The EGM spike (a worker spawning an EGM reviewer) waits for 1.4.0. The dash sweep stays its own commit outside this release.
