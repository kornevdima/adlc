---
type: module
title: "Evals"
path: "evals/"
created: 2026-10-22
updated: 2026-10-22
tags:
  - architecture
  - module
  - evals
status: active
related:
  - "[[Plugin architecture overview]]"
  - "[[Plugin eval suites for claude plugin eval]]"
  - "[[Release and upstream flow]]"
  - "[[Skills Field Eval 2026-10]]"
---

# Evals

Cases for `claude plugin eval` under `evals/`, run locally before each version bump; there is no CI. The ruling behind that is on [[Plugin eval suites for claude plugin eval]]. The suite exists to pin fixed defects and to check that a skill fires and produces the files it promises, not to measure quality at scale: every case runs once by default, and a release decision adds `--runs 3`.

## Shape of a case

`evals/<skill>/<case>/` holds `prompt.md` (frontmatter plus the user prompt), `graders/*.md`, and, when the case needs a starting vault or repo, `case.yaml` naming a `scaffold.sh`. The prompt's frontmatter carries the expected outcome, the tags, the allowed tools and the turn and time budgets.

Twenty-five cases across thirteen skills:

| Skill | Cases |
|---|---|
| `wiki` | scaffold a Mode B vault; resume |
| `wiki-ingest` | single source; batch |
| `wiki-query` | a known concept; an absent one; a large vault with the locator |
| `wiki-lint` | clean vault; seeded defects; history markers and a missing changelog |
| `wiki-faq` | add a source; broken links |
| `save` | a decision; a trivial exchange |
| `autoresearch` | new topic; resume an interrupted plan |
| `project-profile` | fresh repo; augment an existing `AGENTS.md` |
| `wrap-up` | a session with wiki and code changes |
| `ba-export` | a deliverable to `.docx` |
| `obsidian-markdown` | convert GitHub-flavoured Markdown; the contradiction callout |
| `obsidian-bases` | a source base |
| `adlc` | a ruling question cites the record; a ruling question leads with the outcome |

## Fixtures

`evals/_fixtures/use.sh <layer>...` copies layers into the case workspace in order: `vault-base` (a small CQRS and event-sourcing vault), `lint-defects`, `raw-outbox`, `raw-three`, `autoresearch-resume`, `repo-fresh`, `repo-agents`, `ba-checkout`, `wrapup-changes`, `adlc-vault` (a standalone Mode ADLC vault with a stale board on purpose). Two special steps: `@commit` initialises git and commits what is there; `@large` generates sixty pages and the locator. A scaffold script layers fixtures and then adds the case's own files, so a regression case is one heredoc on top of a shared vault.

## Graders

Deterministic first: `file_exists`, `regex` on a named file, `tool_used` with `min` and `max`. Rules learned the hard way, kept in `evals/README.md`: "never called" needs both `min: 0` and `max: 0`; a prompt that starts with a slash command makes no Skill tool call, so `tool_used: Skill` fits natural-language prompts only; an LLM grader over a long trace may not see all of it, so point it at a file or the last message; a regex must not contain a frontmatter delimiter; a pattern must be JavaScript-safe.

## Tags and cost

`fast` (under a minute, cents), `slow` (minutes and dollars), `read-only`, `writes` (needs `--allow-tools Write Edit`, some `Bash`), `scaffold`, `network`, `needs-deps`, `regression`. The fast set is the pre-bump check and costs about two dollars; at 1.0.9 it was eleven cases, all passing. Results and the HTML report go to `evals/results/`, which git ignores.

## Not yet in the suite

- The five graphify skills keep their own runner (cases G1 to G5 with a demo application fixture) under `skills/graphify-ingest/evals/`; the product-management layer keeps cases E1 to E8 under its own `evals/`.
- The two `adlc` cases do not discriminate yet: the no-plugin baseline passes them too, because the field failures they pin happened deep into long sessions. They stay as regression pins.
- The worker agents have no cases. A defect that escapes the verifier in the field becomes a case through the upstream route.
- The twelve slow cases are run before a release but not on every bump.

What the plugin does in the field, as opposed to in a fixture, is the subject of [[Skills Field Eval 2026-10]] and [[ADLC Field Review Findings]].
