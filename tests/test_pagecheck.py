"""Tests for `tools/pagecheck.py` - the static "will this page actually load" check.

`tscheck.py` covers what a compiler can see. A browser is the only thing that evaluates
an ES module graph, and by the time it does, the page is already open and blank.

The real failure, 2026-10-09: an agent wrote a page importing
`three/addons/loaders/TextureLoader.js`. `vendor/three/` ships only `GLTFLoader.js`
under `addons/loaders/`; `TextureLoader` is in the core build and re-exported from
`three`. The browser 404'd the import and aborted the whole module graph, so `init()`
never ran - and the agent reported the game as finished while the studio showed nothing.

These tests build throwaway projects, so they never touch the real game.
"""
from pathlib import Path
import json
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools import pagecheck as pc  # noqa: E402


def _project(tmp, importmap='{"three": "./web3d/vendor/three.module.js",\n'
                            '"three/addons/": "./web3d/vendor/addons/"}',
             module="import * as THREE from 'three';",
             extra="", vendor=("three.module.js", "addons/loaders/GLTFLoader.js")):
    """A minimal project: a page, an importmap, and the vendored runtime it claims."""
    root = Path(tmp)
    (root / "web3d" / "vendor" / "addons" / "loaders").mkdir(parents=True, exist_ok=True)
    for rel in vendor:
        (root / "web3d" / "vendor" / rel).write_text("// stub\n", encoding="utf-8")
    html = (f'<!DOCTYPE html>\n<html><body>\n'
            f'<script type="importmap">{{ "imports": {importmap} }}</script>\n'
            f'<script type="module">\n{module}\n{extra}\n</script>\n</body></html>\n')
    page = root / "game.html"
    page.write_text(html, encoding="utf-8")
    return root, page


# ------------------------------------------------------------------ importmap
def test_the_importmap_is_applied_like_a_browser():
    imap = {"three": "./web3d/vendor/three.module.js",
            "three/addons/": "./web3d/vendor/addons/"}
    assert pc.resolve_specifier("three", imap) == "./web3d/vendor/three.module.js"
    assert pc.resolve_specifier("three/addons/loaders/GLTFLoader.js", imap) == \
        "./web3d/vendor/addons/loaders/GLTFLoader.js"
    # Exact key beats prefix: `three` is a file, not the `three/` directory.
    assert pc.resolve_specifier("three/other.js", imap) is None
    # Not in the map at all -> the browser refuses it before any fetch.
    assert pc.resolve_specifier("lodash", imap) is None


def test_a_comment_in_the_importmap_does_not_break_parsing():
    html = ('<script type="importmap">{ // our runtime\n'
            '"imports": {"three": "./t.js"} }</script>')
    assert pc.parse_importmap(html) == {"three": "./t.js"}


# --------------------------------------------------------- the actual regression
def test_a_vendored_addon_that_exists_is_accepted():
    with tempfile.TemporaryDirectory() as td:
        root, page = _project(td, module="import { GLTFLoader } from "
                                          "'three/addons/loaders/GLTFLoader.js';")
        r = pc.check_page(page, root)
        assert r["problems"] == [], r["problems"]


def test_an_addon_that_is_not_vendored_is_caught():
    """The exact line that left the studio blank: TextureLoader is NOT an addon file."""
    with tempfile.TemporaryDirectory() as td:
        root, page = _project(td, module="import { TextureLoader } from "
                                          "'three/addons/loaders/TextureLoader.js';")
        r = pc.check_page(page, root)
        assert len(r["problems"]) == 1, r["problems"]
        p = r["problems"][0]
        assert p["kind"] == "missing-module"
        assert p["ref"] == "three/addons/loaders/TextureLoader.js"
        # The message has to say why an empty page follows, not just "404".
        assert "module graph" in p["detail"] and "blank" in p["detail"]


def test_importing_the_loader_from_core_is_accepted():
    """The fix: TextureLoader lives in the core build and is re-exported from `three`."""
    with tempfile.TemporaryDirectory() as td:
        root, page = _project(td, module="import { TextureLoader } from 'three';")
        assert pc.check_page(page, root)["problems"] == []


def test_a_bare_specifier_missing_from_the_importmap_is_caught():
    with tempfile.TemporaryDirectory() as td:
        root, page = _project(td, module="import _ from 'lodash';")
        kinds = [p["kind"] for p in pc.check_page(page, root)["problems"]]
        assert kinds == ["unresolved"], kinds


def test_a_page_with_no_module_script_is_caught():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        page = root / "plain.html"
        page.write_text("<html><body>hi</body></html>", encoding="utf-8")
        kinds = [p["kind"] for p in pc.check_page(page, root)["problems"]]
        assert kinds == ["no-module"], kinds


# --------------------------------------------------------------------- assets
def test_a_missing_asset_is_caught():
    with tempfile.TemporaryDirectory() as td:
        root, page = _project(td, extra="const A = 'public/assets/items/apple.png';")
        problems = pc.check_page(page, root)["problems"]
        assert [p["kind"] for p in problems] == ["missing-asset"], problems
        assert problems[0]["ref"] == "public/assets/items/apple.png"


def test_an_asset_under_public_is_reported_with_the_public_hint():
    """`assets/x.png` does not resolve; `public/assets/x.png` does. Say so."""
    with tempfile.TemporaryDirectory() as td:
        root, page = _project(td, extra="const A = 'assets/items/apple.png';")
        (root / "public" / "assets" / "items").mkdir(parents=True)
        (root / "public" / "assets" / "items" / "apple.png").write_bytes(b"x")
        problems = pc.check_page(page, root)["problems"]
        assert len(problems) == 1, problems
        assert "public/assets/items/apple.png" in problems[0]["detail"], problems[0]


def test_an_asset_that_exists_is_accepted():
    with tempfile.TemporaryDirectory() as td:
        root, page = _project(td, extra="const A = 'public/assets/items/apple.png';")
        (root / "public" / "assets" / "items").mkdir(parents=True)
        (root / "public" / "assets" / "items" / "apple.png").write_bytes(b"x")
        assert pc.check_page(page, root)["problems"] == []


def test_remote_urls_are_not_treated_as_local_files():
    with tempfile.TemporaryDirectory() as td:
        root, page = _project(td, extra="const A = 'https://cdn.example.com/a.png';")
        assert pc.check_page(page, root)["problems"] == []


# ----------------------------------------------------------------- the real game
def test_the_real_page_in_the_active_project_loads():
    """Locks in the 2026-10-09 fix: the game page must resolve every module it imports."""
    from threejs import config
    try:
        project = config.resolve_project("")
    except ValueError:
        print("      (skipped: no active project)")
        return
    page = project / "ninja.html"
    if not page.is_file():
        print("      (skipped: %s is not there)" % page)
        return
    result = pc.check_page(page, project)
    assert result["problems"] == [], json.dumps(result["problems"], ensure_ascii=False,
                                                indent=2)


def test_vendor_is_skipped_by_default():
    with tempfile.TemporaryDirectory() as td:
        root, _page = _project(td)
        (root / "web3d" / "vendor" / "readme.html").write_text("<html></html>",
                                                              encoding="utf-8")
        assert [p.name for p in pc.find_pages(root)] == ["game.html"]
        assert "readme.html" in [p.name for p in pc.find_pages(root, include_all=True)]


if __name__ == "__main__":
    import sys, traceback
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failed = 0
    for fn in fns:
        try:
            fn()
            print("PASS", fn.__name__)
        except Exception:
            failed += 1
            print("FAIL", fn.__name__)
            traceback.print_exc()
    print("\n%d/%d passed" % (len(fns) - failed, len(fns)))
    sys.exit(1 if failed else 0)
