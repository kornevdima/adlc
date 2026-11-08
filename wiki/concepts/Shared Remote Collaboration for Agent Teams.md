---
type: concept
title: "Shared Remote Collaboration for Agent Teams"
status: draft
confidence: medium
tags: [git, worktrees, codeowners, secrets, onboarding]
sources: ["[[claude-code-common-workflows-worktrees]]", "[[github-code-owners-and-push-protection]]"]
---

# Shared remote collaboration for agent teams

Several people, each with coding agents, can share one git remote safely if four things hold: each agent works in its own checkout, shared files have one writer or only grow by appending, personal state stays out of commits, and every change reaches the remote through a reviewed pull request with secret checks. Confidence per claim is marked below.

## Concurrent agents in one repository

Give each agent its own git worktree on its own branch. Claude Code does this with `claude --worktree <name>` (Source: [[claude-code-common-workflows-worktrees]], high). Git refuses the same branch in two worktrees (medium, third-party guides). One branch per task is the unit; merge through a PR, not by sharing a checkout.

Worktrees isolate files, not ports or databases (medium, third-party). Conflicts then surface at merge, concentrated in shared files such as indexes, logs and hot caches. Three habits shrink that. Make each shared file single-writer: one role or one closing step owns it, and workers report instead of editing it. Keep logs append-only so merges are mostly additions. Generate index files from page content rather than hand-editing them. These are design practices, not claims from the sources (low as general advice).

## Reviewing documentation like code

Docs in the repo go through the same PR flow. CODEOWNERS routes a PR to the owner of each path, for example a product owner for requirements pages and a lead for architecture pages. It only requests reviewers unless "Require review from Code Owners" is set in branch protection or a ruleset; one owner's approval is enough (Source: [[github-code-owners-and-push-protection]], high). Put an owner on the CODEOWNERS file itself, and list all owners of a path on one line.

## Personal versus shared state

Commit what the team must agree on: AGENTS.md or CLAUDE.md conventions, the wiki, the backlog, shared settings. Keep out of commits: local permission overrides, personal notes, machine paths, session history (Claude Code saves conversations locally). The docs say `.claude/` and `CLAUDE.md` coexist with other tools' config (high). The personal-versus-shared settings split was not confirmed from a fetched page (gap), so check the settings documentation.

## Sensitive input in committed files

Use layers. Pre-commit hooks (gitleaks or similar) catch secrets on the author's machine; GitHub push protection blocks them at the remote, but anyone with write access can bypass with a reason unless delegated bypass is set (Source: [[github-code-owners-and-push-protection]], high). Push protection does not clean history: a leaked secret must be rotated, not just deleted. For personal data and verbatim user text in logs, record a reference or summary rather than the text, and redact before commit. The gitleaks and pre-commit docs were not fetched (gap), so hook configuration is unsourced here.

## When someone joins

A one-person project already has the pieces: AGENTS.md as the contributor guide for agents and humans, the wiki as the knowledge layer. Joining adds CODEOWNERS and branch protection on the default branch, a short CONTRIBUTING note (branch naming, PR flow, who reviews what), secret scanning turned on, and a rule that personal settings stay local. Each newcomer brings an input (design, QA, DevOps), so ownership by path follows inputs, not headcount. Claude Code's own onboarding tip is to ask the agent for a codebase overview and a glossary (high).

See [[Project Within a Larger System]], [[AGENTS.md]].
