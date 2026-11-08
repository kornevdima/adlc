# Attributions

adlc is an original work. The following third-party patterns, tools, and creators informed its design.

---

## LLM Wiki Pattern

**Author:** Andrej Karpathy
**Source:** https://github.com/karpathy
**Use:** The core architecture of adlc — using an LLM to build and maintain a structured wiki from raw sources — is based on the LLM Wiki pattern Karpathy described publicly. adlc is an independent implementation; no code or content from Karpathy's repositories was copied. A reference specification is included as a source document at [`.raw/llm-wiki-pattern-spec.md`](.raw/llm-wiki-pattern-spec.md).

---

## BA method set (ba-suite)

**Author:** dmytro (the ba-suite skill set)
**Use:** The BA methodology docs under `skills/wiki/references/ba/` (one file per method, plus the supporting reference tables in `references/`) are bundled from the author's own ba-suite skill set so adlc's Mode ADLC is self-contained and does not require installing the separate ba-suite plugin. They are applied by `ba-suite-subagent` and `ba-export-subagent`.

---

## Signs of AI writing (Wikipedia)

**Source:** English Wikipedia, [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), by its editors, CC BY-SA 4.0
**Use:** `skills/technical-writer/references/ai-tells.md` adapts the guide's catalogue of patterns into a checklist for wiki pages, with our own fixes and examples, and `skills/technical-writer/scripts/tells_check.py` checks the patterns a regular expression can see. The adapted catalogue is shared under CC BY-SA 4.0.

---

## ub-mode, crapper, dryer, mutator

**Author:** Robert C. Martin ([unclebob](https://github.com/unclebob))
**Source:** https://github.com/unclebob/ub-mode (MIT) and the crapper, dryer and mutator repositories (0BSD)
**Use:** Not bundled. `bin/setup-ub-mode.sh` clones them at pinned commits into a vault that chooses `engineering: ub-mode`; the skill is copied unchanged with its LICENSE. `skills/wiki/references/engineering-ub-mode.md` describes how the delivery loop applies them.

---

## TokenEconomizer

**Author:** Microsoft Research and UC Berkeley
**Source:** https://github.com/microsoft/TokenEconomizer (Apache-2.0)
**Use:** Not bundled. `toolset.md` § Cost describes it as the optional `cost` plugin and the settings that suit a delivery vault; `toolset.py check` looks for it.

---

## Shift-Left Engineering Advisor

**Source:** the `anthropic-skills:shift-left-engineering-advisor` skill
**Use:** The shift-left methodology under `skills/wiki/references/shift-left/` is bundled so adlc's Mode ADLC `architecture-subagent` produces per-service technical specs without requiring an external skill.

