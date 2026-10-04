---
name: wiki/scaffold-mode-b
description: "Scaffold a Mode B code wiki in a repo without touching code"
expected_outcome: "wiki/ with index, hot, log and Mode B folders; no code files overwritten"
tags: [wiki, writes, scaffold]
runs: 1
max_turns: 60
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
---
/wiki — set up a wiki for this repository (mode B). Use sensible defaults and do not ask me questions.
