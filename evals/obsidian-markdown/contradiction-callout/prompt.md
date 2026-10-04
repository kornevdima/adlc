---
name: obsidian-markdown/contradiction-callout
description: "Add a contradiction callout with links to both sides and bump updated"
expected_outcome: "> [!contradiction] callout in Read Models with [[CQRS]] and [[cqrs-journey]] links; updated date changed"
tags: [obsidian-markdown, writes, scaffold, fast]
runs: 1
max_turns: 20
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill]
---
wiki/concepts/Read Models.md contradicts the CQRS page about whether CQRS requires event sourcing. Add a contradiction callout and cross-references to Read Models.
