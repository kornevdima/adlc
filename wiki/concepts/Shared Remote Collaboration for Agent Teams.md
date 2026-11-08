---
type: concept
title: "Shared Remote Collaboration for Agent Teams"
status: draft
confidence: high
created: 2026-11-08
updated: 2026-11-08
tags: [git, worktrees, codeowners, secrets, onboarding]
sources: ["[[claude-code-common-workflows-worktrees]]", "[[github-code-owners-and-push-protection]]", "[[claude-code-settings-files-and-precedence]]", "[[claude-code-worktrees-page]]", "[[gitleaks-readme]]"]
---

# Shared remote collaboration for agent teams

Several people, each with coding agents, can share one git remote safely if four things hold: each agent works in its own checkout, shared files have one writer or only grow by appending, personal state stays out of commits, and every change reaches the remote through a reviewed pull request with secret checks. Confidence per claim is marked below.

## Concurrent agents in one repository

Give each agent its own git worktree on its own branch. Claude Code does this with `claude --worktree <name>` (Source: [[claude-code-common-workflows-worktrees]], high). The worktree is created at `.claude/worktrees/<name>/` on branch `worktree-<name>`, from the remote default branch unless `worktree.baseRef` is `head` (Source: [[claude-code-worktrees-page]], high). Git refuses the same branch in two worktrees (medium, third-party guides). One branch per task is the unit; merge through a PR, not by sharing a checkout.

A worktree is a fresh checkout, so gitignored files such as `.env` are absent unless a `.worktreeinclude` file lists them; it shares the `.git` directory, project plugins and saved permission approvals with the main checkout, and a clean unnamed worktree is removed on exit while one with changes prompts (Source: [[claude-code-worktrees-page]], high). Add `.claude/worktrees/` to `.gitignore`. Worktrees isolate files, not ports or databases (medium, third-party). Conflicts then surface at merge, concentrated in shared files such as indexes, logs and hot caches. Three habits shrink that. Make each shared file single-writer: one role or one closing step owns it, and workers report instead of editing it. Keep logs append-only so merges are mostly additions. Generate index files from page content rather than hand-editing them. These are design practices, not claims from the sources (low as general advice).

## Reviewing documentation like code

Docs in the repo go through the same PR flow. CODEOWNERS routes a PR to the owner of each path, for example a product owner for requirements pages and a lead for architecture pages. It only requests reviewers unless "Require review from Code Owners" is set in branch protection or a ruleset; one owner's approval is enough (Source: [[github-code-owners-and-push-protection]], high). Put an owner on the CODEOWNERS file itself, and list all owners of a path on one line.

## Personal versus shared state

Commit what the team must agree on: AGENTS.md or CLAUDE.md conventions, the wiki, the backlog, and `.claude/settings.json`, which carries team permissions, hooks and plugins (Source: [[claude-code-settings-files-and-precedence]], high). Keep personal state in files that stay local. `~/.claude/settings.json` is per user across projects. `.claude/settings.local.json` is per user in one project: Claude Code adds it to the global git excludes when it creates the file, but a hand-made copy needs a `.gitignore` entry, and "don't ask again" approvals land there (high). Precedence runs managed, command line, local, shared, user, so a teammate overrides a committed value locally without a commit, and allow lists merge. Some committed keys, such as allow rules and most `env` values, apply only after each teammate trusts the folder. A cloud session sees only the committed file. The docs say `.claude/` and `CLAUDE.md` coexist with other tools' config (high). Session history is stored locally under the home config directory, which `CLAUDE_CONFIG_DIR` relocates (high); the local variant of CLAUDE.md and the memory file layout were not on the fetched pages (gap, check the memory page).

## Sensitive input in committed files

Use layers. Pre-commit hooks (gitleaks or similar) catch secrets on the author's machine; GitHub push protection blocks them at the remote, but anyone with write access can bypass with a reason unless delegated bypass is set (Source: [[github-code-owners-and-push-protection]], high). Push protection does not clean history: a leaked secret must be rotated, not just deleted. For personal data and verbatim user text in logs, record a reference or summary rather than the text, and redact before commit. Local hook setup: add the gitleaks repo, a pinned `rev` and the `gitleaks` hook id to `.pre-commit-config.yaml`, then each clone runs `pre-commit install` once; `SKIP=gitleaks` skips one commit (Source: [[gitleaks-readme]], high). Known test secrets take a `gitleaks:allow` comment, reviewed false positives go in `.gitleaksignore` or `.gitleaks.toml`, and a baseline report lets a legacy repository start clean. `detect` and `protect` are deprecated in favour of `git` and `dir`. A hook can be skipped, so it never replaces the remote check.

## When someone joins

A one-person project already has the pieces: AGENTS.md as the contributor guide for agents and humans, the wiki as the knowledge layer. Joining adds CODEOWNERS and branch protection on the default branch, a short CONTRIBUTING note (branch naming, PR flow, who reviews what), secret scanning turned on, and a rule that personal settings stay local. Each newcomer brings an input (design, QA, DevOps), so ownership by path follows inputs, not headcount. Claude Code's own onboarding tip is to ask the agent for a codebase overview and a glossary (high).

See [[Project Within a Larger System]], [[AGENTS.md]].
