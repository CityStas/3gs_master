---
name: Collection
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "A live, query-based group of instances returned by CollectionService:CreateCollection()."
---

# Collection

A live, query-based group of instances returned by
[CollectionService:CreateCollection()](/docs/reference/engine/classes/CollectionService.md).

**Type:** datatype

## Description

A `Collection` is a live, query-based group of instances created by
[CollectionService:CreateCollection()](/docs/reference/engine/classes/CollectionService.md) using a selector string and an
optional root instance. From then on, membership is **automatic** such that an
instance is added the moment it matches the query and removed the moment it
stops matching. You never add or remove instances manually.

You can interact with a `Collection` by assigning **callbacks** to it. Rather
than connecting a signal for each instance and remembering to disconnect it,
you declare behavior once on the collection and it is applied to every
matching instance for you. The collection owns those connections and tears
them down automatically when an instance leaves the set. See the accompanying
code sample for a collection that uses each kind of callback together.

A collection's lifetime is tied to the root instance passed to
[CreateCollection()](/docs/reference/engine/classes/CollectionService.md) (defaulting to
[Workspace](/docs/reference/engine/classes/Workspace.md)). When that root is destroyed or when you call
[Destroy()](/docs/reference/engine/datatypes/Collection.md), the collection is torn down.

#### Callback Assignment Syntax

Callbacks are assigned as fields on the collection using function-statement
syntax, which reads like the contents of a [ModuleScript](/docs/reference/engine/classes/ModuleScript.md). Both of the
following forms are equivalent and assign through the collection's overloaded
`__newindex`:

```lua
local CollectionService = game:GetService("CollectionService")

local collection = CollectionService:CreateCollection("Part")

function collection.OnAdded(instance)

end
```

```lua
local CollectionService = game:GetService("CollectionService")

local collection = CollectionService:CreateCollection("Part")

collection.OnAdded = function(instance)

end
```

Each callback can be **assigned only once**; reassigning the same callback
raises an error. This keeps a collection's behavior declarative at its
definition so that it cannot be silently replaced elsewhere.

#### Core Members and Aliases

`OnAdded`, `OnRemoved`, and [ForEach()](/docs/reference/engine/datatypes/Collection.md) are the
collection's primitive members:

- `OnAdded(instance: Instance)` — Fires when an instance begins matching the
  query. When you first assign `OnAdded`, it **immediately fires once for
  every instance already in the collection**, so a single callback handles
  both current and future members.
- `OnRemoved(instance: Instance)` — Fires when an instance that was in the
  collection stops matching, for example its tag is removed, it is reparented
  out of the collection's root, it is destroyed, or the collection's
  [Enabled](/docs/reference/engine/datatypes/Collection.md) property is set to `false`.
- [ForEach()](/docs/reference/engine/datatypes/Collection.md) — Imperatively iterates the
  instances currently in the collection, operating on a snapshot taken at call
  time.

A collection can also bind a callback to non-deprecated [RunService](/docs/reference/engine/classes/RunService.md)
steps through **aliases** which exist for performance as well as convenience:

| Collection Callback | Equivalent |
| --- | --- |
| `OnHeartbeat` | [RunService.Heartbeat](/docs/reference/engine/classes/RunService.md) |
| `OnPreRender` | [RunService.PreRender](/docs/reference/engine/classes/RunService.md) |
| `OnPreAnimation` | [RunService.PreAnimation](/docs/reference/engine/classes/RunService.md) |
| `OnPreSimulation` | [RunService.PreSimulation](/docs/reference/engine/classes/RunService.md) |
| `OnPostSimulation` | [RunService.PostSimulation](/docs/reference/engine/classes/RunService.md) |
| `OnSimulate` | [RunService:BindToSimulation()](/docs/reference/engine/classes/RunService.md) |

The collection subscribes to each [RunService](/docs/reference/engine/classes/RunService.md) event **once** and
dispatches to its members internally, rather than every instance holding its
own connection. The callback fires once per step **for each instance** in the
collection and receives the instance followed by the step's `deltaTime`:

```lua
local CollectionService = game:GetService("CollectionService")

local collection = CollectionService:CreateCollection("Part")

function collection.OnHeartbeat(instance, deltaTime)

end
```

#### Event, Property, and Attribute Wrappers

Beyond the [RunService](/docs/reference/engine/classes/RunService.md) aliases, a collection can wrap any signal on its
member instances. In these callbacks, `X` stands for the name of an **event**,
**property**, or **attribute**.

- `function collection.OnX(instance, ...)` wraps the `X` event on each member
  and the callback receives the instance followed by that event's arguments.
  For example, `OnTouched` wraps [BasePart.Touched](/docs/reference/engine/classes/BasePart.md).

  ```lua
  local CollectionService = game:GetService("CollectionService")

  local collection = CollectionService:CreateCollection("Part")

  function collection.OnTouched(part, otherPart)
  	print(part, otherPart)
  end
  ```

- `function collection.OnPropertyChanged.X(instance)` fires when property `X`
  changes on a member, equivalent to connecting
  [GetPropertyChangedSignal()](/docs/reference/engine/classes/Instance.md) on
  each instance.

  ```lua
  local CollectionService = game:GetService("CollectionService")

  local collection = CollectionService:CreateCollection("Part")

  function collection.OnPropertyChanged.Color(instance)
  	print(instance)
  end
  ```

- `function collection.OnAttributeChanged.X(instance)` fires when attribute
  `X` changes on a member, equivalent to
  [GetAttributeChangedSignal()](/docs/reference/engine/classes/Instance.md).

  ```lua
  local CollectionService = game:GetService("CollectionService")

  local collection = CollectionService:CreateCollection("Humanoid")

  function collection.OnAttributeChanged.CharacterHealth(instance)
  	print(instance)
  end
  ```

Note that a single collection can match instances of different classes, so a
wrapped signal may not apply to every member:

- If a member does **not** have the signal or property named by the callback,
  that member **silently ignores** the assignment. For example, a collection
  matching both [Part](/docs/reference/engine/classes/Part.md) and [Folder](/docs/reference/engine/classes/Folder.md) can safely define `OnTouched`,
  but only the [Parts](/docs/reference/engine/classes/Part.md) respond.
- If a callback names an event or property that exists **nowhere** in the API
  (for example a misspelled `OnToched`), an error is raised at assignment
  time.

#### Typing and Autocomplete

When the query constrains the class of its matches, the collection is typed
accordingly and callbacks are typed to match. For example,
[CreateCollection("Part.TagName")](/docs/reference/engine/classes/CollectionService.md)
yields a collection whose callbacks receive a [Part](/docs/reference/engine/classes/Part.md), and autocomplete
only suggests callbacks relevant to that class (so
`collection.OnTouched(part: Part, other: BasePart)` is suggested, but not for
a query that cannot match a [BasePart](/docs/reference/engine/classes/BasePart.md)). When no type can be inferred
from the query, the first argument defaults to [Instance](/docs/reference/engine/classes/Instance.md).

## Code Samples

**Collection Lifecycle and Events**

Creates a [Collection](/docs/reference/engine/datatypes/Collection.md) of leaf parts and declares its behavior with
lifecycle, [RunService](/docs/reference/engine/classes/RunService.md), instance event, and property change callbacks,
then sets every current leaf green with [Collection:ForEach()](/docs/reference/engine/datatypes/Collection.md).

```lua
local CollectionService = game:GetService("CollectionService")

-- A live collection of parts tagged "MapleLeaf" that are direct children of a model tagged "MapleTree"
local mapleLeaves: Collection = CollectionService:CreateCollection("Model.MapleTree > Part.MapleLeaf")

local function sway(leaf: Part, deltaTime: number)
	leaf.CFrame *= CFrame.fromEulerAnglesXYZ(0, math.rad(20) * deltaTime, 0)
end

local function fall(leaf: Part)
	leaf.Anchored = false
end

-- OnAdded fires once for every leaf already matching, then for each new match
function mapleLeaves.OnAdded(leaf: Part)
	leaf.Material = Enum.Material.Neon
end

-- OnRemoved fires when a leaf stops matching (untagged, reparented out of the tree, or destroyed)
function mapleLeaves.OnRemoved(leaf: Part)
	leaf:Destroy()
end

-- RunService alias: Fires once per heartbeat for each leaf in the collection
function mapleLeaves.OnHeartbeat(leaf: Part, deltaTime: number)
	sway(leaf, deltaTime)
end

-- Instance-event wrapper: OnTouched wraps BasePart.Touched
-- Collection members without a Touched event silently ignore this assignment
function mapleLeaves.OnTouched(leaf: Part, other: BasePart)
	fall(leaf)
end

-- Property-changed wrapper: React when a leaf turns brown
function mapleLeaves.OnPropertyChanged.Color(leaf: Part)
	if leaf.Color == Color3.fromRGB(124, 92, 70) then
		fall(leaf)
	end
end

-- Imperatively set every leaf currently in the collection green
mapleLeaves:ForEach(function(leaf: Part)
	leaf.Color = Color3.fromRGB(0, 255, 0)
end)
```

## Properties

### Collection.Enabled

**Type:** `bool`

Defaults to `true`. Setting this to `false` fires `OnRemoved` for every
instance currently in the collection and stops all of its callbacks.
Setting it back to `true` re-evaluates the query and fires `OnAdded` again
for every matching instance. Assigning a non-boolean value raises an
error.

## Methods

### Collection:ForEach

**Signature:** `Collection:ForEach(callback: function)`

Iterates over the instances currently in the collection, calling
`callback` with each one. `ForEach()` operates on a snapshot taken at call
time, so it is safe to add, remove, or destroy instances from within the
callback; instances that begin matching during iteration are not visited.
Calling `ForEach()` after the collection has been destroyed raises an
error.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `callback` | `function` |  | A function called with each instance currently in the collection. |

### Collection:Destroy

**Signature:** `Collection:Destroy()`

Stops firing the collection's callbacks, releases the connections it
manages on its members, and empties its set of instances. After a
collection is destroyed, calling [ForEach()](/docs/reference/engine/datatypes/Collection.md)
raises an error. A collection is also destroyed automatically when the
root passed to
[CreateCollection()](/docs/reference/engine/classes/CollectionService.md) is
destroyed.