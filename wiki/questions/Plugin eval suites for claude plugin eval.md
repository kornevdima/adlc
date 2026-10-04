---
type: synthesis
title: "Plugin eval suites for claude plugin eval"
created: 2026-10-02
updated: 2026-10-02
tags:
  - plugin
  - evals
  - adlc
  - workers
status: open
related:
  - "[[Review the ADLC flow against the AI-Native SDLC Playbook]]"
  - "[[Skills Field Eval 2026-10]]"
---

# Plugin eval suites for claude plugin eval

**Opened from** playbook review ruling 4 (operator, 2026-10-02): run evals **locally only**, before each version bump. No CI.

## The gap

- `claude plugin eval` reads cases from `evals/<case>/prompt.md` + `graders/*.md` (optional `case.yaml`, `schema_version: "1.1"`) under the plugin root, or the dir set by `plugin.json` `experimental.evals` (CLI `--help` and https://code.claude.com/docs/en/plugin-evals.md, 2026-10-02). The repo has no top-level `evals/`.
- The 18 `skills/<name>/evals/evals.json` files use the skill-creator format (`prompt`, `expected_output`, `assertions`). Most have empty `assertions`, and `claude plugin eval` does not read them.
- `adlc` and the 14 worker agents have no evals at all. They changed most in the 2026-10-02 fixes.

## Proposed work

1. Scaffold `evals/` with `claude plugin eval init`. Start with the cases that pin today's fixes:
   - CONTEXT LOAD routing (`/adlc:wiki implement US-042` reads hot.md and does not start a run);
   - a verifier FAIL is never marked delivered by `wrap-up`;
   - the epic close relinks before it deletes the ledger.
2. Convert the skill-creator suites that have real expectations; drop the empty ones.
3. Feed cases from the field: a defect that escaped the verifier (Step 4.4's upstream route) becomes a case.

## Progress (2026-10-02)

Step 2 done: the 12 non-graphify skill-creator suites (22 cases) are converted to `evals/<skill>/<case>/` with layered fixtures in `evals/_fixtures/` (`use.sh`, `@commit`, `@large`), and their `evals.json` files are removed. How to run: `evals/README.md`.

- Validated: the 10 `fast` cases pass, after grader fixes (about $2 for the set at 1 run each). Not yet run: the slow and network cases (autoresearch, wiki-ingest batch, ba-export, project-profile, wiki scaffold, wrap-up, wiki-lint).
- Format facts learned: `scaffold_script` resolves from the case dir and runs in the workspace; "never called" needs `min: 0` + `max: 0`; slash prompts make no `Skill` call; `---` inside a regex breaks frontmatter; `llm` graders with `focus: trace` can miss content in long traces.
- Skill gap the evals found: `obsidian-markdown` does not know the vault's `> [!contradiction]` callout (used by wiki-ingest and wiki-lint), so "add a contradiction callout" lands as `[!contradiction]` only some of the time (1 of 3 runs passed).
- Left: graphify (5 json cases + the G1–G5 runner), the product-management-layer E1–E8 runner, and step 1 (new cases for `adlc`, workers, CONTEXT LOAD, wrap-up shipping, epic-close relink).

## Backlog (next session)

1. **Run the 12 slow cases** once (`claude plugin eval . --scaffold --allow-tools Write Edit Bash --ablation none --no-publish -j 4`, about $10–20). Needs network (autoresearch) and a .docx library (ba-export). Fix graders that fail on correct behaviour; file real skill defects.
2. **Fix `obsidian-markdown`:** document the vault's `> [!contradiction]` callout (used by wiki-ingest and wiki-lint). The eval `obsidian-markdown/contradiction-callout` pins it.
3. **Convert graphify:** the 5 `evals.json` cases plus the G1–G5 runner checks (`skills/graphify-ingest/evals/run-evals.sh`), with a scaffold that sets up graphify on the demo-app fixture. Tag `needs-graphify`.
4. **Convert product-management-layer** E1–E8 (regex must / must-not lists map to `regex` graders; the dated registry fixture becomes a scaffold).
5. **New cases (step 1 above):** `adlc` routing and CONTEXT LOAD, wrap-up never ships on a verifier FAIL, epic-close relink, builder/tester ordering. First two `adlc` cases landed 2026-10-04: `adlc/ruling-cites-record` and `adlc/ruling-outcome-first` on the `adlc-vault` fixture ([[Dispatcher rules for writing ruling questions]]). They pass, but so does the baseline (Δ 0); reuse the fixture for the routing cases.

## Release step (in force now)

Before a version bump: `claude plugin eval . --no-publish` (README § Active development). The converted suite is what runs today. Run it with your normal Claude Code credentials; no CI secret is needed.

## Done when

- `evals/` has cases for `adlc` routing, `wrap-up` shipping and the epic-close relink;
- `claude plugin eval . --no-publish` passes locally at the default threshold.
