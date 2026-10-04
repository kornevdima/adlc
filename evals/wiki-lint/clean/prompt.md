---
name: wiki-lint/clean
description: "Clean vault: healthy verdict, no false positives"
expected_outcome: "Healthy verdict, no false-positive dead links or contradictions, pages unchanged"
tags: [wiki-lint, scaffold]
runs: 1
max_turns: 40
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
---
Lint the wiki.
