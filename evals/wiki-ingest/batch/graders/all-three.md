---
type: llm
focus: trace
---

PASS only if all three sources (outbox pattern, choreography sagas, idempotent consumer) got a source page, the resulting pages link each other (outbox <-> idempotent consumer, outbox <-> saga), `.raw/.manifest.json` lists all three, and wiki/index.md was updated with the new pages.
FAIL otherwise, naming what is missing.
