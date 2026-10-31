---
title: "Page layouts"
url: /docs/en-us/ui/page-layouts
last_updated: 2026-10-30T19:56:02Z
description: "Explore how page layouts organize interface content into distinct pages."
---

# Page layouts

When you parent a `Class.UIPageLayout` to a UI container, every sibling `Class.GuiObject` becomes a unique page that you can transition to through scripting. This layout is useful when you want to create user interfaces such as tabbed modals, tutorials, or character customization screens.

After you create multiple pages within the `Class.UIPageLayout`, you need to use scripting to transition from page to page. For example, the following code, pasted into a client‑side sibling `Class.Script` of the layout, transitions forward and then backward between the pages every two seconds.

```lua
local frame = script.Parent

local pageLayout = frame:FindFirstChildWhichIsA("UIPageLayout")

task.wait(2)
pageLayout:Next()

task.wait(2)
pageLayout:Next()

task.wait(2)
pageLayout:Previous()

task.wait(2)
pageLayout:Previous()
```

If you want to view pages while editing in Studio, you can use the [Command Bar](/docs/en-us/studio/overview.md#command-bar) to navigate from one page to another, letting you review where you need to make changes without having to play your game each time.

1. In the [Explorer](/docs/en-us/studio/explorer.md) window hierarchy, select the `Class.UIPageLayout` object.
2. Open the [Command Bar](/docs/en-us/studio/overview.md#command-bar).
3. Input any of the following commands and press `Enter`. | Action | Command |
| --- | --- | | **Next Page** | `game:GetService("Selection"):Get()[1]:Next()` | | **Previous Page** | `game:GetService("Selection"):Get()[1]:Previous()` | | **First Page** | `game:GetService("Selection"):Get()[1]:JumpToIndex(0)` |
