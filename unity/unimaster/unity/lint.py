"""C# lint for the traps a local 9B model actually falls into in Unity.

The compiler catches syntax; it does *not* catch API that was removed between Unity 4/5
and Unity 6, or the two C#-specific mistakes a model trained mostly on Unity 5-era code
reproduces constantly. A local model writes `transform.rigidbody`, `Application.LoadLevel`,
`rb.velocity` and `transform.position.x = 5f` from memory, and every one of those is a
compile error or a silent runtime break.

This is the Unity analogue of the Godot stack's "Godot 3 API lint" (`godot_validate`
adds `lint`/`lint_hint`): `unity_validate` appends the same fields, and the findings are
duplicated into `warnings` because the model reads that field even when it ignores the
new ones.

Severity decides the verdict: `error` reddens `ok`, `warning` does not. An obsolete-but-
working API is a warning (it still compiles today); a removed API, the CS1612 struct
trap and a runtime-only `UnityEngine.Input` call are errors.

Comments and string literals are stripped before matching, so an old API mentioned in a
`//` comment is not a finding.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

from .. import config

# (code, severity, regex, message, fix)
_RAW_RULES: list[tuple[str, str, str, str, str]] = [
    # --- C# language trap: a Vector3/Quaternion returned by value cannot be assigned into
    ("CS-VALUE-COMPONENT", "error",
     r"\.(position|localPosition|eulerAngles|localEulerAngles|rotation|localRotation|"
     r"localScale|size|center|min|max|velocity|linearVelocity|angularVelocity|normal|"
     r"anchoredPosition|anchoredPosition3D|offsetMin|offsetMax|pivot|scale)"
     r"\s*\.\s*[xyz]\s*=(?!=)",
     "C# cannot assign into a member of a struct returned by value: 'Transform.position' is "
     "not a variable (CS1612).",
     "copy to a local: 'var p = transform.position; p.x = 5f; transform.position = p;'"),

    # --- Unity 6 renames ---------------------------------------------------
    ("UNITY6-RIGIDBODY-VELOCITY", "warning", r"\.velocity\b",
     "Rigidbody.velocity / Rigidbody2D.velocity is renamed in Unity 6 (other types such as "
     "NavMeshAgent keep .velocity).",
     "for a Rigidbody/Rigidbody2D use '.linearVelocity' (angularVelocity is unchanged)"),
    ("UNITY6-FIND-OBJECTS", "warning", r"\bFindObjectsOfType\s*<",
     "FindObjectsOfType<T>() is obsolete in Unity 6 and returns an unsorted array.",
     "use FindObjectsByType<T>(FindObjectsSortMode.None)"),
    ("UNITY6-FIND-OBJECT", "warning", r"(?<!s)\bFindObjectOfType\s*<",
     "FindObjectOfType<T>() is obsolete in Unity 6.",
     "use FindFirstObjectByType<T>() (or FindAnyObjectByType<T>())"),

    # --- Unity 4/5 legacy component accessors (removed in 5.x) -------------
    ("LEGACY-COMPONENT-ACCESSOR", "error",
     r"\.(rigidbody2D|rigidbody|renderer|collider|collider2D|audio|light|camera|"
     r"animation|particleEmitter|particleSystem|networkView|guiText|guiTexture|"
     r"constantForce|hingeJoint|boxCollider|sphereCollider|capsuleCollider)\b",
     "Component shorthand accessors (gameObject.rigidbody, .renderer, ...) were removed in "
     "Unity 5.",
     "use GetComponent<Rigidbody>() / GetComponent<Renderer>() / GetComponent<Collider>()"),

    # --- removed Application / scene API -----------------------------------
    ("LEGACY-APPLICATION-LEVEL", "error",
     r"\bApplication\.(LoadLevel|LoadLevelAsync|LoadLevelAdditive|"
     r"LoadLevelAdditiveAsync|loadedLevel|loadedLevelName|isLoadingLevel)\b",
     "Application.LoadLevel* and Application.loadedLevel were removed in Unity 5.3.",
     "use UnityEngine.SceneManagement.SceneManager.LoadScene(...) / "
     "SceneManager.GetActiveScene()"),
    ("LEGACY-ONLEVELWASLOADED", "error", r"\bOnLevelWasLoaded\b",
     "OnLevelWasLoaded was removed in Unity 5.4.",
     "use SceneManager.sceneLoaded += OnSceneLoaded;"),
    ("LEGACY-WWW", "error", r"\bWWW\s*\(|\bWWWForm\b",
     "WWW / WWWForm were removed in Unity 2018+.",
     "use UnityWebRequest / UnityWebRequest.Post"),
    ("LEGACY-UNITY-NETWORKING", "error",
     r"\bUnityEngine\.Networking\b|\bNetwork\.(Instantiate|"
     r"Destroy|DestroyPlayerObjects|SetSendingEnabled)\b|"
     r"\bNetworkView\b|\bOnNetworkInstantiate\b",
     "The legacy built-in networking API (Network/NetworkView) was removed.",
     "use Netcode for GameObjects (com.unity.netcode.gameobjects) or a transport package"),

    # --- misc removed helpers ---------------------------------------------
    ("LEGACY-FINDCHILD", "error", r"\.FindChild\s*\(",
     "Transform.FindChild was renamed in Unity 4.6.", "use Transform.Find(name)"),
    ("LEGACY-SETACTIVERECURSIVELY", "error", r"\.SetActiveRecursively\s*\(",
     "GameObject.SetActiveRecursively was removed in Unity 4.",
     "use SetActive(true/false) on each object"),
    ("LEGACY-PREFABUTILITY", "error",
     r"\bPrefabUtility\.(CreatePrefab|CreateEmptyPrefab|ReplacePrefab|"
     r"ConnectPrefabInstance|DisconnectPrefabInstance|InstantiatePrefab)\b",
     "The old PrefabUtility API was replaced in Unity 2018.3.",
     "use SaveAsPrefabAsset / SaveAsPrefabAssetAndConnect / InstantiatePrefab"),
    ("LEGACY-STRING-COMPONENT", "warning", r"\b(AddComponent|GetComponent)\s*\(\s*\"",
     "String-based AddComponent/GetComponent is obsolete and slow.",
     "use the generic form: AddComponent<Rigidbody>() / GetComponent<Rigidbody>()"),
    ("LEGACY-UNITYSCRIPT", "error", r"^\s*function\s+\w+\s*\(|^\s*#pragma strict\b",
     "UnityScript (.js) was removed in Unity 2018. This file must be C#.",
     "rewrite the script in C#"),

    # --- editor-only API used at runtime ----------------------------------
    # Only fires outside an Editor/ folder and without a `#if UNITY_EDITOR` guard;
    # see `lint_csharp` for the suppression logic.
    ("EDITOR-API-IN-RUNTIME", "warning",
     r"\bUnityEditor\.|\bEditorGUILayout\b|\bEditorApplication\b|\bAssetDatabase\b",
     "UnityEditor is editor-only: in a runtime script this breaks the player build.",
     "wrap in '#if UNITY_EDITOR ... #endif' or move the file under an Editor/ folder"),
]

_COMPILED = [
    (code, sev, re.compile(pat, re.M), msg, fix) for code, sev, pat, msg, fix in _RAW_RULES
]

RE_STRIP_BLOCK_COMMENT = re.compile(r"/\*.*?\*/", re.S)
RE_STRIP_LINE_COMMENT = re.compile(r"//[^\n]*")
RE_STRIP_VERBATIM = re.compile(r'@"(?:[^"]|"")*"', re.S)
RE_STRIP_STRING = re.compile(r'"(?:\\.|[^"\\])*"', re.S)
RE_STRIP_CHAR = re.compile(r"'(?:\\.|[^'\\])'")

RE_UNITY_EDITOR_GUARD = re.compile(r"#if\s+UNITY_EDITOR\b")
RE_EDITOR_FOLDER = re.compile(r"(^|/)(Editor|EditorTools)(/|$)", re.I)

# `Input.*` throws when the project is configured for the new Input System only.
RE_LEGACY_INPUT = re.compile(
    r"\bInput\.(GetKey|GetKeyDown|GetKeyUp|GetAxis|GetAxisRaw|GetButton|GetButtonDown|"
    r"GetButtonUp|mousePosition|mouseScrollDelta|anyKey|touches)\b")
RE_ACTIVE_INPUT_HANDLER = re.compile(r"^\s*activeInputHandler:\s*(\d+)", re.M)


@dataclass
class Finding:
    code: str
    line: int
    message: str
    fix: str
    script: str = ""
    severity: str = "error"

    def to_dict(self) -> dict:
        return {"code": self.code, "line": self.line, "severity": self.severity,
                "message": self.message, "fix": self.fix, "script": self.script}


def strip_code(text: str) -> str:
    """Blank out comments and string/char literals, keeping line numbers intact."""
    def blank(m: re.Match[str]) -> str:
        return re.sub(r"[^\n]", " ", m.group(0))
    text = RE_STRIP_BLOCK_COMMENT.sub(blank, text)
    text = RE_STRIP_VERBATIM.sub(blank, text)
    text = RE_STRIP_STRING.sub(blank, text)
    text = RE_STRIP_CHAR.sub(blank, text)
    text = RE_STRIP_LINE_COMMENT.sub(blank, text)
    return text


def _line_of(text: str, off: int) -> int:
    return text.count("\n", 0, off) + 1


def active_input_handler(project) -> int | None:
    """0 = legacy Input Manager, 1 = new Input System only, 2 = both. None if unknown."""
    try:
        f = project / "ProjectSettings" / "ProjectSettings.asset"
        m = RE_ACTIVE_INPUT_HANDLER.search(f.read_text(encoding="utf-8", errors="replace"))
        return int(m.group(1)) if m else None
    except (OSError, ValueError):
        return None


def lint_csharp(text: str, script: str = "", project=None) -> list[Finding]:
    """Findings for one C# source. `project` (a Path) enables project-aware checks."""
    clean = strip_code(text)
    editor_context = bool(RE_EDITOR_FOLDER.search(script or "")) or \
        bool(RE_UNITY_EDITOR_GUARD.search(clean))
    findings: list[Finding] = []
    for code, sev, rx, msg, fix in _COMPILED:
        if code == "EDITOR-API-IN-RUNTIME" and editor_context:
            continue
        for m in rx.finditer(clean):
            findings.append(Finding(code, _line_of(clean, m.start()), msg, fix, script, sev))
    if project is not None and active_input_handler(project) == 1:
        for m in RE_LEGACY_INPUT.finditer(clean):
            findings.append(Finding(
                "NEW-INPUT-SYSTEM-ONLY", _line_of(clean, m.start()),
                "This project is set to 'Input System Package (New)' only, so "
                "UnityEngine.Input throws InvalidOperationException at runtime.",
                "use UnityEngine.InputSystem (Keyboard.current / Mouse.current) or switch "
                "Active Input Handling to 'Both' in Project Settings > Player",
                script, "error"))
    findings.sort(key=lambda f: (f.line, f.code))
    return findings


def errors(findings: list[Finding]) -> list[Finding]:
    return [f for f in findings if f.severity == "error"]


def lint_hint(findings: list[Finding]) -> str:
    if not findings:
        return ""
    errs = errors(findings)
    warns = len(findings) - len(errs)
    codes = sorted({f.code for f in findings})
    return (f"{len(errs)} error(s) + {warns} warning(s) [{', '.join(codes)}] under "
            f"Unity {config.UNITY_DOC_VERSION}. Most errors are compile breakers, not style. "
            f"Fix them and validate again.")
