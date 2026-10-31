"""Inspect a serialised place/model (`.rbxlx`, `.rbxmx`) without Studio.

A `.rbxlx` is the DataModel as XML: `<Item class="Script">` nested inside services, with
the script body in `<ProtectedString name="Source">`. Reading it directly is how the agent
answers "what is actually in this place" when Studio is closed, and how the project corpus
gets a searchable outline of the place instead of one opaque blob.
"""
from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

MAX_SCRIPTS = 120
SCRIPT_CLASSES = {"Script", "LocalScript", "ModuleScript"}


def _props(item: ET.Element) -> dict:
    out: dict[str, str] = {}
    for props in item.findall("Properties"):
        for p in props:
            name = p.get("name") or ""
            if name:
                out[name] = p.text or ""
    return out


def inspect(path: Path) -> dict:
    """Summary of a place file: services, class counts, scripts with sizes."""
    try:
        root = ET.parse(str(path)).getroot()
    except (ET.ParseError, OSError) as e:
        return {"file": str(path), "error": f"{type(e).__name__}: {e}"}

    counts: dict[str, int] = {}
    services: list[str] = []
    scripts: list[dict] = []
    total = 0

    def walk(item: ET.Element, trail: str, depth: int) -> None:
        nonlocal total
        cls = item.get("class") or "Item"
        props = _props(item)
        name = props.get("Name") or cls
        here = f"{trail}/{name}" if trail else name
        total += 1
        counts[cls] = counts.get(cls, 0) + 1
        if depth == 0:
            services.append(name)
        if cls in SCRIPT_CLASSES and len(scripts) < MAX_SCRIPTS:
            src = props.get("Source") or ""
            scripts.append({
                "path": here,
                "name": name,
                "class": cls,
                "lines": src.count("\n") + 1 if src else 0,
                "bytes": len(src),
                "disabled": props.get("Disabled", "").lower() == "true",
                "run_context": props.get("RunContext", "") or None,
                "head": "\n".join(src.splitlines()[:3]),
            })
        for child in item.findall("Item"):
            walk(child, here, depth + 1)

    for item in root.findall("Item"):
        walk(item, "", 0)

    return {
        "file": str(path),
        "services": services,
        "total_instances": total,
        "class_counts": dict(sorted(counts.items(), key=lambda kv: -kv[1])[:40]),
        "scripts": scripts,
        "scripts_truncated": len(scripts) >= MAX_SCRIPTS,
    }
