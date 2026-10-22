---
type: synthesis
title: "Pages carry their history inline"
created: 2026-10-21
updated: 2026-10-21
tags:
  - adlc
  - wiki
  - writing
  - upstream
status: resolved
upstream: [vault-e/UP-002]
related:
  - "[[Identifiers with no glossary]]"
  - "[[One writing method for every human reader]]"
  - "[[Upstream channel from vaults to the plugin]]"
---

# Pages carry their history inline

**Opened from** a vault's standing ruling, read from its co-located ledger and filed here in redacted form (the vault adds the matching entry to its own upstream log so it can close it). Kind: design the operator approved.

**Outcome:** a wiki page holds the current state only; its history lives in the folder's `_changelog.md`, and the plugin's own skills no longer tell agents to write history into pages.

## What happened

- Over seven weeks of BA work, agents recorded every change inside the page it changed: dated update and correction sections, as-filed markers, strikethrough, "was X, now Y" wording. Registers became stacks of dated tables. The operator's words: the content of the page should be up to date; this information looks like meta.
- The vault swept 67 files in one session, folded every dated block into current content and moved the history into ten per-folder `_changelog.md` files linked from each `_index.md`. A day later the operator struck the same pattern in client documents (dates of our own checks, an internal "supersedes" note).
- The plugin was the source of the habit: `wrap-up` step 5 told agents to add an "as-built diverges" note and step 6 a pointer sentence naming the ADR that retired the page, both inside the page; `wiki-ingest` and `save` said "update the existing page" with no shape for the update. Across the other vaults on the same machine, 24 and 26 pages in the two largest carried such markers, and none had a changelog file.

## Resolution (2026-10-21, unreleased)

- **`writing-style.md` § Pages that stay current:** the rule, the exemptions (`sources/`, `log.md`, `meta/` ledgers and boards), the changelog shape (`Date | Page | Change`, newest first, linked from `_index.md`), frontmatter `status: superseded` + `superseded_by:` as the only in-page history, an unresolved `[!contradiction]` callout as current state.
- **`wiki` skill:** the scaffold creates `_changelog.md` beside every `_index.md`; the vault AGENTS.md template carries the rule in § Conventions and a filing-table row; `frontmatter.md` adds the `changelog` type; `modes.md` notes it on the folder map.
- **`wrap-up` steps 5, 6 and new 6a:** a shipped plan is rewritten to the as-built state, a retired page is flipped in frontmatter, every rewrite gets its changelog row, and the check script runs before the caches are refreshed. **`wiki-ingest`, its subagent, `save`, `ba-suite-subagent`, `architecture-subagent`, `doc-writer`, `/adlc` step 8 and Constraints:** an update rewrites to current state plus one changelog row; workers may write the folder changelog, never the dispatcher's logs.
- **`skills/wiki/scripts/page_history_check.py`** (new, stdlib): lists `history` hits in page bodies and `changelog-missing` / `-unlinked` / `-stale` folders; exit 1 on findings. `wiki-lint` checks 8b and 8c run it; the subagent pastes its output; `permissions.md` allows it.
- Checked on a copy of the reporting vault: 0 history hits after its sweep, the two structural gaps it still had, and nothing on the eval fixtures. On this repo's own wiki: 2 hits, both prose about rule supersession on concept pages, left.

## Open

- Vault-side after 1.0.9: add `_changelog.md` to the folders that still lack one (client documents among them) and an `_index.md` where a changelog has no index; bump the three changelog `updated:` dates; keep the local rule text or replace it with the template's.
- The check cannot tell a quoted operator sentence from page content; lint reports such hits and leaves them.
