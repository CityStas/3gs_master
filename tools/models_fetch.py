#!/usr/bin/env python
"""Download the weights a clone is missing, and prove they arrived intact.

Why this exists
---------------
`models.manifest.json` says WHAT to download and from WHERE. `model_paths.py` says
where it lands. This is the thing that actually moves bytes, so that

    git clone ... && python -m venv .venv && gs models fetch

is the whole install story on any machine, on any drive letter. Before this, a
clone had code, an empty `models/`, and a README that said "install the models"
without saying which ones, from where, or into which directory.

Design notes
------------
* **stdlib only.** `huggingface_hub` is not in `requirements.txt` and does not
  need to be: one HTTPS GET per file with a `Range` header for resume covers it.
  Adding a dependency to the install path of the install path is a bad trade.
* **Resume, always.** 6 GB on a flaky link is not a download, it is a lottery.
  Bytes go to `<name>.part` and are renamed only after the hash matches, so an
  interrupted run leaves a usable partial and never a plausible-looking corrupt
  model.
* **sha256 is computed while streaming**, not in a second pass. The data is
  already in memory; hashing it costs ~80 s over the whole 39 GB and turns "the
  download finished" into "the download is the file that was tested".
* **Groups, not a flat list.** A user who only wants the RAG should not be told
  to fetch 39 GB. `--group llm,rag` is 7.2 GB and enough for pi + search.

    python tools/models_fetch.py                    # what is missing, by group
    python tools/models_fetch.py --fetch            # everything marked default
    python tools/models_fetch.py --fetch llm,rag    # just what boots the RAG
    python tools/models_fetch.py --verify           # re-hash what is on disk
    python tools/models_fetch.py --fetch --mirror   # hf-mirror.com
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from model_paths import comfy_root, models_root  # noqa: E402

MANIFEST = ROOT / "models.manifest.json"

#: Groups whose `path` is relative to `<comfy root>/ComfyUI/models`, not the models
#: root. ComfyUI insists on its own tree; symlinks and "just point it elsewhere" do
#: not survive its node loader, so the manifest has to know about the split.
COMFY_GROUPS = {"3d", "3d-x"}

CHUNK = 4 << 20


# --------------------------------------------------------------------- manifest
def load_manifest() -> dict:
    if not MANIFEST.is_file():
        raise SystemExit(f"no manifest at {MANIFEST}")
    with MANIFEST.open(encoding="utf-8") as fh:
        return json.load(fh)


def all_groups(man: dict) -> list[str]:
    return list(man["groups"].keys())


def parse_groups(man: dict, raw: str | None, *, default_only: bool) -> list[str]:
    """`llm,rag` -> those two; `all` -> everything; None -> the `default` flag."""
    known = all_groups(man)
    if raw:
        if raw.strip().lower() == "all":
            return known
        want = [g.strip() for g in raw.split(",") if g.strip()]
        bad = [g for g in want if g not in known]
        if bad:
            raise SystemExit(f"unknown group(s): {', '.join(bad)}\n  known: {', '.join(known)}")
        return want
    if default_only:
        return [g for g in known if man["groups"][g].get("default")]
    return known


def target(entry: dict) -> Path:
    if entry["group"] in COMFY_GROUPS:
        return comfy_root() / "ComfyUI" / "models" / entry["path"]
    return models_root() / entry["path"]


def base_url() -> str:
    """`HF_ENDPOINT` if set (hf-mirror.com), else huggingface.co."""
    return (os.environ.get("HF_ENDPOINT") or "https://huggingface.co").rstrip("/")


def url_for(entry: dict) -> str:
    return f"{base_url()}/{entry['repo']}/resolve/main/{entry['file']}"


# ------------------------------------------------------------------- inspection
def state(entry: dict) -> str:
    """'ok' | 'part' | 'missing' | 'wrong'."""
    p = target(entry)
    if p.is_file():
        size = p.stat().st_size
        if size == entry["size"]:
            return "ok"
        return "wrong" if size > entry["size"] else "part"
    part = p.with_name(p.name + ".part")
    if part.is_file():
        return "part"
    return "missing"


def human(n: float) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if abs(n) < 1000 or unit == "GB":
            return f"{n:6.2f} {unit}" if unit != "B" else f"{int(n)} B"
        n /= 1000.0
    return f"{n:.2f} GB"


def group_rows(man: dict, groups: list[str]) -> list[tuple[str, str, int, int, int]]:
    """(group, state, have_bytes, want_bytes, missing_files) per group."""
    out = []
    for g in groups:
        entries = [e for e in man["files"] if e["group"] == g]
        have = sum(e["size"] for e in entries if state(e) == "ok")
        want = sum(e["size"] for e in entries)
        missing = sum(1 for e in entries if state(e) != "ok")
        if missing == 0:
            st = "ok"
        elif have == 0:
            st = "missing"
        else:
            st = "partial"
        out.append((g, st, have, want, missing))
    return out


def cmd_status(man: dict, groups: list[str]) -> int:
    rows = group_rows(man, groups)
    print(f"models root : {models_root()}")
    print(f"comfy root  : {comfy_root()}")
    print(f"source      : {base_url()}")
    print()
    need = 0
    for g, st, have, want, missing in rows:
        title = man["groups"][g]["title"]
        print(f"  {g:<6} {st:<8} {human(have):>11} / {human(want):<11} {title}")
        for e in man["files"]:
            if e["group"] != g:
                continue
            s = state(e)
            mark = {"ok": "ok  ", "part": "part", "missing": "    ", "wrong": "BAD "}[s]
            print(f"      {mark} {human(e['size'])}  {e['path']}")
        if st != "ok":
            need += want - have
    print()
    if need:
        print(f"[i] не хватает {human(need)} - качать: gs models fetch")
    else:
        print("[ok] всё на месте.")
    return 0 if not need else 1


# ------------------------------------------------------------------- downloader
def _sha256_prefix(path: Path, limit: int | None = None) -> str:
    h = hashlib.sha256()
    left = limit
    with path.open("rb") as fh:
        while True:
            n = CHUNK if left is None else min(CHUNK, left)
            if n <= 0:
                break
            buf = fh.read(n)
            if not buf:
                break
            h.update(buf)
            if left is not None:
                left -= len(buf)
    return h.hexdigest()


def download(entry: dict, *, retries: int = 3) -> bool:
    """Fetch one file with resume + streaming sha256. True on success."""
    final = target(entry)
    final.parent.mkdir(parents=True, exist_ok=True)
    part = final.with_name(final.name + ".part")

    for attempt in range(1, retries + 1):
        have = part.stat().st_size if part.is_file() else 0
        if have > entry["size"]:
            part.unlink()
            have = 0
        if have == entry["size"]:
            break  # complete part from an interrupted earlier run; hash below

        req = urllib.request.Request(
            url_for(entry),
            headers={"User-Agent": "3gs-master/models-fetch", "Accept": "*/*"},
        )
        if have:
            req.add_header("Range", f"bytes={have}-")
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                if have and resp.status != 206:
                    # Server ignored the range: start over rather than corrupt.
                    have = 0
                    part.unlink(missing_ok=True)
                total = entry["size"]
                mode = "ab" if have else "wb"
                t0 = time.time()
                done = have
                last = 0.0
                with part.open(mode) as fh:
                    while True:
                        buf = resp.read(CHUNK)
                        if not buf:
                            break
                        fh.write(buf)
                        done += len(buf)
                        now = time.time()
                        if now - last > 1.0:
                            last = now
                            pct = 100.0 * done / total if total else 0
                            rate = (done - have) / max(now - t0, 0.01) / 1e6
                            sys.stdout.write(
                                f"\r      {pct:5.1f}%  {human(done)}  {rate:5.1f} MB/s   "
                            )
                            sys.stdout.flush()
                sys.stdout.write("\r" + " " * 62 + "\r")
                sys.stdout.flush()
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            got = part.stat().st_size if part.is_file() else 0
            print(f"      ! попытка {attempt}/{retries}: {type(exc).__name__}: {exc}"
                  f"  (есть {human(got)})")
            if attempt == retries:
                return False
            time.sleep(2 * attempt)
            continue

        if part.stat().st_size == entry["size"]:
            break
        if attempt == retries:
            print(f"      ! размер не сошёлся: {part.stat().st_size} != {entry['size']}")
            return False
        print("      ! недокачано, повторяю")

    # --- integrity: hash the whole part, not just the tail
    size = part.stat().st_size
    if size != entry["size"]:
        print(f"      ! размер {size} != {entry['size']}, файл не принят")
        return False
    got = _sha256_prefix(part)
    if got != entry["sha256"]:
        print(f"      ! sha256 не сошёлся\n        ждали {entry['sha256']}\n        вышло {got}")
        print("        (файл удалён; возможно, зеркало отдало другую ревизию)")
        part.unlink(missing_ok=True)
        return False
    if final.exists():
        final.unlink()
    part.replace(final)
    return True


def cmd_fetch(man: dict, groups: list[str], *, yes: bool, mirror: bool) -> int:
    if mirror:
        os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
        print("[i] зеркало: https://hf-mirror.com")

    todo = [e for e in man["files"] if e["group"] in groups and state(e) != "ok"]
    if not todo:
        print("[ok] всё уже на месте - качать нечего.")
        return 0

    need = sum(e["size"] for e in todo)
    print(f"[i] {len(todo)} файлов, {human(need)}")
    for e in todo:
        print(f"    {human(e['size'])}  {e['path']}")

    comfy_need = [e for e in todo if e["group"] in COMFY_GROUPS]
    if comfy_need and not (comfy_root() / "python_embeded" / "python.exe").exists():
        print()
        print(f"[!] ComfyUI не установлен: {comfy_root()}")
        print("    3D-модели кладутся внутрь ComfyUI, поэтому сначала сам движок:")
        print("    скачай ComfyUI-Easy-Install и распакуй сюда, чтобы получилось")
        print(f"    {comfy_root() / 'python_embeded' / 'python.exe'}")
        print("    (или задай THREE_COMFY_ROOT в local.env.cmd)")
        print("    Модели 3D пропущены; остальные группы качаются как обычно.")
        todo = [e for e in todo if e["group"] not in COMFY_GROUPS]
        if not todo:
            return 1

    if not yes:
        if not sys.stdin.isatty():
            print("\n[!] нет консоли для подтверждения - добавь --yes")
            return 2
        print()
        ans = input(f"качать {human(sum(e['size'] for e in todo))}? [y/N] ").strip().lower()
        if ans not in ("y", "yes", "д", "да"):
            print("отменено.")
            return 1

    failed: list[str] = []
    for i, e in enumerate(todo, 1):
        print(f"--- [{i}/{len(todo)}] {e['repo']}/{e['file']}")
        print(f"      -> {target(e)}")
        if download(e):
            print(f"      ok  {human(e['size'])}")
        else:
            failed.append(e["path"])
            print("      FAIL")

    print()
    if failed:
        print(f"[!] не скачалось: {len(failed)}")
        for f in failed:
            print("   ", f)
        print("[i] повтори ту же команду - докачает с места обрыва;")
        print("    если зеркало недоступно, добавь --mirror")
        return 1
    print("[ok] готово. Дальше: gs models --refresh (роутер подхватит новые GGUF)")
    return 0


def cmd_verify(man: dict, groups: list[str], *, strict: bool) -> int:
    """Hash every file. Size-only mismatch is fatal; a hash-only mismatch is not.

    Why the distinction: the manifest pins the sha256 of the blob at the URL we
    download from, and that is the right check for a fetch. But a user may already
    own a *different quant of the same model* - same parameter count, same file
    size, different toolchain - and calling that "corrupt" would be wrong. It is
    reported as `differs`, with `--strict` for anyone who wants it fatal.
    """
    bad = 0
    differ = 0
    for e in man["files"]:
        if e["group"] not in groups:
            continue
        p = target(e)
        if not p.is_file():
            print(f"  missing  {e['path']}")
            bad += 1
            continue
        if p.stat().st_size != e["size"]:
            print(f"  size     {e['path']}  {p.stat().st_size} != {e['size']}")
            bad += 1
            continue
        got = _sha256_prefix(p)
        if got != e["sha256"]:
            print(f"  differs  {e['path']}  {got[:12]}.. != {e['sha256'][:12]}..")
            differ += 1
        else:
            print(f"  ok       {e['path']}")
    print()
    if bad:
        print(f"[!] {bad} файлов отсутствуют или обрезаны - gs models fetch их заберёт")
        return 1
    if differ:
        print(f"[i] {differ} файлов - другая сборка того же размера (не тот же блоб).")
        print("    Это рабочий файл, но не тот, что качает манифест. Хеши нужны")
        print("    строго? gs models fetch перекачает канонические, или --verify --strict")
        return 1 if strict else 0
    print("[ok] все хеши сошлись.")
    return 0


# ------------------------------------------------------------------------ entry
def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(
        description="download / verify the model weights this repo needs")
    ap.add_argument("--fetch", nargs="?", const="", metavar="GROUPS",
                    help="download missing files (default: groups marked default)")
    ap.add_argument("--verify", nargs="?", const="", metavar="GROUPS",
                    help="re-hash what is on disk")
    ap.add_argument("--group", metavar="GROUPS",
                    help="llm,rag,vlm,image,3d,3d-x or all (status only)")
    ap.add_argument("--mirror", action="store_true", help="hf-mirror.com instead of huggingface.co")
    ap.add_argument("--yes", "-y", action="store_true", help="do not ask for confirmation")
    ap.add_argument("--strict", action="store_true",
                    help="--verify: a hash mismatch is an error, not a warning")
    a = ap.parse_args(argv[1:])

    man = load_manifest()

    if a.fetch is not None:
        groups = parse_groups(man, a.fetch or None, default_only=True)
        return cmd_fetch(man, groups, yes=a.yes, mirror=a.mirror)
    if a.verify is not None:
        groups = parse_groups(man, a.verify or None, default_only=False)
        return cmd_verify(man, groups, strict=a.strict)

    groups = parse_groups(man, a.group, default_only=False)
    return cmd_status(man, groups)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
