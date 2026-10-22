---
type: module
title: "Hooks and host adapters"
path: "hooks/, .claude-plugin/, .cursor-plugin/, .github/plugin/"
created: 2026-10-22
updated: 2026-10-22
tags:
  - architecture
  - module
  - hooks
  - hosts
status: active
related:
  - "[[Plugin architecture overview]]"
  - "[[Scripts]]"
  - "[[Hot Cache]]"
  - "[[Env-guard hook path is relative to the working directory]]"
  - "[[Workers print secrets from env files]]"
---

# Hooks and host adapters

The plugin runs in three hosts from the same source, and two more can use its skills. Each host has a manifest that points at `skills/` and `agents/`, and a hook file in the host's own format with the same two behaviours. What differs per host is only the wiring.

## Manifests

| Host | Manifest | Hooks file |
|---|---|---|
| Claude Code | `.claude-plugin/plugin.json` (name, version, description, repository) | `hooks/hooks.json` |
| Cursor | `.cursor-plugin/plugin.json` and `.cursor-plugin/marketplace.json` (`agents: agents/`, `skills: skills/`) | `hooks/cursor-hooks.json` |
| GitHub Copilot | `.github/plugin/marketplace.json` (source `./`) | `hooks/copilot-hooks.json` |
| Codex CLI, OpenCode | none: symlink `skills/` into the host's skill path | none |

The version is bumped in all four manifest files at once ([[Release and upstream flow]]). Skill frontmatter carries `name` and `description` only, per the Agent Skills spec, so every host reads the same files. The repo's own `AGENTS.md` is read natively by Cursor and alongside the skill descriptions by Claude Code.

## The two plugin hooks

**Session start** prints `wiki/hot.md` when it exists, so the agent has the vault's recent context before the first prompt. Claude Code runs it on `startup|resume`; Cursor and Copilot return it as additional context in their JSON shape. This is how the [[Hot Cache]] earns its name.

**Stop** checks whether `wiki/` has uncommitted changes against `HEAD` and, if so, asks for the hot cache to be rewritten (under 500 words, the four sections, overwrite, a cache not a journal). When the vault has a `services/` folder it adds the ADLC hint: run the wrap-up so code changes reach the code wikis and the product wiki before the session ends. Claude Code's form is a shell one-liner; Cursor's and Copilot's are inline Python that return a follow-up message or a block with the same text, guarded against looping (`loop_count`, `stop_hook_active`).

The hooks are a backstop, not the mechanism: the `wrap-up` skill does the real session sync, and the hook only nudges when it was not run.

## Vault-side hooks

Two hooks live in a vault's own `.claude/settings.json`, written by the wiki skill's scaffold from the `permissions.md` template, because a PreToolUse hook has to exist before any plugin skill runs:

- **The env guard**, `guard_env.py`, shipped in the wiki skill's `scripts/` and copied to the vault's `.claude/hooks/`. It blocks any tool call that reads an env file or prints resolved configuration; `.env.example` stays readable ([[Workers print secrets from env files]]). Commit and PR message text and literal heredoc bodies are not checked, unless they can run code ([[Env guard blocks commands that only mention env files]]); `test_guard_env.py` beside it holds the payload tests.
- **The destructive-ops guard**, `guard.py`, an optional backstop the template wires on `Bash|Write` but does not ship: a vault writes its own pattern list.

Both entries are anchored on `$CLAUDE_PROJECT_DIR` inside `if [ -f … ]; then …; else echo … >&2; fi`: a real block (exit 2 from the hook) still blocks, a missing file warns and passes. A path relative to the working directory once blocked every tool in a vault as soon as the session moved into a subdirectory ([[Env-guard hook path is relative to the working directory]]).

## The permission profile

`permissions.md` is the rest of the vault's `.claude/settings.json`: an allow list for the routine commands and for every shipped script by path, a deny list for env-file reads and for the commands that print secrets, and the rule that in auto mode a narrow allow entry is resolved before the classifier runs, so the shipped script is always the path that needs no judgement ([[Scripts]]). Sign-off, production deploys, force pushes, schema drops and anything that leaves the repo stay the human's call.
