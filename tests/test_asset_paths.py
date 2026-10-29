"""Tests for how the single-asset tools find their input and name their output.

Nothing here talks to ComfyUI or touches the GPU: the cut-out graph is stubbed, so what
is asserted is exactly the part that broke.

The failure this file exists for, from a real run on 2026-10-09:

* the agent asked for five cut-outs with paths relative to the project
  (`public/assets/items/apple.png`), and `asset_remove_bg` - which handed the string
  straight to the pipeline - resolved it against the *server's* working directory. Five
  `FileNotFoundError`s, for a path that was correct.
* it then retried only the ninja, with an absolute path, and got
  `ninja-chubby-nobg-nobg.png`, because the tool appends `-nobg` to whatever `name` it
  is given.
* finally it answered the four remaining failures with
  `cp <one cut-out> <four destinations>`. All five files ended up byte-identical
  (md5 `d23389b6f47c896249163e4f53440edd`), so the apples, burgers, carrots and hotdogs
  in the game were all the same ninja - and nothing anywhere reported an error.

So the properties under test are: a relative path means the same thing to every tool,
a name never carries the suffix twice, and a batch keeps every output paired with its
own source.
"""
from pathlib import Path
import struct
import sys
import tempfile
import zlib

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from threejs import config  # noqa: E402
from threejs.assets import pipeline as P  # noqa: E402


# ------------------------------------------------------------------- doubles
def _png(rgb):
    """A real 1x1 PNG. Distinct bytes per colour, so provenance is provable without a
    model: 'the output came from THIS input' is a byte comparison, not a guess."""
    raw = bytes((0,) + tuple(rgb))          # filter byte + one RGB pixel

    def chunk(tag, data):
        body = tag + data
        return struct.pack(">I", len(data)) + body + struct.pack(">I", zlib.crc32(body))

    return (b"\x89PNG\r\n\x1a\n"
            + chunk(b"IHDR", struct.pack(">IIBBBBB", 1, 1, 8, 2, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(raw))
            + chunk(b"IEND", b""))


def _sources(directory):
    """Five distinguishable inputs, in a directory the caller owns."""
    directory = Path(directory)
    colours = {"apple": (220, 40, 40), "burger": (200, 150, 60), "carrot": (230, 120, 30),
               "hotdog": (190, 90, 70), "ninja-chubby": (40, 40, 60)}
    made = {}
    for name, rgb in colours.items():
        made[name] = directory / (name + ".png")
        made[name].write_bytes(_png(rgb))
    return made


def _stubbed_pipeline(root=None):
    """An AssetPipeline with no ComfyClient, no SdClient and no GPU.

    `__new__` rather than `__init__`: the constructor builds clients that probe the
    card, and none of the path or naming logic needs them.

    `root` retargets the output store. Pass a temp directory: with no root the single
    tool writes into the repository's real `assets/masks/`, and a test has no business
    adding files to the user's asset store.
    """
    pipe = P.AssetPipeline.__new__(P.AssetPipeline)
    pipe.root = Path(root).resolve() if root else None
    pipe.cut_calls = []

    def fake_cut(self, image, *, fast):
        pipe.cut_calls.append(image)
        return image.read_bytes()

    pipe._cut = fake_cut.__get__(pipe, P.AssetPipeline)
    return pipe


def _a_project_with_a_file(directory, name="some_game"):
    """A project built here, not the user's active one.

    The test this replaces walked `data/active_project.txt` and rglob'd whatever game
    happened to be active. `projects/games/` is user data - games get created, renamed
    and deleted - so deleting one turned a *path-resolution* test red, and the failure
    said nothing about paths. A test may not depend on which game is open.
    """
    project = Path(directory) / name
    (project / "public" / "assets" / "items").mkdir(parents=True)
    (project / "public" / "assets" / "items" / "apple.png").write_bytes(_png((220, 40, 40)))
    return project


# --------------------------------------------------------------------- suffix
def test_the_kind_suffix_is_never_doubled():
    """`name="ninja-chubby-nobg"` produced `ninja-chubby-nobg-nobg.png`."""
    assert P._strip_kind_suffix("apple-nobg", "-nobg") == "apple"
    assert P._strip_kind_suffix("ninja-chubby-nobg-nobg", "-nobg") == "ninja-chubby-nobg"
    assert P._strip_kind_suffix("apple", "-nobg") == "apple"
    assert P._strip_kind_suffix("", "-nobg") == ""

    # `_slug_for` returns the BASE: `_save` appends "-nobg" itself.
    assert P.AssetPipeline._slug_for(None, "mask", "ninja-chubby-nobg", "x") == "ninja-chubby"
    assert P.AssetPipeline._slug_for(None, "mask", "", "ninja-chubby-nobg") == "ninja-chubby"
    assert P.AssetPipeline._slug_for(None, "mask", "Apple", "ignored") == "apple"


def test_single_cut_out_names_its_file_once():
    with tempfile.TemporaryDirectory() as td:
        srcs = _sources(td)

        # A caller that passes the suffix anyway gets ONE `-nobg`, not two.
        store = Path(td) / "store-a"
        one = _stubbed_pipeline(root=store).remove_bg(str(srcs["ninja-chubby"]),
                                                      "ninja-chubby-nobg")
        assert Path(one[0].path).name == "ninja-chubby-nobg.png", one[0].path
        assert Path(one[0].path).suffix == ".png", one[0].path      # not ".bin"
        assert Path(one[0].path).parent == store / "masks", one[0].path

        # A source that is already a cut-out must not become `x-nobg-nobg` either.
        already = srcs["ninja-chubby"].with_name("ninja-chubby-nobg.png")
        already.write_bytes(srcs["ninja-chubby"].read_bytes())
        two = _stubbed_pipeline(root=Path(td) / "store-b").remove_bg(str(already))
        assert Path(two[0].path).name == "ninja-chubby-nobg.png", two[0].path

        # Neither call invented a second suffix anywhere under the stores.
        made = [p.name for p in Path(td).rglob("*.png") if "store-" in str(p)]
        assert made, "expected the stores to hold the cut-outs"
        assert not [n for n in made if "-nobg-nobg" in n], made


# ----------------------------------------------------------------------- paths
def test_a_relative_path_resolves_against_the_project():
    """The exact kind of argument that failed five times, for a file that exists.

    Project-first is the whole rule: the same string used to mean one thing to
    `asset_generate_pack` and another to `asset_remove_bg`.

    Hermetic: the project is built in a temp directory and passed explicitly, so this
    asserts the rule itself rather than the state of whichever game is currently open.
    """
    with tempfile.TemporaryDirectory() as td:
        project = _a_project_with_a_file(td)
        target = project / "public" / "assets" / "items" / "apple.png"

        got = P.locate_input("public/assets/items/apple.png", project=project)
        assert got == target.resolve(), "%s != %s" % (got, target.resolve())
        assert got.is_file()


def test_a_repo_relative_path_is_never_joined_onto_the_games_dir():
    """`projects/games/<name>` used to fall through to `GAMES_DIR / p`.

    For a value that already carries directories that produced
    `projects/games/projects/games/<name>` - a path that can never exist, returned
    silently, so every caller failed later with an error about the wrong directory.
    """
    got = config.resolve_project("projects/games/definitely-not-a-real-game")
    assert got == (config.THREE_RAG_HOME / "projects" / "games" /
                   "definitely-not-a-real-game").resolve(), got
    # The signature of the old bug: "games" followed by another "projects".
    tail = got.parts[got.parts.index("games") + 1:]
    assert tail[0] != "projects", got


def test_a_bare_name_still_resolves_under_the_games_dir():
    """The one case `GAMES_DIR` is the right parent for: a game `newgame.cmd` will make."""
    assert (config.resolve_project("not-created-yet")
            == (config.GAMES_DIR / "not-created-yet").resolve())


def test_a_stale_pointer_raises_instead_of_inventing_a_path():
    """A system file must never be able to fabricate a project path.

    `projects/games/` is user data: games get deleted while `data/active_project.txt`
    still names the old one. The pointer is a hint, so it is re-resolved on every call
    and a vanished target is reported instead of guessed at.
    """
    real = config.ACTIVE_PROJECT_FILE
    with tempfile.TemporaryDirectory() as td:
        fake = Path(td) / "active_project.txt"
        fake.write_text("projects/games/deleted-long-ago", encoding="utf-8")
        config.ACTIVE_PROJECT_FILE = fake
        try:
            try:
                config.resolve_project("")
            except ValueError as err:
                assert "deleted-long-ago" in str(err), err
                assert "stale" in str(err), err
            else:
                raise AssertionError("a stale pointer must raise, not return a fake path")
        finally:
            config.ACTIVE_PROJECT_FILE = real


def test_a_stale_absolute_pointer_raises_too():
    """`agent.cmd C:\\gone\\game` writes an absolute path - it can go stale as well."""
    real = config.ACTIVE_PROJECT_FILE
    with tempfile.TemporaryDirectory() as td:
        fake = Path(td) / "active_project.txt"
        fake.write_text(str(Path(td) / "was-here-yesterday"), encoding="utf-8")
        config.ACTIVE_PROJECT_FILE = fake
        try:
            try:
                config.resolve_project("")
            except ValueError as err:
                assert "was-here-yesterday" in str(err), err
            else:
                raise AssertionError("a stale absolute pointer must raise")
        finally:
            config.ACTIVE_PROJECT_FILE = real


def test_a_live_pointer_is_still_followed():
    """The fix must not break the normal case: a pointer at a real project resolves."""
    real = config.ACTIVE_PROJECT_FILE
    with tempfile.TemporaryDirectory() as td:
        project = _a_project_with_a_file(td, "live_game")
        fake = Path(td) / "active_project.txt"
        fake.write_text(str(project), encoding="utf-8")
        config.ACTIVE_PROJECT_FILE = fake
        try:
            assert config.resolve_project("") == project.resolve()
        finally:
            config.ACTIVE_PROJECT_FILE = real


def test_an_explicit_absolute_path_is_still_taken_as_given():
    """An explicit absolute path is the caller's business - it may not exist yet.

    Only the POINTER is treated as a claim about user data that must be true.
    """
    missing = (Path(tempfile.gettempdir()) / "not-created-yet-game").resolve()
    assert config.resolve_project(str(missing)) == missing


def test_an_absolute_path_is_taken_as_is():
    with tempfile.TemporaryDirectory() as td:
        srcs = _sources(td)
        assert P.locate_input(str(srcs["apple"])) == srcs["apple"]


def test_a_missing_path_says_what_it_tried():
    """A bare `No such file: 'public\\assets\\apple.png'` told the agent nothing it could
    act on, so it answered with `cp` instead of a corrected path."""
    try:
        P.locate_input("public/assets/items/does-not-exist.png")
    except P.AssetInputError as err:
        message = str(err)
        assert "Tried:" in message, message
        assert "does-not-exist" in message, message
        # Still a FileNotFoundError, so anything already catching that keeps working.
        assert isinstance(err, FileNotFoundError)
    else:
        raise AssertionError("a missing relative path should raise")

    for bad in ("C:/definitely/not/here.png", ""):
        try:
            P.locate_input(bad)
        except P.AssetInputError:
            pass
        else:
            raise AssertionError("expected AssetInputError for %r" % bad)


# ----------------------------------------------------------------------- batch
def test_a_batch_keeps_every_output_with_its_own_source():
    """The whole point: N files in, N files out, each cut from itself."""
    names = ["apple", "burger", "carrot", "hotdog", "ninja-chubby"]
    with tempfile.TemporaryDirectory() as td:
        srcs = _sources(td)
        pipe = _stubbed_pipeline()
        out = pipe.remove_bg_many([str(srcs[n]) for n in names])

        assert len(out) == len(names), out
        # Every source was read, in order - none skipped, none reused.
        assert pipe.cut_calls == [srcs[n] for n in names], pipe.cut_calls

        for name, artefact in zip(names, out):
            dst = Path(artefact.path)
            assert dst.name == name + "-nobg.png", dst
            assert dst.parent == srcs[name].parent, dst          # beside the source
            assert dst.read_bytes() == srcs[name].read_bytes(), dst  # its OWN pixels

        # The specific corruption: five destinations holding one picture.
        digests = {Path(a.path).read_bytes() for a in out}
        assert len(digests) == len(names), "all outputs are the same file"


def test_a_batch_does_not_double_an_existing_suffix():
    with tempfile.TemporaryDirectory() as td:
        srcs = _sources(td)
        src = srcs["apple"].with_name("apple-nobg.png")
        src.write_bytes(srcs["apple"].read_bytes())
        out = _stubbed_pipeline().remove_bg_many([str(src)])
        assert Path(out[0].path).name == "apple-nobg.png", out[0].path


def test_a_batch_can_be_redirected():
    with tempfile.TemporaryDirectory() as td:
        srcs = _sources(td)
        dest = Path(td) / "elsewhere"
        out = _stubbed_pipeline().remove_bg_many(
            [str(srcs["apple"]), str(srcs["burger"])], out_dir=dest)
        assert [Path(a.path).parent for a in out] == [dest, dest], out
        assert [Path(a.path).name for a in out] == ["apple-nobg.png", "burger-nobg.png"], out


def test_a_batch_fails_on_the_file_it_cannot_find():
    """No silent partial success: the error names the file that was wrong."""
    with tempfile.TemporaryDirectory() as td:
        srcs = _sources(td)
        pipe = _stubbed_pipeline()
        try:
            pipe.remove_bg_many([str(srcs["apple"]), "public/assets/items/nope.png"])
        except P.AssetInputError as err:
            assert "nope.png" in str(err), err
        else:
            raise AssertionError("a batch with a bad path should raise")
        # The first was cut before the second failed, and nothing was written for the
        # second - so there is no half-filled slot to be papered over later.
        assert pipe.cut_calls == [srcs["apple"]], pipe.cut_calls
        assert not (srcs["apple"].parent / "nope-nobg.png").exists()


# ------------------------------------------------------------------- tool surface
def test_the_tool_offers_a_batch_and_says_so():
    """The docstring is the contract the model reads; the schema must expose `images`."""
    try:
        import threejs.mcp.assets_mcp_server as mcp
    except ModuleNotFoundError as err:      # the MCP SDK lives in the project venv
        print("      (skipped: %s)" % err)
        return
    import inspect

    params = inspect.signature(mcp.asset_remove_bg).parameters
    assert "images" in params, params
    assert params["image"].default == "", "`image` should be optional now"

    doc = mcp.asset_remove_bg.__doc__ or ""
    for needle in ("in a single call",
                   "do not call this tool once per file",
                   "copy one cut-out",
                   "Do NOT put the `-nobg` suffix",
                   "relative to the project root",
                   "next to that source"):
        assert needle in doc, "the tool docstring must state: %r" % needle


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
