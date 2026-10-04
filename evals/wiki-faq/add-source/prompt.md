---
name: wiki-faq/add-source
description: "FAQ answer about ingest grounded in the plugin docs"
expected_outcome: "Drop into .raw/, run ingest, manifest delta tracking; no invented features"
tags: [wiki-faq, read-only, fast]
runs: 1
max_turns: 10
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill]
---
How do I add a new source to the wiki and what happens during ingest?
