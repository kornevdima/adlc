"""Tests for tells_check.py. Run: python3 -m pytest -q test_tells_check.py or python3 test_tells_check.py."""
import pathlib
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import tells_check  # noqa: E402


def _page(text):
    d = pathlib.Path(tempfile.mkdtemp())
    p = d / "page.md"
    p.write_text(text, encoding="utf-8")
    return p


def _cats(text, level=None):
    return [f[3] for f in tells_check.check_file(_page(text)) if level is None or f[2] == level]


def test_plain_page_is_clean():
    text = "---\ntype: note\n---\n\n# Queue\n\nThe queue holds jobs. A worker takes one at a time.\n"
    assert tells_check.check_file(_page(text)) == []


def test_significance_and_copula_are_fix_findings():
    cats = _cats("# A\n\nThe cache plays a pivotal role. It serves as a buffer.\n", "fix")
    assert "significance" in cats and "copula avoidance" in cats


def test_dash_curly_quote_and_title_case_heading():
    cats = _cats("# Page\n\n## Key Features And Benefits\n\nThe API — stable — returns “ok”.\n", "fix")
    assert "title case heading" in cats and "dash" in cats and "curly quotes" in cats


def test_closing_summary_and_chatbot_residue():
    cats = _cats("# A\n\nFacts.\n\nIn conclusion, it works. Let me know if you need more.\n", "fix")
    assert "closing summary" in cats and "chatbot residue" in cats


def test_quoted_mentions_and_code_are_skipped():
    text = '# A\n\nAvoid the phrase "plays a pivotal role" in pages.\n\n```\nit serves as a buffer\n```\n'
    assert _cats(text, "fix") == []


def test_placeholder_in_inline_code_is_skipped_but_link_target_is_checked():
    assert _cats("# A\n\nCall `s.edit.insert_after_symbol` here.\n", "fix") == []
    assert "placeholder" in _cats("# A\n\nSee [docs](https://example.com/page).\n", "fix")


def test_include_quotes_checks_quoted_text():
    tells_check.SKIP_QUOTES = False
    try:
        cats = _cats('# A\n\nAvoid "plays a pivotal role".\n', "fix")
    finally:
        tells_check.SKIP_QUOTES = True
    assert "significance" in cats


def test_three_stock_words_in_one_paragraph_is_a_cluster():
    cats = _cats("# A\n\nA robust, seamless and pivotal design.\n", "fix")
    assert "vocabulary cluster" in cats


def test_off_marker_skips_a_catalogue_page():
    text = "<!-- tells-check: off -->\n# A\n\nIt serves as a testament.\n"
    assert tells_check.check_file(_page(text)) == []


def test_frontmatter_is_skipped():
    text = "---\ntitle: It serves as a hub\n---\n\n# Hub\n\nThe hub routes messages.\n"
    assert tells_check.check_file(_page(text)) == []


def test_raw_folders_are_not_walked():
    d = pathlib.Path(tempfile.mkdtemp())
    (d / ".raw").mkdir()
    (d / ".raw" / "source.md").write_text("It serves as a testament.\n", encoding="utf-8")
    (d / "page.md").write_text("# A\n\nPlain.\n", encoding="utf-8")
    assert [p.name for p in tells_check.iter_files([d])] == ["page.md"]


def test_log_files_are_skipped_as_append_only():
    d = pathlib.Path(tempfile.mkdtemp())
    (d / "log.md").write_text("# Log\n\nIt serves as a testament.\n", encoding="utf-8")
    (d / "page.md").write_text("# A\n\nPlain.\n", encoding="utf-8")
    assert [p.name for p in tells_check.iter_files([d])] == ["page.md"]
    assert list(tells_check.iter_files([d / "log.md"])) == []


if __name__ == "__main__":
    failures = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"ok    {name}")
            except AssertionError as e:
                failures += 1
                print(f"FAIL  {name}: {e}")
    sys.exit(1 if failures else 0)
