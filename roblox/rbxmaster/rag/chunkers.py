"""Semantic chunking for Roblox: Luau, Engine API markdown, guides, Rojo JSON, place XML.

The Luau chunker is the reason this module exists. Everything else is the same shape as
the Three.js / Godot / Unity chunkers: one chunk per declaration, with a header line that
carries the path and the pinned corpus version so a stale hit is obvious in the result.
"""
from __future__ import annotations

import hashlib
import json
import re
import xml.etree.ElementTree as ET
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
    member_kind: str = ""
    context: str = ""          # server | client | shared
    section: str = ""
    engine_version: str = config.RBX_VERSION
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


def _meta(kind: str, **extra) -> dict:
    d = {"framework": config.RBX_FRAMEWORK_TAG, "version": config.RBX_VERSION, "kind": kind}
    d.update({k: v for k, v in extra.items() if v})
    return d


# =============================================================================
# Front matter (every official page carries YAML: name, type, last_updated, ...)
# =============================================================================
RE_FM = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)


def split_front_matter(text: str) -> tuple[dict, str]:
    """`(front_matter, body)`. The YAML here is a flat key/value map plus `- item` lists."""
    m = RE_FM.match(text)
    if not m:
        return {}, text
    data: dict = {}
    key = ""
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(("  - ", "- ")):
            if key:
                data.setdefault(key, [])
                if isinstance(data[key], list):
                    data[key].append(line.split("- ", 1)[1].strip().strip('"'))
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            if val == "":
                data[key] = []
            elif val.startswith("[") and val.endswith("]"):
                data[key] = [x.strip().strip('"') for x in val[1:-1].split(",") if x.strip()]
            else:
                data[key] = val.strip('"')
    return data, text[m.end():]


# =============================================================================
# Luau
# =============================================================================
# `local function foo`, `function Class:Method`, `function Class.Method`, `function foo`
RE_LUAU_FUNC = re.compile(
    r"^[ \t]*(?:local[ \t]+)?function[ \t]+([A-Za-z_][\w]*(?:[.:][A-Za-z_][\w]*)*)[ \t]*(?:<[^>\n]*>)?[ \t]*\(",
    re.M)
# `local handler = function(...)` and `local M.foo = function(...)`
RE_LUAU_FN_ASSIGN = re.compile(
    r"^[ \t]*local[ \t]+([A-Za-z_][\w]*(?:[.:][A-Za-z_][\w]*)*)[ \t]*(?::[^=\n]+)?=[ \t]*function[ \t]*\(",
    re.M)
# `type Foo = ...`, `export type Foo<T> = ...`
RE_LUAU_TYPE = re.compile(
    r"^[ \t]*(?:export[ \t]+)?type[ \t]+([A-Za-z_][\w]*)[ \t]*(?:<[^>\n]*>)?[ \t]*=", re.M)
# A declaration boundary: anything that starts a new top-level statement.
RE_LUAU_TOP = re.compile(
    r"^[ \t]*(?:local[ \t]+(?:function[ \t]+)?[\w]+|function[ \t]+|export[ \t]+type[ \t]+|"
    r"type[ \t]+|return\b|end\b|--\[\[)", re.M)


def _skip_long_bracket(src: str, i: int) -> int:
    """`[[`, `[=[`, `[==[` ... -> index just past the matching close, or -1.

    Called with `src[i] == '['`. Returns -1 when this is not a long bracket at all (a
    plain `[` index expression), so the caller can fall through to normal scanning.
    """
    n = len(src)
    j = i + 1
    level = 0
    while j < n and src[j] == "=":
        level += 1
        j += 1
    if j >= n or src[j] != "[":
        return -1
    close = "]" + "=" * level + "]"
    k = src.find(close, j + 1)
    return n if k < 0 else k + len(close)


def _luau_block_end(src: str, start: int) -> int:
    """Index just past the block that the declaration at `start` opens.

    Luau block structure is `function/if/for/while/do/repeat` ... `end`/`until`. A naive
    `src.find("end")` is wrong for the same reason it is wrong in every language: `end`
    is a common substring (`send`, `PlayerAdded` no, but `append`, `-- end of file`).
    So this walks tokens, skipping `--` line comments, `--[[ ]]` block comments and all
    four string forms (`"`, `'`, `[[`, `[=[`).

    `do` is counted as an opener ONLY when it is not the `do` of a `for`/`while` header,
    which is tracked with `pending_do` - otherwise `for i = 1, 10 do` would count twice
    and every loop would eat the rest of the file.
    """
    n = len(src)
    i = start
    depth = 0
    pending_do = False
    while i < n:
        ch = src[i]
        if ch == "-" and i + 1 < n and src[i + 1] == "-":
            if i + 2 < n and src[i + 2] == "[":
                j = _skip_long_bracket(src, i + 2)
                if j > 0:
                    i = j
                    continue
            j = src.find("\n", i)
            i = n if j < 0 else j + 1
            continue
        if ch in ('"', "'"):
            quote = ch
            i += 1
            while i < n:
                c = src[i]
                if c == "\\":
                    i += 2
                    continue
                if c == quote:
                    i += 1
                    break
                if c == "\n":          # unterminated string: do not swallow the file
                    break
                i += 1
            continue
        if ch == "[":
            j = _skip_long_bracket(src, i)
            if j > 0:
                i = j
                continue
            i += 1
            continue
        if ch.isalpha() or ch == "_":
            j = i
            while j < n and (src[j].isalnum() or src[j] == "_"):
                j += 1
            word = src[i:j]
            if word in ("function", "if"):
                depth += 1
            elif word in ("for", "while"):
                depth += 1
                pending_do = True
            elif word == "do":
                if pending_do:
                    pending_do = False
                else:
                    depth += 1
            elif word == "repeat":
                depth += 1
            elif word == "until":
                depth -= 1
            elif word == "end":
                depth -= 1
                if depth <= 0:
                    return j
            i = j
            continue
        i += 1
    return n


def _luau_type_end(src: str, start: int) -> int:
    """End of a `type X = ...` alias.

    Table types are brace-matched; a union/intersection alias runs until the next line
    that starts a new top-level statement.
    """
    eq = src.find("=", start)
    if eq < 0:
        return min(len(src), start + 200)
    i = eq + 1
    n = len(src)
    while i < n and src[i] in " \t":
        i += 1
    if i < n and src[i] in "{(":
        opener = src[i]
        closer = "}" if opener == "{" else ")"
        depth = 0
        j = i
        while j < n:
            c = src[j]
            if c == "-" and j + 1 < n and src[j + 1] == "-":
                k = src.find("\n", j)
                j = n if k < 0 else k + 1
                continue
            if c in ('"', "'"):
                q = c
                j += 1
                while j < n and src[j] != q:
                    j += 2 if src[j] == "\\" else 1
                j += 1
                continue
            if c == opener:
                depth += 1
            elif c == closer:
                depth -= 1
                if depth == 0:
                    return j + 1
            j += 1
        return n
    # Union / function type: stop before the next top-level statement.
    m = RE_LUAU_TOP.search(src, i)
    end = m.start() if m else n
    # A blank line also ends it - aliases are not separated from the next one by anything
    # else in practice, and swallowing a following helper function is worse.
    blank = re.search(r"\n[ \t]*\n", src[i:end])
    if blank:
        end = i + blank.start() + 1
    return max(i, min(end, i + 4000))


def _leading_comments(src: str, start: int, max_lines: int = 8) -> str:
    """The contiguous `--` comment block directly above a declaration (doc comments)."""
    lines = src[:start].splitlines()
    out: list[str] = []
    for line in reversed(lines[-max_lines:]):
        s = line.strip()
        if s.startswith("--") and not s.startswith("--[[") and not s.startswith("--[["):
            out.append(s)
        elif not s:
            break
        else:
            break
    return "\n".join(reversed(out))


def _context_of(text: str) -> str:
    """server / client / shared from the prose, for the `context` column.

    Roblox's own docs say it explicitly ("only works when used in a Script" vs "a client
    script"); those two phrases are the reliable signal, everything else is shared.
    """
    low = text.lower()
    if "client script" in low or "localscript" in low:
        if "server script" not in low and "only works when used in a script" not in low:
            return "client"
    if "only works when used in a script" in low or "server script" in low:
        return "server"
    if "localscript" in low:
        return "client"
    return ""


def chunk_luau(text: str, rel_path: str, source: str = "project") -> list[Chunk]:
    """One chunk per function, one per type alias, plus a file header.

    `context` comes from the path (`ServerScriptService/X.server.luau` -> server), never
    from the prose: Luau code does not contain the phrase "server script", so the
    `_context_of` heuristic that the docs use would leave every project chunk blank and
    make `rbx_rag_search(context="server")` return nothing.
    """
    from ..luau.paths import script_context

    stem = Path(rel_path).stem
    ctx = script_context(rel_path, text)
    chunks: list[Chunk] = []

    funcs = [(m.start(), m.group(1)) for m in RE_LUAU_FUNC.finditer(text)]
    assigned = [(m.start(), m.group(1)) for m in RE_LUAU_FN_ASSIGN.finditer(text)]
    types = [(m.start(), m.group(1)) for m in RE_LUAU_TYPE.finditer(text)]

    services = sorted(set(re.findall(r'GetService\(\s*"(\w+)"', text)))
    requires = sorted(set(re.findall(r'require\(\s*([^)\n]{1,80})\)', text)))
    header = [f"# Luau file: {rel_path}", f"# Roblox {config.RBX_VERSION}"]
    if funcs:
        header.append("declarations:\n" + "\n".join(f"  {n}" for _, n in funcs[:40]))
    if types:
        header.append("types:\n" + "\n".join(f"  {n}" for _, n in types[:40]))
    if services:
        header.append("services: " + ", ".join(services[:30]))
    if requires:
        header.append("requires:\n" + "\n".join("  " + r.strip() for r in requires[:30]))
    chunks.append(Chunk("\n".join(header), source, rel_path, "luau",
                        symbol=f"{stem}:header", section="header", member_kind="header",
                        context=ctx, meta=_meta("luau")))

    for start, name in sorted(set(funcs + assigned)):
        end = _luau_block_end(text, start)
        body = text[start:end].strip()
        if len(body) > 12000:
            body = body[:12000] + "\n-- ... truncated"
        doc = _leading_comments(text, start)
        owner, sep, member = name.partition(":") if ":" in name else ("", "", "")
        if not sep:
            owner, _, member = name.partition(".")
        kind = "method" if (sep or "." in name) else "function"
        head = f"# {rel_path}\n# Luau ({config.RBX_VERSION})"
        if owner:
            head += f"\n# {kind} of {owner}"
        chunks.append(Chunk(
            text=(f"{head}\n\n{doc}\n{body}".strip() if doc else f"{head}\n\n{body}"),
            source=source, path=rel_path, file_type="luau", symbol=name,
            class_name=owner, member_kind=kind, section="declaration",
            context=ctx, meta=_meta("luau")))

    for start, name in sorted(set(types)):
        end = _luau_type_end(text, start)
        body = text[start:end].strip()
        doc = _leading_comments(text, start)
        head = f"# {rel_path}\n# Luau type ({config.RBX_VERSION})"
        chunks.append(Chunk(
            text=(f"{head}\n\n{doc}\n{body}".strip() if doc else f"{head}\n\n{body}"),
            source=source, path=rel_path, file_type="luau", symbol=name,
            member_kind="type", section="type", context=ctx, meta=_meta("luau")))

    if len(chunks) == 1 and len(text) > 60:
        # No declarations at all (config module, data table, a script that is one call):
        # one raw chunk so the file is still searchable.
        chunks.append(Chunk(text[:12000], source, rel_path, "luau", symbol=stem,
                            section="raw", member_kind="raw", context=ctx,
                            meta=_meta("luau")))
    return chunks


# =============================================================================
# Engine API / guides markdown
# =============================================================================
RE_HEADING = re.compile(r"^(#{1,6})[ \t]+(.+)$", re.M)
RE_MEMBER_HEAD = re.compile(
    r"^(Method|Event|Property|Callback|Constructor|Datatype|Function|Field|Item):\s*"
    r"([A-Za-z_][\w]*(?:[.:][A-Za-z_][\w]*)*)\s*$")
RE_SIGNATURE = re.compile(r"\*\*Signature:\*\*\s*`([^`]+)`")
# The tag line is `*` … `*` on one line, segments separated by `·`, and it has SEVEN real
# shapes in the corpus - `*Security: … · Thread Safety: …*`, `*Yields · Security: … ·
# Thread Safety: … · Capabilities: …*`, with and without `Simulation Access:`, and so on.
# Two regexes in a row got this wrong: the first demanded `*` right after `Thread Safety`
# and never matched a real page; the second required `Security:` first and lost the 368
# methods that start with `Yields`. So parse the segments, do not pattern-match the shape.
RE_TAG_LINE = re.compile(r"^\*([^*\n]*Thread Safety[^*\n]*)\*", re.M)
RE_ANY_SECURITY = re.compile(r"Security:\s*([A-Za-z ]+)")
# Property and datatype pages carry their contract as a fenced JSON block instead of the
# `*Security: … · Thread Safety: …*` line that methods use. Same facts, other syntax:
#   {"access":"ReadWrite","security":{"read":"None","write":"None"},
#    "thread_safety":"ReadSafe","capabilities":["AvatarAppearance"]}
RE_JSON_BLOCK = re.compile(r"```json\s*(\{.*?\})\s*```", re.S)


def _parse_tag_line(meta: dict, body: str) -> bool:
    """Fill `security`, `thread_safety` and friends from the `*…*` tag line.

    Segments are `key: value` pairs (`Security: None`, `Capabilities: Monetization`) or bare
    flags (`Yields`). Keys become snake_case, so a field the docs add tomorrow lands in meta
    without touching this function. Returns False when there is no tag line at all.
    """
    m = RE_TAG_LINE.search(body)
    if not m:
        return False
    for seg in m.group(1).split("·"):
        seg = seg.strip()
        if not seg:
            continue
        if ":" in seg:
            key, _, val = seg.partition(":")
            key = key.strip().lower().replace(" ", "_")
            if key:
                meta[key] = val.strip()
        else:
            meta[seg.lower().replace(" ", "_")] = "true"
    return True


def _member_meta_from_json(meta: dict, body: str) -> None:
    m = RE_JSON_BLOCK.search(body)
    if not m:
        return
    try:
        info = json.loads(m.group(1))
    except ValueError:
        return
    sec = info.get("security")
    if isinstance(sec, dict):
        read, write = sec.get("read"), sec.get("write")
        meta["security"] = f"read:{read or 'None'} write:{write or 'None'}"
    elif sec:
        meta["security"] = str(sec)
    if info.get("thread_safety"):
        meta["thread_safety"] = str(info["thread_safety"])
    caps = info.get("capabilities")
    if isinstance(caps, list) and caps:
        meta["capabilities"] = ", ".join(str(c) for c in caps)
    if info.get("access"):
        meta["access"] = str(info["access"])


def _fence_mask(text: str) -> list[bool]:
    """True for every line inside a ``` / ~~~ fence.

    Guides are full of Luau snippets whose `--` comments and `#` characters would
    otherwise be read as headings.
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


def _split_headings(text: str, level: int) -> list[tuple[str, str]]:
    """`[(title, body)]` for every heading of exactly `level`, fence-aware."""
    mask = _fence_mask(text)
    line_starts: list[int] = []
    pos = 0
    for line in text.splitlines(keepends=True):
        line_starts.append(pos)
        pos += len(line)

    import bisect

    def line_of(off: int) -> int:
        return min(bisect.bisect_right(line_starts, off) - 1, max(0, len(mask) - 1))

    hits = [m for m in RE_HEADING.finditer(text)
            if len(m.group(1)) == level and not mask[max(0, line_of(m.start()))]]
    out: list[tuple[str, str]] = []
    for i, m in enumerate(hits):
        end = hits[i + 1].start() if i + 1 < len(hits) else len(text)
        out.append((m.group(2).strip(), text[m.end():end].strip()))
    return out


def chunk_api_md(text: str, rel_path: str, source: str = "engine_api") -> list[Chunk]:
    """Engine API Reference page -> one chunk per member, one per `##` group.

    A class page is `# Class: X`, `## Description`, `## Properties`, `## Methods`,
    `## Events`, each member under `### Method: X:Y` with a `**Signature:**` line and a
    `*Security: … · Thread Safety: …*` tag. Splitting per member is the whole point: the
    agent asks "what does `SetNetworkOwner` do", not "show me BasePart".
    """
    fm, body = split_front_matter(text)
    name = str(fm.get("name") or Path(rel_path).stem)
    doc_type = str(fm.get("type") or "page")
    inherits = fm.get("inherits") if isinstance(fm.get("inherits"), list) else []
    summary = str(fm.get("summary") or "")
    url = str(fm.get("url") or "")
    chunks: list[Chunk] = []

    head = [f"# {rel_path}", f"# Roblox {config.RBX_VERSION} ({doc_type})", f"# {name}"]
    if inherits:
        head.append("# inherits " + " -> ".join(str(x) for x in inherits))
    if summary:
        head.append(f"# {summary}")
    # The page intro: everything before the first `##`.
    intro = re.split(r"^## ", body, maxsplit=1, flags=re.M)[0]
    chunks.append(Chunk("\n".join(head) + "\n\n" + intro.strip()[:12000], source, rel_path,
                        "api", symbol=name, class_name=name, member_kind=doc_type,
                        section="overview",
                        meta=_meta("api", url=url, inherits=inherits, doc_type=doc_type)))

    for group_title, group_body in _split_headings(body, 2):
        if group_title.lower().startswith("inherited members"):
            continue                     # a mirror of other pages, pure duplication
        members = _split_headings(group_body, 3)
        if not members:
            if len(group_body.strip()) > 40:
                chunks.append(Chunk(
                    f"# {rel_path}\n# {name}\n\n## {group_title}\n{group_body.strip()[:12000]}",
                    source, rel_path, "api", symbol=f"{name}.{group_title}",
                    class_name=name, member_kind="section", section=group_title[:200],
                    meta=_meta("api", url=url, group=group_title)))
            continue
        for member_title, member_body in members:
            if member_title.startswith("From "):
                continue
            m = RE_MEMBER_HEAD.match(member_title)
            if m:
                kind = m.group(1).lower()
                symbol = m.group(2)
                owner = symbol.split(":")[0].split(".")[0]
            else:
                kind = "section"
                symbol = f"{name}.{member_title}"
                owner = name
            sig = RE_SIGNATURE.search(member_body)
            meta = _meta("api", url=url, group=group_title)
            if sig:
                meta["signature"] = sig.group(1)
            if not _parse_tag_line(meta, member_body):
                alt = RE_ANY_SECURITY.search(member_body)
                if alt:
                    meta["security"] = alt.group(1).strip()
            _member_meta_from_json(meta, member_body)
            chunk_head = f"# {rel_path}\n# {name} ({config.RBX_VERSION})\n# {member_title}"
            if sig:
                chunk_head += f"\n# {sig.group(1)}"
            chunks.append(Chunk(
                f"{chunk_head}\n\n{member_body[:12000]}", source, rel_path, "api",
                symbol=symbol, class_name=owner, member_kind=kind,
                section=group_title[:200], context=_context_of(member_body), meta=meta))
    return chunks


def chunk_markdown(text: str, rel_path: str, source: str = "official_docs",
                   file_type: str = "markdown") -> list[Chunk]:
    """Guides: one chunk per heading, fence-aware, with the front matter kept as meta."""
    fm, body = split_front_matter(text)
    stem = Path(rel_path).stem
    title = str(fm.get("title") or stem)
    url = str(fm.get("url") or "")
    desc = str(fm.get("description") or "")
    mask = _fence_mask(body)
    if not mask:
        mask = [False] * len(body.splitlines())

    line_starts: list[int] = []
    pos = 0
    for line in body.splitlines(keepends=True):
        line_starts.append(pos)
        pos += len(line)

    import bisect

    def line_of(off: int) -> int:
        return min(bisect.bisect_right(line_starts, off) - 1, max(0, len(mask) - 1))

    matches = [m for m in RE_HEADING.finditer(body)
               if len(m.group(1)) <= 3 and not mask[max(0, line_of(m.start()))]]
    if not matches:
        return [Chunk(f"# {rel_path}\n# {title}\n\n{body.strip()[:12000]}", source, rel_path,
                      file_type, symbol=stem, section="raw",
                      meta=_meta("docs", url=url, description=desc))]
    chunks = []
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        part = body[m.start():end].strip()
        if len(part) < 30:
            continue
        head_title = m.group(2).strip()
        chunks.append(Chunk(
            f"# {rel_path}\n# {title} ({config.RBX_VERSION})\n\n{part[:12000]}", source,
            rel_path, file_type, symbol=f"{stem}:{head_title}", class_name=title,
            section=head_title[:200], meta=_meta("docs", url=url, description=desc)))
    if not chunks:
        return [Chunk(f"# {rel_path}\n# {title}\n\n{body.strip()[:12000]}", source, rel_path,
                      file_type, symbol=stem, section="raw",
                      meta=_meta("docs", url=url, description=desc))]
    return chunks


# =============================================================================
# Rojo / Wally JSON, place and model XML
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
        # Rojo `*.project.json`: `name` and `tree` are separately addressable, and the
        # tree is what actually maps folders to services.
        for key, val in obj.items():
            rendered = json.dumps({key: val}, ensure_ascii=False, indent=2)
            chunks.append(Chunk(rendered[:12000], source, rel_path, "json",
                                symbol=f"{stem}.{key}", section=key,
                                meta=_meta("json")))
    else:
        chunks.append(Chunk(json.dumps(obj, ensure_ascii=False, indent=2)[:12000], source,
                            rel_path, "json", symbol=stem, section="root",
                            meta=_meta("json")))
    return chunks


def chunk_toml(text: str, rel_path: str, source: str = "project") -> list[Chunk]:
    """wally.toml / rokit.toml: one chunk per `[section]`."""
    stem = Path(rel_path).stem
    sections: list[tuple[str, list[str]]] = []
    current = ("root", [])
    for line in text.splitlines():
        if re.match(r"^\s*\[[^\]]+\]\s*$", line):
            if current[1]:
                sections.append(current)
            current = (line.strip(" []"), [])
        else:
            current[1].append(line)
    if current[1]:
        sections.append(current)
    return [Chunk(f"# {rel_path}\n# {config.RBX_VERSION}\n[{title}]\n" + "\n".join(body).strip(),
                  source, rel_path, "toml", symbol=f"{stem}:{title}", section=title,
                  meta=_meta("toml"))
            for title, body in sections if "\n".join(body).strip()]


def chunk_place_xml(text: str, rel_path: str, source: str = "project") -> list[Chunk]:
    """`.rbxlx` / `.rbxmx`: one chunk per `<Item>`, labelled with class and Name.

    A place file is the DataModel serialised as XML. Without a per-Item chunk the whole
    place is one 300 KB blob and "where is the script that handles purchases" is
    unanswerable from the corpus - the answer is in one Item.
    """
    stem = Path(rel_path).stem
    try:
        root = ET.fromstring(text)
    except ET.ParseError:
        return [Chunk(text[:12000], source, rel_path, "rbxlx", symbol=stem,
                      section="raw", meta=_meta("place"))]

    chunks: list[Chunk] = []

    def walk(item, depth: int = 0, parent: str = "") -> None:
        cls = item.get("class") or "Item"
        name = ""
        props: list[str] = []
        for props_el in item.findall("Properties"):
            for p in props_el:
                pname = p.get("name") or ""
                val = (p.text or "").strip()
                if pname == "Name":
                    name = val
                elif pname and val:
                    props.append(f"{pname} = {val[:120]}")
        label = name or cls
        symbol = f"{cls}:{label}"
        head = (f"# {rel_path}\n# Roblox {config.RBX_VERSION} place item\n"
                f"# {cls} {label}")
        if parent:
            head += f"\n# under {parent}"
        if props:
            head += "\n# " + "; ".join(props[:20])
        children = [c for c in item.findall("Item")]
        chunks.append(Chunk(
            f"{head}\n\n<class>{cls}</class>\n<name>{label}</name>\n"
            + ("\n".join(props[:60]) if props else ""), source, rel_path, "rbxlx",
            symbol=symbol, class_name=cls, member_kind="instance",
            section=f"depth{depth}", meta=_meta("place", parent=parent or None)))
        for child in children:
            walk(child, depth + 1, symbol)

    for item in root.findall("Item"):
        walk(item)
    if not chunks:
        chunks.append(Chunk(text[:12000], source, rel_path, "rbxlx", symbol=stem,
                            section="raw", meta=_meta("place")))
    return chunks


# =============================================================================
# Dispatch
# =============================================================================
LUAU_EXTS = {".luau", ".lua"}
API_SOURCE = {"engine_api"}


def chunk_file(path: Path, rel_path: str, source: str) -> list[Chunk]:
    suffix = path.suffix.lower()
    text = path.read_text(encoding="utf-8", errors="replace")
    if suffix in LUAU_EXTS:
        return chunk_luau(text, rel_path, source)
    if suffix in {".rbxlx", ".rbxmx", ".rbxmk", ".xml"}:
        return chunk_place_xml(text, rel_path, source)
    if suffix in {".json", ".jsonc"}:
        return chunk_json(text, rel_path, source)
    if suffix == ".toml":
        return chunk_toml(text, rel_path, source)
    if suffix in {".md", ".txt"}:
        if source in API_SOURCE:
            return chunk_api_md(text, rel_path, source)
        return chunk_markdown(text, rel_path, source, file_type=suffix.lstrip("."))
    if suffix in {".yaml", ".yml"}:
        return chunk_markdown(text, rel_path, source, file_type="yaml")
    return [Chunk(text[:12000], source, rel_path, suffix.lstrip(".") or "txt",
                  symbol=Path(rel_path).stem, section="raw", meta=_meta("text"))]
