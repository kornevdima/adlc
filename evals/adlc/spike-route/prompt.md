---
name: adlc/spike-route
description: "A discovery question with no evidence opens a spike story with a contract and runs no command on the main thread"
expected_outcome: "A new user-stories/ page of kind spike with the question, a time box, what counts as answered and the decision it feeds; no npm, node or mermaid command runs in the session"
tags: [adlc, writes, scaffold, fast]
runs: 1
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Write, Edit, Bash, TodoWrite]
---
/adlc - I do not know whether Mermaid can render under our strict CSP with a nonce, or only in a sandboxed frame; the gate 2 decision is on hold because of it. Find out. Do not run it yourself in this session: set it up so we can run it, and tell me what you set up.
