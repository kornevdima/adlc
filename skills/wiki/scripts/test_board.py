"""Tests for board.py: the frontmatter reader, the rendering and idempotence on a fixture vault.
Run: python3 -m pytest -q test_board.py  or  python3 test_board.py."""
import pathlib
import subprocess
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import board  # noqa: E402

STORY_A = """---
type: user-story
title: "US-001 Save a filter"
kind: feature
feature: "[[FEAT-01 Filters]]"
epic: "[[EPIC-001 Filtering]]"
sprint: "[[S01]]"
release: "[[R-1.0]]"
status: done
created: 2026-11-01
ready: 2026-11-02
started: 2026-11-03
done: 2026-11-04
history:
  - "2026-11-01 draft"
  - "2026-11-04 done"
size: S
priority: must
services:
  - web
updated: 2026-11-04
---

# US-001 Save a filter
"""

STORY_B = """---
type: user-story
title: "US-002 Filters survive a reload"
kind: defect
epic: "[[EPIC-001 Filtering]]"
release: "[[R-1.0]]"
status: blocked
caused_by: "[[BUG-003 Filter lost on reload]]"
size: XS
priority: should
services: [web, api]
created: 2026-11-05
updated: 2026-11-06
---
"""

STORY_C = """---
type: user-story
title: "US-003 Can Mermaid render under the CSP"
kind: spike
epic: "[[EPIC-002 Rendering]]"
status: ready
time_box: 2d
feeds: "[[ADR-WEB-4]]"
mode: autonomous
created: 2026-11-06
updated: 2026-11-06
---
"""


def _vault(reader="none"):
    d = pathlib.Path(tempfile.mkdtemp())
    (d / "AGENTS.md").write_text(f"# V\n\nMode: ADLC\nToolset:\n  reader: {reader}\n", encoding="utf-8")
    us = d / "wiki" / "user-stories"
    us.mkdir(parents=True)
    (us / "US-001 Save a filter.md").write_text(STORY_A, encoding="utf-8")
    (us / "US-002 Filters survive a reload.md").write_text(STORY_B, encoding="utf-8")
    (us / "US-003 Can Mermaid render under the CSP.md").write_text(STORY_C, encoding="utf-8")
    (us / "_index.md").write_text("---\ntype: index\n---\n", encoding="utf-8")
    return d


def test_frontmatter_reader_handles_lists_and_links():
    fm = board.parse_frontmatter(STORY_A)
    assert fm["kind"] == "feature"
    assert fm["services"] == ["web"]
    assert fm["history"] == ["2026-11-01 draft", "2026-11-04 done"]
    assert board.link_name(fm["epic"]) == "EPIC-001 Filtering"
    fm_b = board.parse_frontmatter(STORY_B)
    assert board.listing(fm_b, "services") == ["web", "api"]


def test_load_skips_index_and_reads_three_stories():
    stories = board.load_stories(_vault())
    assert [s["name"] for s in stories] == ["US-001 Save a filter", "US-002 Filters survive a reload",
                                            "US-003 Can Mermaid render under the CSP"]
    assert [s["status"] for s in stories] == ["done", "blocked", "ready"]
    assert stories[2]["kind"] == "spike"


def test_render_has_columns_cards_and_counts():
    text = board.render(board.load_stories(_vault()))
    assert "## Done (1)" in text and "## Blocked (1)" in text and "## Ready (1)" in text
    assert "## Draft (0)" in text and "- none" in text
    assert "- [[US-001 Save a filter]] (feature; S; must; web): feature [[FEAT-01 Filters]], epic [[EPIC-001 Filtering]], sprint [[S01]], release [[R-1.0]]" in text
    assert "| [[EPIC-001 Filtering]] | 1 | 2 | 1 |" in text
    assert "| [[EPIC-002 Rendering]] | 0 | 1 | 0 |" in text
    assert "| [[R-1.0]] | 1 | 2 | 1 |" in text
    assert "| (no release) | 0 | 1 | 0 |" in text
    assert "updated: 2026-11-06" in text


def _run(vault, *extra):
    return subprocess.run([sys.executable, str(pathlib.Path(__file__).parent / "board.py"), "--vault", str(vault), *extra],
                          capture_output=True, text=True)


def test_cli_is_idempotent_and_check_sees_staleness():
    v = _vault()
    r1 = _run(v)
    assert r1.returncode == 0, r1.stderr
    first = (v / "wiki" / "board.md").read_text(encoding="utf-8")
    assert "3 stories" in r1.stdout
    r2 = _run(v)
    assert r2.returncode == 0
    assert (v / "wiki" / "board.md").read_text(encoding="utf-8") == first
    assert _run(v, "--check").returncode == 0
    (v / "wiki" / "user-stories" / "US-003 Can Mermaid render under the CSP.md").write_text(
        STORY_C.replace("status: ready", "status: done"), encoding="utf-8")
    assert _run(v, "--check").returncode == 1
    assert not (v / "wiki" / "board.base").exists()


def test_base_file_only_with_obsidian_reader():
    v = _vault(reader="obsidian")
    assert _run(v).returncode == 0
    base = v / "wiki" / "board.base"
    assert base.exists()
    assert 'file.inFolder("wiki/user-stories")' in base.read_text(encoding="utf-8")
    v2 = _vault(reader="obsidian")
    assert _run(v2, "--no-base").returncode == 0
    assert not (v2 / "wiki" / "board.base").exists()


def test_missing_wiki_is_an_error():
    d = pathlib.Path(tempfile.mkdtemp())
    assert _run(d).returncode == 2


if __name__ == "__main__":
    failures = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"ok   {name}")
            except AssertionError as e:  # noqa: PERF203
                failures += 1
                print(f"FAIL {name}: {e}")
    sys.exit(1 if failures else 0)
