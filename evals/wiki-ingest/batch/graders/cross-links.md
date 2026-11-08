---
type: regex
pattern: '^(?=[\s\S]*\[\[[^\]]*idempotent[ -]consumer)(?=[\s\S]*\[\[[^\]]*saga)'
flags: i
target:
  source: file
  path: wiki/sources/outbox-pattern.md
---
