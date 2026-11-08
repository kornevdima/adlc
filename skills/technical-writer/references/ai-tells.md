<!-- tells-check: off -->
# Patterns of machine-written text, and how to fix them

This catalogue adapts the English Wikipedia guide [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (read 2026-11-07) to the pages of an adlc vault. Wikipedia editors collected the patterns from thousands of drafts that language models wrote. We use the list the other way round: as a checklist of habits to remove from our own pages.

Two warnings from the source come first, because they decide how the list is used.

1. **A pattern on its own proves nothing.** Skilled people write "additionally" and use em dashes. The signal is a cluster: three or four patterns in one paragraph.
2. **The surface patterns point at a deeper problem.** Text full of these patterns usually says less than it seems to, and some of what it says is unchecked. Swapping words fixes nothing. Each fix below asks you to find the fact the sentence was avoiding, or to delete the sentence.

`scripts/tells_check.py` finds the patterns a regular expression can see. The rest (vague attributions, rule of three, elegant variation, padded sections) need a read.

## 1. Content: claims of importance instead of facts

These are the most serious patterns, because they change what the page claims.

| Pattern | Looks like | Fix |
|---|---|---|
| Puffed-up significance | "plays a pivotal role", "is a testament to", "marks a key moment", "underscores the importance of", "the evolving landscape", "leaves an indelible mark", "deeply rooted" | State the fact that would make it important: what it does, how many use it, what breaks without it. If there is no such fact, delete the sentence. |
| Trailing "-ing" analysis | "..., highlighting its flexibility", "..., ensuring a smooth experience", "..., reflecting the team's commitment to quality", "contributing to", "fostering" | Cut the clause. If the claim matters, make it its own sentence with a source: "Requests are retried three times (see `client.ts`)". |
| Vague attribution | "experts argue", "industry reports suggest", "observers have noted", "some critics say", "several sources" when one is cited | Name the source and link it, or say "we think" and mark it as an assumption. |
| Lists of coverage to prove notability | "featured in TechCrunch, Wired and The Verge", "has an active community" | Say what the coverage said, if it matters. A list of outlets tells the reader nothing. |
| Formula "challenges" section | "Despite its strengths, X faces several challenges...", "Future outlook" | Name each concrete limitation with its cause and its consequence for us. Drop the "despite" framing and the outlook paragraph. |
| Vague connection | "in connection with", "is associated with", "is linked to" | Say what the relation is: "calls", "depends on", "replaced", "was written by". |
| Undue weight on listings | "is listed in the npm registry as", "is described by its documentation as" | Say what it is. Cite the listing as the source. |

## 2. Words and grammar

| Pattern | Looks like | Fix |
|---|---|---|
| Stock vocabulary | "delve", "tapestry", "testament", "intricate", "meticulous", "pivotal", "crucial", "robust", "seamless", "vibrant", "showcase", "boasts", "garner", "bolster", "underscore", "highlight", "foster", "enhance", "interplay", "landscape", "realm", "align with", "resonate with", "valuable insights", "deep dive", and from 2026 "leverage", "multifaceted", "prioritize", "quietly", "universally" | Use the plain word for what you mean ("check", "use", "fast", "many"), or a number. One of these words in a page is fine when it is literal (a robust estimator, a print landscape). Three in a paragraph is a rewrite. |
| Avoiding "is" and "has" | "serves as", "stands as", "functions as", "boasts", "features", "represents" | "is", "has". "SQLite is a library", not "SQLite serves as a library". |
| Negative parallelism | "It's not just X, it's Y", "not only X but also Y", "not X, but Y", "no X, no Y, just Z", and the newer "Y rather than X" | Say Y. Mention X only if a reader would really assume it. |
| Rule of three | "fast, flexible, and reliable", three parallel phrases where the facts give one or two | Keep the items you can back with a fact. Two is fine. One is fine. |
| Elegant variation | the same thing called "the library", "the framework", "the tool" and "this solution" in four sentences | Pick one name and repeat it. Repetition is clear; variation makes the reader wonder if these are four things. |
| False range | "from small scripts to large applications", "from beginners to experts" where the two ends are not a real scale | Name the actual cases you checked. |
| Hedged filler | "it's important to note that", "it is worth mentioning", "it is crucial to understand" | Delete the lead-in and state the point. If it is important, its place on the page shows it. |
| Transition stacking | "Additionally,", "Furthermore,", "Moreover,", "Notably," opening sentence after sentence | Remove most of them. Sentences in the right order need no connector. |
| Choppy short sentences (newer models) | many very short declaratives in a row, extra commas and periods | Join sentences that carry one idea. Vary length to fit the content. |

## 3. Format

Our pages are Markdown by design, so Markdown itself is not a pattern here. The patterns are the format habits that replace thinking.

| Pattern | Looks like | Fix |
|---|---|---|
| Title Case Headings | "## Key Features And Benefits" | Sentence case: "## Key features". Proper nouns keep their capitals. |
| Bold everywhere | several **bold** phrases per paragraph | Bold only what a reader scanning the page must not miss: a warning, a term at its definition. At most one per paragraph. |
| Inline-header lists | `- **Speed:** It is fast.` `- **Simplicity:** It is simple.` for content that is really a paragraph | Write the paragraph. Keep a labelled list only when items are parallel and a reader looks them up one by one. |
| Headings for every two sentences | a page with more headings than paragraphs | Merge sections. A heading is a place a reader jumps to. |
| Emoji in headings and bullets | "## ✨ Features", "- 🚀 Fast" | Remove them. |
| Em and en dashes | "the API — which is stable — returns" | Hyphen with the sentence unchanged, per the plugin's writing style, or a comma, or two sentences. |
| Curly quotes | “ ” ‘ ’ | Straight quotes `"` and `'`. |
| Wrong heading levels | a second `#` heading, a heading that repeats the page title | One `#` title per page; sections start at `##`. |
| Tables with no lead-in | a table straight after a heading | One or two sentences before it: what the rows are and the takeaway. |

## 4. Words meant for a chat, left in the document

These show that text was pasted from a conversation without reading it.

| Pattern | Looks like | Fix |
|---|---|---|
| Chatbot phrases | "Certainly!", "Of course!", "Great question", "I hope this helps", "Let me know if", "Would you like me to", "Is there anything else", "You're absolutely right" | Delete. |
| Announcing the answer | "Below is a detailed overview of...", "Here's a breakdown of...", "This document will explore..." | Delete and start with the first fact. |
| Closing summary | "In summary,", "In conclusion,", "Overall,", a final paragraph that repeats the page | Delete. If the page needs a summary, it goes at the top, as the answer, not at the bottom as a recap. |
| Knowledge-cutoff and refusal text | "as of my last update", "As an AI language model" | Delete. Check the fact against a current source and write the date you checked it. |
| Hedging about missing sources | "not widely documented", "based on available information", "details remain limited" | Say what you searched and what you found: "The changelog does not mention it (checked 2026-11-07)." Otherwise it is an unverified claim about the absence of evidence. |
| Corrective framing | "should be treated as X rather than Y", "should not be confused with" | State what it is. |
| Placeholders | "[Your Name]", "[Insert link]", "2025-XX-XX", "INSERT_SOURCE_URL", links to example.com | Fill them in or remove the sentence. Never commit a placeholder. |

## 5. Sources and links

A model writes citations that look right. Each one must be opened.

| Pattern | Looks like | Fix |
|---|---|---|
| Links that do not resolve, or resolve to something else | a dead URL with no archive copy; a DOI that opens an unrelated paper | Open every link before filing. Replace or remove. |
| Tracking residue | `utm_source=chatgpt.com`, `oaicite`, `contentReference[...]`, a stray "↩" | Strip the parameter or marker. |
| A source that does not say the thing | a book cited with no page; a doc page that covers the topic but not the claim | Quote or point to the exact place, or drop the claim. |

## 6. Change reports and edit notes

The Wikipedia guide covers edit summaries. Our equivalent is the change report to the operator and the rows in `_changelog.md`.

| Pattern | Looks like | Fix |
|---|---|---|
| Compliance assurances | "ensures consistency", "improves clarity", "follows best practices", "aligns with the style guide" | Say what changed: "Renamed 'the tool' to 'the scheduler' in 6 places." |
| Narrating what was kept or avoided | "while preserving all references", "avoided changing the meaning" | Mention only what changed, plus anything the reader must check. |
| Talking about sourcing instead of content | "added reliable, independent sources" | Name the source and the claim it supports. |

## What is not a sign

Do not "fix" these. Over-correcting produces choppy, odd text, which is its own problem.

- Correct grammar and spelling.
- A formal register, or formal and casual mixed.
- Technical or academic words in general. Only the specific stock words above matter.
- A single transition word ("Additionally") in a page.
- Markdown, tables and lists used where the content is a list or a table.
- Plain human constructions such as "there is", "in order to", "as a result of", "one of the best". They read as human; keep them where they fit.

## A final read

After the checklist, read the page once as its reader would and ask of each sentence: what does this tell me that I did not know from the sentence before? If the answer is nothing, delete it.
