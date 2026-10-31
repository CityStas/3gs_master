# Roblox Studio MCP — Windows Setup

## 1. Recommendation

Use the **built-in Roblox Studio MCP server**. As of 2026-10-31, Roblox documents it as part of Studio and recommends it instead of the older standalone Rust MCP server, which is no longer actively developed.

Official setup guide: https://create.roblox.com/docs/studio/mcp

## 2. Prerequisites

- Latest Roblox Studio.
- An MCP-compatible AI client (for example Codex CLI, Claude Code/Desktop, Cursor, Gemini CLI or VS Code; check the current quick-connect list in Studio).
- Permission to connect the client to the local Studio process.

## 3. Enable in Roblox Studio

1. Launch Roblox Studio and open the target place.
2. Open the Assistant panel.
3. Click the `...` menu and select `Manage MCP Servers`.
4. Enable `Enable Studio as MCP server`.
5. Use `Quick connect` if your client is listed. This is the easiest option.
6. If quick connect is unavailable, use the JSON configuration below.

## 4. Windows JSON configuration

Add this entry to your MCP client's configuration. Merge it into the existing `mcpServers` object; do not overwrite other servers or create a second top-level JSON object.

```json
{
  "mcpServers": {
    "Roblox_Studio": {
      "command": "cmd.exe",
      "args": [
        "/c",
        "%LOCALAPPDATA%\\Roblox\\mcp.bat"
      ]
    }
  }
}
```

The command documented by Roblox is:

```bat
cmd.exe /c %LOCALAPPDATA%\Roblox\mcp.bat
```

Do not hard-code a versioned Studio install directory: use the documented launcher path shown by Studio.

## 5. What the built-in MCP can do

The official toolset evolves. The current documentation lists capabilities including:

### Inspect and edit scripts

- `script_read`: read scripts, optionally by line range.
- `multi_edit`: apply multiple edits / create a script.
- `script_search`: find scripts by name.
- `script_grep`: search source text across scripts.

### Explore the DataModel

- `search_game_tree`: search the Instance hierarchy.
- `inspect_instance`: inspect an Instance and descendants/properties.
- `list_roblox_studios`: list connected Studio sessions.

### Execute and test

- `execute_luau`: execute Luau in Edit, Client or Server context.
- `get_studio_state`: inspect the current Studio/play state.
- `start_stop_play`: start/stop playtesting.
- `get_console_output`: retrieve Output logs.
- `screen_capture`: capture the Studio viewport.
- `character_navigation`, `user_keyboard_input`, `user_mouse_input`: simulate gameplay input.

### Documentation and assets

- `http_get`: retrieve allowed Roblox documentation content.
- `skill`: retrieve specialist guidance for supported tasks.
- Asset tools may include search/insert and generation capabilities. Verify current tool availability in the live MCP tool list.

Always consult the current official MCP page for the full and latest tool schema.

## 6. Verify connection

1. Restart the MCP client after editing its configuration.
2. Keep the target Roblox Studio place open.
3. Open Assistant → `...` → `Manage MCP Servers`.
4. Confirm the green connected-client indicator is visible.
5. Ask the client to list connected Studio instances, then inspect the intended one by `studio_id`.
6. Test a harmless read operation before allowing edits.

## 7. Important safety model

The MCP server can read and modify content in open Roblox places and can execute code. Only connect trusted clients. For safe agent operation:

- Start with read-only inspection.
- Require a plan before edits.
- Review the target `studio_id` and DataModel path.
- Make small changes and inspect the diff.
- Run tests before accepting changes.
- Do not publish or modify production data without explicit approval.
- Keep API keys and secrets out of ReplicatedStorage, project files and prompts.

## 8. Other tools: what is worth installing?

These are optional and solve different problems; none is required for the built-in MCP connection.

| Tool | Purpose | Recommendation |
|---|---|---|
| Roblox Studio built-in MCP | AI reads/edits/tests open Studio session | **Install/enable this first** (built into Studio) |
| Rojo | Sync local source files with Studio | Add when you want file-based development and Git |
| Rokit | Pin/manage versions of Rojo/Wally/Lune | Useful with a Rojo workflow |
| Wally | Luau package manager | Add only if using reusable third-party packages |
| Git | Version history and rollback | Strongly recommended for serious projects; not an MCP by itself |

Roblox's external-tool workflow guide: https://create.roblox.com/docs/projects/external-tools

## 9. Legacy server warning

Do not choose `Roblox/studio-rust-mcp-server` as the default installation. Roblox states that it is no longer actively developed and that engineering investment has moved to the built-in Studio MCP server:

https://github.com/Roblox/studio-rust-mcp-server
