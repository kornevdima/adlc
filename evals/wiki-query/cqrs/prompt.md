---
name: wiki-query/cqrs
description: "Correct negative answer with citations, read-only"
expected_outcome: "CQRS does not require event sourcing; cites wiki pages; no writes"
tags: [wiki-query, read-only, scaffold, fast]
runs: 1
max_turns: 15
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill]
---
What do we know about whether CQRS requires event sourcing? Answer from the wiki.
