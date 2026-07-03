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

## Per-service agentic build

Each service is its own service: its own repo, its own Mode B code wiki, its own build pipeline. Once a spec lands in the service code wiki, the ADLC agent runs the per-service build pipeline at the service level:

1. **`feature-builder`** — implements the code + unit tests from the spec. Reads the service's own AGENTS.md for commands and conventions; runs typecheck / lint / unit green.
2. **`feature-tester`** — authors e2e specs from the feature's verification contract; keeps coverage tags honest.
3. **`feature-reviewer`** — reviews the diff (correctness, conventions, reuse, efficiency, test coverage) against the service's AGENTS.md / Don'ts; registers a review record in the wiki; returns APPROVED or CHANGES_REQUESTED. Reviews, does not fix.
4. **`feature-verifier`** — runs the contract end-to-end (see Verification below); logs pass/fail; never fixes bugs.
5. **`doc-writer`** — writes the user docs (the `writing` concern) for built + verified features.

**Review loop:** on CHANGES_REQUESTED the dispatcher loops back to `feature-builder` (code findings) and `feature-tester` (test gaps), then re-dispatches `feature-reviewer`. Cap the loop at **3 rounds**; escalate to the human if findings persist. Only on APPROVED does the pipeline proceed to verify. When dispatching the reviewer, **push the standards**: include the service's AGENTS.md conventions + Don'ts (or their exact paths) and the spec / contract in the dispatch packet alongside the diff range — an automated reviewer needs the code and the standards side by side, not a chance to skip the pull.

The dispatcher (ADLC agent) authors the per-feature verification contract, sequences build -> test -> review -> verify, and commits. The product wiki `features/` page links to the service spec; the `wrap-up` skill keeps both sides in sync at session end.

### Model split: workers draft, the dispatcher orchestrates

The workers are pinned to a fast model (Sonnet) — they draft specs, code, tests, and records. The judgment lives at the dispatcher level (the session model, e.g. Opus): it collects the context, authors contracts, sequences the pipeline, arbitrates review loops, and re-verifies claims. Don't upgrade a worker's model to fix a quality problem — tighten its inputs (spec, contract, AGENTS.md) or catch it at the dispatcher.

### Dispatcher rules (from production ADLC audits)

- **Handoffs carry evidence, and unresolved handoffs block progress.** Every worker report ends with an **Evidence** field (the exact commands run, with exit codes, where the worker runs commands) and a **Left undone** field. A handoff with a non-zero exit code, a missing evidence field, or a Left-undone item the next stage depends on BLOCKS the pipeline: resolve it or rescope it before dispatching the next worker — never proceed past it.
- **Re-verify worker claims before commit.** Worker completion reports have been wrong in production ("all N updated" when two weren't; builds claimed green that weren't). Before committing, re-run the checks the worker reported green (typecheck / lint / unit at minimum, using the exact commands from its Evidence field) and spot-check one claimed mutation.
- **Release-ready means every criterion, literally.** If the readiness bar says contract + review APPROVED + verifier PASS on the fingerprinted target + e2e spec green + docs updated, then a feature with any criterion pending is `conditional — <criterion> pending`, never ✅. Dashboards that contradict their own bar erode trust in every other ✅.
- **Records are pages; log entries are pointers.** Verification records, review records, and retros live as their own wiki pages; `log.md` gets one line each. Production logs that carried full records inline grew past 7,000 lines and stopped being greppable.
- **File defects where they belong.** Verifier FAILs and post-ship bugs go to `bugs/` (qa concern) with a log pointer — not inline-only in `log.md`. An empty `bugs/` folder next to a log full of FAIL entries means the routing broke, not that there were no bugs.

## Verification (operator's toolset)

Features are verified by `feature-verifier` with the same tools the agent operator has, not a bespoke harness:

- **Local run:** `docker compose up` the service stack (dev server + dependencies). Verify against localhost.
- **E2E:** the chrome-devtools MCP. Use `navigate_page` + `evaluate_script` to assert computed styles, DOM state, network calls, and console hygiene; `take_screenshot` for evidence. Mirrors the `chrome-ui-verify` pattern.
- **Backend / API:** the service's own test suite (unit + integration + e2e) run via the project's commands.
- **Record:** file a verification execution note (per test case: objective, observed value, PASS / FAIL) and link it from the feature page. The verifier never fixes bugs; it logs and stops.

## Diagrams and HTML export

Tech documentation uses **Mermaid**: inline code blocks in the spec Markdown, which render natively in Obsidian and in HTML. For a shareable rendered copy of a tech doc, HTML-export it into `.raw/exports/` (for example via `npx @mermaid-js/mermaid-cli` or a Markdown-to-HTML step). Reserve **PlantUML** for the formal export bundle that ships with `ba-suite` Office docs (see [`ba-suite-pipeline.md`](ba-suite-pipeline.md)).

## Export to the tracker

The `ba-export` skill (with `ba-export-subagent`) drives export: wiki to Office in `.raw/exports/`, then optionally to the team's tracker via MCP (see [`mcp-setup.md`](mcp-setup.md) § ADLC MCP toolset). ClickUp hierarchy: Project to Space, Objective to Folder, Deliverable to List, Epic to Task, Story to Subtask, Task to Checklist Item. Keep a manifest mapping wiki pages to task IDs so re-export is idempotent.
