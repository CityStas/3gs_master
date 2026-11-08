#!/usr/bin/env python
"""Registry of local GGUF models for the llama.cpp router on :8080.

Why this exists. Until now `cmd\\serve-llm.cmd` loaded exactly one file
(`models\\Qwen_Qwen3.5-9B-Q4_K_M.gguf`) and pi's `models.json` declared exactly one
model. Trying another GGUF meant editing a .cmd, killing the server and restarting it -
and pi's model list stayed a single entry, so `/model` had nothing to switch to.

llama.cpp build b11435 ships **router mode**: one `llama-server` process that reads an
INI registry, advertises every entry on `/v1/models`, loads a model the first time a
request names it, and evicts the least-recently-used one when `--models-max` is reached.
That is a better fit than N servers on N ports: the card is 8 GB, so exactly one model
can be resident anyway, and pi keeps talking to a single `baseUrl`.

This tool owns the two generated artefacts and nothing else:

    models/llm-preset.ini      the router registry (section = model id)
    models/llm-registry.json   the same facts for the doctor / bench / humans
    pi-home*/models.json       provider `3gs` rewritten with every model id

Per-model context is COMPUTED, not guessed: a dense 9B with full attention would need
~73 KiB/token and blow the 8 GB card at 32K, while the Qwen3.5 hybrid stack charges KV
for 8 of 33 blocks only (17 KiB/token, measured in `cmd\\serve-llm.cmd`). `gguf_meta`
reads the block count, the attention interval and the KV head geometry straight out of
the file, so a newly dropped GGUF gets a context that actually fits.

Hand-tuning goes in `models/llm-overrides.json`, never in the generated .ini - the .ini
is overwritten on every launch.

    python tools/llm_models.py                  # rescan, rewrite ini + registry + pi
    python tools/llm_models.py --list           # what is registered, with the math
    python tools/llm_models.py --dry-run        # print the ini, write nothing
    python tools/llm_models.py --only omnicoder # restrict to matching ids
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.gguf_meta import describe  # noqa: E402

MODELS_DIR = ROOT / "models"
PRESET = MODELS_DIR / "llm-preset.ini"
REGISTRY = MODELS_DIR / "llm-registry.json"
OVERRIDES = MODELS_DIR / "llm-overrides.json"

# Every pi profile that talks to :8080. `pi-home` is the untouched default profile;
# the four engine profiles are what `agent.cmd` actually points PI_CODING_AGENT_DIR at.
# A bare `pi` typed in cmd has no PI_CODING_AGENT_DIR and reads ~/.pi/agent/models.json,
# but that profile talks to the user's always-on Ollama (:1234) instead - the router on
# :8080 is only up while serve-all.cmd runs, so advertising `3gs` there produced dead
# entries in `/model`. Only the `ollama` provider of that file is synced (sync_ollama_pi).
PI_PROFILES = ("pi-home", "pi-home-three", "pi-home-godot", "pi-home-unity",
               "pi-home-roblox")

# The model the rest of the system already assumes: settings.json:defaultModel and the
# `--alias` in older launchers. It has to keep this exact id or every session starts
# against a model the router does not advertise.
DEFAULT_ID = "qwen3.5-9b"

# Default model for the pi profiles. `DEFAULT_ID` above is the router's alias, but
# Ollama has no `qwen3.5-9b` manifest - a profile default pointing at it would fail
# on the first request. This id exists in both the registry and Ollama.
DEFAULT_PI_MODEL = "qwen3.5-9b-distill-deepseek-v4.1-flash"

# --- what is NOT a chat model ---------------------------------------------------
# The embedder (:8081), the reranker (:8083) and the vision tower (:8082) are separate
# servers on separate ports. If they leaked into the router they would appear in pi's
# model picker and answer chat requests with garbage.
SKIP_SUBSTRINGS = (
    "mmproj", "bge-", "bge_", "rerank", "embed", "-vlm", "clip-", "siglip",
)
# Directories that hold models for OTHER servers, not chat models:
#   models/vlm            - Qwen2.5-VL on :8082 (`cmd\vlm.cmd`)
#   models/image          - z-image-turbo and its Qwen3-4B text encoder
#   models/text_image_3D  - the ComfyUI stack
# A chat request routed to any of them returns noise, so they never enter the registry.
SKIP_DIR_PARTS = {"vlm", "vision", "text_image_3D", "image", "clip", "mmproj"}
MIN_SIZE = 64 * 1024 * 1024  # anything smaller is not a usable LLM

QUANT_RE = re.compile(r"[-_.](?:i?q\d+(?:_[a-z0-9]+)*|f16|bf16|fp16|fp32|q8_0)$", re.I)
QUANT_LABEL_RE = re.compile(r"(i?q\d+(?:_[a-z0-9]+)*|f16|bf16|fp16)", re.I)


def _roots() -> list[Path]:
    """Where to look for .gguf files, in order.

    `GS_LLM_MODELS_DIR` is a `;`-separated list so a second drive can be added without
    touching code. The default is this machine's `E:\\Programs\\LocalLLM\\Models`,
    which is where the alternative 9B builds live.
    """
    out = [MODELS_DIR]
    raw = os.environ.get("GS_LLM_MODELS_DIR", r"E:\Programs\LocalLLM\Models")
    for part in raw.split(";"):
        part = part.strip().strip('"')
        if part:
            out.append(Path(part))
    return out


def _skip(path: Path) -> str:
    name = path.name.lower()
    for bad in SKIP_SUBSTRINGS:
        if bad in name:
            return f"not a chat model ({bad})"
    # Only the path *below* the search root is inspected: a root that itself lives in a
    # folder called `image` must not be skipped wholesale.
    for part in path.parts[:-1]:
        if part.lower() in SKIP_DIR_PARTS:
            return f"belongs to another server ({part}/)"
    try:
        if path.stat().st_size < MIN_SIZE:
            return "smaller than 64 MB"
    except OSError as e:
        return f"unreadable: {e}"
    return ""


def slugify(stem: str) -> str:
    """`Ornith-1.5-9B-CRACK-Q4_K_M` -> `ornith-1.5-9b-crack`."""
    s = stem
    while True:
        new = QUANT_RE.sub("", s)
        if new == s:
            break
        s = new
    s = re.sub(r"(?<=\d)_(?=\d)", ".", s)  # qwen2-0_5b -> qwen2-0.5b
    s = re.sub(r"[^0-9A-Za-z.]+", "-", s).strip("-")
    return re.sub(r"-{2,}", "-", s).lower()


def quant_label(path: Path) -> str:
    hits = QUANT_LABEL_RE.findall(path.stem)
    return hits[-1].upper() if hits else "GGUF"


def _overrides() -> dict:
    if not OVERRIDES.is_file():
        return {}
    try:
        return json.loads(OVERRIDES.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] {OVERRIDES.name} is unreadable ({e}) - using defaults", file=sys.stderr)
        return {}


def ctx_for(meta: dict, budget_mb: int, cap: int) -> tuple[int, str]:
    """Largest context that fits `budget_mb` of VRAM, in whole 1024-token steps.

    KV bytes per token = 2 (K and V) * kv_heads * key_len * full_attention_layers, and
    q8_0 stores roughly one byte per element (+6 % for block scales). SSM blocks in a
    hybrid stack contribute a constant, not a per-token cost, so they are excluded.
    """
    file_mb = meta["size"] / (1024 * 1024)
    kv_bpt = 2 * meta["kv_heads"] * meta["key_len"] * meta["full_layers"] * 1.06
    avail_mb = budget_mb - file_mb
    if kv_bpt <= 0:
        return min(cap, meta["ctx_train"] or cap), "no KV geometry in the GGUF - capped"
    if avail_mb <= 0:
        return 8192, f"weights alone need {file_mb:.0f} MB of {budget_mb} - floor 8K"
    fits = int(avail_mb * 1024 * 1024 / kv_bpt)
    train = meta["ctx_train"] or cap
    ctx = min(cap, train, fits)
    ctx = (ctx // 1024) * 1024
    ctx = max(ctx, 8192)
    note = (f"{file_mb:.0f} MB weights, {kv_bpt / 1024:.1f} KiB/token, "
            f"fits {fits // 1024}K")
    if ctx < min(cap, train):
        note += f" -> clamped to {ctx // 1024}K"
    return ctx, note


def scan(budget_mb: int, cap: int, only: str = "") -> list[dict]:
    ov = _overrides()
    ov_models: dict = ov.get("models", {}) or {}
    by_id = {k: v for k, v in ov_models.items() if isinstance(v, dict)}

    seen_paths: dict[Path, dict] = {}
    for root in _roots():
        if not root.is_dir():
            continue
        for path in sorted(root.rglob("*.gguf")):
            try:
                rp = path.resolve()
            except OSError:
                continue
            if rp in seen_paths:
                continue
            reason = _skip(path)
            if reason:
                continue
            if only and only.lower() not in str(rp).lower():
                continue
            try:
                meta = describe(path)
            except Exception as e:  # noqa: BLE001
                print(f"[WARN] skip {path.name}: {e}", file=sys.stderr)
                continue
            if not meta["has_chat_template"]:
                print(f"[WARN] skip {path.name}: no chat template (--jinja would fail)",
                      file=sys.stderr)
                continue
            seen_paths[rp] = {"path": rp, "meta": meta}

    # id assignment: an override key wins when its `match` substring hits the path.
    # Identical files are collapsed by BYTE SIZE: the same GGUF is copied in several
    # places (`models\llm\mini` and `E:\...\Models\mini` are literally the same model),
    # and listing it twice would put two indistinguishable entries in pi's picker. Two
    # genuinely different GGUFs never agree to the byte, so this is safe.
    ids: dict[str, Path] = {}
    assigned: dict[Path, str] = {}
    seen_sizes: dict[int, Path] = {}
    for mid, spec in by_id.items():
        match = str(spec.get("match", "") or "")
        if not match:
            continue
        for rp in seen_paths:
            if match.lower() in str(rp).lower() and rp not in assigned:
                assigned[rp] = mid
                break
    for rp in list(seen_paths):
        if rp in assigned:
            continue
        size = seen_paths[rp]["meta"]["size"]
        if size in seen_sizes:
            del seen_paths[rp]
            continue
        seen_sizes[size] = rp
        base = slugify(rp.stem) or "model"
        mid, n = base, 2
        while mid in assigned.values():
            mid = f"{base}-{n}"
            n += 1
        assigned[rp] = mid

    out: list[dict] = []
    for rp, mid in assigned.items():
        meta = seen_paths[rp]["meta"]
        spec = by_id.get(mid, {})
        ctx, note = ctx_for(meta, budget_mb, cap)
        if "ctx" in spec:
            ctx = int(spec["ctx"])
            note += f"; pinned {ctx // 1024}K by overrides"
        out.append({
            "id": mid,
            # Forward slashes: the INI value is a raw string, and a Windows path full of
            # backslashes is one parser change away from being read as escapes.
            "path": str(rp).replace("\\", "/"),
            "ctx": ctx,
            "quant": quant_label(rp),
            "size_mb": round(meta["size"] / (1024 * 1024)),
            "arch": meta["arch"],
            "blocks": meta["blocks"],
            "full_layers": meta["full_layers"],
            "note": note,
            "temp": float(spec.get("temp", 0.6)),
            "top_p": float(spec.get("top_p", 0.95)),
            "top_k": int(spec.get("top_k", 20)),
            "max_tokens": int(spec.get("max_tokens", 0)),
        })

    # The default model first: pi's picker and every log line then start with it.
    out.sort(key=lambda m: (m["id"] != DEFAULT_ID, m["id"]))
    if not any(m["id"] == DEFAULT_ID for m in out) and out:
        print(f"[WARN] no model matched id {DEFAULT_ID!r} - pi settings.json:defaultModel "
              f"points at it. Fix `match` in {OVERRIDES.name}.", file=sys.stderr)
    return out


def render_ini(models: list[dict], cap: int) -> str:
    lines = [
        "; GENERATED by tools/llm_models.py - do not edit.",
        "; Per-model tweaks go in models/llm-overrides.json; this file is rewritten on",
        "; every `serve-llm.cmd` / `serve-all.cmd` launch.",
        ";",
        "; Keys are llama-server flag names without the leading dashes; an unknown key",
        "; makes the router reject the WHOLE preset, so nothing exotic is emitted here.",
        "",
        "[*]",
        f"ctx-size = {cap}",
        "ngl = 999",
        "fa = on",
        "ctk = q8_0",
        "ctv = q8_0",
        "rea = off",
        "",
    ]
    for m in models:
        lines += [
            f"[{m['id']}]",
            f"; {m['arch']}, {m['blocks']} blocks ({m['full_layers']} attention), "
            f"{m['size_mb']} MB {m['quant']}",
            f"; {m['note']}",
            f"model = {m['path']}",
            f"ctx-size = {m['ctx']}",
            f"temp = {m['temp']}",
            f"top-p = {m['top_p']}",
            f"top-k = {m['top_k']}",
            "",
        ]
    return "\n".join(lines)


def render_registry(models: list[dict]) -> str:
    return json.dumps({"default": DEFAULT_ID, "models": models}, ensure_ascii=False, indent=2) + "\n"


def _ollama_ids() -> set[str] | None:
    """Model names Ollama can actually serve, read from its manifests directory.

    The router registry also knows `qwen3.5-9b`, which has no Ollama manifest: listing
    it under the ollama provider would put a dead entry in `/model`. None means the
    manifests are not reachable - in that case the provider is left untouched.
    """
    root = Path(os.environ.get("OLLAMA_MODELS", ""))
    manifests = root / "manifests"
    if not manifests.is_dir():
        return None
    return {p.parent.name for p in manifests.rglob("latest")}


def _ollama_entries(models: list[dict], old: list[dict], names: set[str]) -> list[dict]:
    """Provider model list: keep working entries, append new ids from the registry.

    Existing entries are kept verbatim - their context/maxTokens were tuned by hand,
    and `ornith-1.5-9b` is served by Ollama but no longer scanned as a GGUF. New ids
    are cloned from the first entry so they inherit the same cost/compat shape.
    """
    entries = [e for e in old if e.get("id") in names]
    known = {e.get("id") for e in entries}
    template = old[0] if old else {}
    for m in models:
        if m["id"] not in names or m["id"] in known:
            continue
        e = json.loads(json.dumps(template))
        e["id"] = m["id"]
        e["name"] = f"{m['id']} ({m['quant']}, {m['ctx'] // 1024}K)"
        entries.append(e)
        known.add(m["id"])
    # Ollama can serve ids the GGUF scan no longer sees (`ornith-1.5-9b` was
    # dropped from the registry when its duplicate was collapsed). Keep them in the
    # picker: a model the server answers for is not a dead entry. `_`/`.` variants
    # (`qwen2-0_5b-instruct`) are the same file - do not list it twice.
    for mid in sorted(names - known):
        if mid.replace("_", ".") in known:
            continue
        e = json.loads(json.dumps(template))
        e["id"] = mid
        e["name"] = mid
        entries.append(e)
        known.add(mid)
    return entries


def _router_entries(models: list[dict], old: list[dict]) -> list[dict]:
    """Provider `3gs` (:8080): every registry id, with the router's sampling params."""
    template = old[0] if old else {}
    out = []
    for m in models:
        e = json.loads(json.dumps(template))
        e["id"] = m["id"]
        e["name"] = f"{m['id']} ({m['quant']}, {m['ctx'] // 1024}K)"
        e["contextWindow"] = m["ctx"]
        e["maxTokens"] = m["max_tokens"] or min(8192, max(1024, m["ctx"] // 4))
        sp = e.setdefault("samplingParams", {})
        sp.update({"temperature": m["temp"], "top_p": m["top_p"], "top_k": m["top_k"]})
        out.append(e)
    return out


def sync_pi(models: list[dict]) -> list[str]:
    """Point every pi profile at the always-on Ollama (:1234), not the router.

    `pi-home*` (and the `~/.pi/agent` profile a bare `pi` reads) used to advertise
    provider `3gs` -> :8080. That port only listens while `serve-all.cmd` runs, and
    the user's always-on server is `E:\\Programs\\LocalLLM\\ollama\\start-ollama.cmd`
    on :1234 - so `/model` was full of entries that answered Connection error.
    Provider `3gs` is renamed to `ollama`, its baseUrl moved to :1234, and the list
    filtered by Ollama's manifests. `settings.json` default is moved with it.
    """
    names = _ollama_ids()
    if names is None:
        print(f"[WARN] Ollama manifests not found under "
              f"{os.environ.get('OLLAMA_MODELS', '')!r} - pi profiles left as-is",
              file=sys.stderr)
        return []
    files = [ROOT / prof / "models.json" for prof in PI_PROFILES]
    files.append(Path.home() / ".pi" / "agent" / "models.json")
    touched = []
    for f in files:
        if not f.is_file():
            continue
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            print(f"[WARN] {f} unreadable: {e}", file=sys.stderr)
            continue
        provs = data.setdefault("providers", {})
        prov = provs.get("ollama") or provs.pop("3gs", None)
        if prov is None:
            continue
        provs["ollama"] = prov
        old = prov.get("models") or []
        if not old:
            continue
        entries = _ollama_entries(models, old, names)
        if not entries:
            continue
        prov["models"] = entries
        prov["name"] = "Ollama (:1234)"
        prov["baseUrl"] = "http://127.0.0.1:1234/v1"
        prov["api"] = "openai-completions"
        prov["apiKey"] = "ollama"

        # Second provider: the 3GS router on :8080 (`serve-all.cmd`). Both are listed
        # because both are legitimate: Ollama is the always-on server, the router adds
        # RAG (:8081/:8083) and 64K sampling-tuned models. pi-here.cmd / agent.cmd pick
        # the one whose port answers, so `/model` is never the thing that decides.
        router = provs.get("3gs") or {"api": "openai-completions"}
        router["name"] = "3GS router (llama.cpp :8080)"
        router["baseUrl"] = "http://127.0.0.1:8080/v1"
        router["api"] = "openai-completions"
        router["apiKey"] = "llama.cpp"
        router["models"] = _router_entries(models, router.get("models") or [])
        provs["3gs"] = router
        text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
        if f.read_text(encoding="utf-8") != text:
            f.write_text(text, encoding="utf-8")
            try:
                label = str(f.relative_to(ROOT))
            except ValueError:
                label = str(f)
            touched.append(label)

        # settings.json: a default pointing at the removed `qwen3.5-9b` / `3gs`
        # would start every session against a model the server does not have.
        sf = f.parent / "settings.json"
        if sf.is_file():
            try:
                st = json.loads(sf.read_text(encoding="utf-8"))
            except Exception:  # noqa: BLE001
                continue
            ids = [e["id"] for e in entries]
            if st.get("defaultProvider") in ("3gs", "ollama") and (
                    st.get("defaultProvider") != "ollama"
                    or st.get("defaultModel") != DEFAULT_PI_MODEL
                    or st.get("defaultModel") not in ids):
                st["defaultProvider"] = "ollama"
                st["defaultModel"] = (DEFAULT_PI_MODEL if DEFAULT_PI_MODEL in ids
                                      else ids[0])
                sf.write_text(json.dumps(st, ensure_ascii=False, indent=2) + "\n",
                              encoding="utf-8")
                touched.append(str(sf))
    return touched


def live(port: int) -> int:
    """What the running router says: every id it knows and which ones are resident."""
    import urllib.request

    url = f"http://127.0.0.1:{port}/v1/models"
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(url, timeout=3) as r:
            data = json.loads(r.read().decode("utf-8", "replace"))
    except Exception as e:  # noqa: BLE001
        print(f"router :{port} is not answering ({type(e).__name__}) - "
              f"start it with `serve-all.cmd` or `gs llm`")
        return 1
    rows = data.get("data") or []
    loaded = 0
    for m in rows:
        st = (m.get("status") or {}).get("value", "?")
        loaded += st == "loaded"
        mark = "loaded " if st == "loaded" else "       "
        print(f"  {mark} {m.get('id', '?')}")
    print(f"\n{len(rows)} registered, {loaded} resident on :{port}")
    if not loaded:
        print("(router mode: a model is loaded on the first request that names it)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Register local GGUF models with the router.")
    ap.add_argument("--list", action="store_true", help="print the registry, write nothing")
    ap.add_argument("--live", action="store_true", help="ask the running router what it has")
    ap.add_argument("--dry-run", action="store_true", help="print the generated INI")
    ap.add_argument("--quiet", action="store_true", help="only errors")
    ap.add_argument("--only", default="", help="substring filter on the model path")
    ap.add_argument("--port", type=int,
                    default=int(os.environ.get("THREE_LLM_PORT", "8080")),
                    help="router port for --live (default 8080)")
    ap.add_argument("--vram-mb", type=int,
                    default=int(os.environ.get("GS_LLM_VRAM_MB", "7000")),
                    help="VRAM budget for weights+KV (default 7000 of 8192)")
    ap.add_argument("--ctx-cap", type=int,
                    default=int(os.environ.get("GS_LLM_CTX", "65536")),
                    help="hard ceiling for any model's context (default 65536)")
    a = ap.parse_args()

    if a.live:
        return live(a.port)

    models = scan(a.vram_mb, a.ctx_cap, a.only)
    if not models:
        print("[ERROR] no usable .gguf found. Looked in: "
              + ", ".join(str(p) for p in _roots()), file=sys.stderr)
        return 1

    if a.list:
        print(f"VRAM budget {a.vram_mb} MB, ctx cap {a.ctx_cap}")
        for m in models:
            star = "*" if m["id"] == DEFAULT_ID else " "
            print(f" {star} {m['id']:<28} {m['ctx'] // 1024:>3}K  {m['size_mb']:>5} MB  "
                  f"{m['quant']:<7} {m['path']}")
        print(f"\n{len(models)} model(s); * = pi default")
        return 0

    ini = render_ini(models, a.ctx_cap)
    if a.dry_run:
        print(ini)
        return 0

    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    if not PRESET.is_file() or PRESET.read_text(encoding="utf-8") != ini:
        PRESET.write_text(ini, encoding="utf-8")
        if not a.quiet:
            print(f"preset  : {PRESET.relative_to(ROOT)} ({len(models)} models)")
    reg = render_registry(models)
    if not REGISTRY.is_file() or REGISTRY.read_text(encoding="utf-8") != reg:
        REGISTRY.write_text(reg, encoding="utf-8")
        if not a.quiet:
            print(f"registry: {REGISTRY.relative_to(ROOT)}")
    touched = sync_pi(models)
    if touched and not a.quiet:
        print("pi      : " + ", ".join(touched))
    if not a.quiet:
        print(f"models  : {len(models)} -> " + ", ".join(m["id"] for m in models))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
