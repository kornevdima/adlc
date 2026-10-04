---
name: adlc/ruling-outcome-first
description: "A CSP ruling question opens with what the Mermaid library does and what the reader sees, before the mechanisms"
expected_outcome: "The question first says mermaid injects its own <style> (blocked, so diagrams render unstyled), then gives the mechanism options; one decision"
tags: [adlc, read-only, scaffold, regression]
runs: 1
max_turns: 25
timeout_seconds: 400
allowed_tools: [Read, Glob, Grep, Skill]
---
Run the adlc dispatcher for US-200, but only up to the CSP ruling it needs from me (nonce, template, blob or sandbox, per mission control). Write that question in your reply, with options and your recommendation. Don't dispatch any workers and don't edit anything.
