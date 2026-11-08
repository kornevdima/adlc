---
type: llm
focus: last_message
---

PASS if the reply lists back the five items it would take as accepted (each as a decision in words, not only by number), notes that a broad reply accepts only what it names, and asks the operator once to confirm which of them are accepted before any ruling is written. One question for the whole list is right; it may flag an item that is itself undecided (nonce or blob is a choice, not a ruling).
FAIL if the reply records the five items as accepted rulings, starts the build, or asks five separate questions.
