# Mission control and the metrics seam (ADLC mode)

Two derived pages in the product wiki's `meta/` folder give the agents' view of the delivery and make the agent's cost savings measurable. Together they close the metrics seam: producers stamp `produced_by` / `feature` / `effort_estimate` frontmatter (see [`modes.md`](modes.md)), and these pages are the rollups that consume it. A third page, `wiki/board.md`, outside `meta/`, is the team's board: generated from the story frontmatter, shareable, and described below.

All three are **derived views**. The detailed records — verification contracts and records, review records, feature pages, story frontmatter — always win on disagreement, exactly like the assertion-coverage ledger (see [`concerns/qa.md`](concerns/qa.md)). Never edit delivery state on a board that isn't backed by a record; never trust a board over the record.

## wiki/board.md, the team's board

The board a product owner, a stakeholder or a new teammate reads. `skills/wiki/scripts/board.py --vault .` renders it from the frontmatter of every page in `user-stories/` (`frontmatter.md` § Work records): one section per status (draft, ready, in progress, blocked, done, dropped), one card per story with its kind, size, priority, services, feature, epic, sprint and release, then one table per epic and per release with the count of stories done against the total. It holds no data of its own and is never edited by hand: the loop regenerates it at every story close (`/adlc` Step 2.8), `wrap-up` regenerates it with the other roll-ups (step 6), and `board.py --check` tells `wiki-lint` when it is stale. With `reader: obsidian` in the toolset the script also writes `board.base` beside it, a live Bases view of the same stories. The page lives outside `meta/` because `meta/` is the agents' state and this page is for people.

## meta/mission-control.md — the agents' board

The dispatcher's own view of a running delivery, and the operator's when they plug in mid-run: what is in flight, what is blocked, what needs a human. Chat scrollback doesn't answer that; this page does. It carries the stage detail the team's board leaves out (verdicts, rounds, the defect route, the milestone verify).

```markdown
---
type: meta
title: "Mission Control"
updated: YYYY-MM-DDTHH:MM:SS
tags: [meta, mission-control]
---

# Mission Control

## In flight
| Feature | Service | Stage | Last verdict | Blocked on |
|---|---|---|---|---|
| [[FEAT-012 Saved filters]] | backend | verify | review APPROVED (round 2) | — |
| [[FEAT-013 Bulk export]] | web | build | — | grilling pending |

## Release readiness
Bar: contract + review APPROVED + verifier PASS on fingerprinted target + e2e green + docs updated.
| Feature | Status |
|---|---|
| [[FEAT-010 Role gates]] | ✅ |
| [[FEAT-011 Audit log]] | conditional — fix pending ([[BUG-004]]) |

## Defect route
Open FAILs: N — each must have a `bugs/` page **and** a backlog item ([[technical-planning]] dispatcher rules).
| Bug | Feature | Backlog item | Re-verify |
|---|---|---|---|
| [[BUG-004]] | FEAT-011 | [[US-042]] | pending |

## Milestone
Last holistic verify: YYYY-MM-DD ([[record]]) — next due at ~5 shipped features / sprint close.
Features shipped since: N. Status: `conditional — milestone verify pending` | ✅

## Human gates open
- Grilling session for FEAT-013 (open questions: N)
- Gate 2 sign-off for backend spec
```

**Stage** is one of: `spec` → `grilling` → `build` → `test` → `review` → `verify` → `docs` → `shipped` (matching the pipeline in [`technical-planning.md`](technical-planning.md)).

### Who updates it, when

- **The dispatcher, at stage transitions.** When a worker is dispatched, a handoff is accepted, a verdict lands (APPROVED / CHANGES_REQUESTED / PASS / FAIL), or a FAIL is routed to `bugs/` + backlog — update the affected row in the same breath as the record. One row edit, not a rewrite.
- **`wrap-up`, at session end.** Reconcile the whole board against the records this session touched (it is one of the rollups in the wrap-up reconcile step).
- Statuses obey the readiness bar literally: any pending criterion is `conditional — <criterion> pending`, never ✅.

### When more than one session runs

The one place these rules live; `team-sync.md` points here.

- **Pull before reading.** A session reads the board, the ledgers and the epic pages only after `git pull` of the vault; a board read from a stale checkout is a board from another session's past.
- **One dispatcher per epic.** Two `/adlc` sessions never work the same epic at once; the run ledger `_run <EPIC-ID>.md` is the lock, and a session that finds one it did not write asks before touching the epic (resume is the owner's call). Two sessions on two epics in one vault are fine; they touch different ledgers and different story pages.
- **Regenerate rather than merge.** `board.md` is regenerated from the stories, never merged; `mission-control.md` and `ba-activity.md` are reconciled from the records, never hand-merged; `hot.md` is rewritten from `log.md` and the session. On a conflict in any of them, take either side and regenerate.
- **When two sessions touched mission control:** the one that wraps up second reconciles every row against the records (the verification and review records, the story frontmatter, the ledger Notes) and says so in its log entry; a row with no record behind it is deleted, not kept. The story pages carry the truth about status and dates, so the boards can always be rebuilt from them.

## meta/ba-activity.md — the cost rollup

The value claim of ADLC is measurable: deliverables produced per feature versus the BA / QA / PM time they replace. This page is that rollup.

```markdown
---
type: meta
title: "BA Activity Ledger"
updated: YYYY-MM-DDTHH:MM:SS
tags: [meta, metrics]
---

# BA Activity Ledger

## Per feature
| Feature | Role covered | Deliverables (produced_by) | Effort replaced |
|---|---|---|---|
| FEAT-012 | BA | 3 requirements, 4 stories (ba-elicitation-synthesizer, ba-user-story-factory) | ~1.5d |
| FEAT-012 | QA | 6 test cases (ba-test-case-generator), 4 e2e specs (feature-tester) | ~1d |

## Per role (running totals)
| Role | Deliverables | Effort replaced |
|---|---|---|
| BA | 41 | ~12d |
| QA | 63 | ~9d |
| PM | 8 | ~2d |

## Not counted
Notes missing `produced_by` since last rollup: N (list or "none")
```

Role mapping: `ba-*` skills → BA; `feature-tester` + test-case output → QA; sprint packs / planning-monitor output → PM; `architecture-subagent` → architecture (add a row if the team wants it counted).

### How to compute it (cheap)

Grep frontmatter — never LLM-read the whole vault:

```bash
grep -r "^produced_by:" wiki/ --include="*.md" -h | sort | uniq -c
grep -rl "^feature: \"FEAT-012\"" wiki/ --include="*.md"
```

Sum `effort_estimate:` per feature / role from the matched notes. Notes with `produced_by` empty go under **Not counted** — that line is the seam's own health check, and `wiki-lint` flags the same gap.

### Who updates it, when

- **`wrap-up`, at session end** — the only mandatory refresh. Dispatchers do not touch it mid-flight.
- On demand, when the operator asks "what has the agent saved us" — refresh, then answer from the page.

## meta/usage.md — the token-usage rollup (optional, host-local)

The third derived page, for operators who want to see what drives token consumption. Generated by `skills/wrap-up/scripts/usage_report.py` from the host's Claude Code session transcripts (`~/.claude/projects/<project-slug>/`): a cumulative per-session ledger (date, label, branch, models, input / output / cache-write / cache-read, subagent share) plus top-consumer, per-model, and per-subagent-type breakdowns. Deduped by `requestId`; subagent runs attributed via their `.meta.json` sidecars.

Differences from the other two pages:

- **Host-local.** Transcripts exist only on the machine (and host app) that ran the sessions — each teammate's page reflects their own runs. Team-sync rule is still regenerate-don't-merge, but here "regenerate" means *on your own transcripts*; don't expect the page to agree across machines. On non-Claude-Code hosts the script exits cleanly and the page simply goes stale — that is expected, not drift.
- **Cumulative by design.** Ledger rows survive transcript garbage-collection (the script keeps rows for sessions no longer on disk), so the totals outlive the ~30-day transcript retention. The breakdown tables cover only transcripts currently on disk and say so.
- **Refresh**: `wrap-up` step 7, same cadence as `index.json`. Not seeded at scaffold — the first wrap-up on a Claude Code host creates it.

Reading the numbers: **output** and **cache write** are the expensive token classes; **cache read** is high-volume but roughly 10× cheaper than input; a high **sub %** means subagent fan-out, not the main context, drove the spend.

## Obsidian Bases (optional, for humans, `reader: obsidian` only)

When the vault's `Toolset:` block has `reader: obsidian`, a live, self-maintaining view is one `.base` file away: add `meta/ba-activity.base` with views grouped by `produced_by` and by `feature` (see the `obsidian-bases` skill). Bases render for humans inside Obsidian only; wiki-renderer and plain editors show the Markdown pages above, which remain the agent-readable artifacts in every reader. Keep both, don't replace one with the other.

## Scaffold

At ADLC scaffold time (and on the first initial pass in an existing vault), seed both pages with empty tables and the readiness bar filled in from `technical-planning.md`. An empty board with the right columns is the contract; the first dispatch fills it. Seed `meta/operator-profile.md` at the same time (template in [`operator-profile.md`](operator-profile.md)) — the third `meta/` page the delivery loop reads at Step 0: engagement pole, standing rulings, and the correction log that `/adlc distill` turns into proposed settings.
