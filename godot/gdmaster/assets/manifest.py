"""Manifest внешнего ассета: asset.json рядом с ассетом (см. 04_manifest.md)."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from . import licenses

MANIFEST_NAME = "asset.json"

#: Маркер завершённого скачивания. Пишется ПОСЛЕДНИМ — после всех файлов и
#: манифеста. Его наличие означает «комплект целый», отсутствие — «скачивание
#: оборвалось». Нужен потому, что обрыв реален: MCP-таймаут убивает вызов
#: снаружи, `except` в download_bundle не срабатывает, и неполный каталог
#: остаётся на диске. Без маркера он выглядел бы как готовый пакет.
COMPLETE_MARKER = ".complete"

REQUIRED_FIELDS = ("name", "source", "source_url", "download_url", "license")


def sha256_file(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(chunk), b""):
            h.update(block)
    return h.hexdigest()


def build(name: str, source: str, source_url: str, download_url: str,
          license_raw: str, author: str = "", original_filename: str = "",
          formats: list[str] | None = None, tags: list[str] | None = None,
          sha256: str = "", godot_compatibility: str = "4.x") -> dict:
    """Собрать запись манифеста.

    `license` нормализуется сразу: хранить сырую строку источника нельзя,
    иначе при следующей проверке она снова станет UNKNOWN.
    """
    lic = licenses.normalize_license(license_raw)
    return {
        "name": name,
        "source": source,
        "source_url": source_url,
        "download_url": download_url,
        "license": lic,
        "author": author or "",
        "original_filename": original_filename or "",
        "downloaded_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "sha256": sha256,
        "formats": formats or [],
        "tags": tags or [],
        "godot_compatibility": godot_compatibility,
    }


def write(pack_dir: Path, entry: dict) -> Path:
    pack_dir.mkdir(parents=True, exist_ok=True)
    target = pack_dir / MANIFEST_NAME
    target.write_text(json.dumps(entry, ensure_ascii=False, indent=2), encoding="utf-8")
    return target


def read(pack_dir: Path) -> dict | None:
    target = pack_dir / MANIFEST_NAME
    if not target.exists():
        return None
    try:
        return json.loads(target.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def missing_required(entry: dict) -> list[str]:
    return [f for f in REQUIRED_FIELDS if not str(entry.get(f) or "").strip()]


def scan(root: Path) -> list[dict]:
    """Все манифесты под res://assets/external/. Основа asset_list/asset_manifest."""
    out: list[dict] = []
    if not root.exists():
        return out
    for manifest in sorted(root.rglob(MANIFEST_NAME)):
        entry = read(manifest.parent)
        if entry is None:
            continue
        entry["_pack_dir"] = manifest.parent.relative_to(root).as_posix()
        out.append(entry)
    return out


def find_duplicate(root: Path, sha256: str = "", name: str = "", source: str = "") -> dict | None:
    """Дедупликация (см. 04_manifest.md): по хешу или по name+source."""
    for entry in scan(root):
        if sha256 and entry.get("sha256") == sha256:
            return entry
        if (name and source and entry.get("name", "").lower() == name.lower()
                and entry.get("source", "").lower() == source.lower()):
            return entry
    return None
