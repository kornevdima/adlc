---
name: project-profile/augment
description: "AUGMENT path keeps foreign sections verbatim (DEFECT-001 regression)"
expected_outcome: "AGENTS.md backed up to AGENTS.md.bak; skill-owned sections refreshed; Wiki topology and Team conventions kept verbatim"
tags: [project-profile, writes, scaffold, regression]
runs: 1
max_turns: 60
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
---
/project-profile on this repo. There is no tribal knowledge to add (answer "none" to the interview yourself) and I accept the proposed AGENTS.md.
