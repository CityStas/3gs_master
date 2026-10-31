---
name: roblox-project
description: "Roblox project layout and tooling in this repo: engine.json, Rojo project.json mapping folders to services, .server/.client/init file naming, .rbxlx vs .rbxl, the rbx_project_* tools, rbx_lint and the gs roblox-* commands. Use when creating a project, mapping files to services, or running the gate. Русские триггеры: «rojo», «структура проекта», «project.json», «как собрать», «линтер», «проверка скриптов»."
---

# Project layout and tooling

## Two kinds of Roblox project, and how to tell them apart

| Kind | Marker | Editing |
|---|---|---|
| **File-based (Rojo)** | `default.project.json` + a `src/` tree | `rbx_project_*` tools, git, any editor |
| **Place-based** | `*.rbxlx` (XML) or `*.rbxl` (binary) | Studio; the file tools can read `.rbxlx` only |

`rbx_project_info` answers which one this is. `.rbxl` is binary and cannot be inspected
without Studio - if the corpus needs it, save as `.rbxlx` (File → Save to File As).

## `engine.json`

Every project of this repo declares its engine, and `agent.cmd` picks the pi profile from
it:

```json
{ "engine": "roblox" }
```

Without it the project is treated as Three.js, and the Roblox tools are simply not there.

## Rojo mapping

`default.project.json` maps folders to services. The mapping *is* the architecture:

```json
{
  "name": "my_game",
  "tree": {
    "$className": "DataModel",
    "ServerScriptService": {
      "$path": "src/ServerScriptService"
    },
    "ReplicatedStorage": {
      "$path": "src/ReplicatedStorage"
    },
    "ServerStorage": {
      "$path": "src/ServerStorage"
    },
    "StarterPlayer": {
      "$className": "StarterPlayer",
      "StarterPlayerScripts": {
        "$path": "src/StarterPlayer/StarterPlayerScripts"
      }
    }
  }
}
```

Rules that follow from it:

- A folder that is not in the tree does not exist in the place. Adding a file to a mapped
  folder is enough; adding a *new* folder needs a `$path` entry.
- `init.luau` inside a folder makes the folder itself the script (a `ModuleScript` with
  children). `foo.luau` becomes a `ModuleScript` named `foo`; `foo.server.luau` a `Script`;
  `foo.client.luau` a `LocalScript`.
- `.meta.json` next to a file overrides properties (`RunContext`, `Disabled`).

## File naming

```
src/
  ServerScriptService/
    Bootstrap.server.luau          -> Script
  ServerStorage/Server/
    ShopService.luau               -> ModuleScript
  ReplicatedStorage/Shared/
    Remotes.luau                   -> ModuleScript
  StarterPlayer/StarterPlayerScripts/
    ClientMain.client.luau         -> LocalScript
```

Never put a `.server.luau` in `ReplicatedStorage` (it would be a `Script` in a replicated
container - it runs on the server but every client can read it), and never put a
`.client.luau` in `ServerScriptService` (it never runs).

## Tools of this stack

```bash
# project shape: root, engine, rojo file, luau count, place files, Studio state
rbx_project_info                 # MCP tool
rbx_list_files / rbx_read_file / rbx_write_file / rbx_edit_file
rbx_search_scripts "PromptProductPurchase"
rbx_lint                         # whole project
rbx_place_info                   # services, class counts, scripts of a .rbxlx
rbx_studio_status / rbx_open_place
```

From the shell (bash, from the repo root):

```bash
./.venv/Scripts/python.exe roblox/tools/check.py projects/games/my_game
./.venv/Scripts/python.exe roblox/tools/check.py my_game --json
gs roblox-check my_game
```

`check.py` exits 1 on errors. It catches an unbalanced `end`, `wait`/`spawn`/`delay`/`tick`,
two-argument `Instance.new`, `:findFirstChild(`-style case errors, numeric `require`,
`LoadLibrary`, server-only services in a client script, and `LocalPlayer` on the server.
It cannot prove the script compiles - Studio's Output is the authority for that.

## Corpus and index

```bash
gs roblox-fetch                  # Creator Hub guides + Engine API + Open Cloud + starter kit
gs roblox-index                  # build / refresh the hybrid index
gs roblox-index --vectors        # repair missing embeddings after :8081 was down
gs roblox-doctor                 # Studio, corpus, index, model servers
```

The corpus lives in `roblox/knowledge/` and is *not* per project: it is the platform
documentation. The project's own Luau is indexed as `source=project` when the index is
built with `--project` (or when the active project is a Roblox one).
