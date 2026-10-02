# Review policy (per service)

One typed record per service, `services/<svc>/wiki/reviews/_policy.md` (in a Mode B repo, `wiki/reviews/_policy.md`). It states what `feature-reviewer` checks and where the bar sits, so every review of that service uses the same bar instead of one re-assembled in each dispatch packet.

- **Who writes it:** `project-profile` seeds it from the template below when the repo has a wiki and no policy yet. The operator owns it after that; workers never edit it.
- **Who reads it:** the `adlc` dispatcher passes it verbatim in the reviewer's packet (Step 2.5). If it was not passed, `feature-reviewer` reads it itself. No policy → the reviewer uses the defaults below and says so in its record.
- **What it is not:** a root-level `REVIEW.md`, or a copy of AGENTS.md. Conventions and Don'ts stay in AGENTS.md; the policy only sets which passes run and how findings are weighed.

## Template

```markdown
---
type: review-policy
service: <svc>
updated: YYYY-MM-DD
---

# Review policy: <svc>

## Passes
All on unless struck out: correctness · conventions · reuse / simplification · efficiency · test coverage · test self-sufficiency · instrument reinvention.

## Severity
- **blocker:** wrong behaviour, data loss, security, a broken Don't. Always blocks.
- **major:** a spec divergence, a missing test for a risky path, a second way to do X. Blocks.
- **minor (nit):** anything else worth saying. Never blocks.

## Nit cap
At most 3 minor findings per review, the most useful first. Style the linter enforces is never a finding.

## Exclusions
Generated files, lockfiles, vendored code, snapshots and fixtures recorded by a tool. <add paths>

## Service-specific
<optional: extra passes or a stricter bar for named paths, e.g. "migrations/: every change is major until a rollback is shown">
```
