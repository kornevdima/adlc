---
report: vault-a/UP-009
title: "Wrapper scripts swallow test-runner flags"
kind: improvement
plugin_version: 1.0.7
status: ratified (2026-10-07)
exported: 2026-10-16
---

# vault-a/UP-009 Wrapper scripts swallow test-runner flags

- **Key:** `vault-a/UP-009`
- **Kind:** improvement
- **Target:** `/adlc` Step 2.2 (contract: name the instrument) and the generic tester and verifier
- **Plugin version seen:** 1.0.7
- **Ratified by the vault's operator:** 2026-10-07

## What happened
A contract named a wrapper script as the instrument. The filter flag did not reach the runner through the nested `npm run`, so the whole suite ran instead of the filtered scenarios.

## Evidence
Seen twice in one vault: once in its first epic and again on 2026-10-06 (`npm run <prod-image e2e script> -- -g <pattern>` lost the `-g`).

## Proposed fix
In Step 2.2's name-the-instrument rule and in the tester and verifier: "When an instrument needs flags, name the direct runner command with its environment, not a wrapper script."

## Workaround in the reporting vault
A terrain bullet, "nested npm scripts swallow Playwright flags", in the service's local bindings.
