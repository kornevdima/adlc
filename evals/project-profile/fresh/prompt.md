---
name: project-profile/fresh
description: "First run on a repo with no AGENTS.md"
expected_outcome: "AGENTS.md from the template with build/test/lint commands from the scanner"
tags: [project-profile, writes, scaffold]
runs: 1
max_turns: 60
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
---
/project-profile on this repo. There is no tribal knowledge to add (answer "none" to the interview yourself) and I accept the proposed AGENTS.md.
