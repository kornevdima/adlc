# Engineering method: ub-mode

A vault with `engineering: ub-mode` in its `Toolset:` block changes code by the `ub-mode` skill by Robert C. Martin ([unclebob/ub-mode](https://github.com/unclebob/ub-mode), MIT) and gates every change on three measuring tools from the same author. The default, `engineering: none`, leaves the method to each service's `AGENTS.md`.

ub-mode has three parts. Make it work: the failing test first, the smallest change, the data shape before the logic, checks at the boundary. Make it right: fix root causes, work in small verified units, test behaviour, and measure with the three tools. Practice: keep a log of actions and commit in small steps.

## The three tools

The table lists each tool and the gate this method sets for it.

| Tool | Measures | Gate |
|---|---|---|
| [crapper](https://github.com/unclebob/crapper) | complexity against test coverage, per function | every function below CRAP 10 |
| [dryer](https://github.com/unclebob/dryer) | structural duplication | no candidate at 0.8 or above |
| [mutator](https://github.com/unclebob/mutator) | mutation testing | no surviving mutant in the files the change touched |

dryer's help lists Clojure, Java, Go, TypeScript and Rust among its languages; check the other two tools' READMEs for a service in another language before choosing this method.

## Setting it up

```bash
sh <plugin>/bin/setup-ub-mode.sh <vault>
```

The script copies the skill, unchanged, into `<vault>/.claude/skills/ub-mode/` at a pinned commit; clones the three tools into `<vault>/tools/` at pinned commits, each with its own virtualenv; writes `<vault>/scripts/tool.sh`; and adds `/tools/` and `.metrics/` to `.gitignore`. It is safe to rerun and commits nothing. The upstream launchers expect the Unix virtualenv layout (`.venv/bin`), which Windows does not use; `scripts/tool.sh` finds the interpreter in either layout. `toolset.py check` reports the skill and each tool.

## The service AGENTS.md

`/project-profile` writes these two sections into each service's `AGENTS.md` when the block names `ub-mode`. `feature-builder` and `feature-reviewer` read them there, so the gate is the same in every packet. Replace the test command with the service's own.

```markdown
## Commands

| Task | Command |
|---|---|
| Run the tests | `<the service's test command>` |
| CRAP scores | `sh ../../scripts/tool.sh crapper` |
| Duplication | `sh ../../scripts/tool.sh dryer` |
| Mutation testing | `sh ../../scripts/tool.sh mutator <changed package or folder>` |

## How we change code

Every change follows the `ub-mode` skill (`.claude/skills/ub-mode/SKILL.md` at the vault root): make it work test-first, then make it right with the three tools above. A change is done when:

1. the tests pass, and the new behaviour has a test that failed before the change;
2. every function scores below 10 in crapper;
3. dryer reports no candidate at 0.8 or above;
4. mutator leaves no surviving mutant in the files you touched.
```

The `../../scripts/tool.sh` path holds for the worktree layout ([`service-worktrees.md`](service-worktrees.md)) and for symlinked services under `services/`. A service opened outside the vault calls the script by its absolute path.

## Rules on top of the skill

ub-mode is copied unchanged. Three of its steps meet ADLC rules, and the ADLC rule wins:

- **Push.** ub-mode ends with "push to the main line". In a vault, a push waits for the operator's word, as `permissions.md` already gates `git push`.
- **Glossary.** ub-mode keeps a glossary of domain terms. Service terms go in the service's code wiki; project-wide terms go in `wiki/glossary.md`.
- **Log of actions.** ub-mode reports a log of every action. Workers put it in their hand-back report; facts worth keeping go to the code wiki's `log.md` through the dispatcher.

## In the delivery loop

- `feature-builder` follows the skill and runs the four checks of the service's definition of done before it hands back; it reports each tool's result in its Evidence field.
- `feature-reviewer` re-runs crapper and dryer on the diff and treats a failed gate as a finding with severity high.
- The dispatcher's pre-commit re-verify (`/adlc` step 2.7) re-runs the tests and one of the three tools from the builder's Evidence.
