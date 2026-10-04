# AGENTS.md

## Build & Test

- `npm run build`

## Wiki topology

The product wiki lives in `../product-wiki/`; this repo's code wiki is `wiki/` (Mode B). Never write product requirements here.

## Team conventions

- Money is always integer cents, never floats.
- Every public function in `src/` has a unit test next to it (`*.test.ts`).
- Branch names: `<story-id>-<slug>`.
