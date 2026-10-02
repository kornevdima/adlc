---
type: synthesis
title: "Configurable subagent models per host"
created: 2026-10-02
updated: 2026-10-02
tags:
  - agents
  - adlc
  - plugin
  - models
  - cross-host
status: open
related:
  - "[[Plugin Hooks]]"
  - "[[Integrate the wiki toolset into the ADLC workers]]"
---

# Configurable subagent models per host

**Opened from live use.** Field evidence: [[Skills Field Eval 2026-10]] (K8). The plugin was installed in GitHub Copilot in an org without Claude models. The worker dispatch failed on the agent's `model: sonnet`, and the orchestrator proposed a general-purpose agent instead. That agent does not have the worker's instructions.

## The problem

- 8 agents set `model: sonnet` in their frontmatter: `feature-builder`, `feature-tester`, `feature-reviewer`, `feature-verifier`, `scope-analyst`, `doc-writer`, `architecture-subagent` and `ba-suite-subagent`. The other 6 set nothing, so they inherit the session model.
- `graphify-ingest` and `graphify-update` pass `model: "sonnet"` in their Agent calls.
- A model name that is valid in one host or org is not valid in another. Cursor expects `inherit` or its own ids (`composer-2`, …), and Copilot depends on what the org enables.
- `inherit` everywhere is not acceptable either. The orchestrator runs on Opus, and running workers on Opus costs more without a matching benefit.

## Host facts (checked 2026-10-02)

- **Claude Code**: `plugin.json` `userConfig` is prompted when the plugin is enabled and editable in `/config`. A `string` option takes an `options` picker, which needs v2.1.271 or later. `${user_config.KEY}` is substituted in skill and agent content (documented for "the Markdown body"; substitution in frontmatter is untested). A `model` passed in the Agent call overrides the agent's frontmatter. `CLAUDE_CODE_SUBAGENT_MODEL` sets one model for all subagents, a user-side override.
- **Cursor**: agent `model` takes `inherit` (the default) or a Cursor model id. Plugin `variables` are set by team admins in the dashboard and are documented only for MCP and other config files, not agent files.
- **Copilot**: plugins reuse the Claude Code `agents` / `skills` fields. Not verified: its install folder, and whether its subagent tool accepts a `model` at dispatch time.
- **Installed copies are not stable.** Claude Code installs each version into a new folder. A marketplace added as a local directory loads **in place**, so in plugin development the installed copy is this repo.

## Proposed design (not built)

The operator proposed a skill that rewrites `model:` in the installed agents from user input. Rewriting as the primary mechanism was rejected for two reasons. Edits are lost on every plugin update. In dev mode the edits would land in the git checkout, and one host's model names would be committed for every user.

1. **Agents ship with no `model:` field.** A missing model never errors on any host. This alone fixes the Copilot failure.
2. **Add an `adlc:setup` skill.** It detects the host and asks for a model per tier:
   - orchestrator: the session model
   - worker: build, test, verify, BA, docs (cheap, e.g. `sonnet`)
   - judgement: `feature-reviewer`, `scope-analyst`

   It writes the answers to a per-machine file such as `~/.adlc/models.json`, keyed by host. This is the same pattern other plugins use for a per-machine workspace file. The file survives plugin updates.
3. **Pass the model at dispatch time.** The `adlc` skill and other dispatchers read the file and call `Agent(subagent_type: "adlc:<worker>", model: <tier>)`, with no files edited.
4. **Fall back without a model.** On a model error, retry the same `subagent_type` without `model`, so it inherits the session model, and suggest re-running setup. Never fall back to a general-purpose agent.
5. **Rewrite frontmatter only where dispatch can't pass a model.** This is for a host whose subagent tool has no `model` parameter. Setup rewrites `model:` in the installed copy and records the plugin version. A session-start hook detects a version change and asks to re-run setup. Setup refuses when the installed folder is a git checkout.

## Next steps

- [ ] Steps 1–4. They work in Claude Code today and stop the Copilot failure.
- [ ] In a Copilot session: find the plugin install folder and check whether its subagent tool accepts `model`. Do the same check in Cursor.
- [ ] Step 5, only for the hosts that need it after that check.
- [ ] Decide whether `userConfig` (Claude Code only) replaces or complements `~/.adlc/models.json`.

## Resolution log

- 2026-10-02: opened; design agreed in discussion, nothing built.
- 2026-10-02: field eval confirmed it. The failed dispatch led to an offer to build inline; the retry hardcoded another vendor's model; a plugin reload was tried and did nothing. Add to the fix: remove the "pinned to a fast model (Sonnet)" line in `technical-planning.md`, and never answer a model error by doing the work inline.
