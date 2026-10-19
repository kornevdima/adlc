---
type: synthesis
title: "Workers and processes left running after hand-back"
created: 2026-10-17
updated: 2026-10-20
tags:
  - adlc
  - workers
  - dispatcher
  - wrap-up
  - upstream
status: resolved
upstream: [vault-a/UP-006, vault-a/UP-012, vault-d/UP-001]
related:
  - "[[Upstream channel from vaults to the plugin]]"
  - "[[Parallel builder and tester revert each other's edits]]"
---

# Workers and processes left running after hand-back

**Opened from** two upstream reports from vault-a (`.raw/upstream/vault-a-UP-006.md`, ratified 2026-10-07; `.raw/upstream/vault-a-UP-012.md`, ratified 2026-10-10: "we need to have a check in wrap-up for this").

**Outcome:** a session ends with nothing of its own still running, and the next session's e2e tests the current build.

## What happened

- A worker hands back, and the harness shows it "stopped with background work of its own still running". It stays listed as live, which looks like it is still spending tokens. Seen 5× from 2026-10-04 to 2026-10-08: verifiers, testers and builders. One tester showed as running for about 7 hours with no live process.
- A process a worker started holds a port. On 2026-10-09 a stray production server on the e2e port made local e2e test an old build for a whole story.
- A builder's cleanup ran `pkill -f next-server` and killed another repository's dev server (an occurrence row in the vault, 2026-10-08).
- Every hand-back said "no background processes running". Nothing checked it, neither after the hand-back nor at the session end.

## Resolution (2026-10-17, unreleased)

- **Workers** (`feature-builder`, `feature-tester`, `feature-reviewer`, `feature-verifier`, `devops`, `scope-analyst`): a "Leave nothing running" rule. Stop every process you started, by PID or by the compose project you started. Never stop one you didn't start (no `pkill -f`). The report gains a `Left running:` line.
- **`/adlc` Step 2 § After every hand-back:** once the report is filed, the dispatcher checks the agent list and stops a worker that is still live.
- **`wrap-up` step 7c, "Leave nothing running":**
  - stop this session's subagents that are still listed as running;
  - list the processes on the run's ports with their owner, and stop only this session's, by PID;
  - stop the compose containers this session started, never removing volumes.

  The report carries `Left running: none`, or the list.
- **`permissions.md`:** `lsof -nP -iTCP` and `ps -p` are allowed (read-only). Stopping a process still prompts.

## Follow-up: the shared environment (vault-d/UP-001 and vault-a occurrences)

A second vault, vault-d, reported the other half of the same problem (UP-001, proposed 2026-10-10, 2×): a tester started the app's dev server as its own background task when the port was down, and a verifier left a background job. Both showed "running 40 min" after their reports, and the tester could not be stopped because a later verifier depended on its server. Stopping the stale task would have killed the server. The vault moved its dev server into a compose container and told workers "report a down server, don't start one".

Vault-a's occurrence rows of 2026-10-17 are the same family, four in one day: a tester ran the e2e suite without the session's port override, so the e2e config's `webServer` recreated the shared database and auth emulator on the wrong ports (three times that day, across two workers, with a packet rule in force); a tester restarted a shared emulator it had not started, which wiped every in-memory account, other sessions' included; a verifier cleared every account in the shared emulator to remove its own; worker default ports were taken mid-run by another session's servers.

**Resolution (2026-10-20, unreleased):** `feature-tester` § Shared environment and `feature-verifier` step 1:
- never start a dev server, database or emulator as a background child of the task; bring it up through the service's compose project, detached, or report `ENV_MISMATCH` and let the dispatcher start it;
- check the port is free and who holds it (`lsof -nP -iTCP:<port> -sTCP:LISTEN`) before starting anything that listens;
- carry every environment variable the service's wrapper or AGENTS.md sets (port overrides, the database name);
- never restart or recreate a container you did not start in this run; a stuck shared container is `ENV_MISMATCH`;
- (verifier) delete only the fixtures you created, by id or run tag, never a whole shared store.

## Open

- Vault-side: remove the packet line "before handing back, make sure no process or browser you started is still running" once 1.0.8 is installed; vault-d can drop "report a down server, don't start one" from its briefs.
- Field test: the next `/adlc` run and the next wrap-up in vault-a.
