---
type: bug
title: "BUG-018 Focus ring contrast below 3 to 1"
status: fixed
created: 2026-09-22
updated: 2026-10-01
severity: medium
fixed_in: f265115
---

# BUG-018 Focus ring contrast below 3 to 1

The focus outline on links measured 1.55:1 against the page background (WCAG 2.2 needs 3:1).

## Resolution

Fixed in `f265115` (2026-10-01): the ring uses the `--ring-strong` token. Re-measured 3.4:1 by the verifier ([[verification/US-110 verify 2026-10-01]]).
