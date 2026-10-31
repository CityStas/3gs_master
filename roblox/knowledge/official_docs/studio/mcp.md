---
title: "Connect to the Roblox Studio MCP server"
url: /docs/en-us/studio/mcp
last_updated: 2026-10-30T19:55:57Z
description: "Learn how to connect your AI coding tools to Roblox Studio, enabling them to read your game structure, edit scripts, insert models, execute code, and control play mode."
---

# Connect to the Roblox Studio MCP server

The Roblox Studio MCP server is built into Roblox Studio. It implements the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro), an open standard that lets AI tools securely communicate with external applications. Once connected, your AI client can interact directly with your open Studio session, exploring the data model, writing scripts, running Luau code, and testing your game in play mode.

This guide shows you how to connect the Studio MCP server to popular AI clients. While the setup varies by client, the core idea is the same: you configure your client to connect to the MCP server and then send commands from the client to your active Studio session.

## Prerequisites

Before you can connect to the server, make sure you have the **latest version of Roblox Studio** and your **preferred MCP client** installed on your computer.

## How the Studio MCP server works

The server runs as a local process on your machine and communicates with the AI client using **`stdio` transport**, which uses standard input/output streams. All actions are initiated through your AI client, which then sends a request through this channel to perform actions inside your Studio session.

The server provides the following tools:

| **Scripts** | |
| --- | --- |
| `script_read` | Reads a script from the game using dot-notation paths (for example, `game.ServerScriptService.MyScript`). Supports reading entire scripts or specific line ranges. |
| `multi_edit` | Applies multiple edits to a script in one operation. If the target path doesn't exist, it creates a new script. Requires specifying a `datamodel_type` (Edit). |
| `script_search` | Searches for scripts by name using fuzzy matching. Returns up to 10 results. |
| `script_grep` | Searches for a string pattern across all scripts in the game. Returns up to 50 matches. |
| **Asset and content generation** | |
| `generate_mesh` | Generates a textured 3D mesh from a text prompt using AI. |
| `generate_material` | Generates a custom material variant. Returns the base material and material variant name to apply to parts. |
| `generate_procedural_model` | Creates 3D objects built from primitive parts (blocks, spheres, cylinders, wedges) as a ProceduralModel with configurable attributes. Supports reference images and custom part schemas. |
| `wait_job_finished` | Waits for a procedural model generation job to finish and returns the final status. |
| `search_asset` | Searches for assets across the Creator Store (public marketplace) and Creator Inventory (user, group, or universe). Supports filtering by asset type, price, tags, and scope. |
| `insert_asset` | Inserts an asset into the game by its numeric Roblox asset ID. Supports models, meshes, images, audio, video, animations, and packages. |
| `upload_image` | Uploads a batch of images from HTTP URLs to the Roblox asset server, returning an image path to asset ID map. |
| `store_image` | Loads an image from a local file path and returns an image URI that can be passed to other tools (for example, as a reference image for `generate_procedural_model`). |
| **Data model exploration** | |
| `subagent` | Launches a specialized subagent to handle complex, multi-step tasks autonomously. Available types include `explore` (for codebase investigation and game state queries) and `playtest` (for running gameplay scenarios and verifying outcomes). |
| `search_game_tree` | Explores the instance hierarchy as a flat JSON array. Supports filtering by path, instance type, and keywords, with configurable depth limiting. |
| `inspect_instance` | Returns detailed information about a specific instance, including all readable properties, custom attributes, and a summary of its children and descendants. |
| **Luau execution** | |
| `execute_luau` | Runs Luau code in Studio. Returns either the result or an error. Requires specifying a `datamodel_type` (Edit, Client, or Server). |
| **Playtesting** | |
| `get_studio_state` | Gets the current state of Studio, including the play state and available datamodel types. |
| `start_stop_play` | Starts or stops playtesting. |
| `get_console_output` | Retrieves output from the Studio output log. |
| `screen_capture` | Captures the current Studio viewport and returns the image data. Optionally accepts a custom camera position and look-at target. |
| **Player input simulation** | |
| `character_navigation` | Moves the player character to a given position or instance path. Supports a configurable speed multiplier. |
| `user_keyboard_input` | Sends one or more keyboard actions in order: key down, key up, key press, text input, or wait. Supports targeting specific UI instances. |
| `user_mouse_input` | Sends one or more mouse actions in order: move, click, button down/up, scroll, or wait. Supports targeting specific instances or screen coordinates. |
| **Documentation and skills** | |
| `http_get` | Fetches content from allowed Roblox documentation URLs (Engine API reference, Creator docs, Cloud API, performance optimization guides). Supports keyword search within fetched content. |
| `skill` | Retrieves detailed knowledge, best practices, or reference material for specific skills such as debugging, device simulation, and documentation search. |
| **Session management** | |
| `list_roblox_studios` | Lists all connected Studio instances, including their name, Studio instance ID, and place ID. Local places that don't have a place ID are listed by name only. Useful when multiple Studio windows are open; if two open Studio instances share the same name, the place ID lets you tell apart. |

> **Info:** Every tool call takes a `studio_id` parameter that names the Studio instance it targets, so agents address Studio instances explicitly instead of relying on session state. Use `list_roblox_studios` to look up the ID of the instance you want.
## Enable the MCP server in Studio

To enable the MCP server in Studio:

1. Open **Assistant**.
2. Click **…** ⟩ **Manage MCP Servers**.
3. Turn on **Enable Studio as MCP server**.

Once enabled, the settings panel displays the quick connect option and setup instructions for different clients. When a client connects successfully, a green indicator shows the number of connected clients.

## Connect your client

You can connect your client to the Studio MCP server using quick connect, a JSON configuration, or a CLI command.

- Use **quick connect** if your client is supported.
- If not, use a **JSON configuration** if your client supports MCP config files.
- Otherwise, use a **CLI command**.

The Studio MCP server works with any client that supports `stdio` transport. After adding the configuration, follow your client's documentation to complete setup, then restart the client to apply your changes.

> **Warning:** MCP clients can read and modify content in your open Roblox places. Make sure to only connect clients you trust.
### Quick connect

Quick connect supports the following clients:

- Antigravity
- Codex CLI
- Claude Code
- Claude Desktop
- Cursor
- Gemini CLI
- Visual Studio Code

To connect using quick connect:

1. Go to **Assistant Settings** ⟩ **MCP Servers**.
2. Expand the **Quick connect** dropdown to view supported clients installed on your computer.
3. Turn on your chosen client.

If the client you want doesn't appear in the **Quick connect** list, install it and restart Roblox Studio.

### JSON configuration

Most MCP clients support JSON configuration files. The following examples show complete configurations you can use.

If Roblox Studio is your only MCP server, use these configurations as-is. If you're using multiple MCP servers, copy the `Roblox_Studio` entry and add it to your existing `mcpServers` dictionary.

> **Info:** Your `mcp.json` file might already contain other entries. When adding the `Roblox_Studio` configuration, make sure each entry is separated by a comma. Missing commas will result in invalid JSON and prevent the configuration from loading.

Configurations vary by operating system:

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

```json
{
  "mcpServers": {
    "Roblox_Studio": {
      "command": "/Applications/RobloxStudio.app/Contents/MacOS/StudioMCP"
    }
  }
}
```

### CLI command

Some MCP clients require a CLI command instead of a JSON configuration. Use the appropriate command for your operating system:

```bash
cmd.exe /c %LOCALAPPDATA%\Roblox\mcp.bat
```

```bash
/Applications/RobloxStudio.app/Contents/MacOS/StudioMCP
```

## Use multiple Studio instances

You can connect a single MCP client to multiple running instances of Studio at the same time. Every tool call includes a `studio_id` that identifies the Studio instance to target, which makes workflows with multiple Studio instances and multiple agents or clients reliable.

Use `list_roblox_studios` to list the connected instances with their names, Studio instance IDs, and place IDs. Then pass the ID of the instance you want as `studio_id` on subsequent calls.

## Verify your connection

After setting up your client, verify that the connection is working in Roblox Studio:

1. Open **Assistant**.
2. Click **…** ⟩ **Manage MCP Servers**.
3. Under **Enable Studio as MCP server**, check for the green indicator to confirm that the client has connected successfully.

## Troubleshooting

If the server is not showing up, or the tools aren't available:

- Restart both Roblox Studio and your MCP client.
- Verify that the command or binary path is correct and the file exists.
- Check your JSON syntax. Even a missing comma or bracket can prevent the configuration from loading.
