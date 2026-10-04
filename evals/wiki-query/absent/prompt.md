---
name: wiki-query/absent
description: "Topic absent: admit the gap, do not fabricate"
expected_outcome: "Explicit gap admission, no fabricated content, no writes"
tags: [wiki-query, read-only, scaffold, fast]
runs: 1
max_turns: 15
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill]
---
What does our wiki say about GraphQL federation?
