---
name: obsidian-markdown/convert-gfm
description: "Convert a GFM note to OFM with wikilinks and a callout"
expected_outcome: "[[CQRS]] and [[Saga Pattern]] wikilinks, a > [!warning] callout, frontmatter kept, no broken syntax"
tags: [obsidian-markdown, read-only, fast]
runs: 1
max_turns: 6
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
---
Rewrite this GitHub-flavored Markdown note into correct Obsidian Flavored Markdown. Use wikilinks for the internal links and a callout for the warning. Reply with the rewritten note only.

```markdown
---
title: Outbox relay
tags: [architecture]
---

# Outbox relay

The relay reads the outbox table, see [CQRS](./CQRS.md) and [Saga Pattern](../concepts/Saga%20Pattern.md).

**Warning:** the relay must publish in commit order, or consumers see events out of sequence.

- [ ] add a dead-letter queue
```
