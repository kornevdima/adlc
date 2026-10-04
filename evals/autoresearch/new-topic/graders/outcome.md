---
type: llm
focus: trace
---

PASS only if all of these hold in the trace:
- a research plan was written with 3 to 7 questions, and no active `_plan` file is left at the end (it was deleted at close-out);
- a synthesis page for the topic was written in wiki/questions/ and it has an "Open Questions" section;
- at least 3 new source pages were written, each with `confidence` and `key_claims` frontmatter;
- wiki/index.md and wiki/hot.md were updated;
- no more than 15 new content pages were created (_index pages excluded).
FAIL otherwise, naming the first item that fails.
