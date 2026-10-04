---
type: meta
title: "Token Usage"
updated: 2026-10-02T21:11:05Z
tags:
  - meta
  - usage
  - derived-view
status: evergreen
---

# Token Usage

> [!note] Derived, host-local view — regenerate, don't hand-edit.
> Built by `usage_report.py` from Claude Code transcripts (`/Users/dmytro/.claude/projects/-Users-dmytro-IdeaProjects-adlc`).
> Transcripts exist only on the machine that ran the sessions; teammates regenerate their own
> (team-sync rule: regenerate-don't-merge). Ledger rows outlive transcript garbage-collection.
> Reading the numbers: **output** and **cache write** are the expensive classes;
> **cache read** is high-volume but ~10x cheaper than input; a high **sub %** means
> subagent fan-out (not the main context) drove the spend.

## Totals (cumulative, all ledger rows)

| input | output | cache write | cache read |
|---|---|---|---|
| 393,129 | 1,651,649 | 6,824,039 | 353,842,199 |

## Top sessions by output tokens (transcripts currently on disk)

| session | label | output (main+sub) |
|---|---|---|
| `6cb242e5` | what other bugs we have in backlog | 124,515 |
| `069f95ff` | /adlc:wiki I've added a curosr marketplace. verify it | 44,840 |
| `4c4e9a20` | restarted session, no warnings ✔ Successfully updated marketplace: adl | 34,662 |
| `e503456c` | check the ledger. I've added a new bug | 13,991 |

## By model (main context; transcripts currently on disk)

| model | input | output | cache write | cache read |
|---|---|---|---|---|
| claude-opus-5-5 | 582 | 208,095 | 556,599 | 37,384,540 |

## By subagent type (transcripts currently on disk)

| agent type | runs | input | output | cache write | cache read |
|---|---|---|---|---|---|
| claude-code-guide | 3 | 156 | 7,648 | 185,007 | 717,039 |
| general-purpose | 4 | 112 | 2,265 | 441,675 | 4,297,117 |

## Session ledger (cumulative; newest first)

<!-- ledger -->
| date | session | label | branch | models | requests | input | output | cache write | cache read | sub % |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-02 | `069f95ff` | /adlc:wiki I've added a curosr marketplace. verify it | main | claude-opus-5-5 | 114 | 236 | 44,840 | 581,873 | 11,257,687 | 5% |
| 2026-10-02 | `4c4e9a20` | restarted session, no warnings ✔ Successfully updated marketplace: adl | main | claude-opus-5-5 | 65 | 130 | 34,662 | 86,554 | 5,829,720 | 0% |
| 2026-10-02 | `6cb242e5` | what other bugs we have in backlog | main | claude-opus-5-5 | 142 | 410 | 124,515 | 431,682 | 22,158,565 | 6% |
| 2026-10-02 | `e503456c` | check the ledger. I've added a new bug | main | claude-opus-5-5 | 37 | 74 | 13,991 | 83,172 | 3,152,724 | 0% |
| 2026-07-04 | `f43eac40` | /claude-mem:wiki let's check the latest changes in the project, starti | adlc | claude-fable-5 | 129 | 54,613 | 139,495 | 601,068 | 20,183,269 | 13% |
| 2026-07-03 | `2602cc6b` | /model | adlc | claude-fable-5 | 210 | 162,688 | 224,983 | 1,124,679 | 20,406,575 | 63% |
| 2026-07-03 | `42d7c8d5` | /login | adlc | claude-opus-4-8 | 64 | 38,194 | 71,142 | 166,422 | 6,929,895 | 0% |
| 2026-07-03 | `82c1164b` | /claude-mem:wiki let's continue build the harness. what next left in t | adlc | claude-fable-5 | 54 | 21,591 | 32,434 | 103,373 | 5,117,897 | 0% |
| 2026-07-03 | `9ccdeca2` | /claude-mem:wiki let's continue work on the project, we have 2 planned | adlc | claude-fable-5 | 47 | 22,362 | 55,865 | 196,320 | 5,020,203 | 0% |
| 2026-07-03 | `9d3c1083` | /claude-mem:wiki let's contniue building harness | adlc | claude-fable-5 | 63 | 21,859 | 42,117 | 118,857 | 6,178,250 | 0% |
| 2026-06-29 | `2e8d7fe4` | how to reinstall plugin to have update for aldc locally | adlc | claude-opus-4-8 | 4 | 19,341 | 2,604 | 28,586 | 121,910 | 0% |
| 2026-06-28 | `fd099c2f` | /claude-mem:wiki I want to run the skill re-avalutaion. I have a feedb | adlc-rlm | claude-opus-4-8 | 213 | 39,500 | 398,967 | 1,079,215 | 52,040,410 | 5% |
| 2026-05-09 | `8ccf9641` | Hi! I want to improve cloud-mem project. | master | claude-opus-4-7 | 530 | 12,131 | 466,034 | 2,222,238 | 195,445,094 | 2% |
