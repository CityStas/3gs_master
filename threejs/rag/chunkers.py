"""Semantic chunking for Three.js/web projects."""
from __future__ import annotations

import hashlib
import html
import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path

from .. import config


@dataclass
class Chunk:
    text: str
    source: str
    path: str
    file_type: str
    symbol: str = ""
    class_name: str = ""
    extends: str = ""
    node_type: str = ""
    scene_path: str = ""
    node_path: str = ""
    section: str = ""
    engine_version: str = config.THREE_VERSION
    content_hash: str = ""
    meta: dict = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.content_hash:
            self.content_hash = hashlib.sha256(self.text.encode("utf-8")).hexdigest()

    @property
    def id(self) -> str:
        key = f"{self.source}|{self.path}|{self.symbol}|{self.section}|{self.content_hash[:16]}"
        return hashlib.sha1(key.encode("utf-8")).hexdigest()

    def payload(self) -> dict:
        d = asdict(self)
        d["id"] = self.id
        return d


RE_CLASS = re.compile(r"\bclass\s+([A-Za-z_$][\w$]*)(?:\s+extends\s+([A-Za-z_$][\w$.]*))?", re.M)
RE_FUNC = re.compile(r"\b(?:async\s+)?function\s+([A-Za-z_$][\w$]*)\s*\(([^)]*)\)", re.M)
RE_ARROW = re.compile(r"\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s*)?\([^)]*\)\s*=>", re.M)
RE_METHOD = re.compile(r"^\s*(?:async\s+)?([A-Za-z_$][\w$]*)\s*\(([^)]*)\)\s*\{", re.M)
RE_INTERFACE = re.compile(r"\binterface\s+([A-Za-z_$][\w$]*)", re.M)
RE_TYPE = re.compile(r"\btype\s+([A-Za-z_$][\w$]*)\s*=", re.M)
RE_ENUM = re.compile(r"\benum\s+([A-Za-z_$][\w$]*)", re.M)
RE_EXPORT = re.compile(r"\bexport\s+(?:default\s+)?(?:class|function|const|let|var|interface|type|enum)\b", re.M)


def _block_end(src: str, start: int) -> int:
    brace = src.find("{", start)
    if brace < 0:
        return min(len(src), start + 4000)
    depth = 0
    in_str = None
    esc = False
    for i in range(brace, len(src)):
        ch = src[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == in_str:
                in_str = None
            continue
        if ch in ('"', "'", "`"):
            in_str = ch
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return min(len(src), i + 1)
    return len(src)


def _decl_chunk(src: str, rel_path: str, match: re.Match[str], symbol: str, section: str,
                source: str, class_name: str = "", extends: str = "") -> Chunk:
    body = src[match.start():_block_end(src, match.start())].strip()
    if len(body) > 12000:
        body = body[:12000] + "\n// ... truncated"
    header = f"# {rel_path}\n# Three.js {config.THREE_VERSION}"
    if class_name:
        header += f"\n# class {class_name}"
    return Chunk(
        text=f"{header}\n\n{body}", source=source, path=rel_path, file_type="javascript",
        symbol=symbol, class_name=class_name, extends=extends, section=section,
        meta={"framework": "three.js", "version": config.THREE_VERSION},
    )


def chunk_javascript(text: str, rel_path: str, source: str = "project") -> list[Chunk]:
    chunks: list[Chunk] = []
    path_stem = Path(rel_path).stem
    imports = [ln.strip() for ln in text.splitlines() if ln.strip().startswith("import ")]
    exports = [ln.strip() for ln in text.splitlines() if RE_EXPORT.search(ln)]
    header = [f"# JavaScript/TypeScript file: {rel_path}", f"# Three.js {config.THREE_VERSION}"]
    if imports:
        header.append("imports:\n" + "\n".join("  " + x for x in imports[:40]))
    if exports:
        header.append("exports:\n" + "\n".join("  " + x for x in exports[:40]))
    if len(header) > 2:
        chunks.append(Chunk("\n".join(header), source, rel_path, "javascript", symbol=f"{path_stem}:header", section="header",
                           meta={"framework": "three.js", "version": config.THREE_VERSION}))

    class_matches = list(RE_CLASS.finditer(text))
    for m in class_matches:
        cls, ext = m.group(1), m.group(2) or ""
        chunks.append(_decl_chunk(text, rel_path, m, cls, "class", source, cls, ext))

    class_ranges = [(m.start(), _block_end(text, m.start()), m.group(1)) for m in class_matches]
    for regex, section in ((RE_INTERFACE, "interface"), (RE_TYPE, "type"), (RE_ENUM, "enum"), (RE_FUNC, "function"), (RE_ARROW, "function")):
        for m in regex.finditer(text):
            inside = next((c for a, b, c in class_ranges if a <= m.start() < b), "")
            if inside and section in ("function",):
                continue
            name = m.group(1)
            chunks.append(_decl_chunk(text, rel_path, m, f"{path_stem}.{name}", section, source, inside))

    for m in RE_METHOD.finditer(text):
        inside = next((c for a, b, c in class_ranges if a <= m.start() < b), "")
        if not inside:
            continue
        name = m.group(1)
        if name in {"if", "for", "while", "switch", "catch"}:
            continue
        chunks.append(_decl_chunk(text, rel_path, m, f"{inside}.{name}", "method", source, inside))

    if not chunks:
        chunks.append(Chunk(text=text[:8000], source=source, path=rel_path, file_type="javascript",
                            symbol=path_stem, section="raw", meta={"framework": "three.js", "version": config.THREE_VERSION}))
    return chunks


class _HTMLTextParser:
    """Flatten HTML to a text stream that keeps heading levels as markdown `#` markers.

    The original version recorded the current heading tag but never emitted it, so
    `chunk_html` - which splits on `^#{1,4}\\s+` - could never split anything and every
    page collapsed into a single chunk.
    """

    SKIP = {"script", "style", "noscript", "svg"}

    def __init__(self) -> None:
        from html.parser import HTMLParser

        class P(HTMLParser):
            def __init__(self, outer):
                super().__init__(convert_charrefs=True)
                self.outer = outer
                self.heading = None
                self.heading_pending = False
                self.skip_depth = 0
                self.lines: list[str] = []

            def handle_starttag(self, tag, attrs):
                if tag in _HTMLTextParser.SKIP:
                    self.skip_depth += 1
                elif tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
                    self.heading = tag
                    self.heading_pending = True
                elif tag == "pre":
                    self.lines.append("\n```\n")
                elif tag in {"p", "div", "li", "tr", "br"}:
                    self.lines.append("")

            def handle_endtag(self, tag):
                if tag in _HTMLTextParser.SKIP:
                    self.skip_depth = max(0, self.skip_depth - 1)
                elif tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
                    self.heading = None
                    self.heading_pending = False
                elif tag == "pre":
                    self.lines.append("\n```\n")

            def handle_data(self, data):
                if self.skip_depth:
                    return
                t = html.unescape(data).strip()
                if not t:
                    return
                if self.heading:
                    if self.heading_pending:
                        self.lines.append("#" * int(self.heading[1]) + " " + t)
                        self.heading_pending = False
                    else:
                        self.lines.append(t)
                else:
                    self.lines.append(t)

        self.parser = P(self)

    def feed(self, text: str) -> str:
        self.parser.feed(text)
        return "\n".join(self.parser.lines)


def chunk_html(text: str, rel_path: str, source: str = "official_docs") -> list[Chunk]:
    clean = _HTMLTextParser().feed(text)
    lines = clean.splitlines()
    sections: list[tuple[str, list[str]]] = []
    current = (Path(rel_path).stem, [])
    for line in lines:
        if re.match(r"^#{1,4}\s+", line):
            if current[1]: sections.append(current)
            current = (line.lstrip("# ").strip(), [])
        else:
            current[1].append(line)
    if current[1]: sections.append(current)
    chunks = []
    for title, body in sections:
        txt = "\n".join(body).strip()
        if len(txt) < 20: continue
        symbol = f"{Path(rel_path).stem}:{title}"
        chunks.append(Chunk(
            text=f"# {rel_path}\n# Three.js {config.THREE_VERSION}\n\n## {title}\n{txt[:12000]}",
            source=source, path=rel_path, file_type="html", symbol=symbol, section="docs_section",
            meta={"framework": "three.js", "version": config.THREE_VERSION},
        ))
    return chunks or [Chunk(clean[:12000], source, rel_path, "html", symbol=Path(rel_path).stem, section="raw")]


def _fence_mask(text: str) -> list[bool]:
    """True for every line index that sits inside (or opens/closes) a ``` / ~~~ fence.

    `chunk_markdown` splits on `^#`, and shell snippets inside fences routinely contain
    comments like `# install three`, which produced bogus sections such as
    `instancing:install three`. Fenced regions must never be treated as headings.
    """
    mask: list[bool] = []
    in_fence = False
    marker = ""
    for line in text.splitlines():
        stripped = line.lstrip()
        if not in_fence and (stripped.startswith("```") or stripped.startswith("~~~")):
            in_fence = True
            marker = stripped[:3]
            mask.append(True)
            continue
        if in_fence and stripped.startswith(marker):
            in_fence = False
            mask.append(True)
            continue
        mask.append(in_fence)
    return mask


RE_HEADING = re.compile(r"^#{1,6}\s+(.+)$", re.M)


def chunk_markdown(text: str, rel_path: str, source: str = "cookbook", file_type: str = "markdown") -> list[Chunk]:
    mask = _fence_mask(text)
    if not mask:
        return [Chunk(text[:12000], source, rel_path, file_type, symbol=Path(rel_path).stem, section="raw")]

    line_starts: list[int] = []
    pos = 0
    for line in text.splitlines(keepends=True):
        line_starts.append(pos)
        pos += len(line)

    import bisect

    def line_of(off: int) -> int:
        return min(bisect.bisect_right(line_starts, off) - 1, len(mask) - 1)

    matches = [m for m in RE_HEADING.finditer(text) if not mask[max(0, line_of(m.start()))]]
    if not matches:
        return [Chunk(text[:12000], source, rel_path, file_type, symbol=Path(rel_path).stem, section="raw")]
    chunks = []
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[m.start():end].strip()
        if len(body) < 30:
            continue
        title = m.group(1).strip()
        chunks.append(Chunk(body[:12000], source, rel_path, file_type,
                            symbol=f"{Path(rel_path).stem}:{title}", section="section"))
    if not chunks:
        return [Chunk(text[:12000], source, rel_path, file_type, symbol=Path(rel_path).stem, section="raw")]
    return chunks


def chunk_json(text: str, rel_path: str, source: str = "project") -> list[Chunk]:
    try:
        obj = json.loads(text)
    except json.JSONDecodeError:
        return [Chunk(text[:12000], source, rel_path, "json", symbol=Path(rel_path).stem, section="raw")]
    chunks=[]
    if isinstance(obj, dict):
        for key, val in obj.items():
            rendered=json.dumps({key:val}, ensure_ascii=False, indent=2)
            chunks.append(Chunk(rendered[:12000], source, rel_path, "json", symbol=str(key), section="property"))
    else:
        chunks.append(Chunk(json.dumps(obj, ensure_ascii=False, indent=2)[:12000], source, rel_path, "json", symbol=Path(rel_path).stem, section="root"))
    return chunks


def chunk_shader(text: str, rel_path: str, source: str = "project") -> list[Chunk]:
    blocks=[]
    for m in re.finditer(r"^(?:void|float|vec[234]|mat[234]|fn)\s+([A-Za-z_][\w]*)\s*\([^\n]*\)", text, re.M):
        end=_block_end(text,m.start())
        blocks.append(Chunk(text[m.start():end][:12000],source,rel_path,"shader",symbol=f"{Path(rel_path).stem}.{m.group(1)}",section="function"))
    return blocks or [Chunk(text[:12000],source,rel_path,"shader",symbol=Path(rel_path).stem,section="raw")]


def chunk_file(path: Path, rel_path: str, source: str) -> list[Chunk]:
    suffix=path.suffix.lower()
    text=path.read_text(encoding="utf-8", errors="replace")
    if suffix in {".js",".mjs",".cjs",".ts",".tsx",".jsx",".vue",".svelte"}:
        return chunk_javascript(text, rel_path, source)
    if suffix in {".html",".htm"}:
        return chunk_html(text, rel_path, source)
    if suffix in {".md",".txt",".yaml",".yml",".css",".scss",".sass"}:
        return chunk_markdown(text, rel_path, source, file_type=suffix.lstrip("."))
    if suffix in {".json",".json5"}:
        return chunk_json(text, rel_path, source)
    if suffix in {".glsl",".vert",".frag",".wgsl",".shader"}:
        return chunk_shader(text, rel_path, source)
    return [Chunk(text[:12000], source, rel_path, suffix.lstrip("."), symbol=Path(rel_path).stem, section="raw")]
