---
type: llm
focus: trace
---

PASS only if all of these hold in the trace:
- the agent found the existing plan "_plan Research Change Data Capture Tools" and resumed it instead of starting a new plan;
- it researched Q2 (Debezium vs AWS DMS vs Maxwell) and Q3 (operational pitfalls), and did not research Q1 again (no new source page defining CDC);
- the existing source page cdc-overview was kept;
- a synthesis page covering the CDC topic was written, and the plan file was deleted at the end;
- wiki/index.md and wiki/hot.md were updated.
FAIL otherwise, naming the first item that fails.
