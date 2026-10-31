---
name: AvatarContextMenuOption
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Options for the Avatar Context Menu, a menu that allows users to interact with other players' characters in an experience."
---

# AvatarContextMenuOption

Options for the Avatar Context Menu, a menu that allows users to interact with
other players' characters in an experience.

**Type:** enum

## Description

Options for the [Avatar Context Menu](/docs/en-us/players/avatar-context-menu.md)
(ACM), a menu that allows users to interact with other players' characters in
an experience. Pass these values to [StarterGui:SetCore()](/docs/reference/engine/classes/StarterGui.md) with the
`"AddAvatarContextMenuOption"` or `"RemoveAvatarContextMenuOption"` options to
add or remove default actions from the menu.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Friend` | 0 | Sends a friend request to the selected user. |
| `Chat` | 1 | Opens a private conversation with the selected user in the in-game chat. |
| `Emote` | 2 | Plays a wave emote animation directed at the selected user. |
| `InspectMenu` | 3 | Opens the Avatar Inspect Menu to view the selected user's avatar and equipped items. |