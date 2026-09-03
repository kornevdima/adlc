---
type: comparison
title: "AI-Native SDLC Playbook vs ADLC"
subjects:
  - "[[claude-ai-native-sdlc-playbook]]"
  - "ADLC (this plugin: Mode ADLC vault + the /adlc delivery loop)"
dimensions:
  - "Lifecycle stages and triggers"
  - "Artifact substrate: single common-name files vs typed wiki records"
  - "Human gates and decision rights"
  - "Controls: advisory vs deterministic"
  - "Closing the loop (Stage 6)"
  - "Measurement"
verdict: "Same lifecycle, different substrate. The playbook is the vocabulary for explaining ADLC to outsiders; ADLC already commits the same artifact chain as typed wiki records with stable IDs. Reject the single common-name files; adopt the Stage 6 trigger seam, a per-service review policy page, and evals-on-config-change."
created: 2026-09-03
updated: 2026-09-03
tags:
  - comparison
  - adlc
  - sdlc
  - ai-native-sdlc
  - artifact-chain
status: developing
related:
  - "[[claude-ai-native-sdlc-playbook]]"
  - "[[Review the ADLC flow against the AI-Native SDLC Playbook]]"
  - "[[Agentic Orchestration Levels]]"
  - "[[Harness Engineering]]"
  - "[[ADLC Field Review Findings]]"
  - "[[Grilling Session]]"
  - "[[AGENTS.md]]"
  - "[[Wiki vs RAG]]"
---

# AI-Native SDLC Playbook vs ADLC

Navigation: [[index]] | [[claude-ai-native-sdlc-playbook]] | [[Review the ADLC flow against the AI-Native SDLC Playbook]]

The playbook (Anthropic, 2026-08-21) describes the *AI-native SDLC*: six stages run as a loop, an agent at each, humans at the gates, and every stage committing an artifact the next reads. That is the lifecycle this plugin implements as **ADLC** (Mode ADLC vault + `/adlc` loop + the service-level workers). The two differ in **substrate**: the playbook chains six single-file artifacts (`intent.md` → `spec.md` → `plan.md` → diff → PR findings → incident record) through git; ADLC keeps the same chain as **typed wiki records with stable IDs** (requirement → story → per-service spec → verification contract → verification / review record → bug → backlog item), also through git.

> [!important] Operator stance, 2026-09-03
> *"I don't like the idea to keep one file with common name; the current workflow with wiki files looks better to me. But it is the explanation for AI SDLC — what we have as ADLC."*
> Ruling: keep the typed-record substrate; use the playbook as the external vocabulary; review the `/adlc` flow against it stage by stage (tracked in [[Review the ADLC flow against the AI-Native SDLC Playbook]], with Stage 6 — closing the loop — as the stage the operator pointed at).

## Stage by stage

| Playbook stage → artifact | ADLC equivalent | Gap / note |
|---|---|---|
| **1 Plan** → `intent.md` in the originator's words; product owner accepts | `.raw/` drop (meeting notes, tickets, a Cowork export) → `wiki-ingest` → `ba-suite` elicitation → `requirements/` register with stable FR/NFR IDs → **grilling gate** with the human before Gate 1 freezes | ADLC's "intent" is the source *plus* the IDs it produced, not one file. Missing: a documented route for a non-engineer to drop intent (Cowork → `.raw/` with a small template) — the playbook's `intent/` folder idea, without the common name |
| **2 Design** → `spec.md`, constrained by org skills, concerns flagged | `architecture-subagent` refines requirements into a per-service shift-left spec (Gates 1 / 1.5 / 2 / 3) in that service's code wiki; concerns (`sec`, `design`, `qa`) as folder kits; bundled BA + shift-left method docs | Equivalent. ADLC has no first-class "org policy skills" — AGENTS.md Don'ts + the standards pushed to the reviewer cover part of it |
| **3 Build** → `plan.md` (files, order, risks, proof), `CLAUDE.md`, skills, hooks, subagents, worktrees | run ledger `_run <EPIC>.md` + per-story **verification contract** (scenarios, preconditions, fingerprint, now also the named instrument and a done-condition) = the plan; `AGENTS.md` via `/project-profile` = `CLAUDE.md`; plugin skills; `permissions.md` allow/ask/deny + optional guard hook = hooks; `agents/` = subagents; `git-flow.md` worktree seam | Equivalent, richer on the plan side (contract is per story and typed). "Update `plan.md` in the same commit when implementation departs" ↔ `wrap-up` flips delivered plans to as-built. ADLC adds `scope-analyst` census / reconcile, which the playbook has no counterpart for |
| **4 Test** → self-verification loop; verifier subagent in a fresh context; **evals in CI on config change**; incident → eval | `feature-builder` self-check (typecheck / lint / unit green) = the loop; `feature-verifier` (fresh context, never fixes) = the verifier; the plugin's `claude plugin eval` suites exist for skills | **Gap**: evals are owner-run locally, not triggered by CI on `agents/` / `skills/` change. "Every incident becomes an eval" has no ADLC rule |
| **5 Deploy** → `REVIEW.md` policy, review in both directions, hooks as approval gates, CI/CD + deploy via MCP, agent stops at the production gate | `feature-reviewer` with the standards *pushed* in the packet (AGENTS.md conventions + Don'ts + spec + contract); 3-round loop; `permissions.md` `ask` list = approval gates; **ADLC stops at commit** ("push and PR only on the operator's word") | **Deliberate boundary**: ADLC has no Deploy stage; verification uses the operator's own toolset. Worth adopting: a per-service **review policy page** (passes, what "Important" means, nit cap, exclusions) so the reviewer's standards are one typed record rather than re-assembled per dispatch. "Second occurrence goes into `CLAUDE.md`" ↔ `/adlc distill` (ADLC distils into repo-local workers *and* AGENTS.md Don'ts) |
| **6 Maintain** → deterministic detection → agent at 2σ/3σ → finding becomes a new `intent.md`; scheduled scans; Claude Tag on-call | verifier FAIL → `bugs/` page **and** a backlog item the loop consumes next session; `wrap-up` + `log.md` are the incident record | **Gap — the one the operator pointed at (`#sd-s6`)**: ADLC has no headless entry. Everything starts from an operator session. The FAIL → backlog mechanic is exactly the "finding re-enters the pipeline" seam; what is missing is a trigger layer (schedule / webhook / channel) that files a `bugs/` page + backlog item without a person in the invocation path. The deferred Agent SDK branch ([[Research OpenManus for claude-mem]]) is where this would live |

## Where each is ahead

**ADLC ahead**
- **Typed records with stable IDs and traceability** (`wiki-lint` checks requirement → story → test, and now story ↔ feature back-links, stale denominators, ambiguous names). A repo-wide `plan.md` is one plan at a time and carries no IDs; the playbook's own metrics are all two-commit deltas because the artifacts carry no structure.
- **Scope measurement** (`scope-analyst` census / reconcile) — the playbook assumes the plan's claims are true.
- **Evidence-carrying handoffs**, re-verify before commit, release-ready-means-every-criterion, records-as-pages — from production audits ([[ADLC Field Review Findings]]).
- **Operator profile** (engagement pole, standing rulings, correction log) — the playbook fixes the human's role per stage and never learns it.

**Playbook ahead**
- **Stage 6 trigger layer** and its tiering (log / diagnose / propose by σ), plus "detection stays deterministic; the model is invoked, never the detector".
- **Evals on config change in CI** and "every incident becomes an eval".
- **Per-play leading / lagging indicators** — ADLC's `meta/mission-control.md` and `meta/ba-activity.md` carry delivery state and cost, not time-to-artifact or first-pass merge share.
- **Enterprise controls**: managed settings, sandbox, marketplace allowlists, separation of duties by construction. ADLC's `permissions.md` is the small-team version.
- **A named entry route for non-engineers** (claude.ai / Cowork → intent).

## Vocabulary map (for explaining ADLC in playbook terms)

| Playbook says | ADLC has |
|---|---|
| AI-native / agentic / AI SDLC | ADLC (Agentic Development Life Cycle) |
| `intent.md` | a `.raw/` source + the requirement IDs elicited from it, after the grilling gate |
| `spec.md` | the per-service shift-left spec (Gates 1–3) in the code wiki |
| `plan.md` | run ledger + per-story verification contract |
| `CLAUDE.md` | `AGENTS.md` (built by `/project-profile`) |
| skills as institutional knowledge | plugin skills + bundled method docs (`references/ba/`, `references/shift-left/`) |
| hooks as guardrails / approval gates | `permissions.md` allow / ask / deny + guard hook |
| `verifier` subagent | `feature-verifier` (plus `feature-reviewer` before it) |
| `REVIEW.md` | the standards packet pushed to `feature-reviewer` (candidate: a review policy page per service) |
| "mistake twice → `CLAUDE.md`" | `/adlc distill` → repo-local workers + AGENTS.md Don'ts |
| PR review findings | review record page in `reviews/` |
| incident record | `bugs/` page + backlog item + `log.md` pointer |
| closing the loop | *(gap: headless trigger)* |

## Why not the common-name files

Recorded so the decision does not get re-litigated: (1) a common name is one instance per repo — `plan.md` cannot hold three in-flight stories; (2) the files carry no IDs, so traceability is by git archaeology; (3) they duplicate what the vault already types, and a vault page *is* a committed artifact (the playbook's requirement is "committed and readable by the next stage", which `wiki/` satisfies); (4) the playbook itself limits `.md` artifacts to the early stages and says from Build onward "the artifact is code and its records" — which is ADLC's position everywhere. Where the playbook is useful is the *vocabulary* and the two seams ADLC lacks: the Stage 6 trigger and CI-run evals.
