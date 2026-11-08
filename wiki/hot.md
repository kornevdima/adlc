---
type: meta
title: "Hot Cache"
updated: 2026-11-08T23:30:00
tags:
  - meta
  - hot-cache
status: evergreen
related:
  - "[[index]]"
  - "[[log]]"
  - "[[Plugin architecture overview]]"
  - "[[Configurable toolset for reader, code navigation and design]]"
  - "[[JetBrains MCP server vs Serena for code navigation]]"
  - "[[Upstream channel from vaults to the plugin]]"
  - "[[Glossary links ids to work pages that share them]]"
  - "[[Research How work is organized]]"
  - "[[Operating model for adlc 1.3.0]]"
---

# Recent Context

Navigation: [[index]] | [[log]]

## Last Updated

**2026-11-08 (later session: the operating-model research)**. `/autoresearch` ran on the brief `.raw/briefs/2026-11-08 How work is organized.md`: Q0 from this repository, Q1 to Q8 by Sonnet workers, 25 pages, synthesis [[Research How work is organized]]. The result: adlc governs the story loop well and has almost nothing around it (no product layer, no team or machine record, no spike record, no measurement fields, no step for non-story work); the twelve findings are mapped to a seven-part model with alternatives and trade-offs, and the gaps in adlc as built are listed. A second pass fetched 21 primaries the first could not reach and raised the concept pages' confidence; what is still secondary (TOGAF, BABOK, the 2025 DORA report body, SPACE, BMAD planning pages) is in the synthesis's Open Questions. `max_questions` is 8 and `max_pages` 30 in program.md now. The first pass is committed; the second pass is its own commit after it.

**2026-11-08 (session: review of the 1.2.0 branch, PR 3 closed, the loop wired to the new keys)**. The branch `feat/toolset-layout-engineering-cost` (`layout`, `engineering` and `cost` keys; the AI-tells pass) was reviewed on macOS, all 29 tests green, and its gaps fixed on the branch: `/adlc` reads the two keys and its packets carry the code wiki path and the ub-mode definition of done, Step 2.7 makes two commits under worktrees; `wrap-up`, `wiki-query`, `wiki-lint`, the architecture worker and three references know `service-wikis/`; `tells_check.py` skips `log.md`. Detail in the log entry. PR 3 is closed and its remote branch deleted; the work is merged to main and pushed after the evals (the log entry has the scores).

**2026-11-04**: the `Toolset:` block (reader, code-nav, design, design-system), `toolset.py`, the `feature-designer` worker, 1.1.0; `idea` added as a fourth code-nav value ([[Configurable toolset for reader, code navigation and design]], [[JetBrains MCP server vs Serena for code navigation]]).

**2026-10-23 and 10-22**: glossary shared ids (vault-d/UP-004), `wiki/architecture/` created, 1.0.9.

## Key Recent Facts

- **The checker is loud on old pages by design.** On this repo's wiki it lists 1,502 `fix` findings, 1,408 of them dashes and 90 title-case headings. The operator ruled the dash sweep intended and the first-run scope accepted; the sweep is its own commit.
- **Not run on macOS:** `setup-ub-mode.sh`. The auto-mode sandbox refuses an installer that clones external code; the operator runs it with `!`. Its pins exist: ub-mode at its HEAD holds only SKILL.md, README and LICENSE; crapper, dryer and mutator each carry a `pyproject.toml` and a `__main__.py`.
- `gh` reaches GitHub again. Two accounts are logged in; `kornevdima` owns this repo and was needed to close the PR; `dmytro-esg` is active again.
- `.raw/upstream/vault-f-UP-001.md` is still unfiled (glossary two-part prefixes).

## Active Threads

- **1.3.0 planned: the operating model.** [[Operating model for adlc 1.3.0]] holds fifteen items in seven blocks, the order of work and three open points. Rulings of 2026-11-08: one release; generated Markdown board; separate decision kinds; artifact pages and drivers. Next: start item 6 (story frontmatter), then 5, 3, 4.
- **Operating-model research filed.** [[Research How work is organized]] maps F1 to F12 to the model and lists the gaps; the operator decides the adlc changes in a separate planning step. The research proposed no plugin changes. Standing ruling from the review of it: adlc does not collect metrics or generate DORA reports; the records carry the fields and the computation stays outside the plugin. Open questions on the page name what the page cap left unsourced (RACI, Team Topologies and SAFe primaries, TOGAF and the other bodies, the 2025 DORA report, Kiro and BMAD detail).
- **1.2.0 shipped.** Next: set the new keys in the co-located vaults (`toolset.py detect`), add the Semble and Serena allow lines and `Task(feature-designer)` to their settings, and give each service `AGENTS.md` a `## Code navigation` section.
- **Dash sweep** across `wiki/`, `skills/` and `agents/`, about 3,000 `fix` findings, one dedicated commit; the hot-cache headings in the `wiki` skill's template go with it.
- **EGM moves to 1.4.0 (ruling 2026-11-08), plan agreed in outline, decisions open.** The Elephant-Goldfish Model (Google, Apache-2.0) adds fresh-context reviewers for documents; adlc's workers are already fresh for code, so the gap is the spec. Plan: a `spec-review: egm | none` key; a `spec-reviewer` worker mirroring `feature-designer` that dispatches the `egm:egm-*` reviewers directly (three nesting levels, no synthesizer) on each gate page before its human approval, stages 5 to 8 on Gates 1 to 2 and stage 9 on Gate 3, record in the code wiki's `reviews/`; `egm-drift-report` in `wiki-lint`; the comprehension Goldfish on technical-writer pages; brainstorm operator-run; bootstrap and draft not adopted. Spike first: a worker with `Agent` in `tools:` spawning `egm:egm-comprehension`. Open: the key name and the phase 1 scope. EGM skills are `disable-model-invocation`, read as files; reviewers need Claude Code 2.1.271 or later (this machine: 2.1.319).
- **Follow-ups from 1.2.0:** evals for the scaffold's new questions; `/project-profile` writes `How we change code` on a fresh run only; `impeccable critique` runs degraded inside the designer; no `wiki/code/` graph of this repo.
- **Carried over unchanged:** vault-f/UP-001; the ledger items not addressed (vault-a public-repo records, UP-002, UP-011); the evals backlog ([[Plugin eval suites for claude plugin eval]]); the open tasks [[Integrate the wiki toolset into the ADLC workers]], [[Operator profile - learn engagement style from corrections]], [[Configurable subagent models per host]]; deferred: vault MCP server, `/project-profile --refresh`, Stage 6 trigger, K8, Cursor load check, sharing pilot, OKF exporter, repo rename.
