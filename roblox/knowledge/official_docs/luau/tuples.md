---
title: "Tuples"
url: /docs/en-us/luau/tuples
last_updated: 2026-10-30T19:55:44Z
description: "Tuples are lists of values."
---

# Tuples

A **tuple** is a list of values. Many [methods](/docs/en-us/luau/functions.md#methods) and [callbacks](/docs/en-us/luau/functions.md#callbacks) in the [Roblox Engine API](/docs/en-us/reference/engine.md) accept and return multiple values, but the API Reference says "Tuple" instead of those values.

## Parameters

If a [method](/docs/en-us/luau/functions.md#methods) or [callback](/docs/en-us/luau/functions.md#callbacks) accepts a tuple as a parameter, then it accepts multiple values. For example, the API Reference shows that the `Class.BindableFunction:Invoke()` method accepts a "Tuple" as a parameter, so it accepts multiple arguments.

```lua
BindableFunction:Invoke(1, true, "string", Vector3.new(0, 0, 0))
```

## Returns

If a [method](/docs/en-us/luau/functions.md#methods) or [callback](/docs/en-us/luau/functions.md#callbacks) returns a tuple, then it returns multiple values. For example, the API Reference shows that the `Class.Players:GetUserThumbnailAsync()` method returns a "Tuple", so it returns multiple values. The first return value is a Content URL, and the second is a [boolean](/docs/en-us/luau/booleans.md).

```lua
local Players = game:GetService("Players")

local userId = 156 -- builderman
local thumbType = Enum.ThumbnailType.HeadShot
local thumbSize = Enum.ThumbnailSize.Size420x420
local content, isReady = Players:GetUserThumbnailAsync(userId, thumbType, thumbSize)
print(content, isReady) -- rbxthumb://type=AvatarHeadShot&id=156&w=420&h=420 true
```
