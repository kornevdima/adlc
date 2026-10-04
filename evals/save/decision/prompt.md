---
name: save/decision
description: "File a decision with its rationale and update index/log/hot"
expected_outcome: "A wiki note with frontmatter capturing the decision and reasons; index + log updated; hot refreshed"
tags: [save, writes, scaffold, fast]
runs: 1
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---
Earlier in this session we decided to use PostgreSQL rather than MongoDB for the orders service. Reasons: orders need multi-row transactions (order + order lines + stock reservation), the reporting team needs SQL joins, and the team already runs Postgres for two other services. MongoDB was rejected because its multi-document transactions add latency at our write volume and nobody on the team has operated it.

/save this decision.
