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

## Release step (in force now)

Before a version bump: `claude plugin eval . --no-publish` (README § Active development). Until this task lands the run finds no cases and exits 1 (docs: `plugin-evals`, exit codes), so the step is a known red until the first suite exists. Run it with your normal Claude Code credentials; no CI secret is needed.

## Done when

- `evals/` has cases for `adlc` routing, `wrap-up` shipping and the epic-close relink;
- `claude plugin eval . --no-publish` passes locally at the default threshold.
