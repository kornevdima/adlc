---
type: meta
title: "Hot Cache"
updated: 2026-07-03T00:00:00
tags:
  - meta
  - hot-cache
status: evergreen
related:
  - "[[index]]"
  - "[[log]]"
  - "[[Product Management Layer Skill]]"
  - "[[shift-left-engineering-advisor]]"
  - "[[Project Profile Skill Suite]]"
---

# Recent Context

Navigation: [[index]] | [[log]]

## Last Updated

**2026-07-03 (feature: Product Management Layer Skill)**: Filed the design/plan for a new planned skill. Page at [[Product Management Layer Skill]]; raw governing plan (immutable) at [[pm-layer-execution-plan]] in `.raw/`.

## Key Recent Facts

- **`product-management-layer`** is a planned **"Gate 0" governance skill** above [[shift-left-engineering-advisor]]. It governs *which tools/vendors are allowed* before engineering starts; shift-left governs Gates 1–4 (requirements → ADR).
- **v1 scope (8 FRs):** use-case intake & approval registry · vendor lifecycle + re-review triggers (acquisition/sunset/newUseCase/expiry) · per-use-case compliance scoping · buy-vs-build + TCO · shelfware detection · portfolio STATUS · handoff contracts · decision log.
- **Handoff:** up = shift-left escalates vendor/tool Qs here; down = approved intake → shift-left Gate 1 with trace IDs. Companion shift-left patch is a **separate** skill-creator mini-cycle (its own regression eval).
- **Key rule:** an ApprovalEntry is scoped to (use case × tool) and **never transfers**; acquisition/sunset triggers invalidate dependent approvals; AssetRecord without approval ⇒ shelfware.
- **Main risk:** trigger collision with shift-left → disjoint vocabulary (P3.5) + negative evals E5/E6 + description optimization (P5.9). Golden eval E1 = the Embrace.ai sunset retrospective.

## Recent Changes

- Created: [[Product Management Layer Skill]] (concepts/), [[pm-layer-execution-plan]] (.raw/).
- Updated: [[index]] (+1 concept, 60→61), [[log]] (new plan entry at top).

## Active Threads

- **pm-layer skill**: plan filed, **not yet built**. Build is gated (ai-agent-builder) via skill-creator: Gates 1–4 → SKILL.md → evals E1–E8 → package/install on branch `feat/pm-layer-skill`. Nothing implemented yet.
- **RLM → wiki-query**: design filed ([[RLM-Optimized Wiki Querying]]), not yet implemented.
- **ADLC mode (Phase 11)**: shipped in code (skills/agents/hooks); tracked in the roadmap memory.
