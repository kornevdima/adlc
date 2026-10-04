---
name: wiki-query/large-vault
description: "Large vault (65 pages + index.json): locate via the index, not by reading everything"
expected_outcome: "Names Payments Ledger, Shipment Tracking and the shared Idempotency Key; uses index.json to locate; reads few pages"
tags: [wiki-query, read-only, scaffold]
runs: 1
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---
Which pages in our wiki connect the payments domain to the logistics domain, and through what? Answer from the wiki.
