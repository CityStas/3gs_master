---
name: InstanceHandle
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "A lightweight, weak reference to an Instance that might not be available locally."
---

# InstanceHandle

A lightweight, weak reference to an [Instance](/docs/reference/engine/classes/Instance.md) that might not be
available locally.

**Type:** datatype

## Description

The [InstanceHandle](/docs/reference/engine/datatypes/InstanceHandle.md) data type is a weak reference to an
[Instance](/docs/reference/engine/classes/Instance.md) that might not be available locally. Use it to point at an
instance that hasn't arrived yet, could stream out, or exists only on another
machine, and to pick that instance up once it's there.

A handle always refers to the same target. To reach that target, call
[InstanceHandle:Wait()](/docs/reference/engine/datatypes/InstanceHandle.md), which yields until the instance is
available:

```lua
local Workspace = game:GetService("Workspace")

local part = Instance.new("Part")
local target = Instance.new("Part")
target.Name = "TargetPart"
part.Parent = Workspace
target.Parent = Workspace

part:SetAttribute("Target", target)

local handle = part:GetAttribute("Target")
local instance = handle:Wait(10)
if instance then
	print("Target is", instance.Name) --> Target is TargetPart
end
```

Prefer [InstanceHandle:Wait()](/docs/reference/engine/datatypes/InstanceHandle.md) with a timeout so your code runs as
soon as the instance shows up. Use [InstanceHandle:Get()](/docs/reference/engine/datatypes/InstanceHandle.md) when you
want an immediate answer and can handle `nil`, such as in code that runs every
frame.

#### Examples

##### Attributes

Attributes use [InstanceHandle](/docs/reference/engine/datatypes/InstanceHandle.md) instead of an ordinary instance
reference. Since the handle itself is never `nil`, you can tell apart an
attribute that is missing from one where the instance is not currently
present:

```lua
local part = Instance.new("Part")

print(part:GetAttribute("Target")) --> nil

part:SetAttribute("Target", InstanceHandle.new(nil))
local handle = part:GetAttribute("Target")
print(handle:Get()) --> nil
```

[InstanceHandle](/docs/reference/engine/datatypes/InstanceHandle.md) attributes also appear in
[Instance:GetAttributes()](/docs/reference/engine/classes/Instance.md), which can't hold `nil` values.

[Instance:GetAttributeChangedSignal()](/docs/reference/engine/classes/Instance.md) fires when the attribute is set
to a new target or removed. It does not fire when the target streams in or
out, or when the target is destroyed. To react to availability, combine the
signal with [InstanceHandle:Wait()](/docs/reference/engine/datatypes/InstanceHandle.md):

```lua
local part = Instance.new("Part")

part:GetAttributeChangedSignal("Target"):Connect(function()
	local handle = part:GetAttribute("Target")
	if not handle then
		return
	end

	local instance = handle:Wait(10)
	if instance then
		print("New target:", instance.Name)
	end
end)
```

##### Remote events

Pass a handle through a [RemoteEvent](/docs/reference/engine/classes/RemoteEvent.md) to give the receiver a reference
to an instance it doesn't have yet. The receiver waits for the instance
instead of getting nothing.

In a server script, call this function with your remote event, the receiving
player, and the model to send:

```lua
local function sendHandle(remoteEvent: RemoteEvent, player: Player, spawnedModel: Model)
	local handle = InstanceHandle.new(spawnedModel)
	remoteEvent:FireClient(player, handle)
end
```

In a client script, call this function with the same remote event to start
listening before the server sends the handle:

```lua
local function receiveHandles(remoteEvent: RemoteEvent)
	remoteEvent.OnClientEvent:Connect(function(handle)
		local model = handle:Wait(10)
		if model then
			print("Received", model.Name)
		end
	end)
end
```

#### Ownership

A handle acts as a weak reference. It never keeps its target alive. The
lifetime of the target is controlled by the rest of your experience: its
parent and any ordinary references your scripts hold that prevent it from
being garbage collected.

[InstanceHandle:Get()](/docs/reference/engine/datatypes/InstanceHandle.md) and [InstanceHandle:Wait()](/docs/reference/engine/datatypes/InstanceHandle.md) return an
ordinary instance reference, which does keep the instance alive for as long as
you hold it.

A handle is otherwise lightweight and needs no cleanup.

#### Equality

Two handles are equal when they refer to the same target, even if you created
them separately and even after the target is gone. All empty handles are equal
to each other. Each handle is still a distinct value.

```lua
local instance1 = Instance.new("Part")
local instance2 = Instance.new("Part")

local a = InstanceHandle.new(instance1)
local b = InstanceHandle.new(instance1)
local c = InstanceHandle.new(instance2)

print(a == b) --> true
print(a == c) --> false
```

Equality depends on target identity, so it still works when the target isn't
currently available.

## Constructors

### InstanceHandle.new

**Signature:** `InstanceHandle.new(instance: Instance?)`

The handle refers to the instance weakly and doesn't extend its lifetime.

```lua
local target = Instance.new("Part")
target.Name = "TargetPart"

local handle = InstanceHandle.new(target)
local empty = InstanceHandle.new(nil)

print(handle:Get()) --> TargetPart
print(empty:Get()) --> nil
```

Throws if `instance` is neither an [Instance](/docs/reference/engine/classes/Instance.md) nor `nil`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `instance` | `Instance?` |  | The instance to refer to, or `nil` for an empty handle. |

## Methods

### InstanceHandle:Get

**Signature:** `InstanceHandle:Get(): Instance?`

This method doesn't yield.

`Get()` returns `nil` when the handle is empty, when the target hasn't
arrived on the client or server running the script, when the target is no
longer available after streaming out, when the target has been garbage
collected, and when the target isn't accessible to the calling script. Use
[InstanceHandle:Wait()](/docs/reference/engine/datatypes/InstanceHandle.md) to yield until the target arrives instead
of checking once.

**Returns:** `Instance?` — The referenced instance, or `nil` if it isn't available locally.

### InstanceHandle:Wait

**Signature:** `InstanceHandle:Wait(timeout: number?): Instance?`

Returns `nil` if the handle is empty, the target is inaccessible to the
calling script, or `timeout` elapses first. `Wait()` returns immediately
when the target is already available and when the handle is empty.

Pass a timeout whenever you can't guarantee that the target reaches the
caller. A target that's destroyed before it replicates leaves a handle
that never resolves, and a `Wait()` with no timeout never returns. A
pending wait can't be cancelled: [task.cancel()](/docs/reference/engine/globals/task.md) stops your
coroutine, but the wait isn't unregistered until the target arrives or the
timeout elapses.

`timeout` must be a number greater than zero. Throws if `timeout` is zero,
negative, or not a number.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `timeout` | `number?` |  | How long to wait, in seconds. Must be greater than zero. Waits indefinitely when omitted. |

**Returns:** `Instance?` — The referenced instance, or `nil` if the handle is empty, the target
is inaccessible to the calling script, or `timeout` elapses first.