---
report: vault-a/UP-008
title: "Mass connection failures on a dev server are environment, not code"
kind: improvement
plugin_version: 1.0.7
status: ratified (2026-10-07)
exported: 2026-10-16
---

# vault-a/UP-008 Mass connection failures on a dev server are environment, not code

- **Key:** `vault-a/UP-008`
- **Kind:** improvement
- **Target:** `agents/feature-verifier.md` step 6 (restart once) and `agents/feature-tester.md`
- **Plugin version seen:** 1.0.7
- **Ratified by the vault's operator:** 2026-10-07

## What happened
The generic step 6 allows one restart for one scenario. A long full e2e run that exhausts a Next.js dev server fails many unrelated files with connection errors. Workers either re-ran everything or listed each failure as a new flake.

## Evidence
Seen 15+ times in one epic; for example, one round had 21 failures across 10 files, all green after one dev-server restart, and another logged a dev-server memory restart in the middle of the run.

## Proposed fix
"Connection-class failures across unrelated files (`ERR_EMPTY_RESPONSE`, `socket hang up`, `ECONNRESET`, chunk-load errors) are the dev server: read its log for a restart or memory message, restart it once, rerun only the failed files, and record both runs. Assertion failures are never retried into green."

## Workaround in the reporting vault
A terrain bullet, "the dev server fails under a long full e2e run", in the service's local bindings.
