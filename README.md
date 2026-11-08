# adlc

**Agentic Development Life Cycle harness.** Agent = Model + Harness — this is the harness: a persistent knowledge substrate, role skills that work it, and a delivery loop that ships verified stories through it. Formerly `claude-mem`.

Built on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — the same pattern Google has since standardized as the [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) (OKF). The vault is plain Markdown; read it in Obsidian or in [wiki-renderer](https://github.com/kornevdima/wiki-renderer). Code navigation through [graphify](https://github.com/safishamsi/graphify), the Semble and Serena MCP servers, or the JetBrains IDE's built-in MCP server; an optional design worker on [impeccable](https://github.com/pbakaus/impeccable) and [taste-skill](https://www.tasteskill.dev/). The vault's `Toolset:` block picks them ([`toolset.md`](skills/wiki/references/toolset.md)).

## The Stack

| Layer | What it is | Key pieces |
|---|---|---|
| **Knowledge substrate** | A compounding Markdown wiki vault (Obsidian-flavoured; Obsidian or wiki-renderer reads it), OKF-aligned, plus optional code navigation: a graphify graph, or Semble and Serena. Every source ingested, every question answered from it, zero manual filing. | `wiki`, `wiki-ingest`, `wiki-query`, `wiki-lint`, `save`, `autoresearch`, `graphify-*` |
| **Role skills** | BA, product, and architecture methods that read and write the substrate — the PRD, requirements, epics, stories, releases, architecture artifacts, governance. Methods are bundled; no external plugins. | `product-management-layer`, `ba-export`, bundled BA + shift-left references |
| **Delivery orchestration** | Mode ADLC: a plan-driven loop that works an epic story by story, dispatching (design →) build → test → review → verify workers (or the spike pipeline for a spike), writing the story dates, committing with trace IDs, regenerating the team's board. Routes for the work that is not a story. | `adlc`, `wrap-up`, 17 subagents |
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

Run `/wiki` (or `/adlc:wiki` when installed as a plugin) inside Claude Code. The wiki skill scaffolds the vault structure on first use and asks which tools the vault uses; the answer is a `Toolset:` block in the vault's `AGENTS.md`, beside `Mode:` and `Concerns:`:

```markdown
Toolset:
  reader: wiki-renderer             # obsidian | wiki-renderer | none
  code-nav: semble, serena          # graphify | semble | serena | idea | none
  design: impeccable, taste-skill   # impeccable | taste-skill | none
  design-system: ~/work/design-system
  layout: worktrees                 # symlinks | worktrees
  engineering: ub-mode              # ub-mode | none
  cost: tokeneconomizer             # tokeneconomizer | none
```

Then open the vault in the reader you chose: the project folder in Obsidian, or `wiki-renderer add <vault> && wiki-renderer`. `python3 skills/wiki/scripts/toolset.py --vault <vault> check` lists what is still missing with its install line. Options, defaults and what each choice changes: [`toolset.md`](skills/wiki/references/toolset.md). A vault without the block behaves as before: Obsidian, graphify when a graph exists, no design tool, services symlinked into `services/`, no engineering method, no cost plugin.

### Code navigation and design tools (optional, per the toolset)

```bash
bash bin/setup-graphify.sh /path/to/your-app                                  # code-nav: graphify (Python >=3.10,<3.14), once per project
claude mcp add -s user semble -- uvx --from "semble[mcp]==0.7.0" semble       # code-nav: semble (needs uv)
claude mcp add -s user serena -- serena start-mcp-server --context=claude-code --project-from-cwd   # code-nav: serena (needs the serena CLI)
# code-nav: idea: IntelliJ 2025.2+, Settings | Tools | MCP Server | Auto-Configure for Claude Code (the IDE must be running with the project open)
claude plugin marketplace add pbakaus/impeccable && claude plugin install impeccable@impeccable      # design: impeccable
claude plugin marketplace add leonxlnx/taste-skill && claude plugin install taste-skill@taste-skill  # design: taste-skill
sh bin/add-service-worktree.sh /path/to/vault <service>                      # layout: worktrees, once per service
sh bin/setup-ub-mode.sh /path/to/vault                                       # engineering: ub-mode (git, Python >=3.10)
# cost: tokeneconomizer: clone microsoft/TokenEconomizer, then claude plugin marketplace add "$PWD/TokenEconomizer" && claude plugin install tokeneconomizer@tokeneconomizer
```

With `layout: worktrees` every service is a branch of the vault's own repository, checked out at `services/<service>`, and its code wiki is `service-wikis/<service>/` on the main branch, so code and documentation never share a commit ([`service-worktrees.md`](skills/wiki/references/service-worktrees.md)). With `engineering: ub-mode` every code change follows Robert C. Martin's ub-mode skill and passes crapper, dryer and mutator ([`engineering-ub-mode.md`](skills/wiki/references/engineering-ub-mode.md)).

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
| `obsidian-markdown` / `obsidian-bases` | The Markdown dialect every reader renders; `.base` database files (`reader: obsidian` only) |

### Code graph (`code-nav: graphify`)

With `code-nav: semble, serena` or `idea` the workers and `wiki-query` call the MCP servers instead (Semble, Serena, the JetBrains IDE server), and there is no skill to run.

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
| `/technical-writer` | Documents for a human reader: client briefs and question packs, help pages, the wording of stories and requirements, change reports; source and translation kept in step; an AI-tells pass with a checker (`tells_check.py`) on every page. Method: [`writing-style.md`](skills/wiki/references/writing-style.md), [`ai-tells.md`](skills/technical-writer/references/ai-tells.md) |
| `/project-profile` | Scan a repo, generate/augment its AGENTS.md |

Non-engineers bring a need in by dropping a five-heading note (problem, outcome, who is affected, constraints, open questions) into `.raw/intake/`; the next ingest turns it into requirements and stories. Template: [`modes.md` § Intake for non-engineers](skills/wiki/references/modes.md#intake-for-non-engineers).

Worker subagents (dispatched by the loop, not invoked directly): `scope-analyst`, `feature-designer` (optional: a design brief before the build and a design review after the code review, when the toolset names impeccable or taste-skill), `feature-builder`, `feature-tester`, `feature-reviewer`, `feature-verifier`, `spike` (a time-boxed experiment whose record a decision cites; or the operator runs it and the loop documents it), `devops` (optional: push / deploy / deployed-revision check, only on the operator's word), `doc-writer`, `architecture-subagent`, `ba-suite-subagent`, `ba-export-subagent`, `research-subagent`, `wiki-ingest-subagent`, `wiki-lint-subagent`, `graphify-extract-subagent`, `mechanical-scanner-subagent`.

### The operating model (1.3.0)

The loop sits inside a small operating model, all of it plain pages in the vault ([`modes.md`](skills/wiki/references/modes.md), [`frontmatter.md` § Work records](skills/wiki/references/frontmatter.md), [`records.md`](skills/wiki/references/records.md), [`routes.md`](skills/adlc/references/routes.md)):

| Layer | What the vault holds |
|---|---|
| Product | `product/prd.md` (why and what), `product/context.md` (the C4 context, the team dependencies), `domains/` (product domains and their context map), `catalog-info.yaml` |
| Work | `epics/` (rulings and gate lines), `user-stories/` (features, defects, risks, debt and spikes, with dates the loop writes), `sprints/` (time boxes), `releases/` (what the user gets); `board.md`, generated from the stories by `board.py` |
| Decisions | product decisions in `decisions/` with `decided_by`, `decided_on`, `evidence`; ADRs in the code wiki; team choices in `AGENTS.md` (`Toolset:` and `## How we work`); machine setup in a gitignored local file |
| Gates | one decision line per checkpoint on the epic page; the architecture worker writes drivers, a domain model, ADRs and a workflow, never requirements or gate pages |
| Non-story work | research, spikes, architecture design, setup, plugin complaints and bookkeeping each have one route and one record |

adlc computes no metric from these records; the fields are there for a computation outside the plugin. An existing vault moves to the model with `python3 skills/wiki/scripts/migrate_1_3.py --vault . --apply` ([`migration-1.3.md`](skills/wiki/references/migration-1.3.md)).

### Coming from the AI-Native SDLC Playbook

| Playbook | ADLC |
|---|---|
| `intent.md` | a `.raw/` source or intake note → the PRD, requirements and stories with stable IDs |
| `spec.md` | the per-service architecture artifacts (drivers, domain model, ADRs, workflow) in the code wiki; gates as lines on the epic page |
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
                this repo's own: wiki/architecture/ describes the plugin as built
_attachments/   images and PDFs referenced by wiki pages
services/       (ADLC vaults) symlinks to service checkouts, machine-local
```

## License

MIT. See [LICENSE](LICENSE) and [ATTRIBUTION.md](ATTRIBUTION.md).
