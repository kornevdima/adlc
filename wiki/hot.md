---
type: meta
title: "Hot Cache"
updated: 2026-10-02T23:30:00
tags:
  - meta
  - hot-cache
status: evergreen
related:
  - "[[index]]"
  - "[[log]]"
  - "[[Plugin eval suites for claude plugin eval]]"
  - "[[Skills Field Eval 2026-10]]"
  - "[[AI-Native SDLC Playbook vs ADLC]]"
  - "[[Integrate the wiki toolset into the ADLC workers]]"
---

# Recent Context

Navigation: [[index]] | [[log]]

## Last Updated

**2026-10-02 (session: two releases + evals)**:
- **1.0.5 (`b2b1d45`)**:
  - builder and tester take turns on shared files, and workers undo their own temporary edits instead of restoring snapshots;
  - `relink.py` runs at the epic close, and `permissions.md` covers auto mode;
  - manual mode gets a CONTEXT LOAD route, a contract fallback, and a rule that a feature counts as shipped only when verified.
- **1.0.6 (`8a23c39`)**: the playbook review closed with 8 rulings:
  - non-engineers drop requests into `.raw/intake/`;
  - each service gets `reviews/_policy.md`;
  - evals run locally only;
  - distill proposes only repeats, each with a named target, and Standing rulings keep only cross-story rules;
  - a new optional `devops` worker handles push, PR, deploy and the deployed-revision check, only on the operator's word;
  - the README maps playbook terms to ADLC;
  - time metrics are deferred.
- **K8 postponed.**
- **2026-10-04 (uncommitted):** [[Dispatcher rules for writing ruling questions]] is resolved. `/adlc` Step 2 now has § Writing a ruling question (sourced premises, outcome first, one decision). Two `evals/adlc/` cases on the `adlc-vault` fixture; the baseline passes too (Δ 0). To do after the next release: remove the vault-a profile line.
- **Evals (uncommitted):** 22 skill cases converted to `claude plugin eval` under `evals/`, with layered fixtures. The `fast` set passes. See `evals/README.md`.

## Key Recent Facts

- `claude plugin eval` facts:
  - `scaffold_script` runs in the case workspace;
  - a "never called" check needs `min: 0` and `max: 0`;
  - a slash-command prompt makes no `Skill` tool call;
  - `---` inside a regex breaks the frontmatter;
  - a judge reading the trace can miss content, because the hook output comes first.
- Auto mode ignores `autoMode` in project settings. A narrow `permissions.allow` rule skips the classifier.
- Claude memory is empty for the vault-a and the service checkout projects. Their operator profile file is the only store. The vault-a profile was cleaned on 2026-10-03: Standing rulings went from 122 lines to 8 cross-story rules (`(commit)`).
- 15 agents now (`devops` added, with no `model:`).

## Active Threads

- **Evals backlog** ([[Plugin eval suites for claude plugin eval]] § Backlog):
  1. run the 12 slow cases;
  2. teach `obsidian-markdown` the `[!contradiction]` callout;
  3. convert graphify and `product-management-layer`;
  4. new cases for `adlc` and the workers.
- **Field-eval items** ([[Skills Field Eval 2026-10]]):
  - N4–N6, worker portability (the verifier still lacks remote and port-forwarded targets);
  - N11–N13, graphify reliability;
  - N7–N10 and N14, conventions.
- **Other open tasks:**
  - [[Integrate the wiki toolset into the ADLC workers]]: the field tests, the "wired instrument" clause in 5 workers, a vault manifest;
  - [[Operator profile - learn engagement style from corrections]]: try `effort` per dispatch;
- **In the vaults:**
  - redeploy `agents/*.md` (plus `devops.md`) to the service repos;
  - add the `relink.py` and `Task(devops)` allow rules to existing vaults.
- **Human follow-ups:**
  - install the Cursor plugin and confirm it loads;
  - choose the sharing pilot (a Quartz slice or a GitHub Wiki mirror);
  - point the OKF exporter at the current repo;
  - rename the repo and its directory.
- **Deferred:** vault MCP server; `/project-profile --refresh`; building the Stage 6 trigger; K8.
