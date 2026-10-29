"""Tests for the serialised generation scheduler.

The interesting properties are not "does it generate an image" (that is ComfyUI's job)
but the bookkeeping around it:

* the language model is stopped before ComfyUI starts and restarted afterwards, and
  **restarted even when the run fails** - otherwise an exception leaves the agent with
  no brain until a human notices;
* the two models are never resident at the same time;
* a pack survives one bad job, and dependants of that job are skipped with a reason;
* finished files land in the project at their final paths, with the served URL worked
  out for anything under `public/`.

Nothing here talks to a real server: ComfyUI, llama-server and the pipeline are stubs.
"""
from pathlib import Path
import sys
import tempfile
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from threejs.assets import hardware, scheduler as sched_mod  # noqa: E402
from threejs.assets.pipeline import Artefact  # noqa: E402
from threejs.assets.scheduler import GenerationScheduler, Job  # noqa: E402


# ------------------------------------------------------------------- doubles
class FakeComfy:
    port = 8188

    def __init__(self, events, fail_ensure=False):
        self.events = events
        self.alive = False
        self.fail_ensure = fail_ensure

    def is_alive(self):
        return self.alive

    def ensure(self, timeout=0):
        if self.fail_ensure:
            raise sched_mod.SchedulerError("ComfyUI did not come up")
        self.alive = True
        self.events.append("comfy_up")
        return {"started": True}

    def stop(self, wait=0):
        # Mirrors `ComfyClient.stop()`: a server that never started is a no-op, and its
        # "nothing to stop" branch carries a `vram` key - the shape that used to make
        # `_mark(step, vram=vram(), **stop())` a TypeError *inside the teardown path*.
        if not self.alive:
            return {"stopped": False, "reason": "no pid", "vram": {"used_mb": 0}}
        self.alive = False
        self.events.append("comfy_down")
        return {"stopped": True}

    def status(self):
        return {"alive": self.alive}


class FakeLlama:
    launcher = "serve-llm.cmd"
    log = "llm-sidecar.log"
    port = 8080

    def __init__(self, events, up=True):
        self.events = events
        self.up = up

    def alive(self):
        return self.up

    def pid(self):
        return 4242 if self.up else 0

    def stop(self, wait=0):
        self.up = False
        self.events.append("llm_down")
        return {"stopped": True, "pid": 4242}

    def ensure(self, timeout=0):
        self.up = True
        self.events.append("llm_up")
        return {"started": True}

    def info(self):
        return {"alive": self.up, "port": self.port}


class FakeSd:
    """Stand-in for `SdServer` (z-image on :8687).

    Only `stop()` on a *live* server emits an event, mirroring the real class: its
    "nothing was listening" branch returns a dict with a `vram` key and does nothing,
    which is exactly the shape that used to blow up the teardown path.
    """

    port = 8687

    def __init__(self, events):
        self.events = events
        self._up = False

    def alive(self):
        return self._up

    def pid(self):
        return 5150 if self._up else 0

    def ensure(self, timeout=0):
        if not self._up:
            self._up = True
            self.events.append("sd_up")
        return {"started": True, "pid": self.pid()}

    def stop(self, wait=0):
        if not self._up:
            return {"stopped": False, "reason": "nothing listening on :8687",
                    "vram": {"used_mb": 0}}
        self._up = False
        self.events.append("sd_down")
        return {"stopped": True, "pid": 5150, "port_free": True}

    def info(self):
        return {"alive": self._up, "port": self.port, "pid": self.pid()}


class FakePipeline:
    """Writes a plausible artefact per call, so `_place_all` has something to move.

    `seen` records the keyword arguments every `image` call received: the scheduler
    builds them, and a parameter it forgets to forward (megapixels, once) is invisible
    in the output - the workflow just quietly uses its own default.
    """

    seen: list = []

    def __init__(self, client=None, root=None, sd=None):
        self.client = client
        self.sd = sd                      # the z-image client; the real ctor takes it
        self.root = Path(root)

    def _write(self, kind, name, ext):
        path = self.root / kind / f"{name}{ext}"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"x" * 64)
        return Artefact(kind=kind, path=str(path), bytes=64, filename=path.name)

    def image(self, prompt, name="", **kw):
        FakePipeline.seen.append({"prompt": prompt, "name": name, "via": "image", **kw})
        if name == "boom":
            raise sched_mod.SchedulerError("workflow exploded")
        return [self._write("image", name, ".png")]

    def image_fast(self, prompt, name="", **kw):
        """The z-image path. A separate entry point, so `seen` has to record which one
        was taken - otherwise "did this job stay on the fast engine" is unanswerable."""
        FakePipeline.seen.append({"prompt": prompt, "name": name, "via": "image_fast", **kw})
        if name == "boom":
            raise sched_mod.SchedulerError("workflow exploded")
        return [self._write("image", name, ".png")]

    def upscale(self, image, name="", **kw):
        FakePipeline.seen.append({"name": name, "via": "upscale", **kw})
        return [self._write("image", name, "@2x.png")]

    def recolor(self, image, prompt="", name="", **kw):
        FakePipeline.seen.append({"prompt": prompt, "name": name, "via": "recolor", **kw})
        return [self._write("image", name, ".png")]

    def remove_bg(self, image, name="", **kw):
        return [self._write("mask", name, "-nobg.png")]

    def to_3d(self, image, name="", **kw):
        FakePipeline.seen.append({"name": name, "via": "to_3d", **kw})
        return [self._write("mesh", name, ".glb"), self._write("splat", name, ".spz")]


def _scheduler(tmp, events, *, llm_up=True, comfy=None, sd=None, **kw):
    tmp = Path(tmp)
    return GenerationScheduler(
        comfy=comfy or FakeComfy(events), llm=FakeLlama(events, up=llm_up),
        sd=sd or FakeSd(events),
        log_path=tmp / "generate.log", lock_path=tmp / "gen.lock",
        status_path=tmp / "gen-status.json", staging_dir=tmp / "staging", **kw)


def _patch_pipeline(fake=FakePipeline):
    original = sched_mod.AssetPipeline
    sched_mod.AssetPipeline = fake
    return original


# --------------------------------------------------------------- encoding bug
def test_run_text_survives_a_non_utf8_console():
    """Regression: with PYTHONUTF8=1, `text=True` decoded netstat's CP866 output as
    UTF-8. The UnicodeDecodeError fired in a reader thread, `stdout` came back as None,
    and the failure showed up as `AttributeError: 'NoneType' has no attribute
    'splitlines'` - while `comfy.py` swallowed it and reported "no pid" for a ComfyUI
    that was running perfectly well."""
    cp866 = ("Активные подключения\r\n\r\n"
             "  TCP    127.0.0.1:8080    0.0.0.0:0    LISTENING    4242\r\n").encode("cp866")
    original = hardware.subprocess.run
    hardware.subprocess.run = lambda *a, **k: type("P", (), {"stdout": cp866})()
    try:
        out = hardware.run_text(["netstat"])
    finally:
        hardware.subprocess.run = original
    assert "8080" in out and "4242" in out and "LISTENING" in out


def test_port_pid_ignores_established_connections():
    original = hardware.run_text
    hardware.run_text = lambda *a, **k: (
        "  TCP    127.0.0.1:8080    127.0.0.1:5555    ESTABLISHED    9999\n"
        "  TCP    0.0.0.0:8080      0.0.0.0:0         LISTENING      4242\n")
    try:
        assert hardware.port_pid(8080) == 4242      # the listener, not the client
        assert hardware.port_pid(8188) == 0
    finally:
        hardware.run_text = original


# ------------------------------------------------------------- job parsing
def test_job_aliases_and_validation():
    assert Job.from_dict({"kind": "character", "prompt": "a fox"}, 0).kind == "3d"
    assert Job.from_dict({"kind": "mesh", "prompt": "a fox"}, 0).kind == "3d"
    assert Job.from_dict({"kind": "remove_bg", "image": "a.png"}, 0).kind == "mask"
    # the slug comes from the request, never from a counter
    assert Job.from_dict({"kind": "image", "prompt": "Создай синего монстра"}, 0).name == \
        "sinego-monstra"
    # an explicit name wins, and backslashes in `out` are normalised
    job = Job.from_dict({"kind": "image", "prompt": "x", "name": "Nova Hero",
                         "out": "public\\assets\\nova.png"}, 0)
    assert job.name == "nova-hero" and job.out == "public/assets/nova.png"
    # a nameless mask job borrows the source's stem rather than becoming "asset"
    assert Job.from_dict({"kind": "mask", "image": "src/assets/hero.png"}, 0).name == "hero"
    # 0 means "keep the workflow default", not "run zero steps"
    assert Job.from_dict({"kind": "image", "prompt": "x", "steps": 0}, 0).steps is None
    assert Job.from_dict({"kind": "image", "prompt": "x", "steps": 8}, 0).steps == 8

    for bad in ({"kind": "image"},                                  # no prompt
                {"kind": "3d"},                                     # no input, no prompt
                {"kind": "sausage", "prompt": "x"},                 # unknown kind
                "not an object"):
        try:
            Job.from_dict(bad, 0)
        except sched_mod.SchedulerError:
            pass
        else:
            raise AssertionError(f"expected SchedulerError for {bad!r}")


# ------------------------------------------------------------ path placement
def test_dest_paths_default_and_explicit():
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        project = tmp / "proj"
        s = _scheduler(tmp, [])
        mesh = {"kind": "mesh", "filename": "nova.glb"}
        splat = {"kind": "splat", "filename": "nova.spz"}

        # no `out`: the mirror of the global store, inside the project
        default = Job.from_dict({"kind": "3d", "name": "nova", "prompt": "x"}, 0)
        assert s._dest(default, mesh, project, primary=True).as_posix().endswith(
            "proj/public/assets/3d/nova.glb")

        # explicit `out`, extension inferred from the artefact
        explicit = Job.from_dict({"kind": "3d", "name": "nova", "prompt": "x",
                                  "out": "public/assets/models/player/nova"}, 0)
        assert s._dest(explicit, mesh, project, primary=True).as_posix().endswith(
            "public/assets/models/player/nova.glb")
        # the splat must not overwrite the mesh - it becomes a sibling
        assert s._dest(explicit, splat, project, primary=False).as_posix().endswith(
            "public/assets/models/player/nova-splat.spz")
        # an absolute `out` is honoured as-is
        absolute = Job.from_dict({"kind": "image", "prompt": "x",
                                  "out": str(tmp / "elsewhere" / "a.png")}, 0)
        assert s._dest(absolute, {"kind": "image", "filename": "a.png"}, project,
                       primary=True) == tmp / "elsewhere" / "a.png"


def test_place_moves_files_and_computes_public_urls():
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        project = tmp / "proj"
        staging = tmp / "staging"
        (staging / "3d").mkdir(parents=True)
        src = staging / "3d" / "nova.glb"
        src.write_bytes(b"g" * 32)
        s = _scheduler(tmp, [])
        s._jobs = [Job.from_dict({"kind": "3d", "name": "nova", "prompt": "x",
                                  "out": "public/assets/models/player/nova.glb"}, 0)]
        report = {"jobs": [{"index": 0, "name": "nova", "kind": "3d", "ok": True,
                            "files": [{"kind": "mesh", "path": str(src),
                                       "filename": "nova.glb", "bytes": 32}]}]}
        placed = s._place_all(report, project)
        assert len(placed) == 1
        assert placed[0]["rel"] == "public/assets/models/player/nova.glb"
        assert placed[0]["url"] == "/assets/models/player/nova.glb"
        assert placed[0]["overwrote"] is False
        assert (project / "public/assets/models/player/nova.glb").read_bytes() == b"g" * 32
        assert not src.exists()                     # it was moved, not copied

        # a second run at the same path overwrites in place - the game's import must
        # keep resolving - and says so
        src.write_bytes(b"h" * 48)
        again = s._place_all(report, project)
        assert again[0]["overwrote"] is True
        assert (project / "public/assets/models/player/nova.glb").read_bytes() == b"h" * 48


# --------------------------------------------------------------------- lock
def test_lock_is_exclusive_and_reclaims_a_dead_holder():
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "gen.lock"
        first = hardware.GenLock(path)
        first.acquire()
        try:
            assert path.exists()
            second = hardware.GenLock(path)
            try:
                second.acquire(timeout=0.1)
            except sched_mod.SchedulerError as e:
                assert "already running" in str(e)
            else:
                raise AssertionError("the second lock should not have been granted")
        finally:
            first.release()
        assert not path.exists()

        # a lock whose holder no longer exists must not block forever
        path.write_text('{"pid": 999999, "t": %f}' % time.time(), encoding="utf-8")
        third = hardware.GenLock(path)
        third.acquire(timeout=1.0)
        third.release()


# ------------------------------------------------------- the ordering guarantee
def test_llm_is_off_before_comfy_starts_and_back_after_it_stops():
    with tempfile.TemporaryDirectory() as td:
        events = []
        s = _scheduler(td, events)
        original = _patch_pipeline()
        try:
            report = s.generate_pack(str(Path(td) / "proj"), [
                {"kind": "image", "name": "grass", "prompt": "grass", "engine": "comfy"}])
        finally:
            sched_mod.AssetPipeline = original

        assert events == ["llm_down", "comfy_up", "comfy_down", "llm_up"], events
        assert report["ok"] is True
        assert report["llm"]["was_up"] is True and report["llm"]["restored"] is True
        assert report["files"][0]["rel"] == "public/assets/images/grass.png"
        assert (Path(td) / "proj/public/assets/images/grass.png").exists()


def test_a_plain_image_job_never_wakes_comfyui():
    """`auto` sends images to z-image. The whole point of the fast engine is that a pack
    of backgrounds does not pay a ComfyUI boot - assert the backend stays untouched."""
    with tempfile.TemporaryDirectory() as td:
        events = []
        s = _scheduler(td, events)
        original = _patch_pipeline()
        try:
            report = s.generate_pack(str(Path(td) / "proj"), [
                {"kind": "image", "name": "grass", "prompt": "grass"},
                {"kind": "recolor", "name": "dusk", "from": "grass", "prompt": "dusk"}])
        finally:
            sched_mod.AssetPipeline = original

        assert events == ["llm_down", "sd_up", "sd_down", "llm_up"], events
        assert report["ok"] is True and report["engine_switches"] == 1
        assert [r["engine"] for r in report["jobs"]] == ["z-image", "z-image"]


def test_a_mixed_pack_switches_backends_once_per_engine_change():
    with tempfile.TemporaryDirectory() as td:
        events = []
        s = _scheduler(td, events)
        original = _patch_pipeline()
        try:
            report = s.generate_pack(str(Path(td) / "proj"), [
                {"kind": "image", "name": "a", "prompt": "x"},
                {"kind": "image", "name": "b", "prompt": "x"},
                {"kind": "3d", "name": "c", "from": "a", "quality": "economy"},
                {"kind": "upscale", "name": "d", "from": "b", "scale": 2},
            ])
        finally:
            sched_mod.AssetPipeline = original

        assert events == ["llm_down", "sd_up", "sd_down", "comfy_up", "comfy_down", "llm_up"], events
        assert report["engine_switches"] == 2, report["engine_switches"]
        assert [r["engine"] for r in report["jobs"]] == \
            ["z-image", "z-image", "comfy", "none"]
        assert report["ok"] is True


def test_llm_is_restored_even_when_the_run_fails():
    """The one failure mode that must never happen: an exception on the way out leaves
    the agent with no model to think with."""
    with tempfile.TemporaryDirectory() as td:
        events = []
        s = _scheduler(td, events, comfy=FakeComfy(events, fail_ensure=True))
        original = _patch_pipeline()
        try:
            report = s.generate_pack(str(Path(td) / "proj"), [
                {"kind": "image", "name": "grass", "prompt": "grass", "engine": "comfy"}])
        finally:
            sched_mod.AssetPipeline = original

        # A backend that will not start is a *job* failure, not a pack-level one: the
        # backends are started lazily per engine, so an engine that refuses to come up
        # no longer aborts jobs that never needed it.
        assert report["error"] is None
        assert "ComfyUI did not come up" in report["jobs"][0]["error"]
        assert report["ok"] is False
        # nothing to stop, because nothing ever came up - and the teardown still ran
        assert events == ["llm_down", "llm_up"], events
        assert report["llm"]["restored"] is True
        assert s.llm.alive() is True


def test_teardown_survives_a_stop_report_that_carries_its_own_vram():
    """Regression: `SdServer.stop()` (and ComfyUI's "no pid" branch) return a dict that
    already contains a `vram` key. `self._mark(step, vram=vram(), **that)` is then a
    TypeError *at the call site* - and the call site is the teardown, the one place that
    must not throw, because a throw there skips `_restore_llm` and leaves the agent with
    no model. Every job in the pack had already succeeded when this fired."""
    with tempfile.TemporaryDirectory() as td:
        events = []
        s = _scheduler(td, events)
        original = _patch_pipeline()
        try:
            report = s.generate_pack(str(Path(td) / "proj"),
                                     [{"kind": "image", "name": "a", "prompt": "x"}])
        finally:
            sched_mod.AssetPipeline = original

        assert report["ok"] is True, report.get("error")
        assert report["llm"]["restored"] is True          # the teardown got that far
        assert events == ["llm_down", "sd_up", "sd_down", "llm_up"], events
        # the vram reading on the timeline is a live one, not a stale copy from `stop()`
        stops = [e for e in report["timeline"] if e["step"] in ("comfy_stopped", "sd_stopped")]
        assert stops and all("vram" in e for e in stops), stops


def test_a_failed_job_does_not_abort_the_pack_and_skips_its_dependants():
    with tempfile.TemporaryDirectory() as td:
        events = []
        s = _scheduler(td, events)
        original = _patch_pipeline()
        try:
            report = s.generate_pack(str(Path(td) / "proj"), [
                {"kind": "image", "name": "boom", "prompt": "explode"},
                {"kind": "3d", "name": "child", "from": "boom", "quality": "economy"},
                {"kind": "image", "name": "fine", "prompt": "a rock"},
            ])
        finally:
            sched_mod.AssetPipeline = original

        rows = {r["name"]: r for r in report["jobs"]}
        assert rows["boom"]["ok"] is False and "exploded" in rows["boom"]["error"]
        assert rows["child"]["ok"] is False
        assert "boom" in rows["child"]["error"] and "failed" in rows["child"]["error"]
        assert rows["fine"]["ok"] is True                    # the pack carried on
        assert report["ok"] is False                         # but it is not a clean run
        assert report["failed"] == ["boom", "child"]
        assert [f["job"] for f in report["files"]] == ["fine"]
        assert report["staging"]                             # kept for inspection
        assert Path(report["staging"]).exists()


def test_image_parameters_reach_the_workflow():
    """`resolution` is only the text encoder's pixel hint - the size of the picture that
    comes out is ResolutionSelector(aspect_ratio, megapixels). The scheduler used to drop
    megapixels on the floor, so a job asking for a small, fast image silently got the
    workflow's 1 MP default and a 1024x1024 PNG.

    Both engines are checked: z-image has no `resolution` input at all, so its size comes
    from `aspect_ratio` + `megapixels` alone.
    """
    with tempfile.TemporaryDirectory() as td:
        events = []
        s = _scheduler(td, events)
        original = _patch_pipeline()
        FakePipeline.seen.clear()
        try:
            s.generate_pack(str(Path(td) / "proj"), [
                # z-image first, so the two ComfyUI jobs share one backend session
                {"kind": "image", "name": "fast", "prompt": "x", "megapixels": 0.25,
                 "aspect_ratio": "16:9 (Widescreen)", "steps": 4, "seed": 7},
                {"kind": "image", "name": "tiny", "prompt": "x", "resolution": 512,
                 "megapixels": 0.25, "aspect_ratio": "16:9 (Widescreen)", "steps": 4,
                 "seed": 7, "engine": "comfy"},
                # a 3D job with no input makes its own image and must forward them too
                {"kind": "3d", "name": "tiny-mesh", "prompt": "y", "megapixels": 0.5},
            ])
        finally:
            sched_mod.AssetPipeline = original

        def entry(name, via):
            return next(e for e in FakePipeline.seen
                        if e.get("name") == name and e.get("via") == via)

        fast = entry("fast", "image_fast")
        assert fast["megapixels"] == 0.25 and fast["steps"] == 4 and fast["seed"] == 7, fast
        assert fast["aspect_ratio"] == "16:9 (Widescreen)", fast

        tiny = entry("tiny", "image")
        assert tiny["megapixels"] == 0.25, tiny
        assert tiny["resolution"] == 512 and tiny["steps"] == 4 and tiny["seed"] == 7, tiny
        assert tiny["aspect_ratio"] == "16:9 (Widescreen)", tiny

        assert entry("tiny-mesh", "image")["megapixels"] == 0.5
        # and the parser keeps 0 as "unset" rather than passing a literal 0 megapixels
        assert Job.from_dict({"kind": "image", "prompt": "x", "megapixels": 0}, 0).megapixels is None
        assert Job.from_dict({"kind": "image", "prompt": "x", "megapixels": 0.25}, 0).megapixels == 0.25
        # the 3D lever is a separate field and must survive parsing
        assert Job.from_dict({"kind": "3d", "prompt": "x", "quality": "high",
                              "resolution_3d": 512}, 0).resolution_3d == 512
        assert Job.from_dict({"kind": "3d", "prompt": "x"}, 0).quality == "high"


def test_faces_3d_is_the_knob_that_reaches_the_decimator():
    """`resolution_3d` was documented as the cost lever and measured to be a no-op
    (512 and 1024 both produced ~698 500 faces). The output size is set by
    `DecimateMesh.target_face_count` in the graph, so the scheduler has to be able to
    reach it - otherwise every prop ships at the workflow's 700 000-face default."""
    with tempfile.TemporaryDirectory() as td:
        events = []
        s = _scheduler(td, events)
        original = _patch_pipeline()
        FakePipeline.seen.clear()
        try:
            s.generate_pack(str(Path(td) / "proj"), [
                {"kind": "image", "name": "prop", "prompt": "x"},
                {"kind": "3d", "name": "prop-mesh", "from": "prop",
                 "quality": "high", "faces_3d": 8000, "steps_3d": 6},
            ])
        finally:
            sched_mod.AssetPipeline = original

        three = next(e for e in FakePipeline.seen if e.get("via") == "to_3d")
        assert three["faces"] == 8000, three
        assert three["steps"] == 6, three
        assert three["quality"] == "high", three

        assert Job.from_dict({"kind": "3d", "prompt": "x", "faces_3d": 8000}, 0).faces_3d == 8000
        assert Job.from_dict({"kind": "3d", "prompt": "x"}, 0).faces_3d is None


def test_a_dependency_feeds_the_next_job_within_one_comfy_session():
    with tempfile.TemporaryDirectory() as td:
        events = []
        s = _scheduler(td, events)
        original = _patch_pipeline()
        try:
            report = s.generate_pack(str(Path(td) / "proj"), [
                {"kind": "image", "name": "hero", "prompt": "a fox"},
                {"kind": "3d", "name": "hero-mesh", "from": "hero", "quality": "economy",
                 "out": "public/assets/models/player/nova.glb"},
            ])
        finally:
            sched_mod.AssetPipeline = original
        # one start per backend for the whole pack, not one per job
        assert events.count("sd_up") == 1, events
        assert events.count("comfy_up") == 1, events
        assert events.count("llm_up") == 1, events
        kinds = {f["kind"] for f in report["files"]}
        assert kinds == {"image", "mesh", "splat"}
        assert any(f["url"] == "/assets/models/player/nova.glb" for f in report["files"])


# ------------------------------------------------------------------- opt-outs
def test_keep_comfy_and_stop_llm_false_are_honoured():
    with tempfile.TemporaryDirectory() as td:
        events = []
        s = _scheduler(td, events)
        original = _patch_pipeline()
        try:
            s.generate_pack(str(Path(td) / "proj"),
                            [{"kind": "image", "name": "a", "prompt": "x",
                              "engine": "comfy"}],
                            keep_comfy=True)
        finally:
            sched_mod.AssetPipeline = original
        assert "comfy_down" not in events and s.comfy.is_alive() is True

        events2 = []
        s2 = _scheduler(td, events2)
        original = _patch_pipeline()
        try:
            report = s2.generate_pack(str(Path(td) / "proj"),
                                      [{"kind": "image", "name": "b", "prompt": "x"}],
                                      stop_llm=False)
        finally:
            sched_mod.AssetPipeline = original
        assert events2 == ["sd_up", "sd_down"], events2
        assert report["llm"]["restored"] is False
        assert "stop_llm=False" in report["llm"]["reason"]


def test_a_pack_with_no_jobs_is_refused():
    with tempfile.TemporaryDirectory() as td:
        s = _scheduler(td, [])
        try:
            s.generate_pack(str(Path(td) / "proj"), [])
        except sched_mod.SchedulerError as e:
            assert "empty pack" in str(e)
        else:
            raise AssertionError("an empty pack should be refused")


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
