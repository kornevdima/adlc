---
type: synthesis
title: "Integrate the wiki toolset into the ADLC workers"
created: 2026-08-25
updated: 2026-09-03
tags:
  - agents
  - wiki
  - adlc
  - toolset
status: open
related:
  - "[[LLM Wiki Pattern]]"
  - "[[Hot Cache]]"
  - "[[Compounding Knowledge]]"
  - "[[Context Engineering for Coding Agents]]"
  - "[[AGENTS.md]]"
---

# Integrate the wiki toolset into the ADLC workers

**Opened from live use**, not from design review — surfaced during a delivery session on a static-site content project on
2026-08-25 where the operator caught three separate instances of workers reinventing capability the
system already ships.

## The problem

The ADLC workers in `agents/` — `scope-analyst`, `feature-builder`, `feature-tester`,
`feature-reviewer`, `feature-verifier`, `doc-writer` — all **write into an Obsidian vault**, and none
of them has the wiki toolset available. They have `Read`/`Grep`/`Glob`/`Write`/`Edit` and, for some,
`Bash`. They do not have the `wiki-query`, `wiki-lint`, or `obsidian-markdown` skills, and their
prompts do not tell them the vault has conventions at all.

Three consequences, all observed in one session:

1. **Re-measuring what the vault already records.** A `scope-analyst` census spent a browser session
   deriving a figure that a prior census had already measured and filed. Nothing pointed it at the
   prior record. (A recorded figure is a *claim to check*, not a reason to skip measurement — but
   checking one is an order of magnitude cheaper than deriving it.)
2. **Records that do not resolve.** Workers author `[[wikilinks]]` and frontmatter by pattern-matching
   whatever file they happened to read. That project's vault already carries a lint finding where ten
   evidence folders each hold a file named `census.md`, so every ledger link in the
   `[[<story> census]]` style resolves to nothing.
3. **Filing in the wrong lineage.** A census filed itself under the trace ID of an adjacent story
   because that is where a *previous, differently-scoped* fix had been filed. The orchestrator had to
   rename it and rewrite its internal references by hand.

## The deeper pattern — it is not only the wiki

The same session produced two other instances of the identical failure, which is why this is worth
fixing at the framework level rather than as a docs tweak:

- A worker **reimplemented `astro preview`** as a 35-line static file server with a hand-maintained
  MIME table, in a repo whose `playwright.config.js` **already** declares
  `webServer: 'npm run build && npm run preview'`. The bespoke server was also *lower fidelity* than
  the one it replaced — different 404s, different headers — which defeats the stated reason it existed.
- A worker **built a dist snapshot/diff pipeline** to prove a one-declaration CSS change had not
  altered any HTML — a property true by construction, and already covered by a geometry sweep.

> [!important] **The generalisation: a worker handed a PROPERTY will build an instrument to satisfy it.**
> Contracts and worker prompts that name a property ("serve the built output", "record the census")
> and not an instrument (`npm run preview`, "the vault's census convention") are the actual defect.
> **Name the instrument.**

## Proposed work

1. **Give the wiki-writing workers the wiki toolset.** At minimum `obsidian-markdown`; `wiki-query`
   for the read-before-measure step. Decide whether this is a `tools:` frontmatter change, a bundled
   reference under `skills/wiki/references/`, or prompt-level instruction — the workers are dispatched
   from a vault root that may not resolve repo-local skills.
2. **Add a "use the shipped instrument" clause to every worker.** Before building any harness, server,
   or runner: read `package.json` scripts and the test configs. A bespoke instrument must justify
   itself *in writing* against the wired one. — **DONE for `scope-analyst` 2026-08-25**; the other
   five still need it.
3. **Add a "when NOT to run" gate to `scope-analyst`.** A census resolves *unknown* scope; it is a
   category error against a scope the operator has already given by direct observation and ruling.
   — **DONE 2026-08-25.**
4. **Teach record-filing as a convention, not an improvisation.** Read two sibling files before
   writing a new one; the folder's naming pattern is the spec; an orphan page is a `wiki-lint` finding.
5. **Consider a vault-manifest a worker can read** — folder → artefact-type → naming convention —
   so filing is a lookup rather than an inference. This is the piece most likely to make items 1 and 4
   stick, and the least designed so far.

## Open questions

- Do workers dispatched from a vault root resolve plugin skills at all, or must the orchestrator
  inline the guidance into the dispatch packet? The ADLC skill already documents this problem for
  repo-local worker bindings; **the same constraint probably applies to skills and has not been
  checked.**
- Is `wiki-query` cheap enough to make "query before you measure" a default step, or does it need a
  budget?
- Does giving analysis workers more read-surface undermine the division of labour the ADLC skill
  depends on — workers carry raw material, the dispatcher carries records? **Reading the vault is not
  the same as reading raw artefacts, but the boundary is worth stating explicitly** before it erodes.

## Confirmed in live use, 2026-08-25 — two more integration gaps, both measured

A `ba-suite-subagent` run on the same project vault surfaced two defects that belong to this task
rather than to that project:

1. ⚠ **`skills/wiki/references/ba/` DOES NOT EXIST.** The `ba-suite-subagent` frontmatter promises it
   applies *"the bundled BA method docs (`skills/wiki/references/ba/`, no external plugin)"* — the
   worker reported the path absent and fell back to inferring conventions from neighbouring vault
   files. **It produced good work anyway, which is exactly what makes this dangerous:** the agent's
   own description states a capability the plugin does not ship, so nothing fails loudly. Either
   bundle the method docs or stop promising them.
2. **`wiki-lint` checks requirement → story → test, but not story-claims-feature →
   feature-note-names-story.** Same shape, unchecked. Measured consequence in one vault: **85 of 126
   story pages (67%) were not named in their own feature's note**, and **10 of 12 notes were stale**.
   The 2 current notes were current only because exactly one story claims each — **currency correlated
   with feature size; no note stayed current through being maintained.** An unchecked invariant does
   not decay gradually, it decays completely and invisibly.

**And a law worth carrying into the lint design:** three separate figures in that vault were
percentages or totals whose **denominator** had moved — an `origin link: 106/106 (100%)` measured
against a register that had grown to 108 rows, a staleness marker naming 14 absent rows when 17 were
absent, a test total corrected in a change record written the day after the figure it corrects.
⚠ **A percentage whose denominator is stale reads as complete.** Prefer re-derivation over increment,
and make the lint report the denominator alongside the ratio.

## Resolution log — 2026-09-03 (plugin 1.0.1, uncommitted at time of writing)

**Mechanism chosen for item 1**: prompt-level clauses in every worker + a **filing-conventions table in the vault `AGENTS.md`** (the manifest from item 5), not a `tools:` change and not a bundled reference. Reasons: the workers run from the vault root, so the one file they can always find is the vault's own `AGENTS.md`; a bundled reference has the same plugin-root resolution problem that produced the `references/ba/` finding below; and whether the Skill tool resolves plugin skills inside a subagent is unverified. The clause tells them to read that table plus two sibling files, query before re-deriving, write Obsidian-flavoured Markdown, keep basenames unique, and file under the current story's trace ID.

| Item | Status |
|---|---|
| 1 wiki toolset for wiki-writing workers | **done** — "Filing in the vault" section in `feature-tester`, `feature-reviewer`, `feature-verifier`, `doc-writer` (scope-analyst already had it); `technical-planning.md` dispatcher rule "workers file in the vault's dialect" |
| 2 "use the shipped instrument" clause | **done** — `feature-builder`, `feature-tester` (full clause), `feature-verifier` (stack-as-wired variant); `feature-reviewer` gained review dimension 7 *instrument reinvention*; dispatcher rule "name the instrument, not the property" in `technical-planning.md` and in `/adlc` Step 2.2 |
| 3 "when NOT to run" gate | done 2026-08-25; `/adlc` Step 2.1a now carries the same gate on the dispatcher side, and a Constraints line names over-correction |
| 4 record-filing as convention | **done** — inside the filing clause + lint check 12c (ambiguous record names) |
| 5 vault manifest | **done** — `wiki` skill AGENTS.md template gained a **Filing conventions** table (folder → artefact type → filename pattern → linked from), incl. a `census/` convention the scope-analyst now defaults to |
| `references/ba/` "does not exist" | **root cause found, fixed** — the docs exist (verified in the installed cache `~/.claude/plugins/cache/adlc-marketplace/adlc/1.0.1`, at `c9bed17`); the agent prompts cited `skills/wiki/references/ba/` as a bare relative path, which the worker resolved against the vault root. `ba-suite-subagent`, `ba-export-subagent`, `architecture-subagent` now carry a "where the bundled docs live" paragraph (`$CLAUDE_PLUGIN_ROOT`, then Glob under `~/.claude/plugins/**`, then host skill dirs) and must report `INFERRED` loudly if they still cannot find them |
| story → feature back-link lint | **done** — `wiki-lint` check 12a (both directions), 12b (stale denominators: report the denominator beside the ratio), 12c (ambiguous basenames) |

**Also landed from the same session's evidence**: `scope-analyst` wired into `/adlc` (Step 1a census, Step 8a reconcile), `permissions.md`, `modes.md`, `technical-planning.md`, wiki-faq, README, root AGENTS.md.

**Remaining (open)**:
- Field-validate on the next delivery run that a worker dispatched from a vault root actually reads the filing table (the clause is prompt-level; nothing enforces it — a `wiki-lint` pass after the run is the check).
- `wiki-query` budget for "query before you measure" — unanswered; the clause points workers at `hot.md` / `index.json` / prior records directly rather than at the skill.
- Division-of-labour boundary: workers now read *vault records*; they still never read raw worker artefacts. Stated in the clause; watch for erosion.
- **Field test of `scope-analyst` as the context-offload worker (operator decision 2026-09-03: keep the current wiring, test first).** The operator's intent is that the sub-agent investigates requirements before implementation so the main thread stays lean. Four candidate changes were identified and deliberately *not* applied pending the test: (1) the worker's gate bullet "population enumerable by reading, and has been read" and `/adlc` Step 1a both assume the dispatcher reads source itself — the intended choice is "no investigation (ruling)" vs "scope-analyst investigates, narrowed if small", never "dispatcher reads"; (2) Step 1a is conditional on unknown scope rather than the default whenever a story needs any code investigation; (3) the grilling gate's Explore pass in `technical-planning.md` still grounds itself on the main thread — an epic-level census could replace it; (4) the census report has no length cap (other workers: 200 words). **Watch in the run:** how many source files the dispatcher opens itself before a contract (target: none); whether a census dispatch was refused or narrowed and on what grounds; report length vs the census page; whether the grilling questions were grounded by the dispatcher's own reading.

