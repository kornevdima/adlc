---
type: llm
focus: trace
---

PASS only if the new source page has `confidence` and `key_claims` frontmatter, and at least one concept page (e.g. Transactional Outbox) was created or updated with wikilinks to related existing pages (Saga Pattern, CQRS or Event Sourcing) where relevant.
FAIL otherwise.
