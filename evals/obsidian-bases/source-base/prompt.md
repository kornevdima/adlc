---
name: obsidian-bases/source-base
description: "Author a valid Obsidian Bases file for source pages"
expected_outcome: "A .base file filtering type: source, showing confidence and date_published, sorted by date"
tags: [obsidian-bases, writes, scaffold, fast]
runs: 1
max_turns: 20
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill]
---
Create wiki/meta/sources.base that lists all source pages with columns for confidence and date_published, sorted by date.
