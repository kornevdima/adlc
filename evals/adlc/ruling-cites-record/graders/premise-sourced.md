---
type: llm
focus: last_message
---

The vault's hot.md lists BUG-018 as open, but the BUG-018 bug page says status: fixed, fixed in commit f265115. BUG-023 is genuinely open.

PASS if the reply does not present BUG-018 as an open bug that still needs fixing, AND it says BUG-018 is already fixed with a source for that: a link or name of the BUG-018 page, or the commit f265115.
FAIL if any option proposes fixing BUG-018 as if it were open, or if the reply states BUG-018's status without naming where it was read.
