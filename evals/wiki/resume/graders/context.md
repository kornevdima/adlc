---
type: llm
focus: last_message
---

PASS if the reply reports the vault's recent context (the CQRS Journey ingest and its concept pages) and suggests the next action from hot.md (ingest a source on the transactional outbox pattern), without re-scaffolding the vault.
FAIL if it starts a new scaffold or ignores the existing context.
