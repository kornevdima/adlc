# ADLC upstream log: bugs and improvements for the plugin itself

The operator profile records how the **human** wants to work, and AGENTS.md records the **service's** traps. A third kind of lesson has no home in either: one about the **plugin**. Examples: a skill step that's missing, a worker rule that allows the wrong thing, a script that crashes. Every vault that uses the plugin will hit it again. Without a record it sits in a ledger's Carry-forward or in a chat, and the plugin never hears of it. In one production vault, an operator-approved design for a tester footprint check waited in a run ledger, "for the epic distill". The plugin side learned of it only when the operator pointed at the file.

> AGENTS.md : the service :: operator profile : the human :: adlc-upstream : the plugin.

## Where it lives

`wiki/meta/adlc-upstream.md` in the product wiki of each vault that uses the plugin. It's created the first time a lesson is filed (template below), and git-tracked like the rest of `meta/`. It holds the vault's own words, so it stays private. Only an export (below), cleaned and reviewed by the operator, leaves the vault.

## What goes here

A lesson whose fix belongs in the plugin: `skills/`, `agents/`, the scripts, the references or the templates. The test: **would every other vault that uses the plugin hit this too?**
- **Yes → here.** For example: the dispatcher states a status from `hot.md`; the generic tester may edit app code "temporarily"; `relink.py` misses a link form.
- **No, it's this service → AGENTS.md Don't** (or the repo-local worker).
- **No, it's this operator → the operator profile.**

This is target **upstream** in `operator-profile.md` rule 8. When a local fix was also made (in a repo-local worker, or in the profile), the entry names it as the workaround to remove once the plugin ships the fix.

## Template

```markdown
---
type: adlc-upstream
title: "ADLC upstream log"
vault_key: <opaque alias, e.g. vault-a; never the repo, directory, client or product name>
plugin_version_seen: 1.0.6
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - meta
  - adlc
status: evergreen
---

# ADLC upstream log

## Entries
<!-- one block per lesson that occurred at least twice, or one plugin bug (below). Status: proposed → ratified (the operator edits it) → sent → shipped (x.y.z) | declined. -->

### UP-001 Short title of the defect or improvement
- **Kind:** bug | improvement
- **Target:** `agents/feature-tester.md` · `/adlc` Step 2
- **Status:** proposed
- **Seen:** 2× — YYYY-MM-DD US-175 ([[record]]), YYYY-MM-DD US-179 ([[record]])
- **What happened:** the event, in two or three lines
- **Proposed fix:** the plugin text or mechanism, as concrete as the evidence allows
- **Workaround here:** the local line or worker edit to remove once shipped, or "none"
- **Sent:** YYYY-MM-DD, GitHub issue URL | export file handed over manually

## Occurrences
<!-- single occurrences wait here; a second one makes an entry. The event only, no verdicts. -->
| Date | Where (story / run / session) | What the plugin did | Record |
|---|---|---|---|
```

## Rules

1. **Log the occurrence; propose on repeat.** One occurrence is a row under Occurrences. A second one, in this vault or the same row seen again, makes an `UP-nnn` entry with status `proposed`. This is the same threshold as `/adlc distill`.
2. **A plugin bug needs only one occurrence.** A script crash, a step that contradicts another step, a template that doesn't parse, or a rule that permits exactly the failure it should prevent goes straight to an entry. It is a defect, not a pattern.
3. **The operator ratifies.** They set `Status: ratified` by editing the line, or say so ("Good", "send it"). The dispatcher never ratifies its own proposal.
4. **Name the evidence, not a summary of it.** Each occurrence links the record it rests on (a ledger line, a bug page, a correction-log row), as in the dispatcher's question rules (`/adlc` Step 2 § Writing a ruling question).
5. **One lesson per entry.** Two fixes that share evidence get two entries that link each other, so each can ship or be declined on its own.
6. **Keep the entry after it ships.** Set `shipped (x.y.z)`, remove the workaround it names, and keep the block as history. Don't delete it.

## Sending it upstream: `/adlc upstream`

Run on demand, at `/adlc distill` (Step 4.4), or when `wrap-up` reports ratified entries.

1. **Export.** For each `ratified` entry, write `.raw/exports/upstream/<vault_key>-UP-nnn.md`. It is a self-contained report: title, kind, target, plugin version, what happened, the proposed fix and the evidence.
   - **Clean it:** no client, product or people names, no repo or directory names (this vault's or its services'), no domains, URLs, secrets or customer content.
   - No pointers into private repos: no commit hashes, no page titles that name product features; say "the run ledger" or "a sprint page".
   - Turn wikilinks into short quotes with a role ("the run ledger, 2026-10-04: …"), and generic paths (`src/db/<module>.ts`).
   - The plugin repository may be public.
   - The report's key is `<vault_key>/UP-nnn`. The key is an opaque alias (`vault-a`), because it travels into every plugin page and release note that cites the report.
2. **The operator reads the export.** Sending is an outward action: show it, and send only on their word.
3. **Send. Use GitHub when it works; otherwise hand it over manually.**
   - **GitHub:** only when `gh auth status` passes, and the operator says to send it.
     ```bash
     gh issue create -R <repository from the plugin's .claude-plugin/plugin.json> \
       --title "[upstream] <vault_key>/UP-nnn <title>" --body-file .raw/exports/upstream/<vault_key>-UP-nnn.md
     ```
   - **Manual:** some environments can't reach GitHub (a proxy, no `gh`, a policy). Tell the operator where the file is. They can copy it into the plugin repo's `.raw/upstream/`, or paste it into a new issue.
4. **Record it.** Set `Status: sent` and `Sent:` (the date, plus the issue URL or "exported, handed over").

## Closing the loop

The plugin lists the reports it has shipped in `skills/adlc/references/upstream-shipped.md`: report key, plugin version, what changed. `/adlc` Before Starting and `wrap-up` check the vault's `sent` entries against that list in the installed plugin. For each match:
- set `shipped (x.y.z)`;
- update `plugin_version_seen`;
- tell the operator which workarounds can now be removed.

They remove them, or approve the removal.

## On the plugin side

The plugin repo takes reports in `.raw/upstream/` (manual), and from issues titled `[upstream]`. Each one becomes, or joins, a page in its `wiki/questions/` with `upstream: [<vault_key>/UP-nnn]` in the frontmatter. When a release ships the fix, it adds a row to `upstream-shipped.md`.

The plugin wiki, its commits and its release notes follow the same cleaning as the export. A vault is named only by its `vault_key`, a service as `<service>`, and paths stay generic. This holds when a plugin session works with a co-located vault and can read its real names: what it learns there is filed under the key.
