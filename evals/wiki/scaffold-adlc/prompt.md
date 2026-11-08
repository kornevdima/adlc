---
name: wiki/scaffold-adlc
description: "Scaffold a Mode ADLC vault: the product and work layers, the generated board, the catalog descriptor and the How we work section land beside the BA folders"
expected_outcome: "wiki/product/prd.md, wiki/domains/context-map.md, wiki/epics/_index.md, wiki/releases/_index.md and wiki/board.md exist; catalog-info.yaml at the root; AGENTS.md carries a Toolset block and a How we work section"
tags: [wiki, writes, scaffold, slow]
runs: 1
max_turns: 90
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite, Bash]
---
/wiki - set up a Mode ADLC vault for this repository with the qa concern. One person runs it (every role). We read the pages in a plain editor (reader none), we have no code navigation tool, no design tool, services are symlinked, no engineering method, no cost plugin. Engagement: business-input. Use sensible defaults for everything else and do not ask me questions.
