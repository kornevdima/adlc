# adlc

**Agentic Development Life Cycle harness.** Agent = Model + Harness — this is the harness: a persistent knowledge substrate, role skills that work it, and a delivery loop that ships verified stories through it. Formerly `claude-mem`.

Built on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — the same pattern Google has since standardized as the [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) (OKF). Code-graph layer powered by [graphify](https://github.com/safishamsi/graphify).

## The Stack

| Layer | What it is | Key pieces |
|---|---|---|
| **Knowledge substrate** | A compounding Obsidian wiki vault, OKF-aligned, plus an optional structural code graph. Every source ingested, every question answered from it, zero manual filing. | `wiki`, `wiki-ingest`, `wiki-query`, `wiki-lint`, `save`, `autoresearch`, `graphify-*` |
| **Role skills** | BA, product, and architecture methods that read and write the substrate — requirements, stories, specs, governance. Methods are bundled; no external plugins. | `product-management-layer`, `ba-export`, bundled BA + shift-left references |
| **Delivery orchestration** | Mode ADLC: a plan-driven loop that works an epic story by story, dispatching build → test → review → verify workers, committing with trace IDs, keeping a live mission-control board. | `adlc`, `wrap-up`, 14 subagents |
| **Project bindings** | Per-repo calibration: AGENTS.md profiling, repo-local worker specializations distilled from each run. | `project-profile`, `/adlc distill` |

The operator model: the engineer refines and plans in a **grilling session** (the one stage that never runs unattended), then delegates to the loop and reviews evidence — records, boards, and diffs, not a 700k-token transcript.

## Install

### Persistent install — every Claude Code session

```bash
claude plugin marketplace add /path/to/adlc
claude plugin install adlc@adlc-marketplace
claude plugin list
```

After editing source files: `claude plugin marketplace update adlc-marketplace` then `/reload-plugins` in-session.

### Active development — fastest edit-test loop

```bash
claude --plugin-dir /path/to/adlc
```

Before a version bump, run the eval suites locally (no CI): `claude plugin eval . --scaffold --allow-tools Write Edit Bash --ablation none --no-publish -j 4`. Cases, fixtures, tags and grader rules: [`evals/README.md`](evals/README.md).

### Other options

- **Cowork zip upload** — zip the repo and upload via Cowork UI (no CLI required).
- **GitHub-hosted marketplace** — push to GitHub, then `claude plugin marketplace add <github-url>` in any project.

### Vault setup

Open the project folder in Obsidian, then run `/wiki` (or `/adlc:wiki` when installed as a plugin) inside Claude Code. The wiki skill scaffolds the vault structure on first use.

### Code-graph setup (optional, for code projects)

```bash
bash bin/setup-graphify.sh                     # install graphifyy globally (requires Python >=3.10,<3.14)
bash bin/setup-graphify.sh /path/to/your-app   # also pin to a specific code project
```

## Skills

### Knowledge substrate

| Skill | Trigger |
|---|---|
| `/wiki` | Setup, scaffold (modes, concerns, ADLC topology), route to sub-skills |
| `ingest [source]` | Single or batch source ingestion from `.raw/` |
| `query: [question]` | Answer from wiki content (cache-first; `index.json` locator on large vaults) |
| `lint the wiki` | Health check: orphans, dead links, stale claims, graph staleness |
| `/save` | File the current conversation as a wiki note |
| `/autoresearch [topic]` | Plan-driven autonomous research: resumable question plan, one subagent per question |
| `/wiki-faq` | In-session help: requirements, workflow, troubleshooting, glossary |
| `obsidian-markdown` / `obsidian-bases` | Obsidian Flavored Markdown and `.base` database files |

### Code graph

| Skill | Trigger |
|---|---|
| `/graphify-ingest` | Build the structural code graph, file summaries into `wiki/code/` |
| `/graphify-update` | Incremental rebuild after a feature; preserves community labels |
| `/graphify-query` / `/graphify-path` / `/graphify-explain` | BFS/DFS traversal, shortest path, node + neighbors (no LLM cost) |

### Roles and delivery

| Skill | Trigger |
|---|---|
| `/adlc [epic-or-story]` | The delivery loop: readiness gate, run ledger, story-by-story worker dispatch, epic close |
| `/adlc distill` | Fold a run's hard-won knowledge into repo-local worker files |
| `/wrap-up` | Session sync: down/up-propagate across wikis, reconcile boards, refresh caches |
| `/product-management-layer` | Gate 0 governance: tool approval, buy-vs-build TCO, compliance scoping |
| `/ba-export` | Render wiki BA deliverables to formal Office documents |
| `/technical-writer` | Documents for a human reader: client briefs and question packs, help pages, the wording of stories and requirements, change reports; source and translation kept in step. Method: [`writing-style.md`](skills/wiki/references/writing-style.md) |
| `/project-profile` | Scan a repo, generate/augment its AGENTS.md |

Non-engineers bring a need in by dropping a five-heading note (problem, outcome, who is affected, constraints, open questions) into `.raw/intake/`; the next ingest turns it into requirements and stories. Template: [`modes.md` § Intake for non-engineers](skills/wiki/references/modes.md#intake-for-non-engineers).

Worker subagents (dispatched by the loop, not invoked directly): `scope-analyst`, `feature-builder`, `feature-tester`, `feature-reviewer`, `feature-verifier`, `devops` (optional: push / deploy / deployed-revision check, only on the operator's word), `doc-writer`, `architecture-subagent`, `ba-suite-subagent`, `ba-export-subagent`, `research-subagent`, `wiki-ingest-subagent`, `wiki-lint-subagent`, `graphify-extract-subagent`, `mechanical-scanner-subagent`.

### Coming from the AI-Native SDLC Playbook

| Playbook | ADLC |
|---|---|
| `intent.md` | a `.raw/` source or intake note → requirements and stories with stable IDs |
| `spec.md` | the per-service shift-left spec (Gates 1–3) in the code wiki |
| `plan.md` | the run ledger + per-story verification contract |
| `CLAUDE.md` | `AGENTS.md` (from `/project-profile`) |
| `REVIEW.md` | `reviews/_policy.md` per service |
| verifier subagent | `feature-reviewer` then `feature-verifier` |
| "mistake twice → `CLAUDE.md`" | `/adlc distill` (Don'ts, worker rules, operator profile, upstream) |
| deploy | optional `devops` worker, on the operator's word |
| closing the loop | `bugs/` page + backlog item (headless trigger designed, not built) |

ADLC keeps typed wiki records with stable IDs instead of common-name files. The full map is in the wiki's *AI-Native SDLC Playbook vs ADLC* comparison.

## Wiki Modes and Concerns

A vault has **one base mode** plus **zero or more opt-in concerns**.

| Mode | Use when |
|---|---|
| **B: Repository** | Code projects: architecture, modules, flows, ADRs, dependencies |
| **C: Business / Project** | Product docs: stakeholders, decisions, deliverables, intel, comms |
| **B+C** | A repo that's also the working surface for product/business documentation |
| **ADLC** | Additive: one product wiki + N service code wikis; agents cover BA/QA/PM roles, humans operate |

Concerns add folder kits per SDLC role: `ops`, `qa`, `sec`, `design`, `writing`. Per-concern docs live in [`skills/wiki/references/concerns/`](skills/wiki/references/concerns/); mode details in [`skills/wiki/references/modes.md`](skills/wiki/references/modes.md).

## Reporting back to the plugin

A vault that uses the plugin records what the plugin itself got wrong in `wiki/meta/adlc-upstream.md`: a skill step, a generic worker rule, a script. Single occurrences are rows; a repeat, a plugin bug, or a design the operator approved becomes an `UP-nnn` entry. `/adlc upstream` exports the ratified entries as redacted reports (no names, ids, hashes, paths or links that point back at the vault; `skills/wiki/scripts/upstream_redact_check.py` checks each one). It files them as GitHub issues when `gh` works; otherwise you copy the file into this repo's `.raw/upstream/`. Shipped reports are listed in [`skills/adlc/references/upstream-shipped.md`](skills/adlc/references/upstream-shipped.md), and vaults close their entries from it. Format: [`skills/wiki/references/adlc-upstream.md`](skills/wiki/references/adlc-upstream.md).

## Sharing and Interop

- **Format, not platform.** The vault is plain Markdown + YAML frontmatter + git — readable by humans and agents in any tool. Frontmatter is OKF-compatible (`type` is the one required field); `skills/wiki/scripts/okf_export.py` renders the vault as a portable OKF bundle.
- **Pages stay current.** A page holds the current state only; its history lives in the folder's `_changelog.md`, and every identifier has an entry in `wiki/glossary.md` that pages link on first mention. `skills/wiki/scripts/page_history_check.py` and `glossary.py` keep both honest (`wiki-lint` runs them; format in [`writing-style.md`](skills/wiki/references/writing-style.md) § Pages that stay current and [`glossary.md`](skills/wiki/references/glossary.md)).
- **Git is the state bus.** Team protocol in [`team-sync.md`](skills/wiki/references/team-sync.md); branch topology (session wiki branches, code-only PRs, auto-merge when a feature lands) in [`git-flow.md`](skills/wiki/references/git-flow.md).
- **Cross-project access.** Point any repo's AGENTS.md at the vault: read `wiki/hot.md` first, then `wiki/index.md`, then drill in. An MCP interop server for non-Claude consumers is on the roadmap; inside Claude Code, file reads stay cheaper than tool round-trips.

## Vault Structure

```
.raw/           source documents (immutable)
wiki/           the knowledge base (one page per fact; records are pages)
_attachments/   images and PDFs referenced by wiki pages
services/       (ADLC vaults) symlinks to service checkouts, machine-local
```

## License

MIT. See [LICENSE](LICENSE) and [ATTRIBUTION.md](ATTRIBUTION.md).
