"""ComfyUI sidecar client.

The parts that matter for speed:

* **The server stays resident.** The 19-28 s warm generation time is not a fast model -
  it is ComfyUI never being restarted, so the weights are already in RAM/VRAM. Killing
  the server between runs is what turns 20 s into 30-130 s.
* **Idle stop, not stop-per-run.** A watchdog thread kills the server only after
  `idle_stop_s` of inactivity, and `0` disables it entirely (default).
* **Stale-server adoption.** A ComfyUI left over from a previous session is reused if the
  process listening on the port really is our portable build - identified by its image
  path containing `ComfyUI-Easy-Install`. A ComfyUI the user started by hand is left alone.

Protocol: HTTP `/prompt`, `/history/{id}`, `/view`, `/upload/image`, `/system_stats`,
`/interrupt`. No websocket: progress is polled from `/history`, which is enough for a
tool call and removes a whole class of connection bugs.
"""
from __future__ import annotations

import json
import os
import shutil
import socket
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
import uuid
from pathlib import Path

from .. import config
from .hardware import port_pid, process_path

CEI_DIR = "ComfyUI-Easy-Install"
DEFAULT_IDLE_STOP_S = int(os.environ.get("THREE_COMFY_IDLE_STOP_S", "0"))


class ComfyError(RuntimeError):
    pass


class ComfyClient:
    def __init__(
        self,
        root: Path | str | None = None,
        host: str | None = None,
        port: int | None = None,
        vram_mode: str | None = None,
        idle_stop_s: int | None = None,
        custom_nodes: tuple[str, ...] | None = None,
    ):
        self.host = host or config.COMFY_HOST
        self.port = int(port or config.COMFY_PORT)
        self.base = f"http://{self.host}:{self.port}"
        self.root = Path(root) if root else self.find_root()
        self.vram_mode = vram_mode or os.environ.get("THREE_COMFY_VRAM_MODE", "lowvram")
        self.idle_stop_s = DEFAULT_IDLE_STOP_S if idle_stop_s is None else int(idle_stop_s)
        # `None` means "use the policy default"; `()` means "load no third-party pack at all".
        self.custom_nodes = config.COMFY_CUSTOM_NODES if custom_nodes is None else tuple(custom_nodes)
        self._proc: subprocess.Popen | None = None
        self._lock = threading.RLock()
        self._idle_timer: threading.Timer | None = None
        self._log = config.LOGS_DIR / "comfy-sidecar.log"
        self._pid_file = config.DATA_DIR / "comfy.pid"
        self._opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        # Filled by `run()`: what the last `drop_nodes` call removed and bridged. Kept on the
        # instance rather than printed, because this module is also imported by the stdio
        # MCP servers, where anything written to stdout corrupts the JSON-RPC stream.
        self.drop_report: dict | None = None

    # ---------------------------------------------------------------- discovery
    def _roots(self) -> list[Path]:
        roots: list[Path] = []
        env = os.environ.get("THREE_COMFY_ROOT") or os.environ.get("HC_COMFY_ROOT")
        if env:
            roots.append(Path(env))
        roots.append(config.COMFY_ROOT)
        # dev / legacy layouts. The `models/text_image_3D` entry is the live one (moved
        # there 2026-10-12); the root-level ones stay so a checkout that still has the
        # old layout, or a stray `THREE_TEXT_IMAGE_3D_DIR` override, keeps working.
        base = config.THREE_RAG_HOME
        roots += [
            base / "models" / "text_image_3D" / "3d_gen" / "3d_comfy" / CEI_DIR,
            base / "comfy" / CEI_DIR,
            base / "text_image_3D" / "3d_gen" / "3d_comfy" / CEI_DIR,
            base / "text_image_3D" / "3d" / "3d_comfy" / CEI_DIR,
        ]
        return roots

    def find_root(self) -> Path | None:
        for root in self._roots():
            if (root / "python_embeded" / "python.exe").exists() and (root / "ComfyUI" / "main.py").exists():
                return root
        return None

    @property
    def python(self) -> Path | None:
        return (self.root / "python_embeded" / "python.exe") if self.root else None

    # ---------------------------------------------------------------- lifecycle
    def _get(self, path: str, timeout: float = 8.0):
        req = urllib.request.Request(self.base + path, headers={"User-Agent": "3gs-assets"})
        with self._opener.open(req, timeout=timeout) as r:
            body = r.read()
            return json.loads(body.decode("utf-8", "replace")) if body else {}

    def _post(self, path: str, payload: dict | None = None, timeout: float = 120.0):
        data = json.dumps(payload or {}).encode("utf-8")
        req = urllib.request.Request(
            self.base + path, data=data,
            headers={"Content-Type": "application/json", "User-Agent": "3gs-assets"},
            method="POST",
        )
        try:
            with self._opener.open(req, timeout=timeout) as r:
                body = r.read()
                return json.loads(body.decode("utf-8", "replace")) if body else {}
        except urllib.error.HTTPError as e:
            # ComfyUI answers a rejected graph with a 400 whose *body* names the offending
            # node and input ("Required input is missing: images"). Letting the bare
            # HTTPError escape throws that away and leaves a traceback that says nothing but
            # "HTTP Error 400: Bad Request" - which is what made a broken workflow
            # indistinguishable from a broken client.
            detail = ""
            try:
                detail = e.read().decode("utf-8", "replace")[:1500]
            except Exception:  # noqa: BLE001
                pass
            raise ComfyError(f"POST {path} -> HTTP {e.code} {e.reason}: {detail}") from e

    def is_alive(self) -> bool:
        try:
            self._get("/system_stats", timeout=4.0)
            return True
        except Exception:  # noqa: BLE001
            return False

    def _port_pid(self) -> int:
        """Who holds the port. Delegated to `hardware.port_pid`, which decodes netstat's
        CP866 output correctly - doing it inline with `text=True` used to raise inside a
        reader thread, return `None`, and get swallowed by the caller's `except`,
        silently reporting "no pid" for a ComfyUI that was very much running."""
        return port_pid(self.port)

    def _pid_image(self, pid: int) -> str:
        return process_path(pid)

    def adopt_or_kill_stale(self) -> str:
        """Reuse our own leftover ComfyUI; never touch a foreign process on the port."""
        if not self.is_alive():
            self._pid_file.unlink(missing_ok=True)
            return "none"
        pid = self._port_pid()
        image = self._pid_image(pid)
        if CEI_DIR.lower() in image.lower():
            self._write_pid(pid)
            return f"reused pid={pid}"
        return f"port {self.port} held by a foreign process ({image or 'unknown path'}) - left alone"

    def _write_pid(self, pid: int) -> None:
        try:
            self._pid_file.write_text(str(pid), encoding="ascii")
        except OSError:
            pass

    def _read_pid(self) -> int:
        try:
            return int(self._pid_file.read_text(encoding="ascii").strip())
        except Exception:  # noqa: BLE001
            return 0

    def start(self, wait: bool = True, timeout: float = 240.0) -> dict:
        with self._lock:
            if self.is_alive():
                return {"started": False, "reason": "already running", "adopt": self.adopt_or_kill_stale()}
            if self.root is None:
                raise ComfyError(
                    "ComfyUI-Easy-Install not found. Expected python_embeded\\python.exe + "
                    "ComfyUI\\main.py under one of: " + ", ".join(str(r) for r in self._roots())
                )
            args = [
                "-I", "-W", "ignore::FutureWarning",
                str(self.root / "ComfyUI" / "main.py"),
                "--windows-standalone-build",
                "--port", str(self.port),
                "--disable-auto-launch",
            ]
            # VRAM mode. ComfyUI's own default is NORMAL_VRAM; `lowvram` streams weights
            # per node, which on a 5.4 GB Trellis2 graph against an 8 GB card is the
            # difference between "staged dynamically" and "resident". Keep it explicit so
            # `THREE_COMFY_VRAM_MODE` can actually reach every state.
            vram_flag = {"lowvram": "--lowvram", "normalvram": "--normalvram",
                         "highvram": "--highvram", "novram": "--novram",
                         "cpu": "--cpu"}.get(self.vram_mode)
            if vram_flag:
                args.append(vram_flag)

            # Custom-node filter. `--whitelist-custom-nodes` is `nargs='+'`, so it has to
            # be the last flag on the line or it swallows whatever follows.
            #   None  -> load every pack (legacy behaviour, THREE_COMFY_CUSTOM_NODES=*)
            #   ()    -> load none
            #   (a,b) -> load only those
            if self.custom_nodes is None:
                pass
            elif self.custom_nodes:
                args += ["--disable-all-custom-nodes",
                         "--whitelist-custom-nodes", *self.custom_nodes]
            else:
                args.append("--disable-all-custom-nodes")

            self._log.parent.mkdir(parents=True, exist_ok=True)
            log = self._log.open("ab")
            log.write(f"\n=== start {time.strftime('%Y-%m-%d %H:%M:%S')} : {self.python} {' '.join(args)}\n".encode())
            log.flush()

            creation = 0
            if sys.platform == "win32":
                creation = subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
            self._proc = subprocess.Popen(
                [str(self.python), *args], cwd=str(self.root),
                stdout=log, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,
                creationflags=creation, close_fds=True,
            )
            self._write_pid(self._proc.pid)
            if wait:
                self._wait_alive(timeout)
            return {"started": True, "pid": self._proc.pid, "vram_mode": self.vram_mode,
                    "root": str(self.root), "log": str(self._log)}

    def _wait_alive(self, timeout: float = 240.0) -> None:
        t0 = time.time()
        while time.time() - t0 < timeout:
            if self.is_alive():
                return
            time.sleep(1.5)
        raise ComfyError(f"ComfyUI did not come up within {timeout:.0f}s - see {self._log}")

    def ensure(self, timeout: float = 240.0) -> dict:
        self.cancel_idle_stop()
        if self.is_alive():
            return {"started": False, "reason": "already running"}
        return self.start(wait=True, timeout=timeout)

    def stop(self, wait: float = 15.0) -> dict:
        self.cancel_idle_stop()
        pid = self._proc.pid if self._proc else self._read_pid()
        if not pid:
            return {"stopped": False, "reason": "no pid"}
        if sys.platform == "win32":
            subprocess.run(["taskkill", "/PID", str(pid), "/F", "/T"],
                           capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
        else:
            try:
                os.kill(pid, 9)
            except OSError:
                pass
        self._proc = None
        self._pid_file.unlink(missing_ok=True)
        t0 = time.time()
        while time.time() - t0 < wait:
            if not self.is_alive():
                break
            time.sleep(0.5)
        return {"stopped": True, "pid": pid, "port_free": not self.is_alive()}

    # ---------------------------------------------------------------- idle stop
    def schedule_idle_stop(self) -> None:
        self.cancel_idle_stop()
        if not (self.idle_stop_s > 0):
            return
        self._idle_timer = threading.Timer(self.idle_stop_s, self._idle_fire)
        self._idle_timer.daemon = True
        self._idle_timer.start()

    def _idle_fire(self) -> None:
        try:
            self.stop()
        except Exception:  # noqa: BLE001
            pass

    def cancel_idle_stop(self) -> None:
        if self._idle_timer is not None:
            self._idle_timer.cancel()
            self._idle_timer = None

    # ---------------------------------------------------------------- transfer
    def upload_image(self, data: bytes, filename: str) -> str:
        boundary = "----3gs" + uuid.uuid4().hex
        body = bytearray()
        for key, value in (("overwrite", "true"), ("type", "input")):
            body += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{key}\"\r\n\r\n"
                     f"{value}\r\n").encode()
        body += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"image\"; "
                 f"filename=\"{filename}\"\r\nContent-Type: application/octet-stream\r\n\r\n").encode()
        body += data + b"\r\n"
        body += f"--{boundary}--\r\n".encode()
        req = urllib.request.Request(
            self.base + "/upload/image", data=bytes(body),
            headers={"Content-Type": f"multipart/form-data; boundary={boundary}",
                     "User-Agent": "3gs-assets"},
            method="POST",
        )
        with self._opener.open(req, timeout=120) as r:
            j = json.loads(r.read().decode("utf-8", "replace"))
        return f"{j['subfolder']}/{j['name']}" if j.get("subfolder") else j["name"]

    def fetch_output(self, item: dict) -> bytes:
        q = urllib.parse.urlencode({
            "filename": item.get("filename", ""),
            "subfolder": item.get("subfolder", "") or "",
            "type": item.get("type", "output") or "output",
        })
        with self._opener.open(f"{self.base}/view?{q}", timeout=300) as r:
            return r.read()

    def interrupt(self) -> None:
        try:
            self._post("/interrupt", {}, timeout=10)
        except Exception:  # noqa: BLE001
            pass

    # ---------------------------------------------------------------- workflow
    @staticmethod
    def apply_params(prompt: dict, param_map: dict | None, params: dict | None) -> None:
        """`{"312.width": 1024}` -> node `312`, input `width`.

        Node keys may themselves contain dots (flattened subgraphs: `88.2`, `459.474`),
        so both the key and the target split on the *last* dot.
        """
        for key, value in (params or {}).items():
            if "." not in key:
                continue
            node, _, inp = key.rpartition(".")
            if node in prompt:
                prompt[node]["inputs"][inp] = value
        for pname, pval in (params or {}).items():
            if "." in pname:
                continue
            mapping = (param_map or {}).get(pname)
            if not mapping:
                continue
            for target, cast in mapping.items():
                node, _, inp = target.rpartition(".")
                if node not in prompt:
                    continue
                v = pval
                if cast == "num":
                    v = float(pval) if isinstance(pval, float) else int(pval)
                elif cast == "str":
                    v = str(pval)
                elif cast == "bool":
                    v = bool(pval)
                prompt[node]["inputs"][inp] = v

    @staticmethod
    def drop_nodes(prompt: dict, keys) -> dict:
        """Remove UI-only nodes (previews, compare widgets) and bridge the gap they leave.

        These graphs route real data *through* preview nodes. In `3d_trellis2.json`,
        `ApplyTextureToMesh.base_color` is fed by a `PreviewImage` and
        `Trellis2Conditioning.image` by another - the previews are not taps hanging off the
        side, they sit in the path, because that is what the UI export produced. Deleting a
        node and the reference to it leaves the consumer without a required input, and
        ComfyUI answers 400 naming a node nobody edited:

            "298": required_input_missing: image      (Pixal3DConditioning)
            "210": required_input_missing: base_color (ApplyTextureToMesh)

        So a dropped node with exactly one linked input is **bridged**: every reference to
        it is rewritten to that input, which is the thing the preview was passing through.
        A dropped node with zero or several linked inputs cannot be bridged unambiguously,
        and its references are removed as before.

        Returns a report - `{"dropped": [...], "bridged": {id: replacement}, "unlinked":
        [...]}` - because a silent rewrite of the graph is exactly the kind of change that
        should be visible to the caller when the output looks wrong.
        """
        keys = [str(k) for k in (keys or [])]
        present = [k for k in keys if k in prompt]

        bridge: dict[str, list] = {}
        for k in present:
            links = [v for v in prompt[k].get("inputs", {}).values()
                     if isinstance(v, list) and len(v) == 2 and str(v[0]) in prompt]
            if len(links) == 1:
                bridge[k] = list(links[0])

        def resolve(ref: list) -> list:
            """Follow a chain of bridged nodes to the first node that survives."""
            seen: set[str] = set()
            while (isinstance(ref, list) and len(ref) == 2
                   and str(ref[0]) in bridge and str(ref[0]) not in seen):
                seen.add(str(ref[0]))
                ref = bridge[str(ref[0])]
            return ref

        for k in present:
            prompt.pop(k, None)

        unlinked: list[str] = []
        for node in prompt.values():
            for name in list(node.get("inputs", {})):
                v = node["inputs"][name]
                if not (isinstance(v, list) and len(v) == 2):
                    continue
                if str(v[0]) in bridge:
                    node["inputs"][name] = resolve(v)
                elif str(v[0]) in present:
                    unlinked.append(f"{v[0]}.{name}")
                    del node["inputs"][name]

        return {"dropped": present, "bridged": bridge, "unlinked": unlinked}

    def run(
        self,
        workflow: dict,
        *,
        image_paths: list[Path] | None = None,
        image_nodes: list[str] | None = None,
        prompt: str | None = None,
        prompt_node: str | None = None,
        prompt_input: str = "prompt",
        params: dict | None = None,
        param_map: dict | None = None,
        drop: list[str] | None = None,
        outputs: list[dict] | None = None,
        timeout_s: float = 900.0,
        poll_s: float = 1.2,
    ) -> list[dict]:
        self.ensure()
        graph = json.loads(json.dumps(workflow))  # deep copy, the caller may reuse it

        for i, path in enumerate(image_paths or []):
            if not image_nodes or i >= len(image_nodes):
                raise ComfyError("workflow does not accept that many input images")
            data = Path(path).read_bytes()
            name = self.upload_image(data, f"3gs_in_{i}{Path(path).suffix or '.png'}")
            if image_nodes[i] not in graph:
                raise ComfyError(f"workflow has no LoadImage node {image_nodes[i]}")
            graph[image_nodes[i]]["inputs"]["image"] = name

        if prompt and prompt_node:
            if prompt_node not in graph:
                raise ComfyError(f"workflow has no prompt node {prompt_node}")
            graph[prompt_node]["inputs"][prompt_input] = str(prompt)

        self.apply_params(graph, param_map, params)
        self.drop_report = self.drop_nodes(graph, drop)

        res = self._post("/prompt", {"prompt": graph}, timeout=180)
        prompt_id = res.get("prompt_id")
        if not prompt_id:
            raise ComfyError("ComfyUI returned no prompt_id: " + json.dumps(res)[:400])

        t0 = time.time()
        while True:
            if time.time() - t0 > timeout_s:
                self.interrupt()
                raise ComfyError(f"workflow timed out after {timeout_s:.0f}s (prompt {prompt_id})")
            time.sleep(poll_s)
            try:
                hist = self._get(f"/history/{prompt_id}", timeout=30)
            except Exception:  # noqa: BLE001
                continue
            entry = hist.get(prompt_id)
            if not entry:
                continue
            status = entry.get("status") or {}
            if status.get("status_str") == "error" or status.get("completed") is False:
                msgs = [m for m in status.get("messages", []) if m and m[0] == "execution_error"]
                detail = json.dumps(msgs[0][1])[:700] if msgs else "execution error"
                raise ComfyError("ComfyUI: " + detail)

            collected: list[dict] = []
            for spec in (outputs or []):
                node_out = (entry.get("outputs") or {}).get(str(spec["node"]))
                if not node_out:
                    continue
                for value in node_out.values():
                    for item in (value if isinstance(value, list) else [value]):
                        if not isinstance(item, dict) or not item.get("filename"):
                            continue
                        blob = self.fetch_output(item)
                        collected.append({
                            "filename": item["filename"],
                            "kind": spec.get("type", "file"),
                            "bytes": blob,
                        })
            if not collected:
                raise ComfyError(
                    "ComfyUI finished but produced no outputs. The usual cause is a missing "
                    "model file - ComfyUI validates every node before running. See "
                    f"{self._log}."
                )
            return collected

    def status(self) -> dict:
        alive = self.is_alive()
        info: dict = {"alive": alive, "base": self.base, "vram_mode": self.vram_mode,
                      "root": str(self.root) if self.root else None,
                      "custom_nodes": (list(self.custom_nodes)
                                       if self.custom_nodes is not None else "all"),
                      "idle_stop_s": self.idle_stop_s, "pid_file": str(self._pid_file)}
        if alive:
            try:
                stats = self._get("/system_stats", timeout=6)
                dev = (stats.get("devices") or [{}])[0]
                info["device"] = dev.get("name")
                info["vram_total_mb"] = round((dev.get("vram_total") or 0) / 1048576)
                info["vram_free_mb"] = round((dev.get("vram_free") or 0) / 1048576)
                info["queue_remaining"] = (stats.get("queue") or {}).get("remaining") if isinstance(stats.get("queue"), dict) else None
            except Exception as e:  # noqa: BLE001
                info["stats_error"] = str(e)
        return info


def workflows_dir() -> Path:
    return config.ASSETS_DIR / "workflows"


def load_manifest() -> dict:
    path = workflows_dir() / "manifest.json"
    if not path.exists():
        return {"workflows": []}
    return json.loads(path.read_text(encoding="utf-8"))


def workflow_def(workflow_id: str) -> dict | None:
    return next((w for w in load_manifest().get("workflows", []) if w.get("id") == workflow_id), None)


def load_workflow(workflow_id: str) -> dict:
    definition = workflow_def(workflow_id)
    if not definition:
        known = ", ".join(w.get("id", "?") for w in load_manifest().get("workflows", []))
        raise ComfyError(f"unknown workflow '{workflow_id}'. Known: {known}")
    path = workflows_dir() / definition["file"]
    if not path.exists():
        raise ComfyError(f"workflow file missing: {path}")
    return json.loads(path.read_text(encoding="utf-8"))
