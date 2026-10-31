---
name: roblox-studio-mcp
description: "The built-in Roblox Studio MCP server: how to enable it, which tool answers which question (script_read, multi_edit, script_grep, search_game_tree, inspect_instance, execute_luau, start_stop_play, get_console_output, screen_capture), test modes, and the safe edit-playtest loop. Use before touching a live place. Русские триггеры: «studio mcp», «mcp», «подключить студию», «execute_luau», «плейтест», «playtest», «консоль студии»."
---

# Studio MCP

The agent has **two** ways into a Roblox project, and they are not interchangeable:

| Surface | Sees | Changes |
|---|---|---|
| `rbx_project_*` (this stack, files on disk) | a Rojo tree, a closed `.rbxlx` | files, with backups |
| `roblox-studio` (Studio's own MCP) | the **live DataModel** | the open place, in real time |

Editing the live place with file tools and the file tree with Studio tools is how work gets
silently thrown away: Studio holds the authoritative copy of an open place and will
overwrite the file on the next save.

## One-time setup, in Studio

1. Open the place.
2. **Assistant → … → Manage MCP Servers**.
3. Switch on **Enable Studio as MCP server**.
4. Optionally **Quick connect** if the client is listed; otherwise the client config is
   `cmd.exe /c %LOCALAPPDATA%\Roblox\mcp.bat` (already in `mcp/registry.json` as
   `roblox-studio`).

Verify from the agent side: `list_roblox_studios` returns the connected instances, each
with a `studio_id`. Every call that touches a place should name that id when there is more
than one Studio open.

## Tool map

| Question | Tool |
|---|---|
| Which Studio am I talking to? | `list_roblox_studios`, `get_studio_state` |
| Where is X in the tree? | `search_game_tree` |
| What is on this instance? | `inspect_instance` |
| Show me the script | `script_read` (optionally by line range) |
| Find a string across all scripts | `script_grep` |
| Find a script by name | `script_search` |
| Create or change scripts | `multi_edit` |
| Run code in Edit / Client / Server context | `execute_luau` |
| Playtest | `start_stop_play` |
| What did it print? | `get_console_output` |
| What does it look like? | `screen_capture` |
| Simulate play | `character_navigation`, `user_keyboard_input`, `user_mouse_input` |
| Official docs from inside Studio | `http_get`, `skill` |

## The loop that does not waste a session

1. `get_studio_state` → is it playing? Edit mode is the only place `multi_edit` is safe.
2. Read first: `script_read` the file you are about to change, `inspect_instance` the
   target. The model's memory of "what this script does" is worth nothing.
3. State the plan: exact Instance paths, exact functions, what will be observably different.
4. `multi_edit` one concern at a time. A ten-file refactor in one call cannot be reviewed
   and cannot be bisected when it breaks.
5. Read the result back (`script_read`).
6. `start_stop_play` in the mode that proves the claim:
   - **Play** - one server, one client, full stack;
   - **Start Server** + **Start Player** - two windows, the only way to test replication;
   - **Run** - server only, no character.
7. `get_console_output` and read it. An empty console is a result; an unread console is not.
8. `screen_capture` when the claim is visual.

Report what was observed, not what was intended. "The Output shows `attempt to index nil
with 'Health'` at line 14" is a result. "It should work now" is not.

## `execute_luau` contexts

- **Edit**: changes the DataModel as an edit. Use it to build test fixtures, not to "try"
  code - a mistake here is a change to the place.
- **Server**: runs in the server context of a running playtest. `DataStoreService`,
  `Players`, real replication.
- **Client**: runs in a client context. `LocalPlayer` is non-nil here and nil everywhere
  else; this is where a client-only bug can be reproduced.

A `print` from `execute_luau` lands in Output, so `get_console_output` reads it back.

## Failure modes

| Symptom | Cause |
|---|---|
| no studios listed | Studio is closed, or the MCP toggle is off |
| tools time out | Studio is showing a modal dialog; nothing answers while a dialog is open |
| `multi_edit` "script not found" | the script lives in a different service, or the path starts at `game.` instead of the service |
| edits appear then vanish | the place was in Play mode and the edit was discarded on stop |
| `execute_luau` does nothing | wrong context: a server-only call in Client context fails silently |

## What this server must not be used for

- Publishing, changing permissions or group ownership, paid transactions - always ask.
- Deleting large parts of the tree - ask, and list the paths first.
- Reading or writing production DataStores - ask.
