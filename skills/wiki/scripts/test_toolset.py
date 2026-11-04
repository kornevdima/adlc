"""Tests for toolset.py: the block parser and the defaults. Run: python3 -m pytest -q test_toolset.py
or python3 test_toolset.py."""
import pathlib
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import toolset  # noqa: E402

BLOCK = """# A vault

Mode: ADLC
Concerns: qa, design
Toolset:
  reader: wiki-renderer
  code-nav: semble, serena
  design: impeccable, taste-skill
  design-system: ~/work/design-system

## Structure
"""


def _vault(text=None):
    d = pathlib.Path(tempfile.mkdtemp())
    if text is not None:
        (d / "AGENTS.md").write_text(text, encoding="utf-8")
    return d


def test_block_form_is_read():
    values, found = toolset.parse_block(BLOCK)
    assert found
    assert values == {"reader": "wiki-renderer", "code-nav": "semble, serena",
                      "design": "impeccable, taste-skill", "design-system": "~/work/design-system"}
    res, warnings = toolset.resolve(values, _vault())
    assert warnings == []
    assert res["reader"] == "wiki-renderer"
    assert res["code-nav"] == ["semble", "serena"]
    assert res["design"] == ["impeccable", "taste-skill"]
    assert res["design-system"].endswith("/work/design-system") and "~" not in res["design-system"]


def test_one_line_form_is_read():
    values, found = toolset.parse_block("Mode: B\nToolset: reader=none; code-nav=semble\n")
    assert found
    res, _ = toolset.resolve(values, _vault())
    assert res["reader"] == "none"
    assert res["code-nav"] == ["semble"]
    assert res["design"] == ["none"]


def test_block_ends_at_first_unindented_line():
    values, _ = toolset.parse_block("Toolset:\n  reader: obsidian\nOwner: x\n  design: impeccable\n")
    assert values == {"reader": "obsidian"}


def test_missing_block_gives_defaults():
    v = _vault("Mode: B\nConcerns: none\n")
    agents, values, found = toolset.load(v)
    assert not found and values == {}
    res, warnings = toolset.resolve(values, v)
    assert res == {"reader": "obsidian", "code-nav": ["none"], "design": ["none"], "design-system": "none"}
    assert warnings == []


def test_default_code_nav_is_graphify_when_a_graph_exists():
    v = _vault("Mode: B\n")
    (v / "graphify-out").mkdir()
    (v / "graphify-out" / "graph.json").write_text("{}")
    res, _ = toolset.resolve({}, v)
    assert res["code-nav"] == ["graphify"]


def test_unknown_values_are_dropped_with_a_warning():
    res, warnings = toolset.resolve({"reader": "notion", "code-nav": "graphify, sourcegraph", "design": "figma",
                                     "colour": "blue"}, _vault())
    assert res["reader"] == "obsidian"
    assert res["code-nav"] == ["graphify"]
    assert res["design"] == ["none"]
    assert len(warnings) == 4
    assert any("unknown key `colour`" in w for w in warnings)


def test_none_beside_a_tool_is_dropped():
    res, _ = toolset.resolve({"code-nav": "none, semble"}, _vault())
    assert res["code-nav"] == ["semble"]


def test_fmt_block_round_trips():
    res = {"reader": "wiki-renderer", "code-nav": ["semble", "serena"], "design": ["impeccable"], "design-system": "none"}
    text = toolset.fmt_block(res)
    values, found = toolset.parse_block(text)
    assert found
    back, _ = toolset.resolve(values, _vault())
    assert back["code-nav"] == ["semble", "serena"] and back["design"] == ["impeccable"]


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
