---
name: ba-export/checkout-docx
description: "Render the checkout feature deliverables to .docx without touching the wiki"
expected_outcome: "A .docx under .raw/exports/ built from the feature, requirement and story pages; wiki unchanged"
tags: [ba-export, writes, scaffold, needs-deps]
runs: 1
max_turns: 60
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
---
Export the BA deliverables for the 'checkout redesign' feature from the wiki into a Word document.
