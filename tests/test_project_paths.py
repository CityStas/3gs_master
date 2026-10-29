"""The project-resolver contract, asserted identically on all three stacks.

`projects/games/` is USER DATA: games get created, renamed and deleted while the system
files that point at them (`data/active_project.txt`) keep naming the old one. So the rule
this file locks in is:

    **A pointer is a hint, never a fact.** Resolve it on every call, and never invent a
    path that is not on disk.

Three real failures motivated it (2026-10-11):

1. `threejs` and `unity` fell through to `GAMES_DIR / raw`. For a pointer holding a
   repo-relative `projects/games/<name>`, that produced
   `projects/games/projects/games/<name>` - a path that cannot exist, returned silently,
   so callers failed later with an error about the wrong directory.
2. `godot` was worse: `Path(raw).resolve()` resolves a relative pointer against the
   PROCESS cwd, and MCP servers are started by pi from an arbitrary directory. A correct
   pointer silently became a nonexistent path somewhere else entirely.
3. `tests/test_asset_paths.py` walked the active project to find a file to resolve, so
   deleting a game turned a path-resolution test red.

Per stack the resolver must: follow a live pointer, refuse a stale one (relative or
absolute), resolve a bare name under `GAMES_DIR`, never re-join `GAMES_DIR` onto a path
that already carries directories, and leave an explicit absolute argument alone.

Run:  .venv\\Scripts\\python.exe tests\\test_project_paths.py
"""
from pathlib import Path
import importlib
import os
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
for _p in (ROOT, ROOT / "godot", ROOT / "unity"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

# (label, config module, env vars that override the pointer, name of the repo-root const)
STACKS = [
    ("threejs", "threejs.config", (), "THREE_RAG_HOME"),
    ("godot", "gdmaster.config", ("GDM_PROJECT", "GODOT_PROJECT_PATH"), "REPO_ROOT"),
    ("unity", "unimaster.config", ("UNITY_PROJECT", "UNIM_PROJECT"), "REPO_ROOT"),
]


def _fail(stack, msg):
    raise AssertionError("[%s] %s" % (stack, msg))


class _Stack:
    """A stack's config module with its pointer and roots redirected to a temp tree.

    Also clears the env overrides for the duration: `godot` and `unity` read
    `GDM_PROJECT` / `UNITY_PROJECT` BEFORE the pointer file, so a stray variable in the
    environment would make every pointer test here meaningless.

    Redirecting the ROOTS (not just the pointer) is what keeps this hermetic: a live
    repo-relative pointer can be tested by building a fake `projects/games/` under a temp
    directory, instead of creating games inside the user's real one.
    """

    def __init__(self, label, module_name, env_keys, root_attr):
        self.label = label
        self.cfg = importlib.import_module(module_name)
        self.env_keys = env_keys
        self.root_attr = root_attr
        self._saved = {}

    def __enter__(self):
        for k in self.env_keys:
            self._saved[k] = os.environ.pop(k, None)
        self._real_file = self.cfg.ACTIVE_PROJECT_FILE
        self._real_legacy = getattr(self.cfg, "LEGACY_ACTIVE_PROJECT_FILE", None)
        self._real_root = getattr(self.cfg, self.root_attr)
        self._real_games = self.cfg.GAMES_DIR
        return self

    def __exit__(self, *exc):
        self.cfg.ACTIVE_PROJECT_FILE = self._real_file
        if self._real_legacy is not None:
            self.cfg.LEGACY_ACTIVE_PROJECT_FILE = self._real_legacy
        setattr(self.cfg, self.root_attr, self._real_root)
        self.cfg.GAMES_DIR = self._real_games
        for k, v in self._saved.items():
            if v is not None:
                os.environ[k] = v
        return False

    def redirect_roots(self, root):
        """Point the repo root and `projects/games/` at a temp tree."""
        root = Path(root)
        games = root / "projects" / "games"
        games.mkdir(parents=True, exist_ok=True)
        setattr(self.cfg, self.root_attr, root)
        self.cfg.GAMES_DIR = games
        return games

    def point_at(self, path):
        self.cfg.ACTIVE_PROJECT_FILE = Path(path)
        # Neutralise the LEGACY fallback (`<stack>/data/active_project.txt`) whenever the
        # canonical pointer is redirected. Without this, an empty canonical pointer would
        # fall through to whatever legacy file happens to exist on the developer's disk,
        # and `test_an_empty_pointer_..._raises` would depend on the environment instead of
        # on the code. `threejs` has no legacy file, so this is conditional.
        if getattr(self.cfg, "LEGACY_ACTIVE_PROJECT_FILE", None) is not None:
            self.cfg.LEGACY_ACTIVE_PROJECT_FILE = (
                Path(path).parent / "legacy_active_project.absent.txt")

    def clear_pointer(self, directory):
        p = Path(directory) / "active_project.txt"
        p.write_text("", encoding="utf-8")
        self.point_at(p)
        return p

    @property
    def games_dir(self):
        return Path(self.cfg.GAMES_DIR)

    @property
    def repo_root(self):
        # GAMES_DIR is always <root>/projects/games in all three stacks.
        return self.games_dir.parent.parent

    def resolve(self, arg=""):
        return Path(self.cfg.resolve_project(arg))


def test_a_bare_name_resolves_under_the_games_dir_on_every_stack():
    for label, mod, env, root_attr in STACKS:
        with _Stack(label, mod, env, root_attr) as st:
            with tempfile.TemporaryDirectory() as td:
                st.redirect_roots(td)
                st.clear_pointer(td)
                got = st.resolve("not-created-yet")
                want = (st.games_dir / "not-created-yet").resolve()
                if got != want:
                    _fail(label, "bare name -> %s, expected %s" % (got, want))


def test_a_repo_relative_pointer_is_never_doubled_on_every_stack():
    """The signature of the old bug: `games` immediately followed by another `projects`."""
    for label, mod, env, root_attr in STACKS:
        with _Stack(label, mod, env, root_attr) as st:
            with tempfile.TemporaryDirectory() as td:
                st.redirect_roots(td)
                st.clear_pointer(td)
                got = st.resolve("projects/games/definitely-not-a-real-game")
                want = (st.repo_root / "projects" / "games" /
                        "definitely-not-a-real-game").resolve()
                if got != want:
                    _fail(label, "repo-relative -> %s, expected %s" % (got, want))
                tail = got.parts[got.parts.index("games") + 1:]
                if tail and tail[0] == "projects":
                    _fail(label, "path was doubled: %s" % got)


def test_a_live_pointer_is_followed_on_every_stack():
    """The normal case must keep working - the fix is not allowed to break it."""
    for label, mod, env, root_attr in STACKS:
        with _Stack(label, mod, env, root_attr) as st:
            with tempfile.TemporaryDirectory() as td:
                project = Path(td) / "live_game"
                (project / "assets").mkdir(parents=True)
                pointer = Path(td) / "active_project.txt"
                pointer.write_text(str(project), encoding="utf-8")
                st.point_at(pointer)

                got = st.resolve("")
                if got != project.resolve():
                    _fail(label, "live pointer -> %s, expected %s" % (got, project.resolve()))


def test_a_live_repo_relative_pointer_is_followed_on_every_stack():
    """`agent.cmd projects\\games\\<name>` stores a repo-relative string - the common case.

    This is the exact shape that was in `data/active_project.txt` when the bug surfaced,
    so it is covered explicitly rather than only in its absolute form.
    """
    for label, mod, env, root_attr in STACKS:
        with _Stack(label, mod, env, root_attr) as st:
            with tempfile.TemporaryDirectory() as td:
                games = st.redirect_roots(td)
                project = games / "repo_rel_game"
                project.mkdir(parents=True)
                pointer = Path(td) / "active_project.txt"
                pointer.write_text("projects/games/repo_rel_game", encoding="utf-8")
                st.point_at(pointer)

                got = st.resolve("")
                if got != project.resolve():
                    _fail(label, "live repo-relative pointer -> %s, expected %s"
                          % (got, project.resolve()))


def test_a_stale_repo_relative_pointer_raises_on_every_stack():
    """Same shape, but the game is gone: the pointer must be reported, not guessed at."""
    for label, mod, env, root_attr in STACKS:
        with _Stack(label, mod, env, root_attr) as st:
            with tempfile.TemporaryDirectory() as td:
                st.redirect_roots(td)
                pointer = Path(td) / "active_project.txt"
                pointer.write_text("projects/games/vanished-game", encoding="utf-8")
                st.point_at(pointer)
                try:
                    st.resolve("")
                except ValueError as err:
                    if "vanished-game" not in str(err):
                        _fail(label, "message does not name the dead pointer: %s" % err)
                else:
                    _fail(label, "a stale repo-relative pointer must raise")


def test_a_stale_absolute_pointer_raises_on_every_stack():
    """`agent.cmd C:\\gone\\game` stores an absolute path - it goes stale too."""
    for label, mod, env, root_attr in STACKS:
        with _Stack(label, mod, env, root_attr) as st:
            with tempfile.TemporaryDirectory() as td:
                gone = Path(td) / "was-here-yesterday"
                pointer = Path(td) / "active_project.txt"
                pointer.write_text(str(gone), encoding="utf-8")
                st.point_at(pointer)
                try:
                    st.resolve("")
                except ValueError as err:
                    if "was-here-yesterday" not in str(err):
                        _fail(label, "message does not name the dead pointer: %s" % err)
                else:
                    _fail(label, "a stale absolute pointer must raise")


def test_an_empty_pointer_and_no_argument_raises_on_every_stack():
    for label, mod, env, root_attr in STACKS:
        with _Stack(label, mod, env, root_attr) as st:
            with tempfile.TemporaryDirectory() as td:
                st.clear_pointer(td)
                try:
                    st.resolve("")
                except ValueError:
                    pass
                else:
                    _fail(label, "no project anywhere must raise")


def test_an_explicit_absolute_path_is_left_alone_on_every_stack():
    """Only the POINTER is a claim about user data. An explicit argument is not."""
    for label, mod, env, root_attr in STACKS:
        with _Stack(label, mod, env, root_attr) as st:
            missing = (Path(tempfile.gettempdir()) / "explicit-not-created").resolve()
            got = st.resolve(str(missing))
            if got != missing:
                _fail(label, "explicit absolute -> %s, expected %s" % (got, missing))


def test_the_resolver_reads_the_pointer_at_call_time_not_at_import_on_every_stack():
    """The whole point: a pointer that changes (or dies) is seen on the NEXT call.

    If the value were cached at import, a game deleted mid-session would keep resolving
    to the dead path for the life of the MCP server.
    """
    for label, mod, env, root_attr in STACKS:
        with _Stack(label, mod, env, root_attr) as st:
            with tempfile.TemporaryDirectory() as td:
                project = Path(td) / "first_game"
                project.mkdir(parents=True)
                pointer = Path(td) / "active_project.txt"
                pointer.write_text(str(project), encoding="utf-8")
                st.point_at(pointer)

                if st.resolve("") != project.resolve():
                    _fail(label, "live pointer was not followed")

                # The game is deleted; the pointer now names nothing.
                project.rmdir()
                try:
                    st.resolve("")
                except ValueError:
                    continue
                _fail(label, "the resolver kept using a project that no longer exists")


def test_all_three_stacks_read_the_same_pointer_file():
    """**One fact, one file.** `agent.cmd` writes ONE pointer; every stack must read it.

    The defect this locks in (2026-10-11): `threejs` resolved
    `<repo>/data/active_project.txt`, but `godot` read `godot/data/active_project.txt` and
    `unity` read `unity/data/active_project.txt` - two files that NOTHING ever writes
    (`set_active_project` is the only writer and no caller invokes it). So a Godot or
    Unity agent silently saw "no project" and fell back to "." while the launcher had just
    recorded the real one, and only the threejs agent ever worked.

    A pointer whose location differs per stack is a pointer that will disagree per stack.
    """
    want = (ROOT / "data" / "active_project.txt").resolve()
    seen = {}
    for label, mod, env, root_attr in STACKS:
        cfg = importlib.import_module(mod)
        got = Path(cfg.ACTIVE_PROJECT_FILE).resolve()
        seen[label] = got
        if got != want:
            _fail(label, "reads %s, but the canonical pointer is %s" % (got, want))
    if len(set(seen.values())) != 1:
        raise AssertionError("the stacks disagree about the pointer file: %r" % seen)


def test_a_legacy_pointer_is_only_a_fallback():
    """The per-stack legacy file must never OUTRANK the canonical one.

    Both `godot` and `unity` keep their old `data/active_project.txt` path as a
    `LEGACY_ACTIVE_PROJECT_FILE` so an existing deployment does not lose its pointer. That
    fallback is read SECOND - if it were read first, a stale per-stack file would silently
    override the launcher's canonical write.
    """
    for label, mod, env, root_attr in STACKS:
        cfg = importlib.import_module(mod)
        legacy = getattr(cfg, "LEGACY_ACTIVE_PROJECT_FILE", None)
        if legacy is None:
            continue  # threejs: its DATA_DIR already IS <repo>/data, no legacy path.
        with _Stack(label, mod, env, root_attr) as st:
            with tempfile.TemporaryDirectory() as td:
                legacy_dir = Path(td) / "stack_data"
                legacy_dir.mkdir(parents=True)
                st.cfg.LEGACY_ACTIVE_PROJECT_FILE = legacy_dir / "active_project.txt"
                st.cfg.LEGACY_ACTIVE_PROJECT_FILE.write_text(
                    "projects/games/from-legacy", encoding="utf-8")

                canonical_dir = Path(td) / "repo_data"
                canonical_dir.mkdir(parents=True)
                st.cfg.ACTIVE_PROJECT_FILE = canonical_dir / "active_project.txt"
                st.cfg.ACTIVE_PROJECT_FILE.write_text(
                    "projects/games/from-canonical", encoding="utf-8")

                if st.cfg.pointer_text() != "projects/games/from-canonical":
                    _fail(label, "the legacy file outranked the canonical one")

                # And with the canonical file empty/absent, the legacy one takes over.
                st.cfg.ACTIVE_PROJECT_FILE.write_text("", encoding="utf-8")
                if st.cfg.pointer_text() != "projects/games/from-legacy":
                    _fail(label, "the legacy file was not used as a fallback")


if __name__ == "__main__":
    import traceback
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
