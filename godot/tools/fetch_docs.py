"""Загрузка корпуса документации Godot 4.7 в knowledge/godot_docs/.

Источники:
  * Class reference — `doc/classes/*.xml` из godotengine/godot @ 4.7.2-stable
    (authoritative, структурированный; один API-вызов на листинг + raw-файлы).
  * Туториалы — `.rst` из godotengine/godot-docs @ ветка 4.7.

Запуск:  .venv\\Scripts\\python.exe tools\\fetch_docs.py [--classes-only|--tutorials-only]
"""
from __future__ import annotations

import argparse
import io
import json
import sys
import tarfile
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from gdmaster import config  # noqa: E402

GODOT_TAG = "4.7.2-stable"
DOCS_BRANCH = "4.7"
CLASSES_DIR = config.GODOT_DOCS_DIR / "classes"
TUTORIAL_DIRS = ("tutorials", "getting_started", "about", "engine_details", "community")
# Корневые файлы, на которые ссылаются doc_* метки (index.rst, 404.rst не нужны,
# но classes/index.rst содержит doc_class_reference и идёт через classes/).
TUTORIAL_ROOT_FILES = ("index.rst",)

UA = {"User-Agent": "gdmaster-fetch/1.0"}


def _get(url: str, timeout: float = 60.0) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def fetch_classes() -> int:
    CLASSES_DIR.mkdir(parents=True, exist_ok=True)
    api = (f"https://api.github.com/repos/godotengine/godot/git/trees/{GODOT_TAG}"
           f"?recursive=1")
    print(f"[classes] листинг {GODOT_TAG}...", flush=True)
    tree = json.loads(_get(api).decode("utf-8"))
    paths = [e["path"] for e in tree.get("tree", [])
             if e["path"].startswith("doc/classes/") and e["path"].endswith(".xml")]
    print(f"[classes] найдено {len(paths)} XML", flush=True)

    base = f"https://raw.githubusercontent.com/godotengine/godot/{GODOT_TAG}/"
    ok = 0
    done = 0

    def one(p: str) -> bool:
        dst = CLASSES_DIR / Path(p).name
        if dst.exists() and dst.stat().st_size > 200:
            return True
        try:
            dst.write_bytes(_get(base + p, timeout=45))
            return True
        except Exception as e:  # noqa: BLE001
            print(f"  ! {p}: {e}", file=sys.stderr)
            return False

    with ThreadPoolExecutor(max_workers=12) as ex:
        futs = {ex.submit(one, p): p for p in paths}
        for f in as_completed(futs):
            done += 1
            if f.result():
                ok += 1
            if done % 200 == 0:
                print(f"  {done}/{len(paths)}...", flush=True)
    print(f"[classes] скачано {ok}/{len(paths)}", flush=True)
    return ok


def fetch_tutorials() -> int:
    url = f"https://codeload.github.com/godotengine/godot-docs/tar.gz/refs/heads/{DOCS_BRANCH}"
    print(f"[tutorials] качаю godot-docs@{DOCS_BRANCH}...", flush=True)
    blob = _get(url, timeout=600)
    print(f"[tutorials] {len(blob)/1e6:.1f} MB, распаковка...", flush=True)
    n = 0
    root_prefix = f"godot-docs-{DOCS_BRANCH}/"
    with tarfile.open(fileobj=io.BytesIO(blob), mode="r:gz") as tf:
        for m in tf.getmembers():
            if not m.isfile() or not m.name.endswith(".rst"):
                continue
            rel = m.name[len(root_prefix):] if m.name.startswith(root_prefix) else m.name
            if not (rel.startswith(TUTORIAL_DIRS) or rel in TUTORIAL_ROOT_FILES
                    or rel == "classes/index.rst"):
                continue
            dst = config.GODOT_DOCS_DIR / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            f = tf.extractfile(m)
            if f is None:
                continue
            dst.write_bytes(f.read())
            n += 1
    print(f"[tutorials] распаковано {n} .rst", flush=True)
    return n


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--classes-only", action="store_true")
    ap.add_argument("--tutorials-only", action="store_true")
    args = ap.parse_args()
    t0 = time.time()
    total = 0
    if not args.tutorials_only:
        total += fetch_classes()
    if not args.classes_only:
        total += fetch_tutorials()
    print(f"\nГотово: {total} файлов за {time.time()-t0:.1f}s -> {config.GODOT_DOCS_DIR}")


if __name__ == "__main__":
    main()
