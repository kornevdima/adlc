---
name: wiki-lint/seeded
description: "Report the three seeded defects without fixing them"
expected_outcome: "Dead link [[Compensating Transaction]], orphan Orphan Topic, CQRS contradiction in Read Models; no auto-fixes"
tags: [wiki-lint, scaffold]
runs: 1
max_turns: 40
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
---
Lint the wiki.
