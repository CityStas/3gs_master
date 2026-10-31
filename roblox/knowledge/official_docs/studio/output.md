---
title: "Output"
url: /docs/en-us/studio/output
last_updated: 2026-10-30T19:55:57Z
description: "The Output window in Roblox Studio displays error messages, calls to print(), and calls to warn()."
---

# Output

The **Output** window, accessible from Studio's **Window** menu or **Script** tab toolbar, displays errors captured from running scripts, messages from Roblox Engine, messages from calls to `print()`, and errors from calls to `warn()`.

Plugins can interact with the **Output** window through `Class.LogService` which can record and clear the window's contents. You can customize the output through the following elements:

![Sections of Output window indicated by lettered pointers](../assets/studio/general/Output-Window-Diagram.png)

Filters output by type, such as **Error** or **Warning**.

Filters output by context, such as **Client**, **Server**, or **User Plugin**.

Filters output by the text entered into the field, such as an object name.

Clears all output messages from the window. This action has a shortcut of `Ctrl``K` on Windows or `⌘``K` on Mac.

Controls the level of detail displayed for each output message.

- **Show Timestamp** — Shows a detailed timestamp in `HH:MM:SS.SSS` format.
- **Show Context** — Shows the message context, such as **Client** or **Server**.
- **Show Source** — If applicable, shows the associated script name and line number.
- **Show Tables Expanded by Default** — For outputted tables, contents are expanded by default.
- **Show Memory Address for Expandable Tables** — For expandable tables, shows the internal memory address, such as `0xb4f0417581144ec5`.
- **Log Mode** — Simplifies output by removing options, such as expandable trees.
