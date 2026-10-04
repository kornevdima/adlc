---
name: wiki/resume
description: "Existing vault: read hot.md and report, do not re-scaffold"
expected_outcome: "Reads hot.md, reports recent context, suggests the next action (ingest the outbox source)"
tags: [wiki, read-only, scaffold, fast]
runs: 1
max_turns: 15
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill]
---
/wiki — continue where we left off.
