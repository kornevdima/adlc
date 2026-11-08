---
type: source
source_type: documentation
title: "Claude Code docs, Common workflows (parallel sessions with worktrees)"
author: Anthropic
date_published: 2026-11-08
url: https://code.claude.com/docs/en/common-workflows
confidence: high
key_claims:
  - "claude --worktree <name> starts a session in its own git worktree, a separate checkout on its own branch; a second terminal with another name gives an isolated parallel session."
  - "A worktree is created from an existing commit, so the repository needs at least one commit first."
  - "Claude Code runs in any directory, including notes and documentation folders of markdown files."
  - "Claude Code links a session to a PR it creates with gh pr create or glab mr create, and claude --from-pr finds it later."
  - "Claude Code can run non-interactively in CI and pre-commit hooks."
tags: [claude-code, worktrees, parallel-agents]
---

# Claude Code docs, Common workflows

Vendor documentation. The page is undated, so date_published is the fetch date. Confidence is high for the flags and behavior it states. The page defers cleanup, `.worktreeinclude` and non-git VCS to a separate Worktrees page that was not fetched (gap).

Isolation comes from git, not from the agent. Each worktree is a separate checkout on its own branch, so two sessions do not overwrite each other's files. The docs also say the `.claude/` directory and `CLAUDE.md` sit beside other tools' config, and that Claude reads files fresh on each tool call, so edits made in another application are seen on the next read. PRs created through the CLI are linked to the session.

Not covered by the page: shared resources (ports, databases), merge-conflict handling, and which settings files are personal. Third-party guides found in search discuss these but are low confidence.

See [[Shared Remote Collaboration for Agent Teams]].
