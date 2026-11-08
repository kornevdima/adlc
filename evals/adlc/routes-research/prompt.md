---
name: adlc/routes-research
description: "A research request inside the delivery loop lands on the autoresearch route and is not answered on the main thread"
expected_outcome: "The reply names the research route (autoresearch, as a stop at the story boundary) and the record it leaves, without searching the web or answering the question itself"
tags: [adlc, read-only, scaffold, fast]
runs: 1
max_turns: 15
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep]
---
/adlc - before we build the Mermaid story, research how other static-site wikis render Mermaid under a strict CSP and what the field recommends. Give me the answer.
