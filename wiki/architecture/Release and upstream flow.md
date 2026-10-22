---
type: flow
title: "Release and upstream flow"
created: 2026-10-22
updated: 2026-10-22
tags:
  - architecture
  - flow
  - release
  - upstream
status: active
related:
  - "[[Plugin architecture overview]]"
  - "[[Upstream channel from vaults to the plugin]]"
  - "[[Evals]]"
  - "[[Scripts]]"
---

# Release and upstream flow

How a lesson learned in a vault becomes a plugin change, and how a change becomes a version. The channel is described in [[Upstream channel from vaults to the plugin]]; this page is the as-built path.

## From a vault to this repo

1. **The vault records it.** A skill step that misled, a worker rule that failed, a script that broke: one row in the vault's `wiki/meta/adlc-upstream.md`. A repeat, a plugin bug, or a design the operator approved becomes an `UP-nnn` entry with a kind, a target and a proposed fix.
2. **The vault exports it.** `/adlc upstream` writes each ratified entry as a report with the mechanics and nothing that points back: no tracker ids, ledger names, hashes, URLs, source paths, product nouns or directory names, and a vault key that is an opaque alias (`vault-<letter>`). `upstream_redact_check.py --vault .` stops the export on a hit or a non-opaque key. The report becomes a GitHub issue titled `[upstream]` when `gh` works, or a file handed to this repo's `.raw/upstream/`.
3. **This repo files it.** Each report becomes a page in `wiki/questions/` with `upstream: [<key>/UP-nnn]`, carrying what happened, the resolution and what the vault does after the release. The plugin session also reads the co-located vaults' ledgers directly, so an entry can be filed here before the vault has exported it; the vault then adds the matching entry so it can close it.
4. **The fix lands** in the skill, reference, worker or script named as the target, following the placement rule of [[Shared references]]. A script that answers a report is checked on a copy of the reporting vault, and the numbers go on the question page.

## From a change to a version

1. **Evals** run locally, the fast set at least, the slow set for a release ([[Evals]]).
2. **The version** is bumped in four manifests at once: `.claude-plugin/plugin.json`, `.cursor-plugin/plugin.json`, `.cursor-plugin/marketplace.json`, `.github/plugin/marketplace.json`.
3. **The shipped table** `skills/adlc/references/upstream-shipped.md` gets one row per report: key, version, what changed. Vaults close their entries from this table at their next `/adlc` run, which looks the keys up in the installed plugin.
4. **Redaction** runs on every touched page, log line and reference: `upstream_redact_check.py --vault <a co-located vault>` for each vault's names, never `--vault .` in this repo. The hot cache, the log and the question pages are the usual places a name slips in.
5. **One commit**, `chore(plugin): <version>; <what shipped>`, no co-author trailer. The hot cache and the log entry record the release and the follow-ups each vault owes.
6. **The vaults upgrade** (`claude plugin marketplace update`, then reload), flip their entries to `shipped (<version>)`, and remove the workarounds each question page's Open section names.

## What stays private

A vault's product, client, people, paths and ids never enter this repo, whose remote is public. The rule is written at both ends (`adlc-upstream.md` § Sending it upstream in the vault, `AGENTS.md` § Upstream intake here) and enforced by the script; what the script cannot see, product and feature nouns and quoted names, is a reading rule before the commit.
