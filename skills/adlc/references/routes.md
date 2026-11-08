# Routes for every kind of work

The delivery loop has a step for a feature story and for nothing else. Everything a team also does (research, trying something out, designing a service, setting up a machine, complaining about the plugin, tidying the wiki) used to land on the main thread as improvised work with no record. This table gives each kind of work one route and one record. `/adlc` reads it in Before Starting and at Step 0, and whenever the operator asks for work the loop has no step for; the wiki skill's context-load mode reads it when an engineer works by hand.

## The table

Lead-in: the first column is what the operator asks for, in their words; the route is who does it and through which skill; the record is what exists in the vault afterwards. A kind of work with no row here is a feature story or a bug, and goes through the loop.

| Work | Route | Record |
|---|---|---|
| A question about the field, a technology or a method ("what do others do about X", "compare A and B") | `/autoresearch <topic>`, dispatched from the loop as a stop at the story boundary; the loop never answers a research question on the main thread | `wiki/questions/<synthesis>.md` with its source and concept pages; a story or decision that links the synthesis |
| Discovery: "does X work here", "can the CSP allow Y", a decision with no evidence | a spike story (below) | the story page with its `## Record`, `.raw/spikes/<STORY-ID>.log`, and the decision that cites the spike as `evidence` |
| Architecture design: "design the service", "we need the model for Z", a missing artifact at Step 0 | `architecture-subagent`, dispatched from the loop for that service; the open questions go to the grilling session; the gate lines to the epic page | `architecture-drivers.md`, `domain-model.md`, `adrs/`, `engineering-workflow.md` in the service's code wiki; the Gates table on the epic page |
| Scaffolding or environment setup: "install X", "set up my machine", "we switch to worktrees" | a team choice goes to the vault `AGENTS.md` (`Toolset:` or `## How we work`); a machine fact to `wiki/meta/machine.local.md`; the install itself is the operator's command, with `toolset.py check` after ([`records.md`](../../wiki/references/records.md)) | the edited block or section, one changelog row; the local file, uncommitted |
| A plugin change: "the loop should do X", "the worker got Y wrong", "adlc needs Z" | the upstream route: an occurrence row or an `UP-nnn` entry in `wiki/meta/adlc-upstream.md`, exported with `/adlc upstream`; never a pull request to the plugin from inside a vault session | the upstream entry; the plugin's question page once filed |
| Bookkeeping: "fix the index", "the counts are off", "relink the ledger" | `wrap-up` (its reconcile and relink steps), `wiki-lint`, or the script the task names (`relink.py`, `glossary.py`, `board.py`); never a throwaway script | the regenerated page, a changelog row when a page was rewritten |
| Writing for a reader: a client brief, a help page, a story's wording | `technical-writer` | the document, in its folder per the filing table |
| A defect found outside the loop | a `bugs/` page and a backlog item of `kind: defect` with `caused_by`, then the loop | the two pages |

## Spikes

A spike is a backlog item of `kind: spike` in `user-stories/`, sized by its time box, in an epic and a sprint like any story. It is not a record type of its own: the story page is the record. It opens when a decision has no evidence: the architecture worker proposes it (it never runs one), or the operator asks for one, or the loop finds at Step 0 or at a ruling stop that a decision rests on nobody having tried it. The worker proposes; the backlog accepts.

### The contract

Four lines, written by the dispatcher into the story page before anything runs:

1. **The question**, one sentence, answerable by an observation.
2. **The time box** (`time_box`), two days at most; the story's `size` is this.
3. **What counts as answered**: the observable result that settles the question, written in the shape the decision needs ("the page renders the diagram with the strict CSP header present, or it does not").
4. **What the result feeds** (`feeds`): the ADR, the product decision or the PRD section that will cite the spike as `evidence`.

Then the **mode**, chosen in the contract with the operator when the story does not fix it.

### The two modes

| | `autonomous` | `operator-run` |
|---|---|---|
| Who runs the commands | the spike worker (`agents/spike.md`: Bash, Read, Write, Edit), in its own context | the operator, at the keyboard |
| Who writes the record | the worker returns it; the dispatcher files it | the dispatcher, from the session, as the commands happen |
| Where the raw log comes from | the worker appends every command and its output to `.raw/spikes/<STORY-ID>.log` | the dispatcher appends what the operator ran and what came back, asking for what it cannot see (an exit code, a version) |
| Main-thread commands | none; a spike command never runs in the main session | the operator's own |
| When to choose it | the question is settled by commands a worker can run (a library call, a build, a probe against the local stack) | the question needs the operator's accounts, hardware or eyes, or they want to see it themselves |

Both modes leave the same evidence: the record on the story page and the log in `.raw/spikes/`. That is the point of the operator-run mode: a spike run by hand is otherwise the one piece of work that leaves nothing behind.

### The record

On the story page, under `## Record`, in this order: the commands in the order they ran; the tool and library versions (`node --version`, the package's version from the lock file); the failed attempts, each with why it failed in one line; the result against "what counts as answered". The raw log, `.raw/spikes/<STORY-ID>.log`, is committed with the story: a later move to infrastructure as code needs what was actually typed, and the vault's secret scan (`gitleaks` from the joining checklist, [`team-sync.md`](../../wiki/references/team-sync.md)) covers the folder. A line that printed a secret is reported to the operator at once and removed before the commit.

### The close

The spike closes when the question is answered or the time box ends, whichever comes first. The dispatcher sets `result` (`answered`, `partial`, `not answered`), `status: done`, the `done` date and the `history` line, then writes the decision the spike fed with the story page as its `evidence`. A `partial` or `not answered` result is a result: the record says what is still open, and a second spike is a new story. A spike never grows into the feature it was meant to settle; the feature is its own story.

## Rules the table rests on

- **One record per kind of work.** A route that leaves no record is not a route; "I looked into it" in chat is the failure this table exists for.
- **The main thread talks to the operator and dispatches.** Research, spikes and architecture design run in workers (or, for a spike, at the operator's keyboard); the dispatcher writes contracts, reads reports and files records.
- **A plugin change never ships from a vault session.** The vault records it and exports it; the plugin repository decides. This keeps the two repositories' histories apart and keeps the vault's names out of the plugin ([`adlc-upstream.md`](../../wiki/references/adlc-upstream.md)).
- **No throwaway scripts for bookkeeping.** The scripts the plugin ships are allow-listed in the permission profile and tested; an ad-hoc `sed` is neither, and auto mode may deny it.
