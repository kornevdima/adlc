---
type: source
source_type: documentation
title: "Claude Code docs, Run parallel sessions with worktrees"
author: Anthropic
date_published: 2026-11-08
url: https://code.claude.com/docs/en/worktrees
confidence: high
key_claims:
  - "claude --worktree <name> creates a worktree under .claude/worktrees/<name>/ on a new branch worktree-<name>, branched from the remote default branch by default (worktree.baseRef fresh), or from local HEAD with head."
  - "A worktree is a fresh checkout: gitignored files such as .env are absent unless listed in a .worktreeinclude file at the project root, which uses .gitignore syntax and copies only files that are also ignored."
  - "Worktrees share the repository .git directory, project-scope plugins, and permission approvals saved in the main checkout's .claude/settings.local.json."
  - "On exit a clean unnamed worktree is removed with its branch; a worktree with changes prompts keep or remove; named sessions prompt first."
  - "Subagents can run in their own worktree with isolation: worktree in frontmatter; a periodic sweep removes old subagent and background worktrees only when they hold no work."
  - "While isolated, edits, command working directories and git redirects into the main checkout are blocked; shell writes such as cp or redirects are not tracked by these checks."
  - "Adding .claude/worktrees/ to .gitignore is recommended so worktrees do not show as untracked."
---

# Claude Code docs, Run parallel sessions with worktrees

Official page on isolating parallel sessions. It extends [[claude-code-common-workflows-worktrees]] with creation, cleanup and sharing details.

## Creation

(Source: this page.) `claude --worktree <name>` or `-w` makes `.claude/worktrees/<name>/` on branch `worktree-<name>`. A name that already exists is reopened. `--worktree "#1234"` branches from a pull request head fetched from `origin`. Manual creation with `git worktree add` is supported when a specific existing branch or an outside location is needed.

## What is per-worktree and what is shared

Per worktree: files, branch, and the checked-out `CLAUDE.md` and rules. Shared with the main checkout: the `.git` directory, project-scope plugins, permission approvals written to the main checkout's local settings file, and untracked skills, agents and commands read through from the main checkout. Environment files are not shared; `.worktreeinclude` copies them in.

## Cleanup

Interactive exit removes a clean unnamed worktree and its branch, and asks about anything with changes or commits. Non-interactive runs leave worktrees and their lock in place; remove them with `git worktree remove` (after `git worktree unlock` if needed). Subagent and background worktrees are swept after `cleanupPeriodDays`, never while they hold unpushed work.

## Isolation limits

The enforcement checks block edits and git commands that reach the main checkout. They read paths and command text, so a plain `cp` or shell redirect into the main checkout is governed only by ordinary permissions and sandboxing. The page does not claim isolation of ports or databases.

Related: [[claude-code-settings-files-and-precedence]], [[Shared Remote Collaboration for Agent Teams]].
