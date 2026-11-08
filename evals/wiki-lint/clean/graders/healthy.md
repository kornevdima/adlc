---
type: llm
focus: last_message
---

The vault is clean: every wikilink resolves, no page is an orphan, no claims contradict. PASS if the report gives a healthy verdict and reports no dead links, orphans or contradictions. WARN and INFO rows are fine: missing optional frontmatter, a missing changelog or index file, a concept that could get its own page, a page reached only from meta pages. A WARN count above zero is not a failure.
FAIL if it reports a dead link, orphan or contradiction that does not exist.
