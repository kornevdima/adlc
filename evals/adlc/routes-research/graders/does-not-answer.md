---
type: llm
focus: last_message
---

PASS if the reply routes the request to the autoresearch skill (a research question is dispatched as a research run, as a stop at the story boundary, with a synthesis page in wiki/questions/ as the record) and does not itself answer how Mermaid should be rendered under a CSP.
FAIL if the reply answers the research question from its own knowledge, or improvises a step inside the loop instead of naming the route.
