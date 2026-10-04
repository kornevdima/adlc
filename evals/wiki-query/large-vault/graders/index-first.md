---
type: llm
focus: trace
---

PASS if the agent consulted wiki/index.json (Read, grep or jq) or wiki/index.md to locate candidate pages before opening them, and did not read most of the 65 concept pages one by one.
FAIL if it read pages broadly without using the index.
