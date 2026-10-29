#!/usr/bin/env python
"""Static check that a page in a game can actually load: modules resolve, assets exist.

`tscheck.py` catches the errors a compiler can see. This catches the ones it cannot,
because a browser is the only thing that evaluates them - and by then the page is
already open and blank.

The failure it exists for, 2026-10-09: an agent wrote `ninja.html` importing

    import { TextureLoader } from 'three/addons/loaders/TextureLoader.js';

`vendor/three/` ships `addons/loaders/GLTFLoader.js` and nothing else - `TextureLoader`
lives in the core build and is re-exported from `three`. The specifier resolved to a
file that does not exist, so the browser 404'd the import and **aborted the whole module
graph**: `init()` never ran, the canvas stayed black, and no error was visible outside
devtools. The agent reported the game as finished; the studio showed an empty page.

A missing *asset* is quieter still: the page draws, and one sprite is invisible.

So: every module specifier is resolved through the page's own importmap and checked on
disk, and every referenced media file is checked the same way. Nothing is executed.

Usage
-----
    python tools/pagecheck.py                     # every page in the active project
    python tools/pagecheck.py my_game                     # name under projects/games/
    python tools/pagecheck.py projects/games/my_game/ninja.html    # one page
    python tools/pagecheck.py --json              # machine-readable
    python tools/pagecheck.py --all               # include files under vendor/

Exit code is 0 when every page can load, 1 when one cannot - so it can gate a build.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from threejs import config  # noqa: E402

# --- what a page can reference ---------------------------------------------------
MEDIA_EXT = {
    ".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".svg", ".ico",
    ".glb", ".gltf", ".spz", ".bin", ".ktx2", ".hdr", ".fbx", ".obj",
    ".mp3", ".wav", ".ogg", ".m4a", ".mp4", ".webm",
    ".json", ".css", ".woff", ".woff2", ".ttf", ".otf",
}
# Directories whose contents are the runtime, not the project's own code.
SKIP_DIRS = {".git", "node_modules", ".venv", "__pycache__", "dist", "build",
             ".three-rag", ".pi", "data", "logs", "vendor"}

IMPORTMAP_RE = re.compile(
    r"""<script[^>]*type\s*=\s*["']importmap["'][^>]*>(.*?)</script>""",
    re.S | re.I)
MODULE_SCRIPT_RE = re.compile(
    r"""<script[^>]*type\s*=\s*["']module["'][^>]*>(.*?)</script>""", re.S | re.I)
# `import x from 'a'` / `export * from 'a'` / `import 'a'` / `import('a')`
SPECIFIER_RE = re.compile(
    r"""(?:\bfrom\s*|\bimport\s*\(?\s*|\bimport\s+)["']([^"'\s]+)["']""")
# Any quoted string that ends in a media extension: `'public/assets/a.png'`.
STRING_RE = re.compile(r"""["']([^"'\n]+\.(?:%s))["']"""
                       % "|".join(e.lstrip(".") for e in MEDIA_EXT), re.I)


def _strip_json_comments(text: str) -> str:
    """importmap blocks in the wild carry // comments; json.loads does not."""
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    return re.sub(r"(^|\s)//[^\n]*", r"\1", text)


def parse_importmap(html: str) -> dict:
    """The page's `imports` map. An absent map means bare specifiers cannot resolve."""
    m = IMPORTMAP_RE.search(html)
    if not m:
        return {}
    try:
        data = json.loads(_strip_json_comments(m.group(1)))
    except json.JSONDecodeError:
        return {}
    imports = data.get("imports") or {}
    return {k: v for k, v in imports.items() if isinstance(v, str)}


def resolve_specifier(spec: str, importmap: dict) -> str | None:
    """Apply the importmap the way a browser does: exact key first, then longest
    trailing-slash prefix."""
    if spec in importmap:
        return importmap[spec]
    best = ""
    for key in importmap:
        if key.endswith("/") and spec.startswith(key) and len(key) > len(best):
            best = key
    if best:
        return importmap[best] + spec[len(best):]
    return None


def _looks_remote(spec: str) -> bool:
    return spec.startswith(("http://", "https://", "data:", "blob:", "//"))


def _resolve_on_disk(ref: str, page_dir: Path, project: Path) -> Path:
    """Where the server would look for `ref` written inside a page.

    `serve.py` serves the project directory as the site root, so a page at
    `/ninja.html` resolves `public/assets/a.png` to `<project>/public/assets/a.png`
    and `/public/assets/a.png` to the same file.
    """
    ref = ref.split("?")[0].split("#")[0]
    if ref.startswith("/"):
        return project / ref.lstrip("/")
    return (page_dir / ref).resolve()


def _is_relative(spec: str) -> bool:
    """Относительный или корневой спецификатор браузер разрешает САМ, без importmap.

    Это не мелочь: `./render/world.js` рядом с импортирующим модулем — законный импорт,
    и требовать для него запись в importmap значит красить зелёную страницу в BAD. Гейт,
    который всегда красный, перестают читать, и он перестаёт ловить настоящие ошибки.
    """
    return spec.startswith(("./", "../", "/"))


def _is_local_module(path: Path, project: Path) -> bool:
    """Модуль проекта, а не рантайм: внутрь vendor/ и node_modules/ не ходим."""
    try:
        rel = path.relative_to(project)
    except ValueError:
        return False
    return not (SKIP_DIRS & set(rel.parts))


def check_page(page: Path, project: Path) -> dict:
    """Every module and asset the page needs, and whether it is there.

    Импорты проверяются ПО ГРАФУ, а не только в самой странице. Раньше сканировался лишь
    инлайновый `<script type="module">`, и ошибка в `render/*.js` не находилась вообще —
    хотя именно так выглядел разобранный в заголовке случай с TextureLoader: страница
    цела, модуль битый, экран чёрный. Относительные пути при обходе разрешаются от
    КАТАЛОГА САМОГО МОДУЛЯ (так делает браузер), а значения importmap — от каталога
    страницы (так делает браузер с importmap).
    """
    html = page.read_text(encoding="utf-8", errors="replace")
    importmap = parse_importmap(html)
    problems: list[dict] = []

    module_scripts = MODULE_SCRIPT_RE.findall(html)
    if not module_scripts:
        problems.append({
            "kind": "no-module",
            "ref": "",
            "detail": "no <script type=\"module\"> - nothing will run",
        })

    spec_strings: set[str] = set()
    seen: set[tuple[str, str]] = set()
    walked: set[Path] = set()
    queue: list[tuple[str, Path]] = [(s, page.parent) for s in module_scripts]
    while queue:
        text, base = queue.pop()
        for spec in SPECIFIER_RE.findall(text):
            if _looks_remote(spec):
                continue
            key = (spec, str(base))
            if key in seen:
                continue
            seen.add(key)
            spec_strings.add(spec)

            if _is_relative(spec):
                hit = _resolve_on_disk(spec, base, project)
            else:
                target = resolve_specifier(spec, importmap)
                if target is None:
                    problems.append({
                        "kind": "unresolved",
                        "ref": spec,
                        "detail": "bare specifier is not in the importmap - the browser "
                                  "refuses it before any fetch",
                    })
                    continue
                hit = _resolve_on_disk(target, page.parent, project)

            if not hit.is_file():
                try:
                    shown = hit.relative_to(project).as_posix()
                except ValueError:
                    shown = str(hit)
                problems.append({
                    "kind": "missing-module",
                    "ref": spec,
                    "detail": f"resolves to {shown} -> no such file. The whole module "
                              f"graph fails and the page stays blank.",
                })
                continue

            if hit.suffix == ".js" and hit not in walked and _is_local_module(hit, project):
                walked.add(hit)
                queue.append((hit.read_text(encoding="utf-8", errors="replace"), hit.parent))

    seen_refs: set[str] = set()
    for ref in STRING_RE.findall(html):
        if ref in seen_refs or _looks_remote(ref) or ref.startswith(("#", "data:")):
            continue
        seen_refs.add(ref)
        if ref in spec_strings:
            continue
        if _resolve_on_disk(ref, page.parent, project).is_file():
            continue
        # A very common mistake: the file is under `public/`, and the page says
        # `assets/...` (Vite would rewrite that; a plain static server will not).
        alt = project / "public" / ref.lstrip("/")
        hint = f" (the file is at public/{ref.lstrip('/')} - reference it as " \
               f"public/{ref.lstrip('/')}, or it 404s)" if alt.is_file() else ""
        problems.append({"kind": "missing-asset", "ref": ref,
                         "detail": "no such file" + hint})

    return {"page": page.relative_to(project).as_posix(),
            "modules": len(spec_strings), "refs": len(seen_refs),
            "problems": problems}


def find_pages(root: Path, include_all: bool = False) -> list[Path]:
    skip = set() if include_all else SKIP_DIRS
    out = []
    for p in sorted(root.rglob("*.html")):
        if skip & set(p.relative_to(root).parts):
            continue
        out.append(p)
    return out


def render(results: list[dict]) -> str:
    lines = []
    total = sum(len(r["problems"]) for r in results)
    for r in results:
        if not r["problems"]:
            lines.append(f"OK    {r['page']}  "
                         f"({r['modules']} modules, {r['refs']} refs)")
            continue
        lines.append(f"BAD   {r['page']}  "
                     f"({len(r['problems'])} problem(s), {r['modules']} modules)")
        for p in r["problems"]:
            lines.append(f"        [{p['kind']}] {p['ref']}")
            lines.append(f"            {p['detail']}")
    lines.append("")
    lines.append(f"pages: {len(results)}   problems: {total}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("project", nargs="?", default="",
                    help="game name under projects/games/, a path, or one .html file")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--all", action="store_true",
                    help="also scan vendor/ and other skipped directories")
    # `check.cmd` hands the same flag set to tscheck and to this tool, so tsc-only
    # flags (`--full`, `--code`, `--top`) arrive here too. Ignoring them is the point:
    # the alternative is a gate that fails on a flag meant for its sibling.
    args, _ignored = ap.parse_known_args(argv)

    raw = args.project.strip().strip('"')
    single = None
    if raw.lower().endswith((".html", ".htm")):
        single = Path(raw).expanduser()
        if not single.is_absolute():
            single = (Path.cwd() / single).resolve()
        if not single.is_file():
            print(f"[ERROR] no such page: {single}", file=sys.stderr)
            return 2
        project = single.parent
        for parent in [single.parent, *single.parents]:
            if (parent / "public").is_dir() or (parent / "web3d").is_dir():
                project = parent
                break
    else:
        try:
            project = config.resolve_project(raw)
        except ValueError as exc:
            print(f"[ERROR] {exc}", file=sys.stderr)
            return 2
        if not project.is_dir():
            print(f"[ERROR] not a directory: {project}", file=sys.stderr)
            return 2

    pages = [single] if single else find_pages(project, include_all=args.all)
    if not pages:
        print(f"[ERROR] no .html pages under {project}", file=sys.stderr)
        return 2

    results = [check_page(p, project) for p in pages]
    if args.json:
        print(json.dumps({"project": str(project), "results": results},
                         ensure_ascii=False, indent=2))
    else:
        print(f"project: {project}")
        print(render(results))
    return 0 if all(not r["problems"] for r in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
