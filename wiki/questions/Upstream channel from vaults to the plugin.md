---
type: synthesis
title: "Upstream channel from vaults to the plugin"
created: 2026-10-04
updated: 2026-10-04
tags:
  - adlc
  - plugin
  - distill
  - upstream
status: resolved
related:
  - "[[Parallel builder and tester revert each other's edits]]"
  - "[[Tester edits app code to prove a test bites]]"
  - "[[Dispatcher rules for writing ruling questions]]"
  - "[[Operator profile - learn engagement style from corrections]]"
---

# Upstream channel from vaults to the plugin

**Opened by** the operator on 2026-10-04: "there is no way to send back info for ADLC improvements from project using this plugin … maybe we can store adlc improvement proposals or bugs similar to operator profile".

**Outcome:** a lesson about the plugin, found in any vault that uses it, reaches the plugin repo without depending on someone remembering it. It also comes back closed when a release ships the fix.

## The gap

Gap C of [[Parallel builder and tester revert each other's edits]] ("distill only goes down, never up") was marked resolved on 2026-10-02. The fix was that distill tells the operator a lesson is general, with the proposed text. That's a conversation, not a store. Two days later:
- The vault-a run's approved design for a tester footprint check sat in its run ledger "for the epic's distill". The plugin session that reviewed "new proposals" looked only in this repo and missed it. It arrived because the operator pointed at the ledger.
- The cite-the-record lesson took the same path: a `proposed:` line in the vault's profile, then "file these changes in backlog for adlc".
- From this machine, `gh` can't reach GitHub (`x509: certificate signed by unknown authority`, 2026-10-04). So a GitHub-only channel would fail here.

## Ruling (operator, 2026-10-04)

"I think adlc-upstream.md works. let's do it." It's modelled on the operator profile. GitHub issues are optional; handing a file over by hand always works. No PRs to the plugin repo from vaults.

## Built (unreleased)

- **Format:** `skills/wiki/references/adlc-upstream.md`. The log is `wiki/meta/adlc-upstream.md` per vault.
  - Occurrence rows; `UP-nnn` entries on a repeat, for a plugin bug, or for an operator-approved design.
  - Status: `proposed`, `ratified`, `sent`, then `shipped (x.y.z)` or `declined`.
  - Each entry names the workaround to remove once shipped.
- **Writers:**
  - `/adlc` interjections (a correction about the plugin);
  - Step 4.4 distill (general lessons are filed, not only told);
  - `wrap-up` 7b;
  - manual mode's end-of-task step in the `wiki` skill;
  - `operator-profile.md` rule 8 points upstream lessons here.
- **Out:** `/adlc upstream` exports each ratified entry to `.raw/exports/upstream/<vault_key>-UP-nnn.md`.
  - The export is cleaned: no client, product or people names, domains or customer content, because the repo is public.
  - The operator reads it before it goes anywhere.
  - Then `gh issue create` if `gh auth status` passes and the operator says to send. The repo comes from the new `repository` field in `plugin.json`; the command is in `ask` in `permissions.md`.
  - Otherwise the operator copies the file into this repo's `.raw/upstream/`.
- **In (this repo):**
  - `.raw/upstream/` and `[upstream]` issues;
  - `AGENTS.md` § Key Conventions says to check them and the co-located vaults' logs when reviewing new proposals;
  - each report becomes a question page with `upstream: [<vault_key>/UP-nnn]`.
- **Closing:** `skills/adlc/references/upstream-shipped.md` lists shipped report keys by version. `/adlc` Before Starting (step 4) and `wrap-up` mark matching `sent` entries `shipped`, and list the workarounds that can come out.
- **README:** § Reporting back to the plugin. **Glossary:** ADLC upstream log.

## First log

Vault-a (`wiki/meta/adlc-upstream.md`, uncommitted there) was seeded with UP-001 to UP-004 (status `sent`, by hand) and one occurrence row: this channel's own gap. `upstream-shipped.md` already lists the four entries for 1.0.7, so they close when that release reaches the vault.

## Follow-up: redaction is a step with a check, not a sentence (2026-10-20)

The export step had a cleaning rule since 2026-10-16, and the plugin still leaked on 2026-10-20: a vault's directory name as its report key (copied verbatim from a ledger created under the old template), and on five plugin pages the vaults' story, epic, sprint, bug and test-case ids, run-ledger page names with line numbers, a commit hash, a source path with a symbol and a column name, and product nouns inside quoted corrections. Three causes: the rule ran at export, and the last two batches were read straight from the co-located ledgers with no export; the list named names and hashes, not ids, ledger names or symbols; nothing checked the key. A grep sweep found every leak, including one the cleaning session wrote itself a minute later. Prose did not hold, as with the env-file reports.

**Built (unreleased):**
- `skills/wiki/references/adlc-upstream.md` § Sending step 1: one redaction list for both ends (what goes out, what stays), the check command, and the key rule as a stop. § On the plugin side: three steps for the intake paths that skip the export: redact when reading a ledger directly, alias a key that is not opaque or collides, run the check before the commit.
- `skills/wiki/scripts/upstream_redact_check.py`, stdlib only, read-only. Rules: tracker ids (except `UP-nnn` and technical acronyms), sprint tokens, ledger and as-built names and `file:line` references, commit hashes, URLs and domains, concrete `src/` and `services/` paths, the vault's directory and service names (from `--vault` or `--names`), and the key's form. Exit 1 on a hit, 2 on bad input. Tested on the pre-clean pages as fixtures: 26 hits across the two pages and the snapshot script's docstring, all real; the cleaned pages, the shipped table and the raw reports pass; the directory-name key fails and the three opaque keys pass. It cannot see a product noun in prose; that stays a reading rule.
- `/adlc` Before Starting 3 (`/adlc upstream`), this repo's AGENTS.md § Upstream intake, `permissions.md` (an allow rule, like `relink.py`) and the README sentence.

**Open:** a vault that already exported under a non-opaque key renames its exports when it re-keys; the two raw reports from the five-report vault keep their client's form kinds until the operator decides.

## Open

- Field test: the first `/adlc upstream` export, checking that the cleaning holds on real ledger text.
- The other co-located vault (a service checkout, not a product wiki) has no log; one is created at its first plugin lesson.
- No eval case yet. A natural-language case ("the dispatcher approved a plugin-level design; where does it go?") could reuse the `adlc-vault` fixture.
