---
type: concept
title: "Skills Field Eval 2026-10"
created: 2026-10-02
updated: 2026-10-02
confidence: medium
tags:
  - concept
  - adlc
  - field-evidence
  - skills-eval
  - cross-host
status: developing
related:
  - "[[ADLC Field Review Findings]]"
  - "[[Configurable subagent models per host]]"
  - "[[Operator profile - learn engagement style from corrections]]"
  - "[[Integrate the wiki toolset into the ADLC workers]]"
  - "[[Plugin Hooks]]"
---

# Skills Field Eval 2026-10

A review of three real operator sessions, read to evaluate the plugin's skills, agents and hooks rather than the work done in those sessions. Project specifics are left out on purpose.

| Session | Host | Shape |
|---|---|---|
| A | Claude Code | ~2 h on a new product with no code yet: scaffold, then decisions, then requirements, then Gate 1 architecture |
| B | Copilot CLI | ~43 min on an existing backend service: a wiki question, then a plan, then "implement it" through builder, tester, reviewer, verifier and graph update |
| C | Copilot CLI | ~56 min: a debugging request sent through `/adlc:wiki`, then infrastructure questions |

Method: four parallel read-only reviewers, one per transcript slice. Each finding was classified against the known patterns (K1–K9, listed at the end). Claims about the plugin source were checked against the repo.

## Confirmed patterns

- **K8, hardcoded worker model (strong, B).** The dispatcher passed `model: sonnet` and the host rejected it. The main thread then offered to do the build inline, and the operator stopped that. The operator believed `/adlc` already had a fallback rule; it does not. The retry hardcoded a different vendor's model, so it was just as specific to one host. A plugin reload was tried first and changed nothing. The fix belongs to [[Configurable subagent models per host]]. Separately, `technical-planning.md` still says workers are "pinned to a fast model (Sonnet)" (checked).
- **K2, handoff seams (strong, A and B).**
  - A BA worker wrote 5 of 57 requirements against a scope level that an earlier decision had ruled out. A resumed architecture worker kept a placement from its original brief and missed a ruling made after dispatch. The dispatcher's own review caught both.
  - In B, no verification contract existed, so the verifier invented its own scenarios.
- **K1, gates are real but environment-sensitive (strong, B).** The reviewer caught a real documentation defect. The verifier caught two stale wiki references. Its first FAIL, though, was an environment mismatch (see N4), not a code fault.
- **K3, records as pages (strong, B and C).** Verification and review records were filed as pages with fingerprints, which worked. But:
  - a plan was marked delivered while the verifier still said FAIL;
  - a FAIL record was overridden without re-verifying;
  - in C, two reusable findings were never filed.
- **K5, main-thread marathons (medium, A and B).**
  - In A, every decision turn (new decision page, supersede chain, index, mission control, profile, hot, log) ran on the main thread, taking 6–19 minutes per turn. There were only 2 worker dispatches in 2 hours.
  - In B, about 150 reads and searches stayed on the main thread for a small change, and about 13 of 42 minutes went to repairing tooling.
- **K6, reinventing capability (medium, A).** The main thread wrote ad-hoc dead-wikilink checkers about 8 times and trimmed hot.md against its word budget over several passes.
- **K7, corrections (strong, A and C).**
  - In A, the operator profile captured corrections verbatim, with class and lesson. That is working as designed.
  - In C (no `/adlc`), two operator corrections went unrecorded: a capability stated as fact without checking the configuration, and an invented UI option.

## New findings

| ID | Finding | Evidence | Proposed change |
|---|---|---|---|
| N1 | The SessionStart hook in `hooks/hooks.json` has a `type: "prompt"` entry that Claude Code rejects for that event. The error shows at every startup (checked) | strong | Remove the prompt entry; the command hook already loads hot.md |
| N2 | "Implement it" ran without `/adlc`: the main thread dispatched the workers itself, with no run ledger, census or contract. **This is the manual use case below, not a routing failure.** The real defects are smaller: a plan was marked delivered while the verifier said FAIL, and the workers expected a contract nobody wrote | strong | In manual mode, workers fall back to the plan's acceptance criteria when no contract exists; never mark a plan delivered without a verifier PASS; offer `/adlc` once, never force it |
| N3 | `/adlc:wiki` is used as a "load my context" prefix for tasks that are not wiki operations (confirmed by the operator). The router has no row for that, so hot.md was never read and nothing was offered for filing | strong | Add a "context load" row: see the manual use case below |
| N4 | `feature-verifier` only knows how to bring up a docker compose stack (checked). A service tested against a remote or port-forwarded environment got a false FAIL. The verifier also has no way to say "working tree verified, not deployed" | strong | Read the e2e topology from the service's instructions file; add a target class (working tree / local stack / deployed revision) and an ENV_MISMATCH status |
| N5 | The service used CLAUDE.md, not AGENTS.md. `feature-builder` handles that, but `feature-tester` and `feature-verifier` do not (checked); one worker read a sibling repo's AGENTS.md instead | medium | Every worker preamble should say "AGENTS.md, CLAUDE.md or .github/copilot-instructions.md" |
| N6 | The dispatch prompt contradicted the worker contract: it asked the builder to update the wiki, which the builder never does. Log-line ownership differs between the verifier spec and the orchestrator | medium | Template a dispatch prompt per worker in the adlc skill; name one owner for each log line |
| N7 | The planning references and `architecture-subagent` assume service code wikis already exist. A product with no code had no home for system- or module-level architecture. The operator set the order "architecture gates before stories" and chose a folder for it | strong | Add a project-level solution-architecture path and state that the gates come before story decomposition |
| N8 | Proposals were written into decision prose as if they were rulings | strong | Decision pages keep proposals under an "Open / Proposed" section only |
| N9 | Title-based wikilinks against kebab-case filenames broke path lookups. A plan was filed in `questions/` because Mode B has no folder for plans. Scaffold pages linked by title had no `aliases:` | medium | Document the title-to-filename rule; add a plans location; the scaffold writes `aliases:` |
| N10 | The dispatcher read plugin references from a sibling dev checkout under an absolute path, not from the installed plugin | medium | Reference plugin files through the plugin-root variable |
| N11 | graphify `regenerate.py` rewrites all of hot.md (checked) and inserts its log line inside an existing entry, labelled "ingest" on an update run | strong | Replace only a marked graph block in hot.md; write a separate dated log entry with the right label |
| N12 | graphify-update crashed (KeyError: community members missing from the graph) and needed an inline patch. The label-matching threshold is 0.6 in one place and 0.7 in another (checked) | strong | Filter community members against the graph before regenerate runs; pick one threshold |
| N13 | graphify-update ran a full rebuild through the incremental path: 100% of nodes pruned, 0 labels inherited. Its change detection included an untracked transcript file | strong | Detect large drift and recommend graphify-ingest instead; skip untracked files and transcript exports |
| N14 | When the operator named a tool (the IDE MCP), the agent used shell instead and did not say why | strong | Operator rule: use the tool the operator names, or say why not |

## Use case: manual work with wiki context

Confirmed by the operator: not all work goes through the ADLC pipeline. An engineer often takes a ready story (for example, from the team's tracker) and implements it by hand, using `/adlc:wiki <task>` only to load project context. Sessions B and C are this shape. Nothing in them is a misuse; the gap is that the plugin has no defined behaviour for this mode.

What the plugin should do in this mode:
1. **Load context once at the start.** Read hot.md, grep the index and the code wiki for the story's topic, and read the matching module, flow and decision pages. Report what is known in a few lines, then hand control to the engineer.
2. **Stay out of the way.** No run ledger, census, contract or board. The engineer drives. Workers are optional helpers when asked for, dispatched with the same portability rules (model, instructions file, environment).
3. **Keep the wiki honest at the end.** Offer `save` for reusable findings, record operator corrections in the operator profile, update pages the change made stale, and refresh hot and log. `wrap-up` already covers most of this; the context-load row should point to it.
4. **Offer `/adlc` once.** Only when the work clearly fits a story pipeline, and only as a suggestion.

Open question: whether to give this mode its own entry point (for example `/adlc:wiki context <story>`) or keep it as the router's fallthrough.

## What worked

- **Grilling gate (A).** It followed `technical-planning.md` exactly: one question at a time, each with a recommendation. 10 of 11 recommendations were accepted quickly, and items flagged as unsourced went to the operator.
- **Dispatcher review of worker output (A).** It caught real drift before the operator saw it (K2 above).
- **Wiki hygiene when a skill was loaded.** Operator messages were saved verbatim to `.raw/`. Superseded decisions kept their history. Filed answers had full frontmatter and index/log/hot updates. Superseded plans were archived, not deleted.
- **Workers on Copilot (B).** Once the model problem was resolved they ran cleanly in scope, with exit-coded evidence and honest "left undone" lists. Graph labelling ran in a subagent, which kept the main context lean.

## Priority (proposed)

1. N1 (one-line fix) and the K8 steps 1–4 in [[Configurable subagent models per host]].
2. N3 + the manual use case: a context-load row in the wiki router, with `save` / corrections / `wrap-up` at the end. N2's two real defects (delivered on FAIL, no contract fallback) go with it.
3. N4 + N5 + N6: worker portability across services and hosts.
4. N11–N13: graphify-update reliability.
5. N7–N10, N14: conventions.

## Known patterns referenced

K1 workers catch real bugs, gates are real · K2 handoff seams lose context · K3 records as pages · K4 duplication in the shared layer (not exercised) · K5 cost follows the shape of the ask · K6 workers reinvent wiki capability · K7 learn engagement from corrections · K8 hardcoded subagent model · K9 BA tables (not exercised). K1–K5 come from [[ADLC Field Review Findings]]; K6–K9 from the open tasks and the 2026-09-16 fix in [[log]].
