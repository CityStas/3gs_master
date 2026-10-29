"""Semantic chunking for Unity: C#, Unity docs (HTML), markdown, JSON/asmdef, YAML assets.

The C# and YAML chunkers are the Unity-specific additions. Everything else is the
same shape as the Three.js chunker: one chunk per declaration, with a header line that
carries the path and the pinned version so a stale hit is obvious in the result.
"""
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
    namespace: str = ""
    member_kind: str = ""
    section: str = ""
    engine_version: str = config.UNITY_VERSION
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


def _meta(kind: str) -> dict:
    return {"framework": config.UNITY_FRAMEWORK_TAG, "version": config.UNITY_VERSION, "kind": kind}


# =============================================================================
# C#
# =============================================================================
RE_CS_USING = re.compile(r"^\s*using\s+[\w.]+\s*;", re.M)
RE_CS_NAMESPACE = re.compile(r"^\s*namespace\s+([\w.]+)", re.M)
RE_CS_ATTR = r"(?:\[[^\]]*\]\s*)*"
RE_CS_MODS = r"(?:public|internal|private|protected|static|sealed|abstract|partial|readonly|unsafe|new|ref|file)\s+"
RE_CS_TYPE = re.compile(
    rf"^\s*{RE_CS_ATTR}(?:{RE_CS_MODS})*"
    r"(class|struct|interface|enum|record)\s+([A-Za-z_]\w*)\s*(?:<[^>]*>)?\s*(?::\s*([^{{\n]+))?",
    re.M)
RE_CS_METHOD = re.compile(
    rf"^\s*{RE_CS_ATTR}(?:{RE_CS_MODS})*"
    r"(?:async\s+|extern\s+|override\s+|virtual\s+)*"
    r"([\w<>,\[\]\.\?]+)\s+([A-Za-z_]\w*)\s*(?:<[^>]*>)?\s*\(([^;{{)]*)\)\s*(?:where[^{{]*)?\{?",
    re.M)
RE_CS_PROPERTY = re.compile(
    rf"^\s*{RE_CS_ATTR}(?:{RE_CS_MODS})*"
    r"([\w<>,\[\]\.\?]+)\s+([A-Za-z_]\w*)\s*\{\s*(?:get|set|init)",
    re.M)
RE_CS_FIELD = re.compile(
    rf"^\s*{RE_CS_ATTR}(?:{RE_CS_MODS})*"
    r"([\w<>,\[\]\.\?]+)\s+([A-Za-z_]\w*)\s*(?:=[^;]*)?;",
    re.M)
RE_CS_CALL_KEYWORDS = {
    "if", "for", "foreach", "while", "switch", "catch", "using", "lock", "return",
    "fixed", "checked", "unchecked", "new", "sizeof", "typeof", "nameof", "default",
    "throw", "yield", "get", "set", "init", "where", "base", "this", "else", "do",
}


def _cs_block_end(src: str, start: int) -> int:
    """Index just past the brace block that opens at/after `start`.

    Skips `//`, `/* */`, `"..."`, `@"..."` (doubled quotes), `'...'` - a `}` inside a
    comment or a string literal must not close the block, and in C# both are everywhere.
    """
    brace = src.find("{", start)
    semi = src.find(";", start)
    if brace < 0 or (0 <= semi < brace):
        # Field or expression-bodied member: the declaration ends at the `;`. Falling
        # back to a fixed window here would swallow the rest of the file into one chunk.
        return min(len(src), semi + 1) if semi >= 0 else min(len(src), start + 400)
    depth = 0
    i = brace
    n = len(src)
    while i < n:
        ch = src[i]
        nxt = src[i + 1] if i + 1 < n else ""
        if ch == "/" and nxt == "/":
            j = src.find("\n", i)
            i = n if j < 0 else j + 1
            continue
        if ch == "/" and nxt == "*":
            j = src.find("*/", i + 2)
            i = n if j < 0 else j + 2
            continue
        if ch == "@" and nxt == '"':
            i += 2
            while i < n:
                if src[i] == '"':
                    if i + 1 < n and src[i + 1] == '"':
                        i += 2
                        continue
                    i += 1
                    break
                i += 1
            continue
        if ch in ('"', "'"):
            quote = ch
            i += 1
            while i < n:
                if src[i] == "\\":
                    i += 2
                    continue
                if src[i] == quote:
                    i += 1
                    break
                i += 1
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return min(n, i + 1)
        i += 1
    return n


def _cs_decl(src: str, rel_path: str, match: re.Match[str], symbol: str, section: str,
             source: str, class_name: str = "", namespace: str = "", base: str = "",
             member_kind: str = "") -> Chunk:
    body = src[match.start():_cs_block_end(src, match.start())].strip()
    if len(body) > 12000:
        body = body[:12000] + "\n// ... truncated"
    header = f"# {rel_path}\n# Unity {config.UNITY_VERSION} (C#)"
    if namespace:
        header += f"\n# namespace {namespace}"
    if class_name:
        header += f"\n# class {class_name}"
    if base:
        header += f"\n# inherits {base.strip()}"
    return Chunk(text=f"{header}\n\n{body}", source=source, path=rel_path, file_type="csharp",
                 symbol=symbol, class_name=class_name, namespace=namespace, section=section,
                 member_kind=member_kind, meta=_meta("csharp"))


def chunk_csharp(text: str, rel_path: str, source: str = "project") -> list[Chunk]:
    chunks: list[Chunk] = []
    stem = Path(rel_path).stem
    ns_match = RE_CS_NAMESPACE.search(text)
    namespace = ns_match.group(1) if ns_match else ""

    usings = [ln.strip() for ln in text.splitlines() if ln.strip().startswith("using ")]
    types = list(RE_CS_TYPE.finditer(text))
    header = [f"# C# file: {rel_path}", f"# Unity {config.UNITY_VERSION}"]
    if namespace:
        header.append(f"namespace: {namespace}")
    if types:
        header.append("types:\n" + "\n".join(
            "  " + f"{m.group(1)} {m.group(2)}" for m in types[:40]))
    if usings:
        header.append("usings:\n" + "\n".join("  " + x for x in usings[:40]))
    if len(header) > 2:
        chunks.append(Chunk("\n".join(header), source, rel_path, "csharp",
                            symbol=f"{stem}:header", namespace=namespace, section="header",
                            member_kind="header", meta=_meta("csharp")))

    type_ranges = [(m.start(), _cs_block_end(text, m.start()), m.group(2)) for m in types]
    type_starts = {m.start() for m in types}

    def owner(pos: int) -> str:
        return next((c for a, b, c in type_ranges if a <= pos < b), "")

    for m in types:
        kind, name, base = m.group(1), m.group(2), (m.group(3) or "")
        chunks.append(_cs_decl(text, rel_path, m, name, kind, source, name, namespace, base,
                               member_kind=kind))

    # A `record Foo(int X)` line is matched by both the type and the method regex; the
    # type chunk already carries it, so the declaration line is skipped here.
    for regex, kind in ((RE_CS_METHOD, "method"), (RE_CS_PROPERTY, "property"),
                        (RE_CS_FIELD, "field")):
        for m in regex.finditer(text):
            if m.start() in type_starts:
                continue
            name = m.group(2)
            if name in RE_CS_CALL_KEYWORDS:
                continue
            inside = owner(m.start())
            if not inside:
                continue
            decl = text[m.start():_cs_block_end(text, m.start())]
            # `public float Health => _hp;` has no brace and no `{ get; }`, so the field
            # regex claims it. `=>` means it is an expression-bodied property, not a field.
            if kind == "field" and "=>" in decl:
                kind_here = "property"
            else:
                kind_here = kind
            chunks.append(_cs_decl(text, rel_path, m, f"{inside}.{name}", kind_here,
                                   source, inside, namespace, member_kind=kind_here))

    if not chunks:
        chunks.append(Chunk(text[:8000], source, rel_path, "csharp", symbol=stem,
                            namespace=namespace, section="raw", member_kind="raw",
                            meta=_meta("csharp")))
    return chunks


# =============================================================================
# HTML (Unity Manual / ScriptReference / package docs)
# =============================================================================
class _HTMLTextParser:
    """Flatten HTML to a text stream that keeps heading levels as markdown `#` markers.

    Unity's ScriptReference and Manual pages are plain static HTML: `<h1>` for the
    page/section title, `<h2>`/`<h3>` for members and sub-sections, `<pre>` for code.
    Emitting the heading level is what makes `chunk_html` able to split at all.
    """

    SKIP = {"script", "style", "noscript", "svg", "head", "nav", "footer"}

    def __init__(self) -> None:
        from html.parser import HTMLParser

        class P(HTMLParser):
            def __init__(self, outer):
                super().__init__(convert_charrefs=True)
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
                elif tag in {"p", "div", "li", "tr", "br", "table", "td", "th"}:
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
            if current[1]:
                sections.append(current)
            current = (line.lstrip("# ").strip(), [])
        else:
            current[1].append(line)
    if current[1]:
        sections.append(current)

    stem = Path(rel_path).stem
    chunks = []
    for title, body in sections:
        txt = "\n".join(body).strip()
        if len(txt) < 20:
            continue
        # `section` carries the real heading, not a constant: it is what tells the model
        # (and `unity_rag_search`'s output) which part of the page a passage came from -
        # "Examples" vs "Properties" vs the page intro all read very differently.
        chunks.append(Chunk(
            text=f"# {rel_path}\n# Unity {config.UNITY_VERSION}\n\n## {title}\n{txt[:12000]}",
            source=source, path=rel_path, file_type="html", symbol=f"{stem}:{title}",
            class_name=stem, section=title[:200], meta=_meta("docs")))
    return chunks or [Chunk(clean[:12000], source, rel_path, "html", symbol=stem,
                            class_name=stem, section="raw", meta=_meta("docs"))]


# =============================================================================
# Markdown
# =============================================================================
def _fence_mask(text: str) -> list[bool]:
    """True for every line inside (or opening/closing) a ``` / ~~~ fence.

    `chunk_markdown` splits on `^#`; shell and C# snippets inside fences contain `#`
    comments (`#pragma`, `#if UNITY_EDITOR`) and would otherwise become bogus sections.
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


def chunk_markdown(text: str, rel_path: str, source: str = "cookbook",
                   file_type: str = "markdown") -> list[Chunk]:
    stem = Path(rel_path).stem
    mask = _fence_mask(text)
    if not mask:
        return [Chunk(text[:12000], source, rel_path, file_type, symbol=stem,
                      section="raw", meta=_meta("docs"))]

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
        return [Chunk(text[:12000], source, rel_path, file_type, symbol=stem,
                      section="raw", meta=_meta("docs"))]
    chunks = []
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[m.start():end].strip()
        if len(body) < 30:
            continue
        title = m.group(1).strip()
        chunks.append(Chunk(body[:12000], source, rel_path, file_type,
                            symbol=f"{stem}:{title}", section=title[:200], meta=_meta("docs")))
    if not chunks:
        return [Chunk(text[:12000], source, rel_path, file_type, symbol=stem,
                      section="raw", meta=_meta("docs"))]
    return chunks


# =============================================================================
# JSON (asmdef, manifest, packages-lock) and YAML (prefab / scene / asset)
# =============================================================================
def chunk_json(text: str, rel_path: str, source: str = "project") -> list[Chunk]:
    stem = Path(rel_path).stem
    try:
        obj = json.loads(text)
    except json.JSONDecodeError:
        return [Chunk(text[:12000], source, rel_path, "json", symbol=stem,
                      section="raw", meta=_meta("json"))]
    chunks = []
    if isinstance(obj, dict):
        # asmdef / manifest / lock: one chunk per top-level key keeps `references`,
        # `dependencies` and `name` separately addressable.
        for key, val in obj.items():
            rendered = json.dumps({key: val}, ensure_ascii=False, indent=2)
            chunks.append(Chunk(rendered[:12000], source, rel_path, "json",
                                symbol=str(key), section="property", meta=_meta("json")))
    else:
        chunks.append(Chunk(json.dumps(obj, ensure_ascii=False, indent=2)[:12000],
                            source, rel_path, "json", symbol=stem, section="root",
                            meta=_meta("json")))
    return chunks


RE_YAML_DOC = re.compile(r"^---\s*!u!(\d+)\s*&(\d+)(.*)$", re.M)

# classID -> name, for the `--- !u!<id>` header of every Unity YAML document. Only the
# ids a game scene actually contains: without this, a chunk is labelled `object:114` and
# neither the model nor `unity_rag_search` can tell a Rigidbody from an AudioSource.
YAML_CLASS_IDS = {
    "1": "GameObject", "4": "Transform", "224": "RectTransform",
    "20": "Camera", "21": "Material", "23": "MeshRenderer", "33": "MeshFilter",
    "43": "Mesh", "54": "Rigidbody", "64": "MeshCollider", "65": "BoxCollider",
    "81": "AudioListener", "82": "AudioSource", "95": "Animator",
    "104": "RenderSettings", "108": "Light", "111": "Animation",
    "114": "MonoBehaviour", "115": "MonoScript", "135": "SphereCollider",
    "136": "CapsuleCollider", "143": "CharacterController",
    "156": "TerrainCollider", "157": "LightmapSettings", "196": "NavMeshAgent",
    "198": "ParticleSystem", "199": "ParticleSystemRenderer",
    "208": "NavMeshObstacle", "212": "SpriteRenderer", "222": "CanvasRenderer",
    "223": "Canvas", "225": "CanvasGroup",
}


def chunk_unity_yaml(text: str, rel_path: str, source: str = "project") -> list[Chunk]:
    """`.unity` / `.prefab` / `.asset` / `.mat` are Unity's YAML, one `--- !u!<class> &<id>`
    document per object. Chunk per document and label it with `m_Name` when present."""
    stem = Path(rel_path).stem
    matches = list(RE_YAML_DOC.finditer(text))
    if not matches:
        return [Chunk(text[:12000], source, rel_path, "unityyaml", symbol=stem,
                      section="raw", meta=_meta("unityyaml"))]
    chunks = []
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[m.start():end].strip()
        if len(body) < 40:
            continue
        class_id = m.group(1)
        name_match = re.search(r"^\s*m_Name:\s*(.+)$", body, re.M)
        kind = YAML_CLASS_IDS.get(class_id, f"object:{class_id}")
        # Most components carry no `m_Name` (only GameObject does), so the fallback uses
        # the class name and the file id - `Main:Transform:1234` is searchable, `!u!4`
        # is not, and "find me the Transform in this scene" is a normal request.
        name = name_match.group(1).strip() if name_match else f"{kind}:{m.group(2)}"
        chunks.append(Chunk(
            text=f"# {rel_path}\n# Unity {config.UNITY_VERSION} asset\n# {kind} {name}\n\n{body[:12000]}",
            source=source, path=rel_path, file_type="unityyaml",
            symbol=f"{stem}:{name}", class_name=kind, section="document",
            meta=_meta("unityyaml")))
    return chunks or [Chunk(text[:12000], source, rel_path, "unityyaml", symbol=stem,
                            section="raw", meta=_meta("unityyaml"))]


RE_SHADER_BLOCK = re.compile(
    r"^\s*(Shader\s+\"[^\"]+\"|SubShader|Pass|CGPROGRAM|HLSLPROGRAM|ENDCG|ENDHLSL)\b[^\n]*",
    re.M)


def chunk_shader(text: str, rel_path: str, source: str = "project") -> list[Chunk]:
    """ShaderLab: `Shader`/`SubShader`/`Pass` are brace blocks, `CGPROGRAM` is a
    `#include`-style region terminated by `ENDCG` - the brace walker cannot see the
    latter, so it gets its own end rule."""
    stem = Path(rel_path).stem
    blocks: list[Chunk] = []
    for m in RE_SHADER_BLOCK.finditer(text):
        head = m.group(1)
        if head in ("CGPROGRAM", "HLSLPROGRAM"):
            end_kw = "ENDCG" if head == "CGPROGRAM" else "ENDHLSL"
            j = text.find(end_kw, m.start())
            end = len(text) if j < 0 else j + len(end_kw)
        else:
            end = _cs_block_end(text, m.start())
        body = text[m.start():end][:12000]
        if len(body.strip()) < 20:
            continue
        blocks.append(Chunk(body, source, rel_path, "shader",
                            symbol=f"{stem}:{head[:40]}", section="block", meta=_meta("shader")))
    return blocks or [Chunk(text[:12000], source, rel_path, "shader", symbol=stem,
                            section="raw", meta=_meta("shader"))]


def chunk_file(path: Path, rel_path: str, source: str) -> list[Chunk]:
    suffix = path.suffix.lower()
    text = path.read_text(encoding="utf-8", errors="replace")
    if suffix == ".cs":
        return chunk_csharp(text, rel_path, source)
    if suffix in {".html", ".htm"}:
        return chunk_html(text, rel_path, source)
    if suffix in {".md", ".txt"}:
        return chunk_markdown(text, rel_path, source, file_type=suffix.lstrip("."))
    if suffix in {".json", ".asmdef", ".asmref"}:
        return chunk_json(text, rel_path, source)
    if suffix in {".unity", ".prefab", ".asset", ".mat", ".controller", ".yaml", ".yml"}:
        return chunk_unity_yaml(text, rel_path, source)
    if suffix in {".shader", ".compute", ".cginc", ".hlsl", ".glsl"}:
        return chunk_shader(text, rel_path, source)
    return [Chunk(text[:12000], source, rel_path, suffix.lstrip(".") or "txt",
                  symbol=Path(rel_path).stem, section="raw", meta=_meta("text"))]
