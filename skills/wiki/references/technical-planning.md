# Technical planning and verification (ADLC mode)

The BA layer (`ba-suite`, product wiki) produces business deliverables. Technical planning refines those into per-service specs a repo agent can build, then verification confirms the build with the operator's own toolset. Used by Mode ADLC (see [`modes.md`](modes.md)).

## No project-context folders

Do NOT scaffold a separate `project-context/` folder kit in the product wiki for technical planning. Use the ingest + refinement pipeline instead: requirements are ingested into the product wiki (`ba-suite`), then refined into specs that live in each service's own code wiki (Mode B). The product wiki holds the business view; the service code wiki holds the technical spec.

## Shift-left refinement (ingest to spec)

The `architecture-subagent` (`agents/architecture-subagent.md`) is the worker. It applies the bundled shift-left four-gate methodology (`skills/wiki/references/shift-left/`, no external plugin):

| Gate | Produces |
|---|---|
| Gate 1 | Technical requirements: FR / NFR / SR (security separate), open questions, gaps |
| Gate 1.5 | Domain model: entities, business rules, invariants, Mermaid diagrams |
| Gate 2 | Architecture Decision Records + design rationale |
| Gate 3 | Engineering workflow: CI/CD, test pyramid, deployment, incidents |

Gates are sequential with a human approval between each (no skipping). Refinement traces every technical requirement back to a BA requirement ID. Specs are written to `services/<svc>/wiki/specs/` (or the repo's `plans/` convention), one set per service.

### Grilling gate (before Gate 1 is approved)

Elicitation is non-interactive: `ba-suite` synthesizes requirements from `.raw/` sources and leaves an open-questions list. Before the human approves Gate 1, burn that list down in a **grilling session**: the dispatcher interviews the human relentlessly — one question at a time, each with the dispatcher's recommended answer and written per the dispatcher's question rules (`skills/adlc/SKILL.md` § Writing a ruling question: sourced premises, outcome first, one decision) — walking each branch of the decision tree until shared understanding, not until a spec merely exists. Ground the questions first with an Explore pass over the affected service code so they reference real constraints, not doc assumptions (doc-first claims later falsified against code were a leading planner failure in production audits). Feed the answers back into the Gate 1 spec, and into the BA requirements when an answer changes scope. **Every ruling gets a row:** write the rulings on the epic page with the story each one lands in, and carry each into a contract row before the first build (`/adlc` Step 2.2; the census maps them when it runs). A ruling that only sits on the epic page ships unbuilt.

This is the one stage that cannot be delegated to a worker or run unattended — its whole point is converting unknown unknowns into decisions with the human before requirements freeze. Skip it only for trivial single-service changes with an empty open-questions list; a new epic, a cross-service feature, or any spec with open questions always gets one.

## Per-service agentic build

Each service is its own service: its own repo, its own Mode B code wiki, its own build pipeline. Once a spec lands in the service code wiki, the ADLC agent runs the per-service build pipeline at the service level:

0. **`scope-analyst`** (census — conditional) — before the contract is written, and **only** when the story's scope is unknown or claimed without evidence: measures the story's own claims, sweeps for the defect / change *family* rather than the reported instance, computes the blast radius, reads the source of truth, and checks what already ships. It refutes stories and dispatcher-written contract lines alike, with a command and a number behind each finding. Skipped — and expected to refuse — when the operator gave the scope by direct observation and ruling, or when the population is enumerable by reading.
1. **`feature-builder`** — implements the code + unit tests from the spec. Reads the service's own AGENTS.md for commands and conventions; runs typecheck / lint / unit green.
2. **`feature-tester`** — authors e2e specs from the feature's verification contract; keeps coverage tags honest.
3. **`feature-reviewer`** — reviews the diff (correctness, conventions, reuse, efficiency, test coverage) against the service's AGENTS.md / Don'ts; registers a review record in the wiki; returns APPROVED or CHANGES_REQUESTED. Reviews, does not fix.
4. **`feature-verifier`** — runs the contract end-to-end (see Verification below); logs pass/fail; never fixes bugs.
5. **`doc-writer`** — writes the user docs (the `writing` concern) for built + verified features.

**Review loop:** on CHANGES_REQUESTED the dispatcher loops back to `feature-builder` (code findings) and `feature-tester` (test gaps), then re-dispatches `feature-reviewer`. Cap the loop at **3 rounds**; escalate to the human if findings persist. Only on APPROVED does the pipeline proceed to verify. When dispatching the reviewer, **push the standards**: include the service's AGENTS.md conventions + Don'ts (or their exact paths) and the spec / contract in the dispatch packet alongside the diff range — an automated reviewer needs the code and the standards side by side, not a chance to skip the pull.

**Reconcile loop:** after review passes and before the next story opens, when the shipped outcome could change the remaining plan, the dispatcher re-dispatches `scope-analyst` in **reconcile** mode (diff + review record + ledger). It reports rows now unblocked / newly blocked / obsolete / wrongly scoped, whether the run order should change, and which discoveries belong to an existing row rather than a new one. It proposes; the dispatcher rules. Without this step every discovery becomes a new artifact and the plan grows sideways.

The dispatcher (ADLC agent) authors the per-feature verification contract, sequences (census ->) build -> test -> review -> verify (-> reconcile), and commits. The `adlc` skill is this dispatcher made invocable: a resumable epic loop with a `_run` ledger, checkpoint policy, and end-of-epic distillation into repo-local workers. The product wiki `features/` page links to the service spec; the `wrap-up` skill keeps both sides in sync at session end.

### Code graph grounding (when the service has one)

When a service checkout carries a graphify graph (`graphify-out/graph.json` + `wiki/code/` community pages, built by `/graphify-ingest`), workers ground their structural questions there **before** raw grep — one CLI call answers "what's connected to X", "who calls Y", "blast radius of Z" at zero LLM cost, and the `wiki/code/_COMMUNITY_*.md` pages give Bash-less workers a readable map. Two rules make this safe:

- **Map, not territory.** The graph is for *finding* things, never for *asserting* them. Any claim that lands in a spec, review finding, or test must still be confirmed in the code (Read / Grep). If the graph and the code disagree, the code wins — and the worker reports the mismatch so the dispatcher refreshes the graph.
- **Freshness is the dispatcher's job.** After each shipped feature (post-verify, pre-commit), run `/graphify-update` on the changed service so the graph and `wiki/code/` stay current for the next worker. A stale graph silently degrades every downstream dispatch; `wiki-lint` checks graph staleness against source files.

Mention the graph in the dispatch packet when it exists ("this service has `graphify-out/` — orient there first"); workers skip silently when it doesn't.

### Model split: workers draft, the dispatcher orchestrates

The workers are pinned to a fast model (Sonnet) — they draft specs, code, tests, and records. The judgment lives at the dispatcher level (the session model, e.g. Opus): it collects the context, authors contracts, sequences the pipeline, arbitrates review loops, and re-verifies claims. Don't upgrade a worker's model to fix a quality problem — tighten its inputs (spec, contract, AGENTS.md) or catch it at the dispatcher.

### Dispatcher rules (from production ADLC audits)

- **Handoffs carry evidence, and unresolved handoffs block progress.** Every worker report ends with an **Evidence** field (the exact commands run, with exit codes, where the worker runs commands) and a **Left undone** field. The evidence covers the change, not the checks the worker thought of: lint and typecheck for any source or test file it changed (a test runner is not a typechecker), the unit suite for any unit or guard test in the repo, at least one e2e spec for a change to runtime, configuration, the server's file reads or test setup; each exit code captured without a pipe (`cmd | tail` reports tail's). A handoff with a non-zero exit code, a missing or placeholder evidence field, a covering gate not run, or a Left-undone item the next stage depends on BLOCKS the pipeline: send it back, resolve it or rescope it before dispatching the next worker — never proceed past it.
- **Run the cheap gates before the verify.** Before dispatching `feature-verifier`, the dispatcher runs the service's lint, typecheck and unit gates itself, for every package the story touched. A non-zero exit goes back to the worker that owns the file; the verify waits. A one-minute run that finds an unused import is cheaper than a fifteen-minute verify that stops the run on it (`/adlc` Step 2.6).
- **Re-verify worker claims before commit.** Worker completion reports have been wrong in production ("all N updated" when two weren't; builds claimed green that weren't). Before committing, re-run the checks the worker reported green (typecheck / lint / unit at minimum, using the exact commands from its Evidence field) and spot-check one claimed mutation.
- **Check what each worker touched, not only what it reports.** The dispatcher snapshots the builder's working tree (`refs/adlc/<story>/build-<n>`, no branch commit) and runs a footprint check after every tester round: every changed or rewritten path must match the service's test globs. The reviewer sees only the final diff and the verifier checks outcomes, so an app edit the tester made and reverted is invisible to both. Mechanics: `/adlc` Step 2.3a / 2.4a, `skills/adlc/scripts/build_snapshot.py`.
- **Release-ready means every criterion, literally.** If the readiness bar says contract + review APPROVED + verifier PASS on the fingerprinted target + e2e spec green + docs updated, then a feature with any criterion pending is `conditional — <criterion> pending`, never ✅. Dashboards that contradict their own bar erode trust in every other ✅.
- **Records are pages; log entries are pointers, and the dispatcher writes them.** Verification records, review records, and retros live as their own wiki pages; `log.md` gets one line each. Production logs that carried full records inline grew past 7,000 lines and stopped being greppable. Workers never write `log.md`, `hot.md` or mission control in either wiki: they write their record page and report its path, and the dispatcher logs it. In a multi-repo vault the code wiki may keep no log at all; a worker that "appends a pointer" there creates one (seen 3×).
- **Name the instrument, not the property.** A contract or packet that names a property ("serve the built output", "prove the HTML is unchanged", "record the census") and not an instrument (`npm run preview` as wired in the e2e config, the vault's census convention) is the defect that makes workers reinvent what already ships — in one session a worker rebuilt `astro preview` as a 35-line static server (lower fidelity than the one it replaced) and built a dist snapshot/diff pipeline to prove a property true by construction. Before any bespoke harness, server, or runner, the worker reads the package manifest scripts and test configs; a bespoke instrument must justify itself in writing against the wired one.
- **A contract states outcomes, checked against the code.** A scenario says what must be observable afterwards, including what must keep working, and leaves the mechanism to the worker unless a ruling fixes it: a packet that prescribes "blur the grip at drag end" gets exactly that, and keyboard resizing breaks with it. Every UI state, message key, label, reason list or count a scenario names is checked against the code before dispatch (the loader's scope, the message catalogue, the action), or marked `[UNVERIFIED]` for the tester. When a story moves a mechanism from one source to another, the contract lists every reader of the old source as `moved here` or `deferred to <story>`, and the reviewer checks the list against the diff (`/adlc` Step 2.2).
- **Effort tracks irreversibility and blast radius, never how interesting the problem is.** The unit is the claim, not the task: "the button now has a gap" is settled by one screenshot in front of the operator (effort near zero); "nothing else moved" is invisible if wrong and deserves a mutation pin that survives in the suite. Spend on the artefact with a future; ceremony that proves things true by construction is waste at any effort level. Every dispatch carries a **done-condition** — a worker without one gold-plates a throwaway an hour past value.
- **Workers file in the vault's dialect.** Every worker that writes a record reads the vault `AGENTS.md` (structure + filing conventions) and two sibling files in the target folder first: frontmatter matching the neighbours, `[[wikilinks]]` that resolve, a filename unique across the vault (ten folders each holding `census.md` make every `[[… census]]` link resolve to nothing), filed under **this** story's trace ID, linked from the ledger row that motivated it. A record nobody can find is a lint finding, not a record. Query the wiki (prior censuses, verification records, the run ledger's Carry-forward) before re-measuring — a recorded figure is a claim to check cheaply, not a reason to skip measurement, but checking is an order of magnitude cheaper than deriving.
- **Keep the board current at every stage transition.** The product wiki's `meta/mission-control.md` is the operator's async view (see [`mission-control.md`](mission-control.md)). When you dispatch a worker, accept a handoff, record a verdict, or route a FAIL, update the affected board row in the same breath as the record — one row edit, not a rewrite. A board the operator can't trust mid-flight defeats its purpose; it is a derived view, so on any disagreement the records win.
- **File defects where they belong — and put the fix on the backlog.** Verifier FAILs and post-ship bugs go to `bugs/` (qa concern) with a log pointer — not inline-only in `log.md`. An empty `bugs/` folder next to a log full of FAIL entries means the routing broke, not that there were no bugs. Every FAIL additionally becomes a backlog item (a story / task in the product wiki's `user-stories/` or sprint plan) tracing to the bug page and the exact broken assertion, and the feature flips to `conditional — fix pending` until a re-verify PASSes; a FAIL that exists only as a record never gets scheduled. `ENV_MISMATCH` / `NEEDS_SIGN_IN` are operational blocks, not defects: fix the environment or authenticate, then re-dispatch the verifier — never file them as bugs or let them silently drop the feature from the queue.

## Verification (operator's toolset)

Features are verified by `feature-verifier` with the same tools the agent operator has, not a bespoke harness:

- **Local run:** `docker compose up` the service stack (dev server + dependencies). Verify against localhost.
- **E2E:** the chrome-devtools MCP. Use `navigate_page` + `evaluate_script` to assert computed styles, DOM state, network calls, and console hygiene; `take_screenshot` for evidence. Mirrors the `chrome-ui-verify` pattern.
- **Backend / API:** the service's own test suite (unit + integration + e2e) run via the project's commands.
- **Record:** file a verification execution note (per test case: objective, observed value, PASS / FAIL) and link it from the feature page. The verifier never fixes bugs; it logs and stops.

### Milestone verification (holistic)

Per-feature verification proves each feature against its own contract; it never exercises the seams between features, and its PASSes age as the environment drifts. At each milestone boundary (sprint close, release candidate, or every ~5 shipped features), the dispatcher authors a **milestone verification contract** and dispatches `feature-verifier` with it:

- **Cross-feature journeys:** 2–4 end-to-end scenarios that chain shipped features through their seams (feature A's output is feature B's input) — the paths no per-feature contract covers.
- **Re-verify on a fresh target:** bring the stack up clean (fresh `compose up`, seeded from scratch) and re-run the per-feature contracts of features shipped since the last milestone. A PASS that only ever ran on a lived-in dev environment is unproven — production audits found environment-dependent PASSes that evaporated on clean stacks.
- **Full e2e suite, unscoped** — not the per-feature scoped runs.

Failures route exactly like per-feature FAILs (bug page + backlog item). A release with the holistic pass un-run is `conditional — milestone verify pending`, never ✅.

## Where ADLC ends: the verified commit

The pipeline (census →) build → test → review → verify (→ reconcile) → document ends at a **verified commit** on a feature branch. Push, PR, deploy and checking a deployed revision are a separate, **optional** stage run by the `devops` worker, and only on the operator's word for each dispatch (`adlc` Step 2.7a). `feature-verifier` checks the working tree or local stack; `devops` checks a deployed revision. Infrastructure, secrets, IAM and rollbacks stay with the operator. Teams that want automated deploys can put the playbook's hooks-as-gates in front of `devops`; the plugin does not ship them.

## Headless entry (Stage 6 seam: designed, not built)

Every ADLC run starts from an operator session today. A finding from production re-enters the pipeline through the same route as a verifier FAIL: a `bugs/` page plus a backlog item tracing to it. A headless entry reuses that route:

- **Trigger:** a schedule, a webhook or a channel message. Deciding that something is wrong stays deterministic and outside the model (an alert rule, a failed check, an error-rate threshold).
- **Run:** a bounded, read-only diagnosis (logs, the code wiki, the graph). It writes no code and commits nothing.
- **Output:** a `bugs/` page and a backlog item, filed like a verifier FAIL. The backlog item is the intent; no `intent.md`.
- **Then:** the operator triages it from the board, and `/adlc` picks it up like any other story.

Build it only when a project has a metrics store to trigger from, on the Agent SDK branch.

## Diagrams and HTML export

Tech documentation uses **Mermaid**: inline code blocks in the spec Markdown, which render natively in Obsidian and in HTML. For a shareable rendered copy of a tech doc, HTML-export it into `.raw/exports/` (for example via `npx @mermaid-js/mermaid-cli` or a Markdown-to-HTML step). Reserve **PlantUML** for the formal export bundle that ships with `ba-suite` Office docs (see [`ba-suite-pipeline.md`](ba-suite-pipeline.md)).

## Export to the tracker

The `ba-export` skill (with `ba-export-subagent`) drives export: wiki to Office in `.raw/exports/`, then optionally to the team's tracker via MCP (see [`mcp-setup.md`](mcp-setup.md) § ADLC MCP toolset). ClickUp hierarchy: Project to Space, Objective to Folder, Deliverable to List, Epic to Task, Story to Subtask, Task to Checklist Item. Keep a manifest mapping wiki pages to task IDs so re-export is idempotent.
