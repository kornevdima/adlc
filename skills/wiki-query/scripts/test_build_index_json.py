"""Tests for build_index_json.py. Run: python3 -m pytest -q test_build_index_json.py or python3 test_build_index_json.py."""
import json
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).parent


def _vault():
    root = pathlib.Path(tempfile.mkdtemp())
    for rel in ("wiki/a.md", "services/s1/wiki/b.md", "service-wikis/s2/modules/c.md"):
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f"---\ntype: note\ntitle: {p.stem}\n---\n\n# {p.stem}\n", encoding="utf-8")
    return root


def _paths(root, *flags):
    subprocess.run([sys.executable, str(HERE / "build_index_json.py"), str(root), *flags],
                   check=True, capture_output=True)
    data = json.loads((root / "wiki" / "index.json").read_text(encoding="utf-8"))
    return {page["path"] for page in data["pages"]}


def test_services_flag_indexes_both_code_wiki_layouts():
    assert _paths(_vault(), "--services") == {
        "wiki/a.md", "services/s1/wiki/b.md", "service-wikis/s2/modules/c.md"}


def test_without_the_flag_only_the_product_wiki_is_indexed():
    assert _paths(_vault()) == {"wiki/a.md"}


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
