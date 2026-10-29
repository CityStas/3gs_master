---
name: unity-project
description: "How a Unity project is laid out and how the 3GS agent works inside one: Assets/, Packages/manifest.json, ProjectSettings/, .asmdef, engine.json, the active project, the editor/CLI toolchain, creating a project from scratch, build targets. Use at the start of a Unity task or when project structure, packages or builds are involved. Русские триггеры: «структура проекта», «манифест», «пакеты», «сборка», «новый проект», «engine.json»."
---

# Unity project layout and the 3GS contract

## The folder

```
<project>/
├── Assets/                       everything the game owns (scripts, scenes, prefabs, art)
│   ├── Scripts/
│   ├── Editor/                   editor-only assembly (UnityEditor allowed here)
│   ├── Scenes/*.unity
│   ├── Prefabs/*.prefab
│   ├── Generated/                the asset pipeline's output (images/ masks/ 3d/)
│   └── **/*.asmdef               assembly definitions, when used
├── Packages/
│   ├── manifest.json             the dependency list - the only package file to edit
│   └── packages-lock.json        resolved graph - DELETE it after editing manifest.json
├── ProjectSettings/
│   ├── ProjectVersion.txt        the editor build that owns this project
│   ├── ProjectSettings.asset     activeInputHandler, product name, etc.
│   ├── TagManager.asset          tags and layers
│   └── InputManager.asset        legacy input actions
├── Library/                      generated cache - never commit, safe to delete (5-15 min reimport)
└── engine.json                   the 3GS marker: {"engine": "unity", "version": "6000.3.26f1"}
```

`engine.json` is what makes `agent.cmd` pick the Unity profile and what makes
`.pi/extensions/engine-gate.ts` expose the `unity_*` tools. Without it the agent runs in the
Three.js profile and has none of them.

## Active project

`data/active_project.txt` holds the path the agent was launched with; `dev.cmd <name>` writes
it. Reach the project with its relative path (`projects/games/<name>/`) or the absolute path the
user gave — never guess the folder from the task wording.

`unity_project_info()` reports editor version, package list and counts. It is the first call in
any task, because the project's editor version may differ from the RAG corpus version
(6000.3) — trust the project and warn about the mismatch.

## Toolchain

| Tool | Path | Used for |
|---|---|---|
| Editor | `E:\Programs\Unity Hub\Unity\Editors\6000.3.26f1\Editor\Unity.exe` | compile, `-executeMethod`, build, play |
| CLI | `C:\Users\tio\AppData\Local\Unity\bin\unity.exe` | project create/add, `build`, `test`, `status`, the stdio MCP bridge |

`unity_validate(compile=true)` and `unity_run_method(...)` drive the editor; `unity_open_editor()`
opens the window for the human. The editor can only be open on a project **once** — a batch run
against an open project fails with a lock error, which is why `unity_console()` exists as the
fast path while the editor is open.

## Creating a project

Prefer the CLI (`unity projects create MyGame --path F:/Pets/Projects/games/unity`) or Unity
Hub. Hand-scaffolding needs `Assets/`, `Packages/manifest.json` and
`ProjectSettings/ProjectVersion.txt`, and the **package versions must match the editor build** —
copy them from a project made by the same editor, never from `dist-tags.latest`. Full recipe:
`unity_rag_search("unity project from scratch")`.

Unity Hub **refuses to open a project inside its own install folder**; keep projects outside
`E:\Programs\Unity Hub\`.

## Build

```
unity build --project-path <p> --target Win64        # Unity CLI, --format json for a report
```

or an `-executeMethod` that calls `BuildPipeline.BuildPlayer`. A build is verified by running
the produced player, not by "it made an .exe". `EditorBuildSettings.scenes` must list the
scenes, or the build has no starting scene.

## Conventions to keep

- Do not commit `Library/`, `Temp/`, `obj/`, `Logs/`, `UserSettings/`, `*.csproj`, `*.sln`.
- Do not delete a `.meta` file: the GUID in it is what scenes and prefabs reference.
- `Assets/Generated/` is the pipeline's output — regenerate it, do not hand-edit it.
- An `.asmdef` splits the project into assemblies; a script that cannot see a type is usually in
  a different assembly that is not referenced, not missing.
