---
type: source
source_type: documentation
title: "Claude Code docs, Settings files and precedence"
author: Anthropic
date_published: 2026-11-08
url: https://code.claude.com/docs/en/settings
confidence: high
key_claims:
  - "Claude Code reads user settings from ~/.claude/settings.json, shared project settings from .claude/settings.json (commit it so teammates get it), and project-local settings from .claude/settings.local.json."
  - "Claude Code keeps settings.local.json out of git when it creates the file, by adding it to the global git excludes; a file created by hand must be added to .gitignore."
  - "Precedence, highest first: managed settings, command line, project local, shared project, user. List keys such as permissions.allow merge across files."
  - "Choosing 'Yes, and do not ask again' on a permission prompt writes an allow rule to .claude/settings.local.json; in a worktree it uses the main checkout's file."
  - "CLAUDE_CONFIG_DIR relocates the home-directory settings, session history and plugins; ~/.claude.json holds account details, MCP configurations and per-project state."
  - "Cloud sessions read the committed .claude/settings.json (it is in the clone) but not the user or project-local files."
---

# Claude Code docs, Settings files and precedence

Official page on where Claude Code reads settings and who each file affects. It is the primary source for the split between personal and shared configuration.

## The four scopes

(Source: this page.) A table lists user, shared project, project local and managed scopes. User settings live in `~/.claude/settings.json` and cover every project on the machine. Shared project settings live in `.claude/settings.json` and are meant to be committed, carrying team permissions, hooks, plugins and project environment variables. Project-local settings live in `.claude/settings.local.json`, apply to one person in one project, and are personal overrides. Managed settings are delivered by an organization and sit at the top.

## Keeping personal state out of git

Claude Code adds `**/.claude/settings.local.json` to the global git excludes file the first time it writes the local file in a repository that does not already ignore it. A hand-made local file needs a manual `.gitignore` entry. The local file is where "don't ask again" permission approvals are saved, so it accumulates personal command approvals that should never be committed.

## Precedence and merging

Managed beats command line, which beats project local, which beats shared project, which beats user. A teammate overrides a committed value for themselves in the local file without a commit. Allow lists merge across files rather than replace.

## Trust and cloud sessions

Some committed keys wait for each teammate to trust the folder before they apply: `permissions.allow` rules, additional directories and most `env` values. `deny` and `ask` rules apply at once. A cloud session runs on a fresh clone, so it sees the committed shared file and nothing from the user or local files.

## Not covered

The page does not describe `CLAUDE.md` versus a local variant, or the memory file layout; those are on the memory and claude-directory pages, which were not fetched.

Related: [[claude-code-worktrees-page]], [[Shared Remote Collaboration for Agent Teams]].
