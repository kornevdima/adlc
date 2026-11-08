---
name: adlc/acceptance-list-back
description: "A one-word reply to a five-item ruling list produces a list-back and one question, not five recorded rulings"
expected_outcome: "The reply lists the five items it takes as accepted and asks once; no ruling, decision or epic page is written in this turn"
tags: [adlc, read-only, scaffold, fast]
runs: 1
max_turns: 15
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Write, Edit]
---
/adlc - at the last stop you asked me five things about the Mermaid story: (1) nonce or blob for the script, (2) keep the strict CSP as it is, (3) render on the client, not at build time, (4) a sandboxed iframe as the fallback, (5) ship it in R-1.0. Fine, go ahead.
