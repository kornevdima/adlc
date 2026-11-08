# Frontmatter Schema

Every wiki page starts with flat YAML frontmatter. No nested objects. Obsidian's Properties UI requires flat structure.

---

## Universal Fields

Every page, no exceptions:

```yaml
---
type: <source|entity|concept|domain|comparison|question|overview|meta|changelog|glossary>
title: "Human-Readable Title"
created: 2026-04-07
updated: 2026-04-07
tags:
  - <domain-tag>
  - <type-tag>
status: <seed|developing|mature|evergreen>
related:
  - "[[Other Page]]"
sources:
  - "[[.raw/articles/source-file.md]]"
---
```

**status values:**
- `seed`: exists, barely populated
- `developing`: has real content, not yet complete
- `mature`: comprehensive, well-linked
- `evergreen`: unlikely to need updates

---

## Type-Specific Additions

### changelog

One per folder, `_changelog.md`, linked from the folder's `_index.md`. Pages hold the current state; this page holds their history (`writing-style.md` § Pages that stay current). `updated:` is the date of the newest row.

```yaml
type: changelog
title: "Requirements changelog"
created: 2026-04-07
updated: 2026-04-07
tags: [changelog]
```

### glossary

One per vault, `wiki/glossary.md` (template and script: `glossary.md` in this folder). `link_skip:` lists the folders whose pages `glossary.py link` leaves unlinked (client documents).

```yaml
type: glossary
title: "Glossary"
status: active
created: 2026-04-07
updated: 2026-04-07
tags: [glossary, meta]
link_skip: [client-briefs/]
```

### source

Add these fields after the universal fields:

```yaml
source_type: article    # article | video | podcast | paper | book | transcript | data
author: ""
date_published: YYYY-MM-DD
url: ""
confidence: high        # high | medium | low
key_claims:
  - "First key claim from this source"
  - "Second key claim"
```

### entity

```yaml
entity_type: person     # person | organization | product | repository | place
role: ""
first_mentioned: "[[Source Title]]"
```

### concept

```yaml
complexity: intermediate  # basic | intermediate | advanced
domain: ""
aliases:
  - "alternative name"
  - "abbreviation"
```

### comparison

```yaml
subjects:
  - "[[Thing A]]"
  - "[[Thing B]]"
dimensions:
  - "performance"
  - "cost"
  - "ease of use"
verdict: "One-line conclusion."
```

### question

```yaml
question: "The original query as asked."
answer_quality: solid   # draft | solid | definitive
```

### domain

```yaml
subdomain_of: ""        # leave empty for top-level domains
page_count: 0
```

In a Mode ADLC vault `domains/` holds product domains, not research topics. A domain page adds the services that implement it and a link to each service's bounded-context note (in that service's code wiki); `domains/context-map.md` holds the relations between domains.

```yaml
responsibility: "What this domain is answerable for, in one line"
services:
  - web
  - billing
bounded_contexts:
  - "[[web bounded context]]"
upstream_of: []         # domains that consume this one's model
downstream_of: []       # domains whose model this one conforms to
```

---

## Work records (Mode ADLC)

The plugin owns these schemas; the BA worker creates the records and the delivery loop advances them. No field here is a roll-up: adlc collects no metrics and computes nothing from these dates. The records carry the fields so a computation outside the plugin (from the pages and from git) has what it needs. The record kinds, and what is not a record, are in [`records.md`](records.md).

### user-story (the backlog item)

One page per backlog item in `user-stories/`. `kind` says what sort of work it is; `type` stays `user-story` so the glossary and the filing table treat every item alike. The loop writes the dates at the transitions it already makes: `ready` when the verification contract is written, `started` when the builder is dispatched, `done` at the verified commit. Each transition adds one line to `history`. A human never edits these fields by hand.

```yaml
kind: feature            # feature | defect | risk | debt | spike
feature: "[[FEAT-012 Saved filters]]"
epic: "[[EPIC-003 Filtering]]"
sprint: "[[S07]]"
release: "[[R-1.4]]"
status: ready            # draft | ready | in-progress | done | blocked | dropped
ready: 2026-11-03        # the contract was written
started: ""              # the builder was dispatched
done: ""                 # the verified commit
history:
  - "2026-11-01 draft"
  - "2026-11-03 ready"
size: S                  # XS | S | M | L
priority: must           # must | should | could | wont
services:
  - web
depends_on:
  - "[[US-041 Filter bar]]"
caused_by: ""            # the bug page or verifier FAIL that opened a defect story
```

A spike (`kind: spike`) adds the fields of its own pipeline (`skills/adlc/references/routes.md` § Spikes):

```yaml
kind: spike
question: "Does the CSP allow Mermaid with a nonce, or only in a sandboxed frame?"
time_box: 2d             # the size of a spike is its time box
feeds: "[[ADR-WEB-4]]"   # the decision the answer goes into: an ADR, a product decision, a PRD section
mode: autonomous         # autonomous (the spike worker runs it) | operator-run (the person runs it, the plugin documents it)
log: ".raw/spikes/US-050.log"
result: ""               # answered | partial | not answered, set at the close
```

### epic

One page per epic in `epics/`. The epic page carries the grilling rulings table and the Gates table (`technical-planning.md`); its stories are listed by a query or by the board, never by hand.

```yaml
type: epic
title: "EPIC-003 Filtering"
status: planned          # planned | active | done | dropped
release: "[[R-1.4]]"
feature: "[[FEAT-012 Saved filters]]"
started: ""
done: ""
tags: [epic]
```

### sprint

One page per sprint in `sprints/`, named by its id (`S07.md`). A sprint is a time box: it holds stories from several epics, and a story names its sprint and its epic as two separate fields. The run ledger (`_run <EPIC-ID>.md`) stays in the same folder and is loop state, not a record.

```yaml
type: sprint
title: "S07"
goal: "Readers see diagrams without leaving the page"
start: 2026-11-03
end: 2026-11-14
status: planned          # planned | active | done
epics:
  - "[[EPIC-003 Filtering]]"
planned:
  - "[[US-042 Saved filters survive a reload]]"
tags: [sprint]
```

### release

One page per release in `releases/`. The release is the container the user sees: an epic cannot close without a `release:` link, and a test plan's `release:` points at the record.

```yaml
type: release
title: "R-1.4"
version: "1.4.0"
status: planned          # planned | released
date: ""                 # the day it shipped
epics:
  - "[[EPIC-003 Filtering]]"
tags: [release]
```

The body has two sections: **What the user gets** (plain words, one line per outcome) and **Stories closed** (filled at each epic close, or by the board).

### decision (product decisions, `decisions/`)

Every decision record says who decided, when, and on what evidence. `evidence` points at the message, page, spike or artifact version that carried the decision; a decision with no `decided_by` is a lint finding.

```yaml
type: decision
status: active           # proposed | active | superseded
decided_by: "product owner"
decided_on: 2026-11-03
evidence: "[[US-050 Mermaid under CSP]]"   # a spike, a page, a message reference or an artifact version
supersedes: ""
```

---

## Rules

1. Use flat YAML only. Never nest objects.
2. Dates as `YYYY-MM-DD` strings, not ISO datetime.
3. Lists always use the `- item` format, not inline `[a, b, c]`.
4. Wikilinks in YAML fields must be quoted: `"[[Page Name]]"`.
5. Keep `related` and `sources` as wikilinks, not plain URLs.
6. Update `updated` every time you edit the page content.
