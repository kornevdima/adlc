---
type: meta
title: "Hot Cache"
updated: 2026-07-17T00:00:00
tags:
  - meta
  - hot-cache
status: evergreen
related:
  - "[[index]]"
  - "[[log]]"
  - "[[Harness Engineering]]"
  - "[[Agentic Orchestration Levels]]"
  - "[[ADLC Field Review Findings]]"
---

# Recent Context

Navigation: [[index]] | [[log]]

## Last Updated

**2026-07-17 (RENAME: claude-mem → adlc, plugin 1.0.0 — plus git-flow, OKF export, Day-1 ingest)**: The project is now **adlc**, repositioned as the ADLC harness (knowledge substrate → role skills → delivery orchestration → project bindings). README rewritten; marketplace `adlc-marketplace`; skill namespace `adlc:`; [[Plugin Hooks]] renamed from "Claude-mem Hooks". Historical wiki pages keep the old name by design. Five commits: `d4248f4` (/adlc delivery-loop skill), `625b15b` (git-flow.md), `b45f996` (rename), `b82f425` (OKF export), plus the wiki/ingest commit. **The installed plugin still runs under the old name — reinstall required** (`claude plugin marketplace add` → `adlc@adlc-marketplace`); GitHub repo + local dir rename are the operator's.

**2026-07-17 (git-flow + OKF)**: `skills/wiki/references/git-flow.md` codifies branch topology: session wiki branches `wiki/<epic-id>`, code-only service PRs (free in multi-repo vaults), Mode B worktree seam, **review-by-reading-not-merging** (wiki→feature merge and code-only PRs are mutually exclusive), singleton single-writer rule. Wired into `/adlc` Step 0 + wrap-up. `skills/wiki/scripts/okf_export.py` renders the vault as a Google Open Knowledge Format bundle (test: 91 pages, 806 links rewritten); wiki-lint check 6 notes `type` as the OKF-required field.

**2026-07-17 (Day-1 deck ingested)**: `.raw/Day_1_v3.pdf` (Osmani/Saboo/Kartakis, Google, May 2026) → [[vibe-coding-new-sdlc-day1]] + [[Harness Engineering]] ("Agent = Model + Harness"; "most agent failures are configuration failures"). Operator-authored [[Agentic Orchestration Levels]] (draft): 0 chat session → 3 orchestrator/Mode ADLC; levels 1–2 interpolated, `[!gap]`-flagged. Deck has **no numbered levels** — the ladder is ours; the grilling gate has no deck equivalent either.

**2026-07-08 (eval sweep, committed)**: all 17 skills eval-covered; graphify G1–G5 green after four real `update.py` defects fixed; autoresearch v2.2; pm-layer 8/8. Process traps: installed plugin goes stale vs dev checkout (`claude plugin marketplace update adlc-marketplace` before re-evaling scripts); `claude -p` harnesses need `--dangerously-skip-permissions` + `--add-dir`.

## Key Recent Facts

- **Naming**: plugin/product = adlc; marketplace = adlc-marketplace; version 1.0.0. "claude-mem" survives only in historical wiki pages and the not-yet-renamed repo/dir.
- **Sharing tiers**: intra-team = git ([[Wiki Sharing Patterns]], team-sync.md, git-flow.md); inter-team = OKF bundle. Vault MCP server stays deferred (interop path for non-Claude consumers; inside Claude Code, file reads beat tool round-trips).
- **OKF alignment is cheap**: vault frontmatter is near-conformant (`type` is OKF's only required field); export maps `updated`→`timestamp`, derives `description` from the first paragraph when missing.

## Active Threads

- **Human follow-ups (rename)**: reinstall plugin under new name; rename GitHub repo (old URLs redirect) + local dir; redeploy `agents/*.md` to service repos under the `adlc:` namespace (was already pending — bundle together).
- Prior follow-ups still open: `/graphify-ingest` in graph-less service repos; `.gitattributes` two-liner + seed `meta/` pages in existing project vaults; pm-layer E1 golden case on the default model.
- Deferred by design: vault MCP interop server (build when the headless Agent SDK branch needs it); `/project-profile --refresh` mode.
