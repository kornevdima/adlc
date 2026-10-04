---
name: wiki-ingest/batch
description: "Batch ingest of three related sources with cross-references"
expected_outcome: "All three filed, cross-linked, manifest written, index counts bumped, .raw untouched"
tags: [wiki-ingest, writes, scaffold, slow]
runs: 1
max_turns: 80
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
---
Ingest all unprocessed sources in .raw/ into the wiki (there are three), then cross-reference them.
