---
report: vault-a/UP-010
title: "The dispatcher calls a cause or a fix done without the instrument that sees it"
kind: improvement
plugin_version: 1.0.7
status: ratified (2026-10-07)
exported: 2026-10-16
---

# vault-a/UP-010 The dispatcher calls a cause or a fix done without the instrument that sees it

- **Key:** `vault-a/UP-010`
- **Kind:** improvement
- **Target:** `/adlc` Step 2 dispatcher rules, beside the shipped premise rule (vault-a/UP-001)
- **Plugin version seen:** 1.0.7
- **Ratified by the vault's operator:** 2026-10-07

## What happened
The shipped premise rule covers premises in ruling questions. These were claims of cause or completion, stated before the instrument that can see them had run.

## Evidence
Seen 3 times in one vault's operator correction log:
- 2026-10-03: a colour was called "the brand value" without measurement; measured, it was a 1.09:1 contrast;
- 2026-10-05: a bug's cause was inferred, and the operator answered "Prove the app first";
- 2026-10-06: a border colour was reported fixed without looking at the page that warns about it.

## Proposed fix
Dispatcher rule: "A cause is a hypothesis until a baseline separates it; a fix to a check the dispatcher can't run is 'pending confirmation' until whoever can see the check confirms it."

## Workaround in the reporting vault
A `proposed:` line in the vault's operator profile (2026-10-07).
