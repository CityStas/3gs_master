---
name: GenerationService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "Service that allows developers to generate 3D objects from text prompts."
---

# Class: GenerationService

> Service that allows developers to generate 3D objects from text prompts.

## Description

`GenerationService` enables you to generate 3D objects from text prompts using
Roblox's Cube 3D foundation model. This enables the generation of objects like
environmental props in-experience, as well as fully functional models like
vehicles that drive, planes that fly, and weapons that shoot.

## Methods

### Method: GenerationService:GenerateMeshAsync

**Signature:** `GenerationService:GenerateMeshAsync(inputs: Dictionary, player: Player, options: Dictionary, intermediateResultCallback: Function?): Tuple`

Starts the generation of a new 3D mesh from a text prompt and returns
unique IDs used to track and retrieve the result. Must be called from
server scripts. You can optionally receive intermediate results, such as
the untextured mesh, by providing an `intermediateResultCallback`
function.

After the generation is complete, use
[LoadGeneratedMeshAsync()](/docs/reference/engine/classes/GenerationService.md)
to load and display the generated mesh.

#### Error Codes

| Error                                      | Description                                                              | Recommended action                                                                   |
| ------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| Rate limit exceeded                        | The maximum number of mesh generations has been exceeded for the minute. | Wait until the rate limit resets.                                                    |
| Moderation failed                          | The mesh generation was flagged for moderation.                          | Review and modify the prompt to ensure it adheres to Roblox's moderation guidelines. |
| Internal server error                      | An unexpected issue occurred on the server.                              | Retry the request later or check server status for issues.                           |
| Character limit exceeded                   | The input prompt length for this generation request exceeded the limit.  | Reduce the number of characters in the `Prompt` string of the `input` dictionary.    |
| Service overloaded                         | The service is overloaded.                                               | Retry the request later.                                                             |
| Size dimensions must all be greater than 0 | Invalid size provided.                                                   | Change the size to above `0`.                                                        |

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `inputs` | `Dictionary` |  | A dictionary containing the mesh generation prompts. Currently, the only supported key is the `Prompt` (string) that describes the mesh to generate. |
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) requesting the generation. |
| `options` | `Dictionary` |  | A dictionary for additional generation options to influence the result. The optional `SuggestedSize` key ([Vector3](/docs/reference/engine/datatypes/Vector3.md)) represents a size guide for the generated asset, meaning `GenerationService` will attempt to create a model with a size and proportion similar to the provided [Vector3](/docs/reference/engine/datatypes/Vector3.md), although there is no guarantee on the final output size. |
| `intermediateResultCallback` | `Function?` |  | A callback function triggered with intermediate generation results. Useful for retrieving early mesh versions before textures are applied. |

**Returns:** `Tuple` — A tuple of the generation ID (a unique ID returned for each invocation
of `GenerateMeshAsync()`) and context ID (not currently used).

**Client-Side Mesh Generation**

The following example adds client-side functionality to request mesh
generation from the server and display the results. This code assumes that the
two [RemoteEvent](/docs/reference/engine/classes/RemoteEvent.md) instances created by the server-side example
(`GenerationEvent` and `GenerationResultEvent`) exist inside
[ReplicatedStorage](/docs/reference/engine/classes/ReplicatedStorage.md).

```lua
local GenerationService = game:GetService("GenerationService")
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

-- Reference to RemoteEvent instances created in server-side script
local generationEvent = ReplicatedStorage:WaitForChild("GenerationEvent")
local generationResultEvent = ReplicatedStorage:WaitForChild("GenerationResultEvent")

local player = Players.LocalPlayer

-- Store generated meshes
local generatedMeshes = {}

-- Function to request mesh generation
local function requestMeshGeneration(prompt)
	print("Requesting mesh generation for prompt:", prompt)
	generationEvent:FireServer(prompt)
end

-- Handle generation results from the server
generationResultEvent.OnClientEvent:Connect(function(generationId, isIntermediate)
	if not generationId then
		warn("Generation failed")
		return
	end

	print(isIntermediate and "Loading intermediate result..." or "Loading final result...")

	-- Use generation ID generated on the server to retrieve and load the mesh
	local mesh = GenerationService:LoadGeneratedMeshAsync(generationId)

	if mesh then
		-- Clean up previous mesh if it exists
		if generatedMeshes[isIntermediate and "intermediate" or "final"] then
			generatedMeshes[isIntermediate and "intermediate" or "final"]:Destroy()
		end

		mesh.Parent = workspace

		-- Position the mesh in front of the player
		local character = player.Character
		if character and character:FindFirstChild("HumanoidRootPart") then
			local rootPart = character.HumanoidRootPart
			mesh:PivotTo(rootPart.CFrame * CFrame.new(0, 0, -10))
		end

		-- Store the mesh for cleanup
		generatedMeshes[isIntermediate and "intermediate" or "final"] = mesh
		print(isIntermediate and "Loaded intermediate result" or "Loaded final result")
	else
		warn("Failed to load mesh")
	end
end)

-- Example usage
requestMeshGeneration("toy robot")
```

**Server-Side Mesh Generation**

This setup includes server-side functionality to handle mesh generation
requests from clients.

```lua
local GenerationService = game:GetService("GenerationService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

-- Create a RemoteEvent for client-server communication
local generationEvent = Instance.new("RemoteEvent")
generationEvent.Name = "GenerationEvent"
generationEvent.Parent = ReplicatedStorage

-- Create a RemoteEvent to send generation results back to clients
local generationResultEvent = Instance.new("RemoteEvent")
generationResultEvent.Name = "GenerationResultEvent"
generationResultEvent.Parent = ReplicatedStorage

-- Handle mesh generation requests from clients
generationEvent.OnServerEvent:Connect(function(player, prompt)
	print("Generating mesh for player", player.Name, "with prompt:", prompt)

	-- Generate the mesh on the server
	local success, generationId, contextId = pcall(function()
		return GenerationService:GenerateMeshAsync(
			{ ["Prompt"] = prompt },
			player,
			{},
			function(intermediateType, intermediateGenerationId, intermediateContextId)
				-- Send intermediate result to the requesting client
				generationResultEvent:FireClient(
					player,
					intermediateGenerationId,
					true -- isIntermediate
				)
			end
		)
	end)

	if success then
		-- Send the final generation ID to the client
		generationResultEvent:FireClient(player, generationId, false)
		print("Successfully generated mesh with ID:", generationId)
	else
		generationResultEvent:FireClient(player, nil, false)
		warn("Failed to generate mesh:", generationId)
	end
end)
```

**Button-Triggered Mesh Generation With Suggested Size**

The following example sends the generation request to the server via a parent
[TextButton](/docs/reference/engine/classes/TextButton.md). This code assumes there's a [Part](/docs/reference/engine/classes/Part.md) named `SizeBox`
in the [Workspace](/docs/reference/engine/classes/Workspace.md). It also assumes that the [RemoteEvent](/docs/reference/engine/classes/RemoteEvent.md)
instance created by the server-side example (`GenerationEvent`) exists inside
[ReplicatedStorage](/docs/reference/engine/classes/ReplicatedStorage.md).

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

-- Reference to RemoteEvent instance created in server-side script
local generationEvent = ReplicatedStorage:WaitForChild("GenerationEvent")

local button = script.Parent

local PROMPT = "cabinet"

button.Activated:Connect(function()
	local prompt = PROMPT
	print("Client requesting generation with prompt:", prompt)
	generationEvent:FireServer(prompt)
end)
```

**Server-Side Mesh Generation With Suggested Size**

This server-side script gets the size from a [Part](/docs/reference/engine/classes/Part.md) in the
[Workspace](/docs/reference/engine/classes/Workspace.md) named `SizeBox` and tells the client when the model is
ready.

```lua
local GenerationService = game:GetService("GenerationService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Workspace = game:GetService("Workspace")

-- Create a RemoteEvent for client-server communication
local generationEvent = Instance.new("RemoteEvent")
generationEvent.Name = "GenerationEvent"
generationEvent.Parent = ReplicatedStorage

-- Create a RemoteEvent to send generation results back to clients
local generationResultEvent = Instance.new("RemoteEvent")
generationResultEvent.Name = "GenerationResultEvent"
generationResultEvent.Parent = ReplicatedStorage

local sizeBox = Workspace:WaitForChild("SizeBox")

generationEvent.OnServerEvent:Connect(function(player, prompt)
	-- Get the size from the part
	local boundingBoxSize = sizeBox.Size
	print("Server received request; using SuggestedSize:", boundingBoxSize)
	-- Run the generation in a separate thread
	task.spawn(function()
		local success, generationId = pcall(function()
			return GenerationService:GenerateMeshAsync(
				{ ["Prompt"] = prompt },
				player,
				{ ["SuggestedSize"] = boundingBoxSize } -- Use the size from the box
			)
		end)

		if success and generationId then
			print("Server generation complete; sending ID to client:", generationId)
			-- Tell the client it's ready and provide the position for the new model
			generationResultEvent:FireClient(player, generationId, sizeBox.CFrame)
		else
			warn("Server generation failed:", generationId)
		end
	end)
end)
```

**Client-Side Mesh Generation With Suggested Size**

The following code, placed in a [LocalScript](/docs/reference/engine/classes/LocalScript.md) in
[StarterPlayerScripts](/docs/reference/engine/classes/StarterPlayerScripts.md), listens for the server's signal and loads the
model. This example assumes there's a [Part](/docs/reference/engine/classes/Part.md) named `SizeBox` in the
[Workspace](/docs/reference/engine/classes/Workspace.md). It also assumes that the [RemoteEvent](/docs/reference/engine/classes/RemoteEvent.md) instance
created by the server-side example (`GenerationEvent`) exists inside
[ReplicatedStorage](/docs/reference/engine/classes/ReplicatedStorage.md).

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local GenerationService = game:GetService("GenerationService")
local Workspace = game:GetService("Workspace")

local sizeBox = Workspace:WaitForChild("SizeBox")

-- Reference to RemoteEvent instance created in server-side script
local generationEvent = ReplicatedStorage:WaitForChild("GenerationEvent")

generationEvent.OnClientEvent:Connect(function(generationId, targetCFrame)
	print("Client received signal to load model with ID:", generationId)
	local success, result = pcall(function()
		return GenerationService:LoadGeneratedMeshAsync(generationId)
	end)

	if success and result then
		result.Parent = Workspace
		result:PivotTo(targetCFrame)
		print("Client successfully loaded and placed model")
		-- Make the box a transparent, non-collidable container
		sizeBox.CanCollide = false
		sizeBox.Transparency = 0.85
	else
		warn("Client failed to load model:", result)
	end
end)
```

### Method: GenerationService:GenerateModelAsync

**Signature:** `GenerationService:GenerateModelAsync(inputs: Dictionary, schema: Dictionary, options: Dictionary?): Tuple`

Enables generation of multi-mesh geometries according to provided `inputs`
and a `schema`.

Provide creative direction through `inputs`: a `TextPrompt`, an `Image` to
condition on visually, or both. Control the output structure through
`schema`, supplying either a built-in `PredefinedSchema` or a custom
`SchemaDefinition` that names the parts to produce.

This method throws an error during the generation process for issues like
prompt rejection, generation timeouts, `schema` mismatches, or backend
service errors. It's recommended to wrap it in a
[LuaGlobals.pcall()](/docs/reference/engine/globals/LuaGlobals.md) to catch such errors.

See [this guide](/docs/en-us/parts/model-generation.md) for more detailed
examples including usage of a `Behaviors` module to connect functional
behaviors to generated models.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `inputs` | `Dictionary` |  | A table representing conditioning inputs with the following keys:  - `TextPrompt` — String description of the object to generate.   Required unless an `Image` is provided; you must supply at least one   of `TextPrompt` or `Image`. - `Image` — Optional [Content](/docs/reference/engine/datatypes/Content.md) referencing an image asset   (for example, the result of [Content.fromAssetId()](/docs/reference/engine/datatypes/Content.md)) used   to visually condition the generation. Supply it together with or   instead of `TextPrompt`. - `Size` — Optional [Vector3](/docs/reference/engine/datatypes/Vector3.md) describing the object size to   generate. This is only approximate; scale the model extents   post‑generation if you need a specific size. - `MaxTriangles` — Optional integer describing the maximum number of   triangles that the returned model will contain. Lower values result   in more faceted and low-poly generations. - `GenerateTextures` — `true` (default) textures the resulting   generation, while `false` will not generate textures. |
| `schema` | `Dictionary` |  | Table representing the generation schema. Provide exactly one of the following keys:  - `PredefinedSchema` — String selecting a built-in schema. Current   valid options are `Car5` for a basic vehicle chassis consisting of   five [Models](/docs/reference/engine/classes/Model.md), or `Body1` which results in a single mesh   output. - `SchemaDefinition` — Table describing a custom multi-part structure.   It contains a `Groups` array of part-name strings (one entry per   desired part); the returned [Model](/docs/reference/engine/classes/Model.md) is organized to match the   named groups. Use this instead of `PredefinedSchema` when you need a   structure the predefined schemas don't cover. |
| `options` | `Dictionary?` |  | Currently not used; reserved for future customization options. |

**Returns:** `Tuple` — Tuple with the following elements:

- A standard [Model](/docs/reference/engine/classes/Model.md) container instance that is compliant with
  the specified `schema`.
- A table containing a UUID and other metadata about the generation.

**Generation of Basic Car Chassis**

The code below invokes [GenerationService:GenerateModelAsync()](/docs/reference/engine/classes/GenerationService.md) using
the `Car5` schema to request output of a basic car chassis consisting of five
[MeshParts](/docs/reference/engine/classes/MeshPart.md) (body, front‑left wheel, front‑right wheel,
rear‑left wheel, rear‑right wheel).

```lua
local GenerationService = game:GetService("GenerationService")
local Workspace = game:GetService("Workspace")

-- Set up inputs for the generated geometry
local inputs = {
	TextPrompt = "a green dragon car with 4 wheels"
}
-- Set schema to the predefined five-model car chassis
local schema = {
	PredefinedSchema = "Car5"
}

-- Make the call to generate the model
local success, model, metadata = pcall(function()
	return GenerationService:GenerateModelAsync(inputs, schema)
end)
if success then
	-- Scale model to target size and position near world center
	local targetSize = 16
	local modelSize = model:GetExtentsSize()
	local scaleFactor = targetSize / math.max(modelSize.X, modelSize.Y, modelSize.Z)
	model:ScaleTo(scaleFactor)
	model:PivotTo(CFrame.new(15, model:GetExtentsSize().Y / 2, 0))

	-- Anchor all parts so that the meshes don't fall apart
	for _, descendant in model:GetDescendants() do
		if descendant:IsA("BasePart") then
			descendant.Anchored = true
		end
	end

	-- Name the model and parent it to workspace
	model.Name = "BasicDragonCarGeneration"
	model.Parent = Workspace
end
```

**Generation With a Custom Schema**

The code below invokes [GenerationService:GenerateModelAsync()](/docs/reference/engine/classes/GenerationService.md) with a
custom `SchemaDefinition` instead of a `PredefinedSchema`. Each entry in the
`Groups` array names a part to produce, so the returned [Model](/docs/reference/engine/classes/Model.md) is
organized to match the named groups.

```lua
local GenerationService = game:GetService("GenerationService")
local Workspace = game:GetService("Workspace")

-- Describe the object to generate
local inputs = {
	TextPrompt = "a wooden cart with four wheels",
}
-- Define a custom multi-part structure instead of using a predefined schema.
-- Each entry in `Groups` names a part the generation should produce.
local schema = {
	SchemaDefinition = {
		Groups = { "body", "wheel_fl", "wheel_fr", "wheel_rl", "wheel_rr" },
	},
}

-- Make the call to generate the model
local success, model, metadata = pcall(function()
	return GenerationService:GenerateModelAsync(inputs, schema)
end)
if success then
	-- Anchor all parts so that the meshes don't fall apart
	for _, descendant in model:GetDescendants() do
		if descendant:IsA("BasePart") then
			descendant.Anchored = true
		end
	end

	-- Name the model and parent it to workspace
	model.Name = "CustomSchemaGeneration"
	model.Parent = Workspace
end
```

**Generation Conditioned on an Image**

The code below invokes [GenerationService:GenerateModelAsync()](/docs/reference/engine/classes/GenerationService.md) with an
`Image` input so the generation is conditioned on a reference image. When an
`Image` is supplied the `TextPrompt` is optional, though you can provide both
for additional direction.

```lua
local GenerationService = game:GetService("GenerationService")
local Workspace = game:GetService("Workspace")

-- Reference image used to condition the generation. Replace `0` with the asset
-- ID of your own uploaded image.
local imageAssetId = 0

local inputs = {
	Image = Content.fromAssetId(imageAssetId),
	TextPrompt = "a low-poly treasure chest",
}
-- Produce a single-mesh output
local schema = {
	PredefinedSchema = "Body1",
}

-- Make the call to generate the model
local success, model, metadata = pcall(function()
	return GenerationService:GenerateModelAsync(inputs, schema)
end)
if success then
	-- Anchor all parts so that the meshes don't fall apart
	for _, descendant in model:GetDescendants() do
		if descendant:IsA("BasePart") then
			descendant.Anchored = true
		end
	end

	-- Name the model and parent it to workspace
	model.Name = "ImageConditionedGeneration"
	model.Parent = Workspace
end
```

### Method: GenerationService:LoadGeneratedMeshAsync

**Signature:** `GenerationService:LoadGeneratedMeshAsync(generationId: string): MeshPart`

Retrieves and loads a mesh generated by
[GenerateMeshAsync()](/docs/reference/engine/classes/GenerationService.md) using
the provided `generationId`. Must be called from client scripts.

The mesh can be returned as a [MeshPart](/docs/reference/engine/classes/MeshPart.md) or [Model](/docs/reference/engine/classes/Model.md). Because
editable meshes are not replicated, the loaded mesh is not replicated to
any other clients and can only be loaded once per `generationId`.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `generationId` | `string` |  | The unique ID returned by [GenerateMeshAsync()](/docs/reference/engine/classes/GenerationService.md). Identifies the mesh to load. |

**Returns:** `MeshPart` — The generated asset, returned as a [Model](/docs/reference/engine/classes/Model.md) with a single
[MeshPart](/docs/reference/engine/classes/MeshPart.md) containing an [EditableMesh](/docs/reference/engine/classes/EditableMesh.md).

### Method: GenerationService:SegmentMeshAsync

**Signature:** `GenerationService:SegmentMeshAsync(meshPart: MeshPart, schema: Dictionary, options: Dictionary?): Tuple`

Segments an existing [MeshPart](/docs/reference/engine/classes/MeshPart.md) into multiple named parts according
to a provided schema and returns a [Model](/docs/reference/engine/classes/Model.md) with the segmented parts
organized by the schema groups.

The `schema` parameter accepts the same structure as
[GenerateModelAsync()](/docs/reference/engine/classes/GenerationService.md):
either a `PredefinedSchema` string (such as `"Car5"` for a five-part
vehicle chassis or `"Body1"` for a single-mesh output) or a
`SchemaDefinition` table with a `Groups` array of custom part names.

This method can only be called from Roblox Studio (edit mode or plugin
context). For published mesh assets, the caller must have edit permission
for the asset. Wrap calls in [LuaGlobals.pcall()](/docs/reference/engine/globals/LuaGlobals.md) to handle errors
such as permission failures or mesh export issues.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `meshPart` | `MeshPart` |  | The [MeshPart](/docs/reference/engine/classes/MeshPart.md) to segment. Must contain mesh geometry (either an [EditableMesh](/docs/reference/engine/classes/EditableMesh.md) or a published mesh asset the caller has edit permission for). |
| `schema` | `Dictionary` |  | A table specifying how to segment the mesh. Provide exactly one of `PredefinedSchema` (a string such as `"Car5"` or `"Body1"`) or `SchemaDefinition` (a table with a `Groups` array of part-name strings defining the segmentation structure). |
| `options` | `Dictionary?` |  | Has no effect. |

**Returns:** `Tuple` — A tuple containing a [Model](/docs/reference/engine/classes/Model.md) whose children are organized
according to the specified schema (each group as a child [Model](/docs/reference/engine/classes/Model.md)
with a [MeshPart](/docs/reference/engine/classes/MeshPart.md) inside), and a table with a `UUID` key holding
the backend job identifier.

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