# Bundled shift-left method

The Shift-Left Engineering Advisor methodology, **bundled into adlc** so the `architecture-subagent` needs no external `anthropic-skills:shift-left-engineering-advisor` skill. The worker reads `shift-left-engineering-advisor.md` directly.

Source: the shift-left-engineering-advisor skill (see `ATTRIBUTION.md` at the plugin root).

## ADLC overrides (read before applying)

The advisor describes gates 1 / 1.5 / 2 / 3 (/ 4) as documents a chat produces one per exchange. In adlc Mode ADLC a gate is a checkpoint, and the worker writes artifacts, not gate pages:

1. **Gates are decisions, not documents.** The four checkpoints keep their order and their meaning (requirements understood; domain modelled; decisions taken; workflow agreed), but each is one line in the **Gates table on the epic page** in the product wiki's `epics/` (gate, verdict `go` / `hold` / `recycle`, date, deciding role, evidence pointers, conditions), written by the dispatcher when the role rules ([`../technical-planning.md`](../technical-planning.md) § Gates as checkpoints). No file is named after a gate; there is no `GATE-N` page and no sign-off document.
2. **The worker writes no requirement.** Where the advisor's Gate 1 writes FRs, NFRs and SRs, the ADLC worker reads the BA's requirements (`requirements/`, functional and non-functional, with stable ids) and writes **`architecture-drivers.md`**: the requirements it selected as drivers, each quality requirement restated as a quality attribute scenario (`QAS-{SVC}-N`), the constraints (`CON-{SVC}-N`), the open questions. A requirement the register lacks is an open question for the BA, never a new `FR-{SVC}-N`. Security stays a separate thread inside the drivers page.
3. **Four artifact pages per service**, in the service's own code wiki (`services/<svc>/wiki/` or `service-wikis/<svc>/` under `layout: worktrees`), never a `project-context/` folder: `architecture-drivers.md`, `domain-model.md` (entities, `BR-{SVC}-N`, invariants, Mermaid; linked up to the product domain page, with the service's bounded-context note), `adrs/ADR-{SVC}-N <title>.md` (Nygard-style, with `decided_by`, `decided_on`, `evidence`), `engineering-workflow.md` (CI/CD, test pyramid, deployment, incidents, the traceability matrix).
4. **Trace down from BA.** Every driver, rule and decision cites the BA requirement ids it serves; the traceability matrix in `engineering-workflow.md` runs requirement id to artifact to test.
5. **Diagrams: Mermaid** in the living artifacts; PlantUML reserved for formal export.
6. **A decision without evidence is a spike, not a guess.** When an ADR would rest on nobody having tried it, the worker proposes a spike story (question, time box, what counts as answered, the ADR it feeds; `skills/adlc/references/routes.md` § Spikes) and leaves the ADR `proposed`. The worker never runs the spike.
7. **Gate 0 escalation (up).** Governance questions — vendor viability, tool approval, buy-vs-build, subscription/budget, compliance class, shelfware — are not engineering decisions. Route them up to the `product-management-layer` skill and keep the advisor's vocabulary disjoint. See the doc's "Governance Escalation" section.
8. **Headless operation.** The advisor is written for an interactive chat; the `architecture-subagent` runs it headless. Skip the On Init interview and the per-gate "Does this look right?" loop: inputs come from the dispatch packet, and the verdicts are the people's at the gates. File open questions in the artifact instead of asking mid-run.
9. **Code-grounded claims.** Where the advisor says to extract constraints from source docs, the ADLC override is stricter: any claim about the existing codebase must be confirmed in the service checkout or marked `[UNVERIFIED — from docs]` (see `agents/architecture-subagent.md` at the plugin root).

The advisor's Gate 4 (implementation) is the delivery loop (`skills/adlc/SKILL.md`), not this worker. See [`../technical-planning.md`](../technical-planning.md).
