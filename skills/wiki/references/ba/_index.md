# Bundled BA method set

These are the BA methodology docs (the ba-suite skill set) **bundled into adlc** so the external `ba-suite` plugin is NOT required. The `ba-suite-subagent` and `ba-export-subagent` read these directly; they do not call `ba-suite:*` via the Skill tool.

Source: derived from the ba-suite skill set (see `ATTRIBUTION.md` at the plugin root). One file per method, plus `references/`: the 23 supporting tables (taxonomies, scoring rubrics, templates, decision rules) the method docs tell you to read before processing input. Those pointers are written as plugin-root paths (`skills/wiki/references/ba/references/<name>.md`); resolve the plugin root the same way as for the method docs. A method doc applied without its reference files is not applied: report it as `INFERRED`.

## ADLC overrides (read these BEFORE applying any method doc)

The method docs were written to emit Office files to `/mnt/user-data/outputs/`. In adlc that is overridden:

1. **System of record is the wiki Markdown.** When authoring (ingest), write each deliverable as a Markdown note into the ADLC wiki folder (table below), with YAML frontmatter, `[[wikilinks]]`, and stable IDs. Do NOT emit Office files during authoring.
2. **Office only on export.** `.docx` / `.xlsx` are produced only by the `ba-export` path, into `.raw/exports/`. PlantUML for formal-export diagrams; Mermaid in the living wiki docs.
3. **Stable IDs, never renumber** (append new IDs at the end). The ID schemes in `ba-suite-orientation.md` are the anchors for traceability.
4. **No PII** in the committed wiki (person names, headcount, contract values) — keep those in gitignored private notes.
5. **Decisions have levels.** `decisions/` holds product decisions only, each with `decided_by`, `decided_on` and `evidence`. A team choice (a tool, a branching rule, a review rule, a definition of done) is never filed there: it goes to the vault `AGENTS.md` (`Toolset:` block or `## How we work` section), and the worker reports it as filed there (`../records.md`). A release the sources name gets a record in `releases/`; an epic gets one in `epics/` (`../frontmatter.md` § Work records).

## Method to wiki folder to ID

| Method doc | Lifecycle | Wiki folder | ID scheme |
|---|---|---|---|
| `ba-suite-orientation` | conventions | — | ID schemes, writing standards |
| `ba-elicitation-synthesizer` | Discovery | `requirements/` | `{PREFIX}-FR/NFR-NNN` |
| `ba-prd` | Definition | `product/prd.md` | the requirement and feature ids it links |
| `ba-stakeholder-analyzer` | Discovery | `stakeholders/` | RACI roles |
| `ba-workshop-facilitator` | Discovery | `comms/` | session synthesis |
| `ba-process-modeler` | Analysis | `features/` | process spec |
| `ba-gap-analysis` | Analysis | `gaps/` | `G-{DIM}-NNN` |
| `ba-user-story-factory` | Definition | `user-stories/` (the backlog items), `epics/` (the epic records) | `{PREFIX}-{EPIC}-NNN`, `EPIC-NNN`; story frontmatter per `../frontmatter.md` § Work records |
| `ba-business-case-builder` | Definition | `deliverables/` | business case |
| `ba-rfi-rfp-analyzer` | Definition | `deliverables/` or `intel/` | `{Section}-NNN` |
| `ba-solution-assessment` | Validation | `deliverables/` | scoring |
| `ba-test-case-generator` | Validation | `test-cases/` (qa concern) | `TC-{STORY}-{TYPE}-NNN` |
| `ba-scrum-events-pack` | Delivery | `sprints/` (the sprint record `S<NN>.md` and the event packs) | `S<NN>`, `IMP-/DEP-/RA-NNN` |
| `ba-requirements-lifecycle` | Cross-cutting | `requirements/` | RTM, approval pack, CRs |
| `ba-planning-monitor` | Cross-cutting | `planning/` | BA approach, governance |

Always read `ba-suite-orientation.md` first for the shared conventions, then the relevant method doc(s).
