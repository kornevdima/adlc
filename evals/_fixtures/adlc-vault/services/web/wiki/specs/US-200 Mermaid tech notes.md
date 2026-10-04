---
type: spec
title: "US-200 Mermaid tech notes"
story: US-200
---

# US-200 Mermaid tech notes

## Candidate mechanisms

1. Nonce: patch mermaid's output to add the per-request nonce to its `<style>`.
2. Template: pre-render diagrams at build time to static SVG with inline `style` attributes.
3. Blob `<img>`: render to a blob URL and show it as an `<img>`; the SVG's styles apply inside the image.
4. Sandbox: render in a sandboxed `<iframe>` with its own relaxed CSP.

## Notes

`mermaid.render()` builds the SVG in the browser and **inserts its own `<style>` element** into it on every render, with the theme CSS. The page cannot pass that element a nonce. Under the current CSP the browser blocks it, so diagrams render unstyled: black boxes on black text in dark mode.

Open: which mechanism. Needs an operator ruling (product: dark mode, text selection, links inside diagrams).
