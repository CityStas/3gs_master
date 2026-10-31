---
title: "Studio command-line interface"
url: /docs/en-us/studio/cli
last_updated: 2026-10-30T19:55:57Z
description: "Roblox Studio supports command-line arguments that let you start Studio in a variety of ways and access special Studio functionality."
---

# Studio command-line interface

Roblox Studio supports command-line arguments that let you launch it with special functionality, such as opening a specific place or script when Studio starts. The Roblox Studio executable is typically installed in the following locations:

| OS | Location |
| --- | --- |
| Windows | `%localappdata%\Roblox\Versions\[version]\RobloxStudioBeta.exe` |
| Mac | `/Applications/RobloxStudio.app/Contents/MacOS/RobloxStudio` |

When launched from the command line, Studio pipes verbose logs to `stdout` that are more detailed than what appears in the [Output](/docs/en-us/studio/output.md) window. Arguments use a double-dash prefix and are case-insensitive. File paths that contain spaces must be quoted.

> **Info:** Any arguments not documented here are for internal use only and are subject to change without notice.
## Open a place

To open a published place, specify the place ID, universe ID, and a task.

| Argument | Required | Description |
| --- | --- | --- |
| `--placeId <placeId>` | Yes | The numeric ID of the place to open. |
| `--universeId <universeId>` | Yes | The universe that owns the place. |
| `--task <taskName>` | Yes | Specifies how Studio opens the place based on the given task.`--task EditPlace` opens the latest published version of the place for editing.`--task EditPlaceRevision` opens a specific previous version of the place and requires`--placeVersion <versionNumber>` to specify the version. |
| `--targetInstanceId <guid>` | No | Moves the Studio camera to focus on the instance with this GUID after the place loads. |
| `--annotationId <guid>` | No | Opens the annotation with this GUID after the place loads. |

```shell
# Open the latest version of a place
RobloxStudio.exe --task EditPlace --placeId 74265016723074 --universeId 7127583708

# Open a specific previous version
RobloxStudio.exe --task EditPlaceRevision --placeId 74265016723074 --universeId 7127583708 --placeVersion 2
```

## Open a local file

To open a local place, use `--task EditFile` with the following argument.

| Argument | Required | Description |
| --- | --- | --- |
| `--localPlaceFile <path>` | Yes | Absolute path to a local `.rbxl` or `.rbxlx` place file to open. |

You can also open a local place file by passing the file path as the first positional argument without a flag name.

```shell
# Open a local place file
RobloxStudio.exe --task EditFile --localPlaceFile "Projects\MyGame.rbxl"

# Shorthand
RobloxStudio.exe "Projects\MyGame.rbxl"
```

## Open a script

To open a script, specify the place ID, universe ID, and task as described in the [open a place](#open-a-place) section. Then provide one of the following arguments depending on how you want to open the script.

| Argument | Description |
| --- | --- |
| `--openScriptPath <path>` | The path to the script. Must use `/` as separators and follow absolute `require-by-string` semantics. |
| `--openScriptFromId <uniqueId>` | The unique ID of the script to open. |

Optionally, highlight specific lines or a character range when opening the script.

| Argument | Description |
| --- | --- |
| `--startLine <n>` | Starting line of the highlight range. 1-based and inclusive. |
| `--endLine <n>` | Ending line of the highlight range. 1-based and exclusive. |
| `--startCharacter <n>` | Starting character position within the line. 1-based. |
| `--endCharacter <n>` | Ending character position within the line. 1-based and exclusive. |

```shell
# Open a script by path
RobloxStudio.exe --task EditPlace --placeId 74265016723074 --universeId 7127583708 --openScriptPath Workspace/MyFolder/MyScript

# Open a script by ID
RobloxStudio.exe --task EditPlace --placeId 74265016723074 --universeId 7127583708 --openScriptFromId 604a6aa2-04cc-c820-09b3-a1dc0000537f

# Open a script and highlight specific lines
RobloxStudio.exe --task EditPlace --placeId 74265016723074 --universeId 7127583708 --openScriptPath Workspace/MyFolder/MyScript --startLine 1 --endLine 5

# Open a script and highlight a character range
RobloxStudio.exe --task EditPlace --placeId 74265016723074 --universeId 7127583708 --openScriptPath Workspace/MyFolder/MyScript --startLine 1 --endLine 1 --startCharacter 1 --endCharacter 6
```

## Run a script

Use `--task RunScript` to execute a Luau script after a place finishes loading. Scripts run at the same permission level as the Studio command bar. You can combine this with `--placeId` and `--universeId` to run the script in a specific game, or `--localPlaceFile` to run the script in a local place file. If those arguments are omitted, Studio opens the default empty baseplate template and runs the script there.

| Argument | Required | Description |
| --- | --- | --- |
| `--runScriptFile <path>` | Yes | Absolute path to a `.lua` or `.luau` file to execute. |
| `--outputFile <path>` | No | Path to a file where script output is written. |
| `--quitAfterExecution` | No | If provided, Studio closes after the script finishes executing. |

```shell
# Run a script in a specific game and exit when done
RobloxStudio.exe --task RunScript --placeId 74265016723074 --universeId 7127583708 --runScriptFile smokeTest.luau --outputFile out.log --quitAfterExecution

# Run a script in the default Baseplate
RobloxStudio.exe --task RunScript --runScriptFile smokeTest.luau
```

## Try an asset

Use `--task TryAsset` to insert a specific asset into a baseplate template and open it for editing.

| Argument | Required | Description |
| --- | --- | --- |
| `--assetId <id>` | Yes | The asset ID to insert. |

```shell
RobloxStudio.exe --task TryAsset --assetId 53326
```

## API dump

Use `--api`, `--fullApi`, or `--apiV2` to write the Roblox API surface to a file and exit.

| Argument | Required | Description |
| --- | --- | --- |
| `--api <path>` | Yes | Writes the Luau scripting API as JSON to the specified file. |
| `--fullApi <path>` | Yes | Writes the full API surface as JSON to the specified file. |
| `--apiV2 <path>` | Yes | Writes the full API as JSON in the V2 schema format to the specified file. |

```shell
RobloxStudio.exe --api "Desktop/output.json"

RobloxStudio.exe --fullApi "Desktop/output.json"

RobloxStudio.exe --apiV2 "Desktop/output.json"
```
