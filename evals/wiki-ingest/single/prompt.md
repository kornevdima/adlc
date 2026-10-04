---
name: wiki-ingest/single
description: "Single-source ingest files source + concept pages and updates rollups"
expected_outcome: "Source page with confidence + key_claims, concept page(s), .raw untouched, index updated, log prepended, manifest written"
tags: [wiki-ingest, writes, scaffold]
runs: 1
max_turns: 40
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---
Ingest .raw/outbox-pattern.md into the wiki.
