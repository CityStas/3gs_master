---
name: unity-debug
description: "Diagnose Unity failures: compile errors (error CS), Safe Mode, MissingReferenceException, NullReferenceException, missing script references, pink/magenta materials, invisible objects, unbaked NavMesh, Input System runtime exceptions, import and build errors. Use when something in a Unity project is broken or a build fails. Русские триггеры: «ошибка», «не работает», «падает», «краш», «error CS», «NullReference», «розовый материал», «Safe Mode»."
---

# Unity debug loop

## Order of operations

1. `unity_console()` — the live editor's own errors, instant while it is open. This is the fast
   path: the editor recompiles on save, so write → wait → read.
2. `unity_validate(paths_list=[...])` — lint without the editor; catches API that no longer
   exists, the CS1612 struct trap, editor-only API in a runtime script.
3. `unity_validate(compile=true)` — the real batch gate. Editor must be closed. Minutes.
4. Only then look at behaviour in play mode (`unity_open_editor()`).

## `error CSxxxx` — read the first one

```
Assets/Scripts/Player.cs(23,17): error CS0117: 'BuildTarget' does not contain a definition for 'ReservedCFE'
```

Fix the **first** error and recompile; later errors are usually its fallout. A long cascade
after one line is normal.

| Code | Meaning | Typical cause |
|---|---|---|
| CS0117 | member does not exist | package/editor version mismatch |
| CS0246 / CS0234 | type or namespace not found | missing package, missing `using`, wrong assembly |
| CS0101 | duplicate definition | two files declare the same class |
| CS1612 | cannot modify a struct return value | `transform.position.x = 5f` |
| CS1061 | no such member on the type | Unity 4/5 API (`gameObject.rigidbody`) |
| CS0029 | cannot convert type | `Instantiate` returning `Object` assigned to `GameObject` |

## Safe Mode

The editor opened but scripts do not compile, so nothing runs. It is a symptom — find the first
`error CS`. Recovery when the editor is wedged: close it, delete `Library/ScriptAssemblies` and
`Library/Bee`, reopen. A full `Library` delete costs a 5–15 minute reimport.

## Package version mismatch

`error CS0117: 'BuildTarget' does not contain a definition for 'ReservedCFE'` was
`com.unity.inputsystem@1.12.0` on editor `6000.3`. Match the versions a project created by
*that editor* uses, not `dist-tags.latest`. After editing `manifest.json`, **delete
`Packages/packages-lock.json`** or Unity keeps the old resolution.

## Runtime failures the compiler cannot see

| Symptom | Cause |
|---|---|
| `MissingReferenceException` after a scene reload | event subscribed in `OnEnable`, never removed in `OnDisable`; or a static/singleton holding a destroyed object |
| `NullReferenceException` on a `[SerializeField]` | the field was never assigned (a script added by code, or a batch-built scene) |
| `InvalidOperationException` on `Input.GetKey` | the project is on the Input System package only (`activeInputHandler: 1`) |
| `The referenced script on this Behaviour is missing` | the script did not compile, or its `.meta` GUID was lost |
| everything is magenta/pink | a Built-in shader on a URP project (or the reverse) |
| the object is invisible | camera culling mask, a disabled `Renderer`, a layer the camera does not render, or `localScale` = 0 |
| the scene is black | no `Light` and no ambient in `RenderSettings` |
| a trigger never fires | neither collider has a `Rigidbody` |
| the character walks through walls | moved with `transform.position +=` instead of `CharacterController.Move` |
| `SetDestination` does nothing | NavMesh not baked, or the agent spawned off the mesh (`agent.isOnNavMesh == false`) |
| `Tag: X is not defined` | the tag is not in `ProjectSettings/TagManager.asset` |

## What a headless agent cannot verify

`-batchmode -nographics` does not render and does not accept input. Compile errors, import
errors and `Debug.Log` output are visible; a wrong-looking model, a camera that clips through a
wall and a UI that overflows are not. Say which of the two you checked.

## Log locations

- Live editor: `%LOCALAPPDATA%\Unity\Editor\Editor.log` (on this machine a junction to `E:`).
- Per project: `<project>/Logs/AssetImportWorker0.log`, `<project>/Logs/shadercompiler-*.log`.
- A batch run: the `-logFile` path passed by `unity_run_method`, returned in the result.

## Do not guess

`unity_find_symbol` and `unity_read_file` before editing: a "missing" type is usually a file
that exists under a different name, or a second definition of the same class. Fix the named
line, not the symptom.
