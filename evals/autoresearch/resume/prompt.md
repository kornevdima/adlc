---
name: autoresearch/resume
description: "Resume an interrupted plan: answer only Q2/Q3, keep Q1, close out"
expected_outcome: "Detects the _plan, answers Q2 and Q3 only, preserves cdc-overview, deletes the plan, synthesis covers the open questions"
tags: [autoresearch, writes, network, slow, scaffold]
runs: 1
max_turns: 120
timeout_seconds: 1800
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
---
Continue the research on change data capture tools.
