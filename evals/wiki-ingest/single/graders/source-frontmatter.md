---
type: regex
pattern: '^(?=[\s\S]*^confidence:)(?=[\s\S]*^key_claims:)'
flags: m
target:
  source: file
  path: wiki/sources/outbox-pattern.md
---
