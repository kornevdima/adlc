---
name: wiki/scaffold-toolset
description: "Scaffold a Mode B wiki whose toolset is wiki-renderer plus Semble and Serena; the Toolset block lands in AGENTS.md and no Obsidian-only file is written"
expected_outcome: "wiki/ scaffolded; AGENTS.md carries a Toolset block with reader wiki-renderer and code-nav semble, serena; nothing under .obsidian/ and no .base or .canvas file"
tags: [wiki, writes, scaffold, toolset]
runs: 1
max_turns: 60
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
---
/wiki — set up a wiki for this repository (mode B, no concerns). We read the wiki in wiki-renderer, not Obsidian; we navigate code with the Semble and Serena MCP servers, not graphify; we have no design tool. Use sensible defaults and do not ask me questions.
