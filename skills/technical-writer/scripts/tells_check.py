#!/usr/bin/env python3
"""Find patterns of machine-written text in Markdown pages.

Usage:
    python tells_check.py [PATH ...]          # files or folders; default: wiki/
    python tells_check.py --strict wiki/x.md  # exit 1 on review items too

Prints one line per finding: path:line: [level] category: match -> fix.
Levels: "fix" (remove before filing) and "review" (read in context; may be literal).
Exit code 1 when any "fix" finding exists (or any finding with --strict).

Skips YAML frontmatter, fenced code blocks, inline code and text in double
quotes (a quoted phrase is a mention; use --include-quotes to check it).
A page whose first ten lines contain <!-- tells-check: off --> is skipped; only
pages that catalogue the patterns as examples carry it. The catalogue
behind each check is references/ai-tells.md.
"""
import argparse
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VOCAB = [
    "delve", "delves", "delving", "tapestry", "testament", "intricate", "intricacies",
    "meticulous", "meticulously", "pivotal", "crucial", "robust", "seamless", "seamlessly",
    "vibrant", "showcase", "showcases", "showcasing", "boasts", "garner", "garnered",
    "bolster", "bolstered", "underscore", "underscores", "underscoring", "foster", "fosters",
    "fostering", "enhance", "enhances", "enhancing", "interplay", "landscape", "realm",
    "align with", "aligns with", "resonate with", "resonates with", "valuable insights",
    "deep dive", "leverage", "leverages", "leveraging", "multifaceted", "quietly",
    "universally", "enduring", "nestled", "groundbreaking", "game-changer", "unlock",
    "unleash", "elevate", "empower", "empowers", "streamline", "streamlines", "holistic",
    "navigate the", "ever-evolving", "cutting-edge", "comprehensive",
]

# (category, regex, fix, level)
PATTERNS = [
    ("significance", r"\b(plays?|played) an? (pivotal|vital|key|crucial|significant|important) role\b",
     "state the fact that makes it important, or delete", "fix"),
    ("significance", r"\b(is|stands as|serves as) a (testament|reminder)\b", "delete or state the fact", "fix"),
    ("significance", r"\b(evolving|ever-changing) landscape\b|\bindelible mark\b|\bdeeply rooted\b",
     "delete or state the fact", "fix"),
    ("significance", r"\bunderscores? (the|its) (importance|significance)\b|\bhighlights? (the|its) (importance|significance)\b",
     "delete or state the fact", "fix"),
    ("trailing -ing", r",\s+(highlighting|underscoring|emphasizing|emphasising|showcasing|reflecting|symbolizing|symbolising|ensuring|fostering|contributing to|enhancing|demonstrating)\b",
     "cut the clause, or make it a sourced sentence", "review"),
    ("copula avoidance", r"\b(serves|serve|served|stands|stand) as (a|an|the)\b", "use 'is'", "fix"),
    ("copula avoidance", r"\bboasts?\b", "use 'has'", "fix"),
    ("negative parallelism", r"\bnot (just|only|merely|simply)\b[^.!?\n]{1,80}?\bbut\b", "say the second part only", "fix"),
    ("negative parallelism", r"\b(it|this|that)(?:'s| is) not (just |only |merely )?(about )?[^.!?\n]{1,60}?[,;—–-]\s*(it|this|that)(?:'s| is)\b",
     "say the second part only", "fix"),
    ("negative parallelism", r"\bno [^,.\n]{1,30}, no [^,.\n]{1,30}, just\b", "state it plainly", "fix"),
    ("vague attribution", r"\b(experts|observers|critics|analysts|industry reports?|studies|many developers|some (people|users|developers)) (argue|say|suggest|note|have noted|believe|agree|show)\b",
     "name and link the source, or mark as our assumption", "fix"),
    ("challenges formula", r"\bdespite (its|these|their|this)\b[^.\n]{0,60}\b(challenges|limitations|drawbacks)\b|\bfaces? (several|many|numerous) challenges\b|\bfuture outlook\b",
     "name each concrete limitation and its consequence", "fix"),
    ("hedged filler", r"\b(it(?:'s| is) (important|worth|crucial|essential) to (note|mention|remember|understand|highlight))\b|\bit (should|must) be noted\b|\bworth noting\b",
     "delete the lead-in, state the point", "fix"),
    ("closing summary", r"(^|\n)\s*(in summary|in conclusion|to sum up|overall|ultimately|all in all)\b", "delete the recap", "fix"),
    ("announcing", r"\b(below is|here(?:'s| is)) (a|an) (detailed |comprehensive |quick |brief )?(overview|breakdown|summary|look)\b|\bthis (document|page|article|guide) (will )?(explores?|delves?|dives?)\b",
     "delete; start with the first fact", "fix"),
    ("chatbot residue", r"\b(certainly!|of course!|great question|i hope this helps|let me know if|would you like (me )?to|is there anything else|you'?re absolutely right|happy to help|feel free to)(?!\w)",
     "delete", "fix"),
    ("cutoff / refusal", r"\b(as of my (last|latest) (knowledge |training )?update|as an ai( language model)?|my knowledge cutoff)\b",
     "delete; check against a current source and date it", "fix"),
    ("hedging about sources", r"\b(not widely documented|based on (the )?available information|details remain (limited|scarce|unclear)|limited information is available)\b",
     "say what was searched and found, with the date", "fix"),
    ("corrective framing", r"\bshould be (treated|understood|seen|viewed) as\b[^.\n]{0,60}\brather than\b|\bshould not be confused with\b",
     "state what it is", "review"),
    ("placeholder", r"\[(your|insert|add|todo|tbd|placeholder)[^\]]*\]|\b\d{4}-XX-XX\b|\bINSERT_[A-Z_]+|PASTE_[A-Z_]+|\bexample\.com/",
     "fill in or remove", "fix"),
    ("tracking residue", r"utm_source=|oaicite|contentReference\[|↩", "strip it", "fix"),
    ("change-report assurance", r"\b(ensures?|improves?|enhances?) (consistency|clarity|readability|neutrality|verifiability)\b|\bwhile preserving\b|\b(follows|aligns with) best practices\b",
     "say what changed instead", "fix"),
    ("vague connection", r"\b(in connection with|in association with)\b", "say what the relation is", "review"),
    ("false range", r"\bfrom (beginners|small [a-z]+|startups|hobbyists|novices) to (experts|large [a-z]+|enterprises|professionals|seasoned [a-z]+)\b",
     "name the actual cases", "review"),
]

TRANSITIONS = re.compile(r"(?:^|(?<=[.!?]\s))(Additionally|Furthermore|Moreover|Notably|Importantly|Consequently),", re.M)
DASH = re.compile(r"[—–]")
CURLY = re.compile(r"[“”‘’]")
EMOJI = re.compile(r"[\U0001F300-\U0001FAFF☀-➿⭐✅]")
BOLD = re.compile(r"\*\*[^*\n]+\*\*")
INLINE_HEADER = re.compile(r"^\s*[-*+]\s+\*\*[^*]+:\*\*|^\s*[-*+]\s+\*\*[^*]+\*\*:")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
SMALL = {"a", "an", "the", "and", "or", "but", "for", "nor", "of", "on", "in", "to", "at", "by", "with", "vs", "via", "as", "is"}

OFF_MARKER = "<!-- tells-check: off -->"  # for pages that list the patterns as examples
RAW_CATS = {"placeholder", "tracking residue"}  # also check link targets
COMPILED = [(c, re.compile(p, re.I), f, l) for c, p, f, l in PATTERNS]
VOCAB_RE = re.compile(r"\b(" + "|".join(re.escape(v) for v in sorted(VOCAB, key=len, reverse=True)) + r")\b", re.I)


QUOTED = re.compile(r'"[^"\n]{1,120}"')
SKIP_QUOTES = True


def strip_inline(line: str) -> str:
    line = re.sub(r"`[^`]*`", "", line)
    if SKIP_QUOTES:  # a quoted phrase is a mention (an example, a UI label), not a use
        line = QUOTED.sub('""', line)
    line = re.sub(r"\]\([^)]*\)", "]", line)  # link targets
    return line


def title_case(text: str) -> bool:
    words = [w for w in re.findall(r"[A-Za-z][A-Za-z'-]*", text)]
    if len(words) < 3:
        return False
    rest = [w for w in words[1:] if w.lower() not in SMALL]
    if len(rest) < 2:
        return False
    caps = [w for w in rest if w[0].isupper() and not w.isupper()]
    return len(caps) == len(rest)


def check_file(path: Path):
    findings = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (UnicodeDecodeError, OSError) as e:
        return [(path, 0, "review", "unreadable", str(e), "")]
    if any(OFF_MARKER in l for l in lines[:10]):
        return []
    in_fm = bool(lines) and lines[0].strip() == "---"
    in_code = False
    h1 = 0
    para_vocab, para_start, para_bold = set(), 0, 0
    trans_count = 0

    def flush(n):
        nonlocal para_vocab, para_bold
        if len(para_vocab) >= 3:
            findings.append((path, para_start, "fix", "vocabulary cluster",
                             ", ".join(sorted(para_vocab)), "rewrite the paragraph in plain words"))
        if para_bold >= 3:
            findings.append((path, para_start, "review", "bold density",
                             f"{para_bold} bold spans in one paragraph", "keep at most one"))
        para_vocab, para_bold = set(), 0

    for i, raw in enumerate(lines, 1):
        if in_fm:
            if i > 1 and raw.strip() == "---":
                in_fm = False
            continue
        if raw.lstrip().startswith(("```", "~~~")):
            in_code = not in_code
            continue
        if in_code:
            continue
        if not raw.strip():
            flush(i)
            para_start = i + 1
            continue
        if not para_vocab and not para_bold:
            para_start = i
        line = strip_inline(raw)
        raw_no_code = re.sub(r"`[^`]*`", "", raw)  # link targets kept, inline code dropped

        m = HEADING.match(line)
        if m:
            level, text = len(m.group(1)), m.group(2)
            if level == 1:
                h1 += 1
                if h1 == 2:
                    findings.append((path, i, "fix", "heading levels", text, "one # title per page; sections use ##"))
            if title_case(text):
                findings.append((path, i, "fix", "title case heading", text, "sentence case"))
            if EMOJI.search(text):
                findings.append((path, i, "fix", "emoji", text, "remove"))
        elif re.match(r"^\s*[-*+]\s", line) and EMOJI.match(line.lstrip("-*+ \t")):
            findings.append((path, i, "fix", "emoji", line.strip()[:60], "remove"))

        if INLINE_HEADER.match(line):
            findings.append((path, i, "review", "inline-header list", line.strip()[:60],
                             "write prose unless items are parallel lookups"))
        para_bold += len(BOLD.findall(line))

        for mm in DASH.finditer(line):
            findings.append((path, i, "fix", "dash", line[max(0, mm.start() - 25): mm.end() + 25].strip(),
                             "hyphen with the sentence unchanged, a comma, or two sentences"))
        if CURLY.search(line):
            findings.append((path, i, "fix", "curly quotes", line.strip()[:60], "straight quotes"))
        for cat, rx, fix, level in COMPILED:
            target = raw_no_code if cat in RAW_CATS else line
            for mm in rx.finditer(target):
                findings.append((path, i, level, cat, mm.group(0).strip(), fix))
        for mm in VOCAB_RE.finditer(line):
            para_vocab.add(mm.group(1).lower())
            findings.append((path, i, "review", "stock vocabulary", mm.group(1), "plain word or a number, unless literal"))
        trans_count += len(TRANSITIONS.findall(line))
    flush(len(lines) + 1)
    if trans_count >= 3:
        findings.append((path, 0, "review", "transition stacking",
                         f"{trans_count} sentences open with Additionally/Furthermore/Moreover/Notably",
                         "remove most connectors"))
    return findings


def iter_files(paths):
    for p in paths:
        p = Path(p)
        if p.is_dir():
            yield from sorted(x for x in p.rglob("*.md") if ".raw" not in x.parts)
        elif p.suffix.lower() == ".md":
            yield p


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", default=["wiki"])
    ap.add_argument("--strict", action="store_true", help="exit 1 on review findings too")
    ap.add_argument("--include-quotes", action="store_true",
                    help="also check text inside double quotes (skipped by default as mentions)")
    ap.add_argument("--fix-only", action="store_true", help="print only 'fix' findings")
    args = ap.parse_args()
    global SKIP_QUOTES
    SKIP_QUOTES = not args.include_quotes

    total = {"fix": 0, "review": 0}
    for f in iter_files(args.paths):
        for path, line, level, cat, match, fix in check_file(f):
            total[level] = total.get(level, 0) + 1
            if args.fix_only and level != "fix":
                continue
            arrow = f" -> {fix}" if fix else ""
            print(f"{path}:{line}: [{level}] {cat}: {match}{arrow}")
    print(f"\n{total['fix']} to fix, {total['review']} to review.")
    if total["fix"] or (args.strict and total["review"]):
        sys.exit(1)


if __name__ == "__main__":
    main()
