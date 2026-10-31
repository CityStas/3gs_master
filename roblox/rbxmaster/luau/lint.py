"""Luau lint that needs no external toolchain.

There is no `selene`, `luau-lsp` or `luau-analyze` on this machine, and the ASSET-POLICY
prefers what is already local, so the gate is a small set of rules that catch the mistakes
a model actually makes in Roblox code:

  * structural - an unbalanced `end`, which is what a truncated or half-edited script looks
    like, and which the Studio compiler reports only after you press Play;
  * API-surface - deprecated globals (`wait`, `spawn`, `delay`, `tick`), the two-argument
    `Instance.new`, numeric `require`, `LoadLibrary`;
  * client-server boundary - a server-only service used from a LocalScript, or
    `LocalPlayer` used on the server. Both are `nil`/error at runtime, never at parse time;
  * case - Roblox method names are PascalCase, and `:findFirstChild(` silently returns nil
    because the method does not exist.

This is a linter, not a type checker. It says "this will not work"; it cannot say "this
will not compile". Studio MCP (`execute_luau`, `start_stop_play`) is the real gate for
behaviour, and `check.py` says so in its summary.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from ..rag.chunkers import _skip_long_bracket
from .paths import script_context, source_files

# Roblox API methods, lowercase -> canonical spelling. `method-case` fires ONLY on a name
# that is really an API method written in the wrong case.
#
# The naive version of this rule (`any :lowercase( is an error`) is worse than no rule at
# all: `Shop:total()` and `function Shop.new(): typeof(Shop)` are valid Luau, and the
# second one is a *type annotation*, not even a call. A linter that reddens every real
# project gets switched off, and then it catches nothing. Membership in this table is the
# evidence that the receiver is a Roblox instance and the call will really be nil.
API_METHOD_CASE = {
    # hierarchy / lookup
    "findfirstchild": "FindFirstChild",
    "findfirstchildofclass": "FindFirstChildOfClass",
    "findfirstchildwhichisa": "FindFirstChildWhichIsA",
    "findfirstancestor": "FindFirstAncestor",
    "findfirstancestorofclass": "FindFirstAncestorOfClass",
    "findfirstancestorwhichisa": "FindFirstAncestorWhichIsA",
    "waitforchild": "WaitForChild",
    "getchildren": "GetChildren",
    "getdescendants": "GetDescendants",
    "getservice": "GetService",
    "getfullname": "GetFullName",
    "isdescendantof": "IsDescendantOf",
    "isancestorof": "IsAncestorOf",
    "getdebugid": "GetDebugId",
    "destroy": "Destroy",
    "clone": "Clone",
    "isa": "IsA",
    # attributes / tags / properties
    "getattribute": "GetAttribute",
    "setattribute": "SetAttribute",
    "getattributes": "GetAttributes",
    "getpropertychangedsignal": "GetPropertyChangedSignal",
    "gettags": "GetTags",
    "addtag": "AddTag",
    "removetag": "RemoveTag",
    "hastag": "HasTag",
    # signals
    "connect": "Connect",
    "once": "Once",
    "disconnect": "Disconnect",
    "wait": "Wait",
    # remotes
    "fireserver": "FireServer",
    "fireclient": "FireClient",
    "fireallclients": "FireAllClients",
    "invokeserver": "InvokeServer",
    "invokeclient": "InvokeClient",
    # data stores
    "getasync": "GetAsync",
    "setasync": "SetAsync",
    "updateasync": "UpdateAsync",
    "removeasync": "RemoveAsync",
    "incrementasync": "IncrementAsync",
    "getdatastore": "GetDataStore",
    "getordereddatastore": "GetOrderedDataStore",
    "getmemorystore": "GetMemoryStore",
    "getsortedmap": "GetSortedMap",
    "getqueue": "GetQueue",
    # players / characters
    "getplayers": "GetPlayers",
    "getplayerbyuserid": "GetPlayerByUserId",
    "getplayerfromcharacter": "GetPlayerFromCharacter",
    "loadcharacter": "LoadCharacter",
    "kick": "Kick",
    "takedamage": "TakeDamage",
    "breakjoints": "BreakJoints",
    "gethumanoiddescription": "GetHumanoidDescription",
    # parts / physics
    "getmass": "GetMass",
    "setnetworkowner": "SetNetworkOwner",
    "getnetworkowner": "GetNetworkOwner",
    "getpivot": "GetPivot",
    "setpivot": "SetPivot",
    "pivotto": "PivotTo",
    "moveto": "MoveTo",
    "gettouchingparts": "GetTouchingParts",
    "getconnectedparts": "GetConnectedParts",
    "getboundingbox": "GetBoundingBox",
    "getextentssize": "GetExtentsSize",
    "getscale": "GetScale",
    "setscale": "SetScale",
    "getjointsof": "GetJointsOf",
    # animation / sound
    "getstate": "GetState",
    "play": "Play",
    "stop": "Stop",
    "pause": "Pause",
    "resume": "Resume",
    "adjustspeed": "AdjustSpeed",
    # gui
    "tweenposition": "TweenPosition",
    "tweensize": "TweenSize",
    "setprimarypartcframe": "SetPrimaryPartCFrame",
    "getchildrenofclass": "GetChildrenOfClass",
}

SERVER_ONLY_SERVICES = (
    "DataStoreService", "MemoryStoreService", "MessagingService", "ServerStorage",
    "ServerScriptService", "HttpService", "BadgeService", "DataStore", "OrderedDataStore",
)

RE_DEPRECATED_CALL = re.compile(r"(?<![\w.:])(wait|spawn|delay|tick)\s*\(")
RE_INSTANCE_NEW_PARENT = re.compile(r"Instance\.new\s*\(\s*([\"'])[^\"']*\1\s*,")
# Receiver is required on purpose: without it, the return-type annotation `): typeof(X)`
# reads as a call to `:typeof`. `::` casts and `local x: number` do not match either.
RE_LOWER_METHOD = re.compile(r"(?<![\w:])([A-Za-z_]\w*)\s*:\s*([a-z]\w*)\s*\(")
RE_NUMERIC_REQUIRE = re.compile(r"(?<![\w.])require\s*\(\s*\d")
RE_LOADLIBRARY = re.compile(r"(?<![\w.:])LoadLibrary\s*\(")
RE_LOCAL_PLAYER = re.compile(r"LocalPlayer")
RE_BUSY_LOOP = re.compile(r"\bwhile\s+true\s+do\b")


@dataclass
class Issue:
    severity: str          # error | warning
    rule: str
    line: int
    message: str
    file: str = ""

    def to_dict(self) -> dict:
        return {"severity": self.severity, "rule": self.rule, "line": self.line,
                "message": self.message, "file": self.file}

    def text(self) -> str:
        return f"{self.severity:7s} {self.file}:{self.line}: [{self.rule}] {self.message}"


def mask(text: str, strings: bool = True) -> str:
    """Blank out comments (and, with `strings`, string literals) keeping every offset.

    Offsets are preserved so a regex match maps back to the original line number, and so
    `wait(` inside a comment or a string never fires a rule about real code.
    """
    out = list(text)
    n = len(text)
    i = 0

    def blank(a: int, b: int) -> None:
        for k in range(a, min(b, n)):
            if out[k] != "\n":
                out[k] = " "

    while i < n:
        ch = text[i]
        if ch == "-" and i + 1 < n and text[i + 1] == "-":
            if i + 2 < n and text[i + 2] == "[":
                j = _skip_long_bracket(text, i + 2)
                if j > 0:
                    blank(i, j)
                    i = j
                    continue
            j = text.find("\n", i)
            j = n if j < 0 else j
            blank(i, j)
            i = j
            continue
        if strings and ch in ('"', "'"):
            j = i + 1
            while j < n:
                c = text[j]
                if c == "\\":
                    j += 2
                    continue
                if c == ch:
                    j += 1
                    break
                if c == "\n":
                    break
                j += 1
            blank(i, j)
            i = j
            continue
        if ch == "[":
            j = _skip_long_bracket(text, i)
            if j > 0:
                blank(i, j)
                i = j
                continue
        i += 1
    return "".join(out)


def _line_starts(text: str) -> list[int]:
    starts = [0]
    for i, ch in enumerate(text):
        if ch == "\n":
            starts.append(i + 1)
    return starts


def _line_of(starts: list[int], off: int) -> int:
    import bisect
    return max(1, bisect.bisect_right(starts, off))


def block_balance(code: str) -> list[tuple[int, str]]:
    """`[(line, opener)]` for every block left open at EOF, and `(line, "end")` for strays.

    `do` counts only when it is not the `do` of a `for`/`while` header - otherwise every
    loop would look like two opens and the file would "end" one block early.
    """
    issues: list[tuple[int, str]] = []
    starts = _line_starts(code)
    stack: list[tuple[str, int]] = []
    pending_do = False
    n = len(code)
    i = 0
    while i < n:
        ch = code[i]
        if ch.isalpha() or ch == "_":
            j = i
            while j < n and (code[j].isalnum() or code[j] == "_"):
                j += 1
            word = code[i:j]
            line = _line_of(starts, i)
            if word in ("function", "if", "for", "while"):
                stack.append((word, line))
                pending_do = word in ("for", "while")
            elif word == "do":
                if pending_do:
                    pending_do = False
                else:
                    stack.append((word, line))
            elif word == "repeat":
                stack.append((word, line))
            elif word in ("end", "until"):
                if not stack:
                    issues.append((line, word))
                else:
                    stack.pop()
            i = j
            continue
        i += 1
    issues.extend((line, word) for word, line in stack)
    return issues


def lint_text(text: str, rel_path: str = "", context: str = "") -> list[Issue]:
    ctx = context or script_context(rel_path)
    code = mask(text, strings=True)
    raw = mask(text, strings=False)
    starts = _line_starts(text)
    issues: list[Issue] = []

    def add(severity: str, rule: str, off: int, message: str) -> None:
        issues.append(Issue(severity, rule, _line_of(starts, off), message, rel_path))

    for line, opener in block_balance(code):
        if opener in ("end", "until"):
            add("error", "stray-close", starts[min(line - 1, len(starts) - 1)],
                f"`{opener}` with no block open - the script will not compile")
        else:
            add("error", "unclosed-block", starts[min(line - 1, len(starts) - 1)],
                f"`{opener}` is never closed (no matching `end`) - the script will not compile")

    for m in RE_DEPRECATED_CALL.finditer(code):
        name = m.group(1)
        replacement = {"wait": "task.wait", "spawn": "task.spawn",
                       "delay": "task.delay", "tick": "os.clock / DateTime.now().UnixTimestamp"}[name]
        add("warning", "deprecated-api", m.start(),
            f"`{name}(...)` is deprecated in Roblox Luau - use `{replacement}`")

    for m in RE_INSTANCE_NEW_PARENT.finditer(raw):
        add("warning", "instance-new-parent", m.start(),
            "Instance.new(class, parent) is deprecated: set `.Parent` after configuring the "
            "instance, otherwise every property write replicates separately")

    for m in RE_LOWER_METHOD.finditer(code):
        name = m.group(2)
        canonical = API_METHOD_CASE.get(name.lower())
        if not canonical:
            continue                   # a module method, a stdlib method, `typeof` - fine
        # `function Shop:total()` is a definition of a method, not a call to one.
        if "function" in code[max(0, m.start() - 12):m.start()]:
            continue
        add("error", "method-case", m.start(2),
            f"`:{name}(...)` - Roblox API methods are PascalCase; a lowercase name is a "
            f"nil call at runtime (did you mean `:{canonical}`?)")

    for m in RE_LOADLIBRARY.finditer(code):
        add("error", "removed-api", m.start(),
            "`LoadLibrary` was removed from Roblox and does not exist at runtime")

    for m in RE_NUMERIC_REQUIRE.finditer(code):
        add("warning", "numeric-require", m.start(),
            "`require(<number>)` is the legacy asset-id form - use a ModuleScript reference")

    if ctx == "client":
        for svc in SERVER_ONLY_SERVICES:
            m = re.search(rf"\b{svc}\b", code)
            if m:
                add("error", "server-only-service", m.start(),
                    f"`{svc}` is server-only and is not available in a client script "
                    f"(this file is {rel_path or 'a client script'}); move the call behind "
                    f"a RemoteEvent/RemoteFunction")
    if ctx == "server":
        for m in RE_LOCAL_PLAYER.finditer(code):
            add("error", "localplayer-on-server", m.start(),
                "`Players.LocalPlayer` is always nil on the server - take the player from "
                "the event argument (`PlayerAdded`, `RemoteEvent.OnServerEvent`)")

    if RE_BUSY_LOOP.search(code) and not re.search(r"task\.wait|:Wait\(|RunService", code):
        m = RE_BUSY_LOOP.search(code)
        add("warning", "busy-loop", m.start(),
            "`while true do` with no `task.wait()` yields forever and freezes the thread")

    issues.sort(key=lambda x: (x.line, x.rule))
    return issues


def lint_project(root: Path, limit: int = 400) -> list[Issue]:
    """Lint every Luau source of the project. Errors first, then by file."""
    out: list[Issue] = []
    for p in source_files(root)[:limit]:
        try:
            rel = p.relative_to(root).as_posix()
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        out.extend(lint_text(text, rel))
    out.sort(key=lambda x: (x.severity != "error", x.file, x.line))
    return out
