"""Semantic chunking для Godot-корпуса.

Единица индекса — не «500 токенов», а смысловой элемент:
  * GDScript  -> заголовок файла + отдельные функции/классы
  * .tscn     -> нормализованный документ сцены + отдельные узлы
  * .tres     -> ресурс
  * class ref -> один член класса (метод/свойство/сигнал/константа) = один chunk
  * tutorial  -> секция по заголовку

Любой chunk несёт metadata, пригодную для фильтров Qdrant/FTS.
"""
from __future__ import annotations

import hashlib
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field, asdict
from pathlib import Path

ENGINE_VERSION = "4.7"


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
    engine_version: str = ENGINE_VERSION
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
        d["text"] = self.text
        return d


# --------------------------------------------------------------------------
# GDScript
# --------------------------------------------------------------------------

_RE_CLASS_NAME = re.compile(r"^class_name\s+([A-Za-z_][\w]*)", re.M)
_RE_EXTENDS = re.compile(r"^extends\s+([A-Za-z_][\w\.]*)", re.M)
_RE_INNER_CLASS = re.compile(r"^class\s+([A-Za-z_][\w]*)\s*:", re.M)
_RE_SIGNAL = re.compile(r"^\s*signal\s+([A-Za-z_][\w]*)\s*(\([^)]*\))?", re.M)
_RE_FUNC = re.compile(r"^([ \t]*)func\s+([A-Za-z_][\w]*)\s*(\([^)]*\))\s*(->\s*[^:\n]+)?\s*:", re.M)
_RE_VAR = re.compile(
    r"^([ \t]*)(@export[^\n]*?)?\s*(?:@onready\s+)?var\s+([A-Za-z_][\w]*)\s*(?::\s*([A-Za-z_][\w\.\[\]]*))?\s*(?:=\s*([^\n]+))?",
    re.M,
)
_RE_CONST = re.compile(r"^([ \t]*)const\s+([A-Za-z_][\w]*)\s*(?::\s*([A-Za-z_][\w\.]*))?\s*=\s*([^\n]+)", re.M)
_RE_ENUM = re.compile(r"^([ \t]*)enum\s+([A-Za-z_][\w]*)?\s*\{([^}]*)\}", re.M | re.S)
_RE_DOC = re.compile(r"^([ \t]*)##\s?(.*)$", re.M)
_RE_COMMENT = re.compile(r"^([ \t]*)#\s?(.*)$", re.M)


def _leading_doc_comment(src: str, decl_start: int) -> str:
    """Собрать ##-комментарии непосредственно перед объявлением."""
    before = src[:decl_start]
    lines = before.splitlines()
    out: list[str] = []
    for ln in reversed(lines):
        s = ln.strip()
        if s.startswith("##"):
            out.append(s[2:].strip())
        elif s == "" and not out:
            continue
        elif s.startswith("#"):
            out.append(s[1:].strip())
        else:
            break
    return "\n".join(reversed(out)).strip()


def _block_end(src: str, decl_end: int, indent: str) -> int:
    """Конец блока по отступу: первая непустая строка с отступом <= decl indent."""
    lines = src[decl_end:].splitlines(keepends=True)
    pos = decl_end
    base = len(indent)
    for ln in lines:
        pos += len(ln)
        if not ln.strip():
            continue
        cur = len(ln) - len(ln.lstrip(" \t"))
        if cur <= base:
            return pos - len(ln)
    return len(src)


def chunk_gdscript(text: str, rel_path: str, source: str = "project") -> list[Chunk]:
    chunks: list[Chunk] = []
    class_name = (_RE_CLASS_NAME.search(text) or [None, ""])[1] if _RE_CLASS_NAME.search(text) else ""
    extends = ""
    m = _RE_EXTENDS.search(text)
    if m:
        extends = m.group(1)

    # --- шапка файла: сигналы, экспорты, константы, enum'ы, класс-комментарий
    header_bits: list[str] = [f"# GDScript file: {rel_path}"]
    if class_name:
        header_bits.append(f"class_name {class_name}")
    if extends:
        header_bits.append(f"extends {extends}")

    sig_lines = []
    for sm in _RE_SIGNAL.finditer(text):
        doc = _leading_doc_comment(text, sm.start())
        sig_lines.append(f"signal {sm.group(1)}{sm.group(2) or '()'}" + (f"  ## {doc}" if doc else ""))
    if sig_lines:
        header_bits.append("signals:\n" + "\n".join("  " + s for s in sig_lines))

    const_lines = [f"const {c.group(2)}{(': ' + c.group(3)) if c.group(3) else ''} = {c.group(4).strip()}"
                   for c in _RE_CONST.finditer(text)]
    if const_lines:
        header_bits.append("constants:\n" + "\n".join("  " + s for s in const_lines))

    enum_lines = []
    for em in _RE_ENUM.finditer(text):
        name = em.group(2) or "(anonymous)"
        enum_lines.append(f"enum {name} {{ {' '.join(em.group(3).split())} }}")
    if enum_lines:
        header_bits.append("enums:\n" + "\n".join("  " + s for s in enum_lines))

    var_lines = []
    for vm in _RE_VAR.finditer(text):
        if vm.group(1) and len(vm.group(1)) > 0:
            continue  # только top-level (без отступа) попадает в шапку
        name = vm.group(3)
        if name in ("_init",):
            continue
        typ = f": {vm.group(4)}" if vm.group(4) else ""
        exp = "@export " if (vm.group(2) or "").strip().startswith("@export") else ""
        var_lines.append(f"{exp}var {name}{typ}")
    if var_lines:
        header_bits.append("variables:\n" + "\n".join("  " + s for s in var_lines))

    header = "\n".join(header_bits)
    if len(header) > 80:
        chunks.append(Chunk(
            text=header, source=source, path=rel_path, file_type="gdscript",
            symbol=f"{class_name or Path(rel_path).stem}:header",
            class_name=class_name, extends=extends, section="header",
        ))

    # --- функции
    for fm in _RE_FUNC.finditer(text):
        indent, name, args, ret = fm.group(1), fm.group(2), fm.group(3), fm.group(4) or ""
        start = fm.start()
        body_end = _block_end(text, fm.end(), indent)
        body = text[start:body_end].rstrip()
        if len(body) > 12000:
            body = body[:12000] + "\n# ... truncated"
        doc = _leading_doc_comment(text, start)
        head = f"# {rel_path}\n"
        if class_name:
            head += f"class {class_name} extends {extends}\n" if extends else f"class {class_name}\n"
        elif extends:
            head += f"extends {extends}\n"
        head += f"\nfunc {name}{args}{ret}:"
        if doc:
            head += f"\n## {doc}"
        chunks.append(Chunk(
            text=head + "\n" + body,
            source=source, path=rel_path, file_type="gdscript",
            symbol=f"{class_name or Path(rel_path).stem}.{name}",
            class_name=class_name, extends=extends, section="function",
        ))

    if not chunks:
        chunks.append(Chunk(text=text[:8000], source=source, path=rel_path,
                            file_type="gdscript", symbol=Path(rel_path).stem, section="raw"))
    return chunks


# --------------------------------------------------------------------------
# Godot scene / resource (.tscn / .tres)
# --------------------------------------------------------------------------

_RE_SECTION = re.compile(r"^\[(?P<tag>\w+)(?P<attrs>[^\]]*)\]\s*$")
_RE_ATTR = re.compile(r'(\w+)=("(?:[^"\\]|\\.)*"|[\w\.\-]+)')


def _parse_attrs(raw: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for m in _RE_ATTR.finditer(raw):
        v = m.group(2)
        if v.startswith('"'):
            v = v[1:-1]
        out[m.group(1)] = v
    return out


def _tscn_sections(text: str) -> list[tuple[str, dict[str, str], list[str]]]:
    """Разбить файл на секции: (tag, attrs, body_lines)."""
    sections: list[tuple[str, dict[str, str], list[str]]] = []
    cur_tag, cur_attrs, cur_body = "", {}, []
    for line in text.splitlines():
        m = _RE_SECTION.match(line.strip())
        if m:
            if cur_tag:
                sections.append((cur_tag, cur_attrs, cur_body))
            cur_tag = m.group("tag")
            cur_attrs = _parse_attrs(m.group("attrs"))
            cur_body = []
        elif cur_tag:
            if line.strip():
                cur_body.append(line)
    if cur_tag:
        sections.append((cur_tag, cur_attrs, cur_body))
    return sections


def chunk_scene(text: str, rel_path: str, source: str = "project") -> list[Chunk]:
    sections = _tscn_sections(text)
    ext_res: dict[str, tuple[str, str]] = {}
    nodes: list[tuple[str, str, str, list[str]]] = []  # name, type, fullpath, body

    for tag, attrs, body in sections:
        if tag == "ext_resource":
            ext_res[attrs.get("id", "")] = (attrs.get("type", ""), attrs.get("path", ""))
        elif tag == "node":
            name = attrs.get("name", "?")
            ntype = attrs.get("type", attrs.get("instance", "?"))
            parent = attrs.get("parent", "")
            full = name if parent in ("", ".") else f"{parent}/{name}"
            full = full.replace("./", "")
            nodes.append((name, ntype, full, body))

    # --- нормализованный документ сцены
    lines = [f"# Scene: {rel_path}", f"# Godot scene tree ({len(nodes)} nodes)", "", "Nodes:"]
    for name, ntype, full, body in nodes:
        depth = full.count("/")
        script = ""
        for b in body:
            if b.strip().startswith("script = ExtResource("):
                rid = re.search(r'ExtResource\("([^"]+)"\)', b)
                if rid and rid.group(1) in ext_res:
                    script = ext_res[rid.group(1)][1]
        lines.append(f"{'  ' * depth}- {full} : {ntype}" + (f"   [script={script}]" if script else ""))

    summary = "\n".join(lines)
    chunks.append(Chunk(
        text=summary, source=source, path=rel_path,
        file_type="scene" if rel_path.endswith(".tscn") else "resource",
        symbol=Path(rel_path).stem, scene_path=rel_path, section="scene_tree",
        meta={"node_count": len(nodes)},
    ))

    # --- отдельные узлы
    for name, ntype, full, body in nodes:
        props = "\n".join("  " + b.strip() for b in body)
        txt = f"# Scene: {rel_path}\nNode: {full}\nType: {ntype}\nParent path: {full.rsplit('/', 1)[0] if '/' in full else '.'}\n"
        if props:
            txt += "Properties:\n" + props
        chunks.append(Chunk(
            text=txt, source=source, path=rel_path,
            file_type="scene_node", symbol=f"{Path(rel_path).stem}:{full}",
            node_type=ntype, scene_path=rel_path, node_path=full, section="node",
        ))
    return chunks


def chunk_tres(text: str, rel_path: str, source: str = "project") -> list[Chunk]:
    sections = _tscn_sections(text)
    head = []
    for tag, attrs, body in sections:
        if tag in ("gd_resource", "gd_scene"):
            head.append(f"{tag}: {attrs}")
        elif tag == "ext_resource":
            head.append(f"ext_resource: {attrs.get('type')} {attrs.get('path')}")
        elif tag == "sub_resource":
            head.append(f"sub_resource: {attrs.get('type')} id={attrs.get('id')}")
        elif tag == "resource":
            head.append("resource props:\n" + "\n".join("  " + b.strip() for b in body))
    return [Chunk(
        text=f"# Resource: {rel_path}\n" + "\n".join(head),
        source=source, path=rel_path, file_type="resource",
        symbol=Path(rel_path).stem, section="resource",
    )]


# --------------------------------------------------------------------------
# Godot class reference XML
# --------------------------------------------------------------------------

def _xml_text(el: ET.Element | None) -> str:
    if el is None:
        return ""
    return " ".join("".join(el.itertext()).split())


def _bbcode_clean(s: str) -> str:
    s = re.sub(r"\[/?codeblocks?\]", "", s)
    s = re.sub(r"\[/?code\]", "`", s)
    s = re.sub(r"\[/?b\]", "", s)
    s = re.sub(r"\[/?i\]", "", s)
    s = re.sub(r"\[url[^\]]*\]", "", s)
    s = re.sub(r"\[/url\]", "", s)
    s = re.sub(r"\[method\s+([^\]]+)\]", r"\1()", s)
    s = re.sub(r"\[member\s+([^\]]+)\]", r"\1", s)
    s = re.sub(r"\[signal\s+([^\]]+)\]", r"\1", s)
    s = re.sub(r"\[constant\s+([^\]]+)\]", r"\1", s)
    s = re.sub(r"\[param\s+([^\]]+)\]", r"\1", s)
    s = re.sub(r"\[[^\]]+\]", "", s)
    return s.strip()


def chunk_class_ref(xml_text: str, rel_path: str, source: str = "official_docs") -> list[Chunk]:
    chunks: list[Chunk] = []
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return chunks
    cname = root.get("name", "")
    inherits = root.get("inherits", "")
    brief = _bbcode_clean(_xml_text(root.find("brief_description")))
    desc = _bbcode_clean(_xml_text(root.find("description")))

    chunks.append(Chunk(
        text=f"# Godot {ENGINE_VERSION} class reference: {cname}\nInherits: {inherits}\n\n{brief}\n\n{desc}"[:8000],
        source=source, path=rel_path, file_type="class_ref",
        symbol=cname, class_name=cname, extends=inherits, section="class_description",
    ))

    def _member_block(name: str, kind: str, extra: str, body: str) -> str:
        return (
            f"# Godot {ENGINE_VERSION} :: {cname} :: {kind} {name}\n"
            f"Class: {cname} (inherits {inherits})\n{extra}\n\n{body}"
        )

    for m in root.findall("./methods/method"):
        name = m.get("name", "")
        ret = m.find("return")
        ret_type = ret.get("type", "void") if ret is not None else "void"
        args = []
        for a in m.findall("param"):
            args.append(f"{a.get('name')}: {a.get('type')}" + (f" = {a.get('default')}" if a.get("default") else ""))
        doc = _bbcode_clean(_xml_text(m.find("description")))
        extra = f"Signature: {cname}.{name}({', '.join(args)}) -> {ret_type}"
        if m.get("qualifiers"):
            extra += f"\nQualifiers: {m.get('qualifiers')}"
        chunks.append(Chunk(
            text=_member_block(name, "method", extra, doc)[:8000],
            source=source, path=rel_path, file_type="class_ref",
            symbol=f"{cname}.{name}", class_name=cname, extends=inherits, section="method",
            meta={"return_type": ret_type, "args": args},
        ))

    for m in root.findall("./members/member"):
        name = m.get("name", "")
        extra = (f"Property: {cname}.{name}: {m.get('type')}"
                 + (f" = {m.get('default')}" if m.get("default") else "")
                 + f"\nSetter: {m.get('setter')}  Getter: {m.get('getter')}")
        chunks.append(Chunk(
            text=_member_block(name, "property", extra, _bbcode_clean(_xml_text(m)))[:8000],
            source=source, path=rel_path, file_type="class_ref",
            symbol=f"{cname}.{name}", class_name=cname, extends=inherits, section="property",
        ))

    for s in root.findall("./signals/signal"):
        name = s.get("name", "")
        args = ", ".join(f"{a.get('name')}: {a.get('type')}" for a in s.findall("param"))
        extra = f"Signal: {cname}.{name}({args})"
        chunks.append(Chunk(
            text=_member_block(name, "signal", extra, _bbcode_clean(_xml_text(s.find("description"))))[:8000],
            source=source, path=rel_path, file_type="class_ref",
            symbol=f"{cname}.{name}", class_name=cname, extends=inherits, section="signal",
        ))

    for c in root.findall("./constants/constant"):
        name = c.get("name", "")
        extra = f"Constant: {cname}.{name} = {c.get('value')}  (enum {c.get('enum')})" if c.get("enum") else f"Constant: {cname}.{name} = {c.get('value')}"
        chunks.append(Chunk(
            text=_member_block(name, "constant", extra, _bbcode_clean(_xml_text(c)))[:4000],
            source=source, path=rel_path, file_type="class_ref",
            symbol=f"{cname}.{name}", class_name=cname, extends=inherits, section="constant",
        ))

    for a in root.findall("./annotations/annotation"):
        name = a.get("name", "")
        extra = f"Annotation: @{name}"
        chunks.append(Chunk(
            text=_member_block(name, "annotation", extra, _bbcode_clean(_xml_text(a)))[:4000],
            source=source, path=rel_path, file_type="class_ref",
            symbol=f"@{name}", class_name=cname, extends=inherits, section="annotation",
        ))
    return chunks


# --------------------------------------------------------------------------
# Markdown / произвольный текст
# --------------------------------------------------------------------------

_RE_HEADING = re.compile(r"^(#{1,6})\s+(.*)$", re.M)


def chunk_markdown(text: str, rel_path: str, source: str = "official_docs", file_type: str = "tutorial") -> list[Chunk]:
    chunks: list[Chunk] = []
    marks = list(_RE_HEADING.finditer(text))
    if not marks:
        return [Chunk(text=text[:8000], source=source, path=rel_path, file_type=file_type,
                      symbol=Path(rel_path).stem, section="body")]

    title = marks[0].group(2).strip()
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        body = text[m.start():end].strip()
        if len(body) < 40:
            continue
        heading = m.group(2).strip()
        chunks.append(Chunk(
            text=f"# {title}\n## {heading}\n\n{body}"[:8000],
            source=source, path=rel_path, file_type=file_type,
            symbol=heading, section=heading,
        ))
    if not chunks:
        chunks.append(Chunk(text=text[:8000], source=source, path=rel_path,
                            file_type=file_type, symbol=Path(rel_path).stem, section="body"))
    return chunks


_RST_UNDERLINE = re.compile(r"^(=+|-+|~+|\^+|\*+|\"+|#+)\s*$")


def _rst_sections(text: str) -> list[tuple[int, str, str]]:
    """RST-заголовки: строка + подчёркивание. Возвращает (offset, level, title)."""
    lines = text.splitlines()
    offsets: list[int] = []
    pos = 0
    for ln in lines:
        offsets.append(pos)
        pos += len(ln) + 1
    out: list[tuple[int, str, str]] = []
    order: dict[str, int] = {}
    for i in range(len(lines) - 1):
        title = lines[i].strip()
        under = lines[i + 1].strip()
        if (title and under and len(under) >= max(3, len(title) - 2)
                and _RST_UNDERLINE.match(under) and not title.startswith("..")):
            ch = under[0]
            if ch not in order:
                order[ch] = len(order)
            out.append((offsets[i], order[ch], title))
    return out


def chunk_rst(text: str, rel_path: str, source: str = "official_docs", file_type: str = "tutorial") -> list[Chunk]:
    """RST-документация Godot: режем по секциям, чистим директивы."""
    # выкинуть Sphinx-директивы и мета-блоки
    text = re.sub(r"^\s*\.\.\s+(?:\w[\w-]*::.*(?:\n(?:\s{3,}.*|\s*$))*)+", "", text, flags=re.M)
    text = re.sub(r"^\s*:[\w-]+:.*$", "", text, flags=re.M)
    text = re.sub(r":ref:`([^<`]+)<[^>`]+>`", r"\1", text)
    text = re.sub(r":ref:`([^`]+)`", r"\1", text)
    text = re.sub(r":doc:`([^<`]+)<[^>`]+>`", r"\1", text)
    text = re.sub(r"\|[^|]+\|", "", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)

    marks = _rst_sections(text)
    if not marks:
        return [Chunk(text=text[:8000], source=source, path=rel_path, file_type=file_type,
                      symbol=Path(rel_path).stem, section="body")]

    doc_title = marks[0][2]
    chunks: list[Chunk] = []
    for i, (off, level, title) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        body = text[off:end].strip()
        if len(body) < 60:
            continue
        chunks.append(Chunk(
            text=f"# {doc_title}\n## {title}\n\n{body}"[:8000],
            source=source, path=rel_path, file_type=file_type,
            symbol=title, section=title, meta={"level": level},
        ))
    if not chunks:
        chunks.append(Chunk(text=text[:8000], source=source, path=rel_path,
                            file_type=file_type, symbol=Path(rel_path).stem, section="body"))
    return chunks


def chunk_plain(text: str, rel_path: str, source: str = "cookbook", file_type: str = "cookbook") -> list[Chunk]:
    if rel_path.endswith((".md", ".markdown")):
        return chunk_markdown(text, rel_path, source, file_type)
    if rel_path.endswith(".rst"):
        return chunk_rst(text, rel_path, source, file_type)
    return [Chunk(text=text[:8000], source=source, path=rel_path, file_type=file_type,
                  symbol=Path(rel_path).stem, section="body")]


# --------------------------------------------------------------------------
# Диспетчер
# --------------------------------------------------------------------------

def chunk_file(path: Path, rel_path: str, source: str) -> list[Chunk]:
    suffix = path.suffix.lower()
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []

    if suffix == ".gd" or suffix == ".cs":
        return chunk_gdscript(raw, rel_path, source)
    if suffix == ".tscn":
        return chunk_scene(raw, rel_path, source)
    if suffix in (".tres", ".godot"):
        return chunk_tres(raw, rel_path, source) if suffix == ".tres" else chunk_plain(raw, rel_path, source, "project_config")
    if suffix in (".gdshader", ".shader", ".gdshaderinc"):
        return [Chunk(text=f"# Shader: {rel_path}\n{raw[:8000]}", source=source, path=rel_path,
                      file_type="shader", symbol=Path(rel_path).stem, section="shader")]
    if suffix in (".md", ".markdown"):
        # Знания о внешних ассетах — не «cookbook» по смыслу: это источники,
        # лицензии и политика. Отдельный file_type нужен, чтобы фильтр по типу
        # не выдавал их за примеры кода проекта.
        if source == "official_docs":
            ft = "tutorial"
        elif source == "external_assets":
            ft = "asset_knowledge"
        else:
            ft = "cookbook"
        return chunk_markdown(raw, rel_path, source, ft)
    if suffix == ".rst":
        return chunk_rst(raw, rel_path, source,
                         "tutorial" if source == "official_docs" else "cookbook")
    return chunk_plain(raw, rel_path, source)
