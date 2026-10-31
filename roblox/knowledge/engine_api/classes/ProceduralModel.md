---
name: ProceduralModel
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Model
  - PVInstance
  - Instance
  - Object
type: class
memory_category: BaseParts
summary: "Procedural models support edit-time procedural generation. Instead of manually constructing model content, a procedural model generates its contents automatically in response to parameter changes."
---

# Class: ProceduralModel

> Procedural models support edit-time procedural generation. Instead of manually
> constructing model content, a procedural model generates its contents
> automatically in response to parameter changes.

## Description

`ProceduralModel` inherits from [Model](/docs/reference/engine/classes/Model.md) and supports edit-time
procedural generation of its contents. Instead of manually constructing model
content, a procedural model generates its contents automatically in response
to parameter changes.

Generation is defined by a **generator module**, a [ModuleScript](/docs/reference/engine/classes/ModuleScript.md)
referenced by the [Generator](/docs/reference/engine/classes/ProceduralModel.md) property. The
engine invokes the module's `OnGenerate` function to produce the model's
contents.

A procedural model regenerates when any of the following inputs change:

- The [Size](/docs/reference/engine/classes/ProceduralModel.md) property of the procedural model,
  which defines a bounding box for the model to generate within.
- Any attributes on the procedural mode, as defined by the generator module.
- The generator's module sandboxing configuration (`Sandboxed` and
  `Capabilities`).
- The source code of the generator module.

When any of these inputs change, the engine schedules regeneration. This
scheduled regeneration is performed by calling `OnGenerate` and applying its
results once it returns. In most cases, generation happens within the same
frame, but can be deferred to maintain performance.

## Properties

### Property: ProceduralModel.GenerationError

```json
{
  "type": "string",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Basic"
  ]
}
```

If the generator module encounters an error during generation, the
contents of the `ProceduralModel` are replaced with an error state
placeholder. The error is stored in the `GenerationError` property to give
you visibility into why the generation failed.

### Property: ProceduralModel.Generator

```json
{
  "type": "ModuleScript",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Basic"
  ]
}
```

A reference to a [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) containing code that defines how the
`ProceduralModel` generates its contents in response to parameter changes.

Setting `Generator` triggers generation using the new generator module.
The `Attributes` table exported by the module is automatically applied as
default attribute values on the `ProceduralModel`.

Clearing `Generator` preserves the current contents of the
`ProceduralModel`, and prevents further generation until a new generator
is assigned.

Guidelines for writing the generator module's `OnGenerate` function:

- Only write results into the provided `targetContainer`. `OnGenerate`
  should not modify the [DataModel](/docs/reference/engine/classes/DataModel.md) directly; writes elsewhere may
  not interact correctly with engine systems.
- `OnGenerate` is allowed to yield and call yielding methods (for example,
  [GeometryService](/docs/reference/engine/classes/GeometryService.md) CSG APIs). Generation is considered complete
  whenever `OnGenerate` returns.
- Calling `parameters:Pause()` inside long-running loops lets the engine
  break up work. It only yields when needed to avoid dropping frames, so
  calls are low-cost when the frame budget is not exceeded.

**Default Generator Module**

The default generator module that Studio inserts when a new
[ProceduralModel](/docs/reference/engine/classes/ProceduralModel.md) is created. It illustrates the required shape of a
generator module: an `Attributes` table of default attribute values, and an
`OnGenerate` function that populates the `targetContainer` based on the passed
`parameters`. Returning the module makes it assignable to
[ProceduralModel.Generator](/docs/reference/engine/classes/ProceduralModel.md).

```lua
-- A generator module is a ModuleScript that defines how a ProceduralModel builds its contents.
-- See https://create.roblox.com/docs/reference/engine/classes/ProceduralModel for details.
--
-- To be used as a generator, the ModuleScript must return a table with two fields:
--   * `Attributes`  - a table of default values. Each key becomes an attribute on every
--                     ProceduralModel that uses this generator. Users can then tweak these
--                     attributes in the Properties panel to re-run generation with new inputs.
--   * `OnGenerate`  - a function the engine calls to (re)build the model's contents.
--
-- Nothing about this script or its placement is special. It can live anywhere in the DataModel
-- and the `Generator` property on a ProceduralModel can be reassigned to point at it.

-- The type annotations below are optional but documented here so the required shape is explicit.

-- `GenerationFunctionParams` is passed to `OnGenerate` every time generation runs. It exposes:
--   * `Attributes` - the current attribute values on the ProceduralModel.
--   * `Size`       - the bounding volume to generate within (from `ProceduralModel.Size`).
--   * `Pause`      - a cooperative yield. Call `parameters:Pause()` inside long loops so large
--                    generations don't stall the calling thread; the engine may resume you later.
type GenerationFunctionParams<Attributes> = {
	Attributes: Attributes,
	Size: Vector3,
	Pause: (self: GenerationFunctionParams<Attributes>) -> (),
}

-- `GeneratorModuleDefinition` is the table the ModuleScript must return.
-- `OnGenerate` must not return a value; parent generated instances into `targetContainer` instead.
-- Anything parented to `targetContainer` (or its descendants) becomes the output of generation.
type GeneratorModuleDefinition<Attributes> = {
	Attributes: Attributes,
	OnGenerate: (
		parameters: GenerationFunctionParams<Attributes>,
		targetContainer: GeneratedFolder
	) -> (),
}

-- Default attributes. Each entry here shows up as an editable attribute on the ProceduralModel.
-- A fixed `RandomSeed` keeps generation deterministic: the same inputs always produce the same
-- output, which is important because generation may run many times as the user edits properties.
local defaultAttributes = {
	BorderThickness = 1,
	RandomSeed = 142376088,
}

local Generator: GeneratorModuleDefinition<typeof(defaultAttributes)> = {
	Attributes = defaultAttributes,
	OnGenerate = function(parameters, targetContainer)
		-- Inputs. `parameters.Attributes` reflects whatever the user has set on the
		-- ProceduralModel; `parameters.Size` is the bounding box to build into.
		local borderThickness = parameters.Attributes.BorderThickness
		local random = Random.new(parameters.Attributes.RandomSeed)
		local size = parameters.Size

		-- Derived values. Seeded `random` above makes these reproducible per RandomSeed.
		local minSize = math.min(size.X, size.Y, size.Z)
		local baseColor = Color3.fromHSV(random:NextNumber(0.5, 0.8), 0.7, 0.8)
		local outlineColor = Color3.fromHSV(random:NextNumber(), 0.4, 0.25)

		-- Small helpers to make the construction below read top-to-bottom. You don't need
		-- helpers like these to write a generator; they just cut down on repetition.
		local function assignProperties(instance: Instance, properties: { [string]: unknown })
			-- Set Parent last so other properties are in place before the instance enters
			-- the DataModel and fires Changed events.
			for name, value in properties do
				if name ~= "Parent" then
					(instance :: any)[name] = value
				end
			end
			if properties.Parent ~= nil then
				instance.Parent = properties.Parent :: Instance
			end
			return instance
		end

		local function createInstance(className: string, properties: { [string]: unknown })
			return assignProperties(Instance.new(className), properties)
		end

		local function createPartWithDefaults(properties: { [string]: unknown })
			-- Generated parts are typically anchored and non-colliding; override per-part as needed.
			local part = createInstance("Part", {
				Anchored = true,
				CanCollide = false,
				Color = baseColor,
				Material = Enum.Material.SmoothPlastic,
				BottomSurface = Enum.SurfaceType.Smooth,
				TopSurface = Enum.SurfaceType.Smooth,
			})
			return assignProperties(part, properties)
		end

		-- Everything below parents into `targetContainer`, which is how instances become
		-- part of the generated output. Instances not parented here are discarded.

		-- Invisible bounding part used as the billboard adornee.
		local bounds = createPartWithDefaults({
			Name = "Bounds",
			Parent = targetContainer,
			Transparency = 1,
			Size = size,
		})

		-- A recessed platform with a border outline underneath it.
		local base = createPartWithDefaults({
			Name = "PlatformBase",
			Parent = targetContainer,
			Color = baseColor,
			CFrame = CFrame.new(0, (-size.Y + 1) / 2, 0),
			Size = Vector3.new(
				size.X - 2 * borderThickness,
				1.01,
				size.Z - 2 * borderThickness
			),
		})
		local outline = createPartWithDefaults({
			Name = "PlatformOutline",
			Parent = targetContainer,
			Color = outlineColor,
			Position = Vector3.yAxis * (-size.Y + 1) / 2,
			Size = Vector3.new(size.X, 1, size.Z),
		})

		-- "Hello World!" billboard. Generators can create any instance type, not just parts.
		local billboard = createInstance("BillboardGui", {
			Name = "Text",
			Parent = targetContainer,
			Adornee = bounds,
			LightInfluence = 0,
			Size = UDim2.fromScale(minSize, minSize),
		})
		local textLabel = createInstance("TextLabel", {
			Name = "HelloWorld",
			Parent = billboard,
			AnchorPoint = Vector2.new(0.5, 0.5),
			BackgroundTransparency = 1,
			Position = UDim2.fromScale(0.5, 0.5),
			Size = UDim2.fromScale(1, 1),
			Text = "Hello World!",
			TextColor3 = baseColor,
			TextScaled = true,
			TextStrokeTransparency = 0,
		})
		local textStroke = createInstance("UIStroke", {
			Parent = textLabel,
			Color = outlineColor,
			Thickness = borderThickness * 3,
		})
	end,
}

-- Returning the module definition is what makes this ModuleScript usable as a `Generator`.
return Generator
```

**Classic Ladder Generator Module**

A minimal generator module that builds a ladder from rungs and two side posts,
sized to fit the [Size](/docs/reference/engine/classes/ProceduralModel.md) of the ProceduralModel that
references it. Demonstrates the required shape of a generator (an `Attributes`
table plus an `OnGenerate` function) and shows how to use `parameters:Pause()`
to cooperatively yield during large generations.

```lua
-- A generator module is a ModuleScript that returns a table with `Attributes` and `OnGenerate`.
-- Assigning this ModuleScript to a ProceduralModel's `Generator` property runs `OnGenerate`
-- whenever the model's Size, attributes, or the module source changes.
-- See https://create.roblox.com/docs/reference/engine/classes/ProceduralModel.

local ClassicRobloxLadderGenerator = {}

-- Default attribute values. Each key becomes an editable attribute on any ProceduralModel that
-- uses this generator, and shows up in the Studio Properties panel under Attributes. Editing any
-- of them re-runs `OnGenerate` with the new values.
ClassicRobloxLadderGenerator.Attributes = {
	RungSpacing = 2,
	RungThickness = 1,
	PostSize = 1,
	Color = Color3.new(0.5, 0.3, 0),
}

-- `OnGenerate` is called by the engine to build the model's contents.
-- Contract:
--   * `parameters.Size`       - the bounding box (from `ProceduralModel.Size`) to build within.
--   * `parameters.Attributes` - current attribute values on the ProceduralModel.
--   * `parameters:Pause()`    - cooperative yield; call inside long loops so large generations
--                               don't stall the thread.
--   * `targetContainer`       - anything parented here (or to its descendants) becomes the output.
--   * Do not return a value from `OnGenerate`; outputs are communicated via `targetContainer`.
ClassicRobloxLadderGenerator.OnGenerate = function(parameters, targetContainer)
	local size = parameters.Size
	local rungThickness = parameters.Attributes.RungThickness
	local postSize = parameters.Attributes.PostSize
	local count = (size.Y - rungThickness) // parameters.Attributes.RungSpacing + 1

	local function createPart(position, size)
		local part = Instance.new("Part")
		part.Size = size
		part.Position = position
		part.Anchored = true
		part.Color = parameters.Attributes.Color
		part.TopSurface = Enum.SurfaceType.Smooth
		part.BottomSurface = Enum.SurfaceType.Smooth
		-- Parenting into `targetContainer` is what adds the part to the generated output.
		part.Parent = targetContainer
	end

	-- Rungs, stacked from the bottom of the bounding box upward.
	local position = Vector3.new(0, -size.Y / 2 + rungThickness / 2, 0)
	for i = 1, count do
		-- Yield between rungs so a ladder with many rungs doesn't block the thread.
		parameters:Pause()
		createPart(position, Vector3.new(size.X - 2 * postSize, rungThickness, size.Z))
		position += Vector3.new(0, parameters.Attributes.RungSpacing, 0)
	end

	-- Left and right side posts spanning the full height.
	createPart(Vector3.new(-0.5 * size.X + postSize / 2, 0, 0), Vector3.new(postSize, size.Y, size.Z))
	createPart(Vector3.new(0.5 * size.X - postSize / 2, 0, 0), Vector3.new(postSize, size.Y, size.Z))
end

-- Returning the module definition is what makes this ModuleScript usable as a `Generator`.
return ClassicRobloxLadderGenerator
```

### Property: ProceduralModel.Size

```json
{
  "type": "Vector3",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Transform",
  "capabilities": [
    "Basic"
  ]
}
```

The `Size` of a `ProceduralModel` defines the bounding volume used for
generation.

In a standard model, size is a derived output value based on its contents
and can be queried using [GetBoundingBox()](/docs/reference/engine/classes/Model.md).
A procedural model inverts this relationship: `Size` is an **input** that
determines how generation occurs, and is explicitly set as a property.

The `Size` property represents the **physical** dimensions of the
`ProceduralModel` and is affected by [ScaleTo](/docs/reference/engine/classes/Model.md). The
`OnGenerate` function in a generator module doesn't need to account for
position or scaling: it produces a result of the specified `Size` around
the origin at a scale of 1, and the procedural model system automatically
uses [PivotTo()](/docs/reference/engine/classes/PVInstance.md) and
[ScaleTo()](/docs/reference/engine/classes/Model.md) to place and scale the output in the
`ProceduralModel`.

## Methods

### Method: ProceduralModel:ForceGeneration

**Signature:** `ProceduralModel:ForceGeneration(): boolean`

Generation is normally scheduled soon after a parameter changes so work
can be deferred for performance. `ForceGeneration()` instead runs any
pending generation synchronously and returns whether the
[ProceduralModel](/docs/reference/engine/classes/ProceduralModel.md) is up to date.

If nothing is pending, returns `true` without regenerating. Otherwise runs
the generator to completion under a hard timeout, then returns `true` only
if the model is no longer waiting to regenerate and produced no
[GenerationError](/docs/reference/engine/classes/ProceduralModel.md). On failure or
timeout, returns `false` and re-queues normal scheduled generation. Unlike
scheduled generation, a forced generation doesn't yield to preserve the
frame budget, so `parameters:Pause()` inside the generator returns without
pausing.

Throws if called from within a generator's `OnGenerate` function.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `boolean` — Whether the `ProceduralModel` is up to date after the call: `true` if
generation completed successfully or nothing needed to be regenerated,
`false` otherwise.

### Method: ProceduralModel:WaitForGenerationAsync

**Signature:** `ProceduralModel:WaitForGenerationAsync(): boolean`

Generation is scheduled to run as soon as possible after a parameter
changes, but not immediately. Use `WaitForGenerationAsync()` to wait for
generation to complete before parameters are changed.

This method errors if called on a [ProceduralModel](/docs/reference/engine/classes/ProceduralModel.md) that is not in
the [DataModel](/docs/reference/engine/classes/DataModel.md) because generation isn't performed for instances
without a parent.

This method returns `false` if the [ProceduralModel](/docs/reference/engine/classes/ProceduralModel.md) is removed from
the [DataModel](/docs/reference/engine/classes/DataModel.md) while generation is in progress, since this cancels
the operation.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `boolean` — Was the generation successful?

**Failed generation**

This code snippet simulates a failed generation.

```lua
local proceduralModel = ...
proceduralModel:SetAttribute("ThrowAnError", true) --> Deliberately fail
print(proceduralModel:WaitForGenerationAsync()) --> false
```

## Inherited Members

### From [Model](/docs/reference/engine/classes/Model.md)

- **Property `LevelOfDetail`** (`ModelLevelOfDetail`): Sets the level of detail on the model for experiences with instance
- **Property `ModelStreamingMode`** (`ModelStreamingMode`): Controls the model streaming behavior on Models when
- **Property `PrimaryPart`** (`BasePart`): The primary part of the Model, or `nil` if not explicitly set.
- **Property `Scale`** (`float`): Editor-only property used to scale the model around its pivot. Setting
- **Property `WorldPivot`** (`CFrame`): Determines where the pivot of a Model which does **not** have a
- **Method `AddPersistentPlayer(playerInstance?: Player): ()`**: Sets this model to be persistent for the specified player.
- **Method `BreakJoints(): ()`**: Breaks connections between `BaseParts`, including surface connections with *(deprecated)*
- **Method `breakJoints(): ()`**:  *(deprecated)*
- **Method `GetBoundingBox(): Tuple`**: Returns a description of a volume that contains all parts of a Model.
- **Method `GetExtentsSize(): Vector3`**: Returns the size of the smallest bounding box that contains all of the
- **Method `GetModelCFrame(): CFrame`**: This value historically returned the CFrame of a central position in the *(deprecated)*
- **Method `GetModelSize(): Vector3`**: Returns the Vector3 size of the Model. *(deprecated)*
- **Method `GetPersistentPlayers(): List<Player>`**: Returns all the Player objects that this model object is
- **Method `GetPrimaryPartCFrame(): CFrame`**: Returns the CFrame of the model's Model.PrimaryPart. *(deprecated)*
- **Method `GetScale(): float`**: Returns the canonical scale of the model, which defaults to 1 for newly
- **Method `MakeJoints(): ()`**: Goes through all BaseParts in the Model. If any *(deprecated)*
- **Method `makeJoints(): ()`**:  *(deprecated)*
- **Method `move(location: Vector3): ()`**:  *(deprecated)*
- **Method `MoveTo(position: Vector3): ()`**: Moves the PrimaryPart to the given position. If
- **Method `moveTo(location: Vector3): ()`**:  *(deprecated)*
- **Method `RemovePersistentPlayer(playerInstance?: Player): ()`**: Makes this model no longer persistent for the specified player.
- **Method `ResetOrientationToIdentity(): ()`**: Resets the rotation of the model's parts to the previously set identity *(deprecated)*
- **Method `ScaleTo(newScaleFactor: float): ()`**: Sets the scale factor of the model, adjusting the sizing and location of
- **Method `SetIdentityOrientation(): ()`**: Sets the identity rotation of the given model, allowing you to reset the *(deprecated)*
- **Method `SetPrimaryPartCFrame(cframe: CFrame): ()`**: Sets the BasePart.CFrame of the model's Model.PrimaryPart. *(deprecated)*
- **Method `TranslateBy(delta: Vector3): ()`**: Shifts a Model by the given Vector3 offset, preserving

### From [PVInstance](/docs/reference/engine/classes/PVInstance.md)

- **Property `Origin`** (`CFrame`): Editor-only property that reads and sets the world CFrame of
- **Property `Pivot Offset`** (`CFrame`): Editor-only property that displays and edits the pivot's CFrame
- **Method `GetPivot(): CFrame`**: Gets the pivot of a PVInstance.
- **Method `PivotTo(targetCFrame: CFrame): ()`**: Transforms the PVInstance along with all of its descendant

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