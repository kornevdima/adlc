---
name: wrap-up/session
description: "Session wrap-up refreshes hot and log and calls out uncommitted work"
expected_outcome: "hot.md Last Updated entry prepended, log entry at the top, uncommitted changes called out"
tags: [wrap-up, writes, scaffold]
runs: 1
max_turns: 40
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---
Wrap up this session. This session I created the concept page Transactional Outbox and added a frontmatter convention to AGENTS.md.
