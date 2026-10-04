---
name: adlc/ruling-cites-record
description: "A ruling question on which bugs to fix sources the bug's status from its page, not from a stale hot.md"
expected_outcome: "BUG-018 is not offered as an open bug to fix; the reply says it is fixed and cites its bug page or commit f265115"
tags: [adlc, read-only, scaffold, regression]
runs: 1
max_turns: 25
timeout_seconds: 400
allowed_tools: [Read, Glob, Grep, Skill]
---
Run the adlc dispatcher on this vault, but only up to the first ruling: before US-200 starts I want to decide which of the open bugs we fix in S07. Mission control has them: BUG-018 and BUG-023. Write the question for me in your reply, with options and your recommendation. Don't dispatch any workers and don't edit anything.
