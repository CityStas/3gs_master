---
name: GeometryService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "Service containing geometric operations."
---

# Class: GeometryService

> Service containing geometric operations.

## Description

Service containing geometric operations not directly related to specific
objects.

## Methods

### Method: GeometryService:CalculateConstraintsToPreserve

**Signature:** `GeometryService:CalculateConstraintsToPreserve(source: Instance, destination: Array, options?: Dictionary): Array`

Returns a table of [Constraints](/docs/reference/engine/classes/Constraint.md) and
[Attachments](/docs/reference/engine/classes/Attachment.md) which you may choose to preserve, along
with their respective parents. Iterating over this table lets you decide
whether to reparent recommended constraints and attachments to their
respective parents.

For more information and detailed examples, see
https://create.roblox.com/docs/parts/solid-modeling#in-experience-solid-modeling.

*Security: None · Thread Safety: Unsafe · Capabilities: CSG*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `source` | `Instance` |  | An original object that the solid modeling operation was performed on, for example `part` in [UnionAsync()](/docs/reference/engine/classes/GeometryService.md). |
| `destination` | `Array` |  | Array of resulting [BaseParts](/docs/reference/engine/classes/BasePart.md) from the solid modeling operation, for example the results of [UnionAsync()](/docs/reference/engine/classes/GeometryService.md). |
| `options` | `Dictionary` | `nil` | Options dictionary for the method:  - `tolerance` — The distance tolerance, in regards to   [Attachment](/docs/reference/engine/classes/Attachment.md) preservation, between the attachment and the   closest point on the original part's surface versus the closest   point on the resulting part's surface. If the resulting distance   following the solid modeling operation is greater than this value,   the [Parent](/docs/reference/engine/classes/Instance.md) of attachments and their   associated constraints will be `nil` in the returned recommendation   table. - `weldConstraintPreserve` — A [WeldConstraintPreserve](/docs/reference/engine/enums/WeldConstraintPreserve.md) enum   value describing how [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md) are   preserved in the resulting recommendation table. - `dropAttachmentsWithoutConstraints` — Boolean with default of   `true`. If set to `false`, [Attachments](/docs/reference/engine/classes/Attachment.md) that have   no [Constraints](/docs/reference/engine/classes/Constraint.md) will be preserved. |

**Returns:** `Array` — Table containing information for general case
[Constraints](/docs/reference/engine/classes/Constraint.md),
[NoCollisionConstraints](/docs/reference/engine/classes/NoCollisionConstraint.md), and
[WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md). In cases where an
[Attachment](/docs/reference/engine/classes/Attachment.md) or [Constraint](/docs/reference/engine/classes/Constraint.md) should be dropped, its
respective parent will be `nil`.

For general case [Constraints](/docs/reference/engine/classes/Constraint.md) such as
[HingeConstraint](/docs/reference/engine/classes/HingeConstraint.md):

| Key | Type |
| --- | --- |
| `Attachment` | [Attachment](/docs/reference/engine/classes/Attachment.md) |
| `Constraint` | [Constraint](/docs/reference/engine/classes/Constraint.md) or `nil` |
| `AttachmentParent` | [BasePart](/docs/reference/engine/classes/BasePart.md) or `nil` |
| `ConstraintParent` | [BasePart](/docs/reference/engine/classes/BasePart.md) or `nil` |

For [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md):

| Key | Type |
| --- | --- |
| `WeldConstraint` | [WeldConstraint](/docs/reference/engine/classes/WeldConstraint.md) |
| `WeldConstraintParent` | [BasePart](/docs/reference/engine/classes/BasePart.md) or `nil` |
| `WeldConstraintPart0` | [BasePart](/docs/reference/engine/classes/BasePart.md) |
| `WeldConstraintPart1` | [BasePart](/docs/reference/engine/classes/BasePart.md) |

For [NoCollisionConstraints](/docs/reference/engine/classes/NoCollisionConstraint.md):

| Key | Type |
| --- | --- |
| `NoCollisionConstraint` | [NoCollisionConstraint](/docs/reference/engine/classes/NoCollisionConstraint.md) |
| `NoCollisionConstraintParent` | [BasePart](/docs/reference/engine/classes/BasePart.md) or `nil` |
| `NoCollisionConstraintPart0` | [BasePart](/docs/reference/engine/classes/BasePart.md) |
| `NoCollisionConstraintPart1` | [BasePart](/docs/reference/engine/classes/BasePart.md) |

**Preserve Constraints**

The following example shows how to preserve [Attachments](/docs/reference/engine/classes/Attachment.md) and
[Constraints](/docs/reference/engine/classes/Constraint.md) based on a recommended table produced by
[CalculateConstraintsToPreserve()](/docs/reference/engine/classes/GeometryService.md).

```lua
local GeometryService = game:GetService("GeometryService")
local main, other = workspace.Part1, workspace.Part2

local success, newParts = pcall(function()
	return GeometryService:SubtractAsync(main, {other})
end)
if success and newParts then
	for _, p in newParts do p.Parent = workspace end

	for _, rec in GeometryService:CalculateConstraintsToPreserve(main, newParts) do
		if rec.Constraint then
			rec.Constraint.Parent = rec.ConstraintParent
		end
	end
end
main:Destroy()
other:Destroy()
```

### Method: GeometryService:FragmentAsync

**Signature:** `GeometryService:FragmentAsync(part: BasePart, sites: Array, options?: Dictionary): Array`

Breaks a [BasePart](/docs/reference/engine/classes/BasePart.md) into multiple [MeshPart](/docs/reference/engine/classes/MeshPart.md) instances,
according to the pattern of points passed in, by using voronoi
decomposition. [Terrain](/docs/reference/engine/classes/Terrain.md) is not supported. Similar to
[Clone()](/docs/reference/engine/classes/Instance.md), the returned parts have no set
[Parent](/docs/reference/engine/classes/Instance.md).

For more information and detailed examples, see
https://create.roblox.com/docs/parts/solid-modeling#in-experience-solid-modeling.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: CSG*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `part` | `BasePart` |  | A [Part](/docs/reference/engine/classes/Part.md), [PartOperation](/docs/reference/engine/classes/PartOperation.md), or [MeshPart](/docs/reference/engine/classes/MeshPart.md) to operate on. |
| `sites` | `Array` |  | Array of `Vector3` defining the site positions. Each site will become a separate part. You can also provide a jagged 2D array of `Vector3` by including inner arrays of `Vector3` as elements of the outer array. Each inner array will have all of its voronoi cells merged into a single part. [GeometryService:GenerateFragmentSites](/docs/reference/engine/classes/GeometryService.md) can be used to easily create this input. |
| `options` | `Dictionary` | `nil` | Options table containing all the controls for the method:  - `CollisionFidelity` — The value of   [CollisionFidelity](/docs/reference/engine/classes/TriangleMeshPart.md) in the   resulting parts, with one caveat: If a 2D array of sites is   provided, this collision fidelity will only be applied to parts   which came from more than one site. The others will be given `Hull`   precision. - `RenderFidelity` — The value of   [RenderFidelity](/docs/reference/engine/classes/MeshPart.md) in the resulting   parts. - `FluidFidelity` — The value of   [FluidFidelity](/docs/reference/engine/classes/TriangleMeshPart.md) in the   resulting parts. - `SplitApart` — Boolean controlling whether a part should be split   into multiple parts if it contains multiple connected components.   Default is `true` (split). |

**Returns:** `Array` — Array of [MeshPart](/docs/reference/engine/classes/MeshPart.md) along with mapping info. Each array element
is a Dictionary with two elements:
`{ “Instance”: instance, “Index”: index }`. `Index` is the index in
the outer array of sites; in other words, it tells you which group of
sites this instance came from. Note that it is possible for multiple
instances to have the same index, if SplitApart is `true`.

**Fragment a Part**

This example shatters the entire input part into pieces.

```lua
local GeometryService = game:GetService("GeometryService")

local inputPart = Instance.new("Part")
inputPart.Position = Vector3.new(0, 0.7, 20)

local sites = GeometryService:GenerateFragmentSites(inputPart)

local success, fragments = pcall( function()
	return GeometryService:FragmentAsync(inputPart, sites)
end)
if success and fragments then
	for _, item in fragments do
		local instance = item.Instance
		instance.Parent = workspace
	end
end
```

### Method: GeometryService:GenerateFragmentSites

**Signature:** `GeometryService:GenerateFragmentSites(part: BasePart, options?: Dictionary): Array`

Provides an array of positions which can easily be passed into
[FragmentAsync()](/docs/reference/engine/classes/GeometryService.md) to perform common
types of destruction: Fragmenting an entire [BasePart](/docs/reference/engine/classes/BasePart.md) into pieces,
or a localized area of a [BasePart](/docs/reference/engine/classes/BasePart.md) into pieces.

The positions outputted are partially random, so the output should not be
relied on to look exactly the same as the first time it is run with the
same parameters.

For more information and detailed examples, see
https://create.roblox.com/docs/parts/solid-modeling#in-experience-solid-modeling.
Luau code to mimic this API has also been provided on that page, which can
be freely modified if a slightly different effect is desired.

*Security: None · Thread Safety: Unsafe · Capabilities: CSG*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `part` | `BasePart` |  | The [Part](/docs/reference/engine/classes/Part.md), [PartOperation](/docs/reference/engine/classes/PartOperation.md), or [MeshPart](/docs/reference/engine/classes/MeshPart.md) which you are planning to pass into [FragmentAsync()](/docs/reference/engine/classes/GeometryService.md). This is necessary to make the fragment site generation and the subsequent [FragmentAsync()](/docs/reference/engine/classes/GeometryService.md) call efficient. |
| `options` | `Dictionary` | `nil` | Options table containing all the controls for the method:  - `SiteSpacing` — The approximate distance between sites, which   directly corresponds to the diameter of the resulting fragments. If   not specified, a reasonable value will be chosen. - `Origin` — If provided, this will be the center of the area to be   fragmented. If not provided, the entire object will be fragmented. - `Radius` — If provided, this will be the center of the area to be   fragmented. Either `Origin` and `Radius` should both be provided, or   neither. |

**Returns:** `Array` — An array of `Vector3` which is typically passed into
[FragmentAsync()](/docs/reference/engine/classes/GeometryService.md). The output
depends on the options provided. If `Origin` and `Radius` are
provided, then the output array will contain several `Vector3`
elements which will all be located within the radius, but the first
element of the array will be an inner array containing many `Vector3`
sites which are outside the radius. If `Origin` and `Radius` are not
provided, the output will simply be an array of `Vector3` positions
within the extents of the input `part`.

**Localized Fragment**

This example shatters the corner of a part into pieces.

```lua
local GeometryService = game:GetService("GeometryService")

local inputPart = workspace.Part
local pos = inputPart.Position + inputPart.Size / 2
local sites = GeometryService:GenerateFragmentSites(inputPart, {Origin = pos, Radius = 1.5})

local success, fragments = pcall( function()
	return GeometryService:FragmentAsync(inputPart, sites)
end)
if success and fragments then
	for _, item in fragments do
		local instance = item.Instance
		instance.Parent = inputPart.Parent
	end
	inputPart:Destroy()
end
```

### Method: GeometryService:IntersectAsync

**Signature:** `GeometryService:IntersectAsync(part: Instance, parts: Array, options?: Dictionary): Array`

Creates one or more [PartOperations](/docs/reference/engine/classes/PartOperation.md) or
[MeshParts](/docs/reference/engine/classes/MeshPart.md) from the intersecting geometry of multiple
parts. Primitive [Parts](/docs/reference/engine/classes/Part.md), [PartOperations](/docs/reference/engine/classes/PartOperation.md),
and [MeshParts](/docs/reference/engine/classes/MeshPart.md) are supported as inputs, but not
[Terrain](/docs/reference/engine/classes/Terrain.md).

Similarly to [Clone()](/docs/reference/engine/classes/Instance.md), the returned parts have no
set [Parent](/docs/reference/engine/classes/Instance.md). In most cases, you should parent the
results to the same place as the main part, then
[Destroy()](/docs/reference/engine/classes/Instance.md) the original parts.

This function replaces [BasePart:IntersectAsync()](/docs/reference/engine/classes/BasePart.md). Go to that page
for a description of the differences.

For more information and detailed examples, see
https://create.roblox.com/docs/parts/solid-modeling#in-experience-solid-modeling.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: CSG*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `part` | `Instance` |  | Main [Part](/docs/reference/engine/classes/Part.md), [PartOperation](/docs/reference/engine/classes/PartOperation.md), or [MeshPart](/docs/reference/engine/classes/MeshPart.md) to operate on. |
| `parts` | `Array` |  | Array of other parts to intersect with the main part. |
| `options` | `Dictionary` | `nil` | Options table containing all the controls for the method:  - `CollisionFidelity` — The value of   [CollisionFidelity](/docs/reference/engine/classes/TriangleMeshPart.md) in the   resulting parts. - `RenderFidelity` — The value of   [RenderFidelity](/docs/reference/engine/classes/PartOperation.md) or   [RenderFidelity](/docs/reference/engine/classes/MeshPart.md) in the resulting   parts. - `FluidFidelity` — The value of   [FluidFidelity](/docs/reference/engine/classes/TriangleMeshPart.md) in the   resulting parts. - `SplitApart` — Boolean controlling whether the objects should all be   kept together or properly split apart. Default is `true` (split). |

**Returns:** `Array` — One or more [PartOperations](/docs/reference/engine/classes/PartOperation.md) or
[MeshParts](/docs/reference/engine/classes/MeshPart.md). If the input contained any
[MeshParts](/docs/reference/engine/classes/MeshPart.md), then the results will always be
[MeshParts](/docs/reference/engine/classes/MeshPart.md).

**Union two parts**

This example intersects the geometry of two blocks.

```lua
local GeometryService = game:GetService("GeometryService")

local mainPart = Instance.new("Part")
local otherPart = Instance.new("Part")
otherPart.Position = Vector3.new(1, 0.5, 1)

local success, newParts = pcall(function()
	return GeometryService:IntersectAsync(mainPart, {otherPart})
end)
if success and newParts then
	for _, newPart in pairs(newParts) do
		newPart.Parent = workspace
	end
end
```

### Method: GeometryService:SubtractAsync

**Signature:** `GeometryService:SubtractAsync(part: Instance, parts: Array, options?: Dictionary): Array`

Creates one or more [PartOperations](/docs/reference/engine/classes/PartOperation.md) or
[MeshParts](/docs/reference/engine/classes/MeshPart.md) consisting of the space occupied by one part
minus the space occupied by the other parts. Primitive [Parts](/docs/reference/engine/classes/Part.md),
[PartOperations](/docs/reference/engine/classes/PartOperation.md), and [MeshParts](/docs/reference/engine/classes/MeshPart.md) are
supported as inputs, but not [Terrain](/docs/reference/engine/classes/Terrain.md).

Similarly to [Clone()](/docs/reference/engine/classes/Instance.md), the returned parts have no
set [Parent](/docs/reference/engine/classes/Instance.md). In most cases, you should parent the
results to the same place as the main part, then
[Destroy()](/docs/reference/engine/classes/Instance.md) the original parts.

This function replaces [BasePart:SubtractAsync()](/docs/reference/engine/classes/BasePart.md). Go to that page
for a description of the differences.

For more information and detailed examples, see
https://create.roblox.com/docs/parts/solid-modeling#in-experience-solid-modeling.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: CSG*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `part` | `Instance` |  | Main [Part](/docs/reference/engine/classes/Part.md), [PartOperation](/docs/reference/engine/classes/PartOperation.md), or [MeshPart](/docs/reference/engine/classes/MeshPart.md) to operate on. |
| `parts` | `Array` |  | Array of parts to subtract from the main part. |
| `options` | `Dictionary` | `nil` | Options table containing all the controls for the method:  - `CollisionFidelity` — The value of   [CollisionFidelity](/docs/reference/engine/classes/TriangleMeshPart.md) in the   resulting parts. - `RenderFidelity` — The value of   [RenderFidelity](/docs/reference/engine/classes/PartOperation.md) or   [RenderFidelity](/docs/reference/engine/classes/MeshPart.md) in the resulting   parts. - `FluidFidelity` — The value of   [FluidFidelity](/docs/reference/engine/classes/TriangleMeshPart.md) in the   resulting parts. - `SplitApart` — Boolean controlling whether the objects should all be   kept together or properly split apart. Default is `true` (split). |

**Returns:** `Array` — One or more [PartOperations](/docs/reference/engine/classes/PartOperation.md) or
[MeshParts](/docs/reference/engine/classes/MeshPart.md). If the input contained any
[MeshParts](/docs/reference/engine/classes/MeshPart.md), then the results will always be
[MeshParts](/docs/reference/engine/classes/MeshPart.md).

**Subtract two parts**

This example subtracts the geometry of two blocks.

```lua
local GeometryService = game:GetService("GeometryService")

local mainPart = Instance.new("Part")
local otherPart = Instance.new("Part")
otherPart.Position = Vector3.new(1, 0.5, 1)

local success, newParts = pcall(function()
	return GeometryService:SubtractAsync(mainPart, {otherPart})
end)
if success and newParts then
	for _, newPart in pairs(newParts) do
		newPart.Parent = workspace
	end
end
```

### Method: GeometryService:SweepPartAsync

**Signature:** `GeometryService:SweepPartAsync(part: BasePart, cframes: Array, options?: Dictionary): MeshPart`

Creates a [MeshPart](/docs/reference/engine/classes/MeshPart.md) which has the shape of the input part
stretched/dragged through the given set of `CFrame` positions. The exact
shape of the result is defined as the union of the convex hulls of each
adjacent pair of `CFrames`.

If a single `CFrame` is provided, the result will be a convex hull of the
input part.

For more information and detailed examples, see
https://create.roblox.com/docs/parts/solid-modeling#in-experience-solid-modeling.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: CSG*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `part` | `BasePart` |  | A [Part](/docs/reference/engine/classes/Part.md), [PartOperation](/docs/reference/engine/classes/PartOperation.md), or [MeshPart](/docs/reference/engine/classes/MeshPart.md) to operate on. |
| `cframes` | `Array` |  | Array of coordinate frames to sweep parts through. |
| `options` | `Dictionary` | `nil` | Options table containing all the controls for the method:  - `CollisionFidelity` — The value of   [CollisionFidelity](/docs/reference/engine/classes/TriangleMeshPart.md) in the   resulting parts. - `RenderFidelity` — The value of   [RenderFidelity](/docs/reference/engine/classes/MeshPart.md) in the resulting   parts. - `FluidFidelity` — The value of   [FluidFidelity](/docs/reference/engine/classes/TriangleMeshPart.md) in the   resulting parts. |

**Returns:** `MeshPart` — A new [MeshPart](/docs/reference/engine/classes/MeshPart.md) with the swept geometry.

**Sweep a Part**

This example sweeps a block through a twisting path of `CFrames`.

```lua
local GeometryService = game:GetService("GeometryService")

local inputPart = Instance.new("Part")
inputPart.Shape = Enum.PartType.Ball

local cframeList = {}
for i = 1, 50 do
	local rotation = CFrame.Angles(0, i * 0.2, 0)
	local position = Vector3.new(0, i * 0.1, -1)
	table.insert(cframeList, rotation * CFrame.new(position))
end

local success, sweptPart = pcall( function()
	return GeometryService:SweepPartAsync(inputPart, cframeList)
end)
if success and sweptPart then
	sweptPart.Parent = workspace
end
```

### Method: GeometryService:UnionAsync

**Signature:** `GeometryService:UnionAsync(part: Instance, parts: Array, options?: Dictionary): Array`

Creates one or more [PartOperations](/docs/reference/engine/classes/PartOperation.md) or
[MeshParts](/docs/reference/engine/classes/MeshPart.md) consisting of the space occupied by one part
plus the space occupied by the other parts. Primitive [Parts](/docs/reference/engine/classes/Part.md),
[PartOperations](/docs/reference/engine/classes/PartOperation.md), and [MeshParts](/docs/reference/engine/classes/MeshPart.md) are
supported as inputs, but not [Terrain](/docs/reference/engine/classes/Terrain.md).

Similarly to [Clone()](/docs/reference/engine/classes/Instance.md), the returned parts have no
set [Parent](/docs/reference/engine/classes/Instance.md). In most cases, you should parent the
results to the same place as the main part, then
[Destroy()](/docs/reference/engine/classes/Instance.md) the original parts.

This function replaces [BasePart:UnionAsync()](/docs/reference/engine/classes/BasePart.md). Go to that page for
a description of the differences.

For more information and detailed examples, see
https://create.roblox.com/docs/parts/solid-modeling#in-experience-solid-modeling.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: CSG*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `part` | `Instance` |  | Main [Part](/docs/reference/engine/classes/Part.md), [PartOperation](/docs/reference/engine/classes/PartOperation.md), or [MeshPart](/docs/reference/engine/classes/MeshPart.md) to operate on. |
| `parts` | `Array` |  | Array of parts to union with the main part. |
| `options` | `Dictionary` | `nil` | Options table containing all the controls for the method:  - `CollisionFidelity` — The value of   [CollisionFidelity](/docs/reference/engine/classes/TriangleMeshPart.md) in the   resulting parts. - `RenderFidelity` — The value of   [RenderFidelity](/docs/reference/engine/classes/PartOperation.md) or   [RenderFidelity](/docs/reference/engine/classes/MeshPart.md) in the resulting   parts. - `FluidFidelity` — The value of   [FluidFidelity](/docs/reference/engine/classes/TriangleMeshPart.md) in the   resulting parts. - `SplitApart` — Boolean controlling whether the objects should all be   kept together or properly split apart. Default is `true` (split). |

**Returns:** `Array` — One or more [PartOperations](/docs/reference/engine/classes/PartOperation.md) or
[MeshParts](/docs/reference/engine/classes/MeshPart.md). If the input contained any
[MeshParts](/docs/reference/engine/classes/MeshPart.md), then the results will always be
[MeshParts](/docs/reference/engine/classes/MeshPart.md).

**Union two parts**

This example combines the geometry of two blocks.

```lua
local GeometryService = game:GetService("GeometryService")

local mainPart = Instance.new("Part")
local otherPart = Instance.new("Part")
otherPart.Position = Vector3.new(1, 0.5, 1)

local success, newParts = pcall(function()
	return GeometryService:UnionAsync(mainPart, {otherPart})
end)
if success and newParts then
	for _, newPart in pairs(newParts) do
		newPart.Parent = workspace
	end
end
```

## Inherited Members

### From [Instance](/docs/reference/engine/classes/Instance.md)

- **Property `Archivable`** (`boolean`): Determines if an Instance and its descendants can be cloned using
- **Property `archivable`** (`boolean`):  *(deprecated, hidden)*
- **Property `Capabilities`** (`SecurityCapabilities`): The set of capabilities allowed to be used for scripts inside this
- **Property `IsInSandbox`** (`boolean`): Indicates whether the instance is inside a sandboxed container.
- **Property `Name`** (`string`): A non-unique identifier of the Instance.
- **Property `Parent`** (`Instance`): Determines the hierarchical parent of the Instance.
- **Property `PredictionMode`** (`PredictionMode`): Reflects the client-side prediction mode applied to the instance under
- **Property `RobloxLocked`** (`boolean`): A deprecated property that used to protect CoreGui objects. *(hidden)*
- **Property `Sandboxed`** (`boolean`): When enabled, the instance can only access abilities in its `Capabilities`
- **Property `UniqueId`** (`UniqueId`): A unique identifier for the instance.
- **Method `AddTag(tag: string): ()`**: Applies a tag to the instance.
- **Method `children(): Instances`**: Returns an array of the object's children. *(deprecated)*
- **Method `ClearAllChildren(): ()`**: This method destroys all of an instance's children.
- **Method `Clone(): Instance`**: Create a copy of an instance and all its descendants, ignoring instances
- **Method `clone(): Instance`**:  *(deprecated)*
- **Method `Destroy(): ()`**: Sets the Instance.Parent property to `nil`, locks the
- **Method `destroy(): ()`**:  *(deprecated)*
- **Method `FindFirstAncestor(name: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorOfClass(className: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorWhichIsA(className: string): Instance?`**: Returns the first ancestor of the Instance for whom
- **Method `FindFirstChild(name: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance found with the given name.
- **Method `findFirstChild(name: string, recursive?: boolean): Instance`**:  *(deprecated)*
- **Method `FindFirstChildOfClass(className: string): Instance?`**: Returns the first child of the Instance whose
- **Method `FindFirstChildWhichIsA(className: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance for whom
- **Method `FindFirstDescendant(name: string): Instance?`**: Returns the first descendant found with the given Instance.Name.
- **Method `GetActor(): Actor?`**: Returns the Actor associated with the Instance, if any.
- **Method `GetAttribute(attribute: string): Variant`**: Returns the value which has been assigned to the given attribute name.
- **Method `GetAttributeChangedSignal(attribute: string): RBXScriptSignal`**: Returns an event that fires when the given attribute changes.
- **Method `GetAttributes(): Dictionary`**: Returns a dictionary of the instance's attributes.
- **Method `GetChildren(): Instances`**: Returns an array containing all of the instance's children.
- **Method `getChildren(): Instances`**:  *(deprecated)*
- **Method `GetDebugId(scopeLength?: int): string`**: Returns a coded string of the debug ID used internally by Roblox.
- **Method `GetDescendants(): Instances`**: Returns an array containing all of the descendants of the instance.
- **Method `GetFullName(): string`**: Returns a string describing the instance's ancestry.
- **Method `GetStyled(name: string, selector: string?): Variant`**: Returns the styled or explicitly modified value of the specified property,
- **Method `GetStyledPropertyChangedSignal(property: string): RBXScriptSignal`**: Returns an event that fires when the given style property changes on the
- **Method `GetTags(): Array`**: Gets an array of all tags applied to the instance.
- **Method `HasTag(tag: string): boolean`**: Check whether the instance has a given tag.
- **Method `IsAncestorOf(descendant: Instance): boolean`**: Returns true if an Instance is an ancestor of the given
- **Method `IsDescendantOf(ancestor: Instance): boolean`**: Returns `true` if an Instance is a descendant of the given
- **Method `isDescendantOf(ancestor: Instance): boolean`**:  *(deprecated)*
- **Method `IsPropertyModified(property: string): boolean`**: Returns `true` if the value stored in the specified property is not equal
- **Method `QueryDescendants(selector: string): Instances`**: Returns an array containing all descendants of the instance that match the
- **Method `Remove(): ()`**: Sets the object's `Parent` to `nil`, and does the same for all its *(deprecated)*
- **Method `remove(): ()`**:  *(deprecated)*
- **Method `RemoveTag(tag: string): ()`**: Removes a tag from the instance.
- **Method `ResetPropertyToDefault(property: string): ()`**: Resets a property to its default value.
- **Method `SetAttribute(attribute: string, value: Variant): ()`**: Sets the attribute with the given name to the given value.
- **Method `WaitForChild(childName: string, timeOut: double): Instance`**: Returns the child of the Instance with the given name. If the
- **Event `AncestryChanged`**: Fires when the Instance.Parent property of this object or one of
- **Event `AttributeChanged`**: Fires whenever an attribute is changed on the Instance.
- **Event `ChildAdded`**: Fires after an object is parented to this Instance.
- **Event `childAdded`**:  *(deprecated)*
- **Event `ChildRemoved`**: Fires after a child is removed from this Instance.
- **Event `DescendantAdded`**: Fires after a descendant is added to the Instance.
- **Event `DescendantRemoving`**: Fires immediately before a descendant of the Instance is removed.
- **Event `Destroying`**: Fires immediately before (or is deferred until after) the instance is
- **Event `StyledPropertiesChanged`**: Fires whenever any style property is changed on the instance, including

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some