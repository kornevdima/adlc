---
type: synthesis
title: "Wiki maintenance edits blocked in ADLC vaults"
created: 2026-10-02
updated: 2026-10-02
tags:
  - adlc
  - plugin
  - permissions
  - wrap-up
  - epic-close
status: resolved
related:
  - "[[Configurable subagent models per host]]"
  - "[[Integrate the wiki toolset into the ADLC workers]]"
---

# Wiki maintenance edits blocked in ADLC vaults

**Opened from live use** (vault-a, EPIC-001 close, 2026-10-02). The operator asked for this to be fixed in the plugin, so that every vault the plugin scaffolds can do routine wiki maintenance without being blocked.

## What happened

1. `/adlc` Step 4.3 folded `_run EPIC-001.md` into an as-built page and **deleted the ledger**.
2. 23 wikilinks on 13 live pages still pointed at `[[_run EPIC-001]]`. These were the overview, the index, six sprint packs, three bug pages, an ADR and the operator profile.
3. The dispatcher tried a bulk relink with `sed -i '' 's/\[\[_run EPIC-001.../[[EPIC-001 As-built.../g'` over those files.
4. The **auto-mode classifier denied it** without an explanation. The vault's `.claude/settings.json` (built from `skills/wiki/references/permissions.md`) allows `Edit(//<vault>/**)` but has no rule for bulk in-place shell edits. Auto mode judges such a command on its own, whatever the file-edit allow rules say.
5. The denial rules forbid a workaround, so the work was handed back to the operator. They approved a page-by-page fix with the Edit tool: 13 files, 23 links, many tool calls for a mechanical change.

## Root causes

- **A. The epic-close step leaves dangling links.** Step 4.3 deletes the ledger but never repoints the pages that link to it. Sprint packs, bug pages and rollups link the ledger all through the run, as the `adlc` skill and `technical-planning.md` tell them to. So every epic close produces dead links.
- **B. The permissions profile has no wiki-maintenance path.** `permissions.md` covers git, search, npm, docker and workers. It says nothing about:
  - bulk Markdown rewrites (relinks, renames, frontmatter flips across many pages);
  - auto mode, where the classifier, not the allow list, makes the call.

## Side finding

`permissions.md` uses `Write(//<VAULT_PATH>/**)` and `Write(//etc/**)`. Current Claude Code matches every file-writing tool through `Edit(path)` rules, and `Write(path)` rules are not matched by file permission checks. Those template lines do nothing. Drop them, or replace them with `Edit(...)` in the deny list.

## Proposed fix (to rule on before building)

1. **Relink at epic close.** Before Step 4.3 deletes the ledger, it repoints every live `[[_run <EPIC>…]]` link to `[[<EPIC> As-built…]]`. It keeps aliases and anchors, and leaves `log.md`, log archives and dated lint reports alone (they are history). `wrap-up` should flag any links that remain.
2. **Ship a deterministic relink tool instead of ad-hoc `sed`.** For example, `skills/wiki/scripts/relink.py --from "<old>" --to "<new>" --vault wiki/ [--exclude log.md …]`. It does a dry run by default and reports per-file counts, and `wiki-lint` reuses it for its dead-link fixes. The profile can then allow exactly that script, e.g. `Bash(python3 <plugin>/skills/wiki/scripts/relink.py:*)`. That is much narrower than `Bash(sed:*)`, which would allow `sed -i` on any path.
3. **Document auto mode in `permissions.md`.** Explain that the classifier, not the allow list, decides on shell edits in auto mode. Recommend that the operator add a path-scoped `autoMode.allow` rule in **user** settings (for example "in-place edits to Markdown under `<vault>/wiki/` are routine wiki maintenance"). Explain why it doesn't go in the checked-in project file: classifier rules in a repo could be planted by anyone who can commit. Check against current Claude Code whether project-level `autoMode` is honoured at all before recommending either place.
4. **Fix the side finding** (`Write(...)` → `Edit(...)`).

## Done when

- an epic close in a test vault leaves no `[[_run …]]` link outside history;
- a vault scaffolded from the updated profile can run the relink in auto mode without a denial;
- `permissions.md` documents auto mode, and its template has no `Write(path)` rules.

## Resolution (2026-10-02)

Built all four, as proposed:
1. **Relink at epic close:** `skills/adlc/SKILL.md` Step 4.3 runs the relink (dry run, then `--apply`) before it deletes the ledger. `wrap-up` flags any `[[_run …]]` link left on a live page when no ledger survives.
2. **`skills/wiki/scripts/relink.py`:** a dry run by default. It keeps aliases and anchors, lists anchored links to check, handles embeds, path-qualified targets and a `.md` suffix, and skips code. It leaves `log.md`, `log-archive*.md` and `lint-report-*.md` alone. `wiki-lint` points at it for renamed or folded pages. Tested on a scratch vault. A dry run on vault-a finds 0 links left (they were relinked by hand) and skips its log, archive and lint report.
3. **Auto mode in `permissions.md`:** checked against the Claude Code docs (`auto-mode-config`, `permissions`). A narrow `permissions.allow` rule is resolved before the classifier, so the template allows `Bash(python3 *skills/wiki/scripts/relink.py *)`. The classifier never reads `autoMode` from project settings, so the template has none. Other wiki maintenance can go in an operator's **user** `autoMode.allow`, which is their call.
4. **Side finding:** the template no longer has `Write(path)` rules. The allow-list line is gone, deny uses `Edit(//etc/**)`, and the mechanism text says `Edit(path)` governs every file-writing tool.

**Still to field-test:** an auto-mode epic close in a vault scaffolded from the new profile. Existing vaults need the new allow rule added by hand.

## Evidence

Vault-a, 2026-10-02:
- `wiki/log.md`, the entry "S07 CLOSE + EPIC-001 CLOSE";
- `meta/operator-profile.md`;
- `planning/EPIC-001 As-built.md` (the fold).
