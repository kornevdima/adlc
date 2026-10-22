---
name: wiki-lint/history-markers
description: "A page keeps a dated Update block and the folder has no changelog: lint names both"
expected_outcome: "The report names the page with the dated Update section as history kept inside a page, and the concepts folder as missing its _changelog.md; pages are not edited"
tags: [wiki-lint, scaffold, writes, fast, regression]
runs: 1
max_turns: 40
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Bash, Skill, Agent, TodoWrite]
---
Lint the wiki.
