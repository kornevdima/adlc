---
name: wiki-faq/broken-links
description: "Troubleshooting answer that points at wiki-lint and relink"
expected_outcome: "Explains rename vs link update, suggests wiki-lint (and relink.py) per vault conventions"
tags: [wiki-faq, read-only, fast]
runs: 1
max_turns: 10
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill]
---
Why are my wikilinks broken after I renamed a page in Obsidian?
