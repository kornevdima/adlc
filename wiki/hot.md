---
type: meta
title: "Hot Cache"
updated: 2026-10-04T12:00:00
tags:
  - meta
  - hot-cache
status: evergreen
related:
  - "[[index]]"
  - "[[log]]"
  - "[[Upstream channel from vaults to the plugin]]"
  - "[[Tester edits app code to prove a test bites]]"
  - "[[Dispatcher rules for writing ruling questions]]"
  - "[[Plugin eval suites for claude plugin eval]]"
---

# Recent Context

Navigation: [[index]] | [[log]]

## Last Updated

**2026-10-04 (session: 1.0.7)**. Committed as `chore(plugin): 1.0.7` (push pending: no git credentials in the agent shell):
- [[Dispatcher rules for writing ruling questions]]: `/adlc` Step 2 § Writing a ruling question (sourced premises, outcome first, one decision per question; several questions can share a stop). Pointers from grilling, distill and `scope-analyst`.
- [[Tester edits app code to prove a test bites]]:
  - `skills/adlc/scripts/build_snapshot.py` snapshots each builder round to `refs/adlc/<story>/build-<n>`, then checks the tester's footprint (Step 2.3a, 2.4a and 7);
  - the tester never edits app code, not even temporarily.
- [[Upstream channel from vaults to the plugin]]:
  - each vault keeps `wiki/meta/adlc-upstream.md`, and `/adlc upstream` exports it (a GitHub issue, or a manual hand-off);
  - `skills/adlc/references/upstream-shipped.md` closes entries; it lists vault-a UP-001 to UP-004 under 1.0.7.
- Evals: the 22 skill cases now live under `evals/`, plus 2 `adlc` cases (`adlc-vault` fixture). Their no-plugin baseline also passes (Δ 0).

## Key Recent Facts

- **Review new proposals in the co-located vaults too.** The snapshot design waited in vault-a's `_run EPIC-002` Carry-forward, and a review of this repo alone missed it. AGENTS.md § Upstream intake now says so.
- `gh` can't reach GitHub from this machine (`x509: certificate signed by unknown authority`). The manual hand-off is the working route.
- `claude plugin eval` takes only the last `--case`; run cases one at a time. With no `--ablation none`, it adds a no-plugin arm.
- Auto mode ignores `autoMode` in project settings; a narrow `permissions.allow` rule skips the classifier.

## Active Threads

- **In vault-a** (uncommitted there):
  - commit the new `wiki/meta/adlc-upstream.md`;
  - after 1.0.7 is installed: mark UP-001 to UP-004 shipped, remove the profile's "Cite the record" line and its two `proposed:` lines, and drop the ledger's distill item;
  - copy `feature-tester.md` into `<service>/.claude/agents/`; add the `build_snapshot.py` and `relink.py` allow rules and `Task(devops)`;
  - field-test the footprint check: files the suite regenerates go in the Test globs line.
- **Evals backlog** ([[Plugin eval suites for claude plugin eval]]):
  - run the 12 slow cases;
  - the `[!contradiction]` callout;
  - convert graphify and pm-layer;
  - `adlc` routing and worker cases on `adlc-vault`.
- **Field-eval items** ([[Skills Field Eval 2026-10]]): N4–N6 worker portability, N11–N13 graphify, N7–N10 and N14 conventions.
- **Open tasks:**
  - [[Integrate the wiki toolset into the ADLC workers]];
  - [[Operator profile - learn engagement style from corrections]] (`effort` per dispatch);
  - the first real `/adlc upstream` export (check that the cleaning holds).
- **Human follow-ups:** the Cursor plugin load check, the sharing pilot, the OKF exporter, renaming the repo.
- **Deferred:** vault MCP server; `/project-profile --refresh`; the Stage 6 trigger; K8.
