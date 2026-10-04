---
type: regex
pattern: '^(?=[\s\S]*outbox-pattern)(?=[\s\S]*saga-choreography)(?=[\s\S]*idempotent-consumer)'
target:
  source: file
  path: .raw/.manifest.json
---
