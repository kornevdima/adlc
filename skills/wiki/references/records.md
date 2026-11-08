# Records: the four decision levels, and what is not a decision

A delivery vault holds decisions at four levels, and each level has one home. Writing a team choice as a product decision, or a machine path into a committed page, is how `decisions/` folders fill with "we use Serena" and "node 22 on my laptop" until nobody reads them. This page names the levels, their homes and the things that look like decisions and are not. The frontmatter of each record is in [`frontmatter.md`](frontmatter.md) § Work records.

## The four levels

The level is decided by one question: who is bound by it, and for how long.

| Level | Binds | Home | Record |
|---|---|---|---|
| Product | what the product does for its users | `wiki/decisions/` | a decision record: `decided_by`, `decided_on`, `evidence`, the pages it settles |
| Architecture | how a service is built | that service's code wiki, `adrs/` | a Nygard-style ADR with options, the chosen one, and the drivers it serves ([`shift-left/_index.md`](shift-left/_index.md)) |
| Team | how the people and agents on this project work | the vault `AGENTS.md`: the `Toolset:` block for the tools, the `## How we work` section for the rest | not a record; a change is one row in the vault's changelog |
| Machine | what is installed where on one computer | `wiki/meta/machine.local.md` | not a record; the file is gitignored (`*.local.md`) and never leaves the machine |

A product decision and an ADR are records because a later reader must be able to find who decided, when, and on what; they are the two kinds the glossary indexes (`DEC-NNN`, `ADR-{SVC}-N`). Team and machine choices are state, not history: the current value is what matters, and the changelog carries the dates.

## Team choices

The `Toolset:` block names the tools (reader, code navigation, design, design system, layout, engineering method, cost plugin; [`toolset.md`](toolset.md)). Everything else the team agrees on is a plain line under `## How we work` in the same file:

- how branches are named and where code is reviewed;
- who reviews what (the reviewer worker on every story; a second person on the areas the team names);
- the definition of done for a story (the service `AGENTS.md` adds its own gates, for example the ub-mode tools);
- where personal settings live (`.claude/settings.local.json`) and where machine setup lives (`meta/machine.local.md`), both outside git.

`/project-profile` seeds the service-level counterpart, the `## How we change code` section of a service `AGENTS.md`. The scaffold (wiki skill, step 8) fills the vault-level section with the operator's answers, or with these defaults: one branch per story named after the story id, review in a pull request before merge, done means built, reviewed, verified against the contract, documented and committed with the trace id.

Changing a team choice is editing the line and adding a row to the vault's changelog. It is never a page in `decisions/`, and the BA worker refuses to file one there.

## Machine setup

`wiki/meta/machine.local.md` holds what one computer has: the runtimes and their versions, the IDE and its MCP server port, the paths the `services/` symlinks point at, the containers that are usually up. It helps the next session on that machine and nobody else. The vault's `.gitignore` excludes `*.local.md` ([`git-setup.md`](git-setup.md)); `toolset.py check` reports the tools the block names without reading this file.

## What is not a decision

Each of these has been filed as a decision record in a production vault at least once. None of them is one.

| Looks like a decision | Is | Lives in |
|---|---|---|
| "We use Semble and Serena" | a team tool choice | the `Toolset:` block |
| "Stories branch from main, PR before merge" | a team working rule | `## How we work` |
| "Use the shared component, no per-route rules" on one story | a ruling on that story | the story page, with `decided_by`, `decided_on`, `evidence`; the operator profile's Standing rulings only if the operator says it is standing |
| a design brief (`feature-designer`, shape) | the input to a build | `designs/` |
| the run ledger's Carry-forward | loop state | `sprints/_run <EPIC-ID>.md`, deleted at the epic close |
| "Try library X for the export" | a tool selection that is cheap to reverse | the story that uses it; an ADR only when reversing it would cost a sprint or more |
| a gate verdict (go, hold, recycle) | a checkpoint line | the epic page's Gates table ([`technical-planning.md`](technical-planning.md) § Gates as checkpoints) |
| "Metrics are computed outside adlc" for one vault | a standing ruling | the operator profile |

The test for a product decision: would a user of the product notice if it went the other way? The test for an ADR: would reversing it cost more than a story? If neither, it is a team choice, a story ruling or a tool selection, and it goes where the table says.

## Evidence

Every decision record and every ruling row carries three fields: `decided_by` (a role, never a person's name in a committed page), `decided_on` (the date) and `evidence` (what carried the decision: a page, a spike story, a session reference, an artifact version, a message reference). A decision whose `evidence` is empty rests on nobody having tried it; the loop opens a spike for it (`skills/adlc/references/routes.md` § Spikes) and the spike's story page becomes the evidence. `wiki-lint` flags a decision record with no `decided_by` or no `evidence`.

## The project in a bigger system

Two files place the project among the teams and systems around it. The scaffold creates both with placeholders filled from the vault description; `product/context.md` is kept current by `wrap-up` when a service or a dependency changes.

**`wiki/product/context.md`** holds a C4 context and container description in text (the system, the people and systems around it, the containers inside it, each with one line and a link to the service's code wiki), a dependency table per team pair (this team, the other team, what flows, the interaction mode as collaboration, X-as-a-service or facilitating, and the end date the mode is reviewed at), and, with `reader: obsidian`, a `context.canvas` beside it. The bounded-context note of each service (in that service's code wiki, written by the architecture worker) is what the domain page links; the context page links the domains.

**`catalog-info.yaml`** at the vault root is the descriptor a software catalog reads. The scaffold writes it from `Owner:` and the description:

```yaml
apiVersion: backstage.io/v1alpha1
kind: System
metadata:
  name: <system-slug>
  description: <the vault's Purpose line>
spec:
  owner: <team or role from Owner:>
  domain: <the product domain the system belongs to>
```

Each service may carry its own `catalog-info.yaml` (`kind: Component`, `spec.system` naming this system); `/project-profile` proposes it when the service lacks one.
