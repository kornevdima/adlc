# Plugin evals

Cases for `claude plugin eval`, run **locally** before each version bump (no CI). Each case is `evals/<skill>/<case>/` with `prompt.md` (frontmatter + the user prompt), `graders/*.md`, and, when it needs a starting vault or repo, `case.yaml` + `scaffold.sh`.

## Run

```bash
# release check: every case, workspaces built from fixtures, write tools granted
# (the two `network` cases cannot pass here, see Tags; the rest should be 1.00)
claude plugin eval . --scaffold --allow-tools Write Edit Bash --ablation none --no-publish -j 4

# quick pass (cheap, about $2)
claude plugin eval . --scaffold --allow-tools Write Edit --ablation none --no-publish --tag fast -j 4

# one case
claude plugin eval . --scaffold --allow-tools Write Edit --ablation none --no-publish --case 'wiki-ingest/single'
```

- `--scaffold` is needed for any case with a `scaffold.sh`; it runs our own fixture scripts as you.
- `--allow-tools` grants write tools; cases tagged `writes` fail without it.
- Every case sets `runs: 1` to keep cost down. Add `--runs 3` for a release decision: single runs are noisy.
- Drop `--ablation none` to also run a no-plugin baseline arm (double cost) and see how much the plugin adds.
- Results and the HTML report go to `evals/results/` (git-ignored).

## Tags

| Tag | Meaning |
|---|---|
| `fast` | under a minute, cents each |
| `slow` | many turns; minutes and dollars |
| `read-only` | no write tools needed |
| `writes` | needs `--allow-tools Write Edit` (some also `Bash`) |
| `scaffold` | builds a workspace from `_fixtures/` |
| `network` | does web research (autoresearch). Cannot pass under `claude plugin eval`: the runner's sandbox allows no outbound network (`network.allowedDomains: []`) and grants no web tool, so every question comes back blocked. A sandboxed run still shows the loop stopping honestly, with a plan, no invented sources and a report of what blocked it; the two cases are for a run by hand with network |
| `needs-deps` | needs local tools (e.g. a .docx library for ba-export) |
| `regression` | pins a fixed defect |

## Fixtures

`_fixtures/use.sh <layer>...` copies layers into the case workspace in order. Layers: `vault-base` (a small CQRS / event-sourcing vault with hot, index, log, a source and three concepts), `lint-defects` (orphan, dead link, contradiction), `raw-outbox`, `raw-three`, `autoresearch-resume` (an interrupted plan), `repo-fresh`, `repo-agents` (an AGENTS.md with custom sections), `ba-checkout`, `wrapup-changes`, `adlc-vault` (a standalone Mode ADLC vault: mission control, operator profile, a fixed and an open bug, a Mermaid CSP story with a service spec; mission control is stale on purpose). Special steps: `@commit` (git init + commit so far) and `@large` (60 generated pages + `wiki/index.json`).

## Writing graders

- Prefer deterministic graders: `file_exists`, `regex` on a named file (`target: {source: file, path: ...}`), `tool_used` with `min`/`max`.
- "Never called" needs **both** `min: 0` and `max: 0` (the default `min` is 1).
- `input_match` is tested against the whole JSON of the tool's input, content included. A "did not write this file" check anchors on the path, `'"file_path"\s*:\s*"[^"]*wiki/concepts/'`; a bare `'wiki/concepts/'` also fires on a lint report or a source page that only mentions the folder, which is how `wiki-lint/clean` and `wiki-ingest/single` failed on 2026-11-08.
- An `llm` grader with `focus: trace` sees about the first 20,000 characters of the trace, and the SessionStart hook output comes first; a long run's writes never reach the judge. Grade files instead: `regex` or `llm` on `{source: file, path}`, or `regex` with `target: files` (the list of paths created during the run).
- A prompt that starts with a slash command expands directly and makes no `Skill` tool call, so `tool_used: Skill` only fits natural-language prompts.
- A regex pattern must not contain `---` (it ends the frontmatter); write `-{3}`.

## Not yet converted

The graphify skills (`graphify-ingest`, `-query`, `-path`, `-explain`, `-update`) still use `skills/<name>/evals/` (the `graphify-ingest` G1–G5 runner and fixture app). `product-management-layer` keeps its own E1–E8 runner. `adlc` has two older read-only cases, `adlc/ruling-cites-record` and `adlc/ruling-outcome-first`, which pin the Step 2 question rules. They don't discriminate yet: the no-plugin baseline also passes (Δ 0.00, 2026-10-04), because the field failures happened deep into long sessions. Keep them as regression pins. The worker agents have no cases yet.

Run with 1.3.0 on macOS (2026-11-09, Claude Code 2.1.319): 28 of 30 cases at 1.00 once the `input_match` graders were anchored (above); the two `network` cases cannot pass in the runner's sandbox. The 1.3.0 cases are `adlc/routes-research` (a research request lands on the autoresearch route), `adlc/spike-route` (a discovery question opens a spike story and runs no command), `adlc/acceptance-list-back` (a one-word reply to five items produces a list-back, not five rulings) and the slow `wiki/scaffold-adlc` (the product and work folders, `board.md`, `catalog-info.yaml`, the How we work section). The `adlc-vault` fixture carries an epic record with a Gates table, a release record and the 1.3.0 story frontmatter.
