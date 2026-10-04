---
type: llm
focus: last_message
---

Context: the US-200 tech notes say mermaid.render() inserts its own <style> element on every render, the CSP blocks it, and diagrams render unstyled. Four mechanisms are listed (nonce, build-time template, blob <img>, sandboxed iframe).

Find the ruling question about the CSP approach in the reply.
PASS if, before the mechanism options are listed, the question states the outcome that decides it: that the mermaid library injects its own <style> itself (so the page cannot add a nonce to it) and/or what the reader sees (diagrams unstyled or broken). The question must ask for one decision (the mechanism), not bundle a second unrelated decision into the same question.
FAIL if the question opens straight into the mechanism list (nonce / template / blob / sandbox) without first saying what the library does or what the reader sees, or if it bundles two decisions into one question.
