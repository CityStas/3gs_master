---
name: AvatarCreationService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "A service to support developer avatar creators."
---

# Class: AvatarCreationService

> A service to support developer avatar creators.

## Description

`AvatarCreationService` is a service that supports developer avatar creators,
providing methods that support the prompting of avatar creation from within
experiences.

## Methods

### Method: AvatarCreationService:AutoSetupAvatarAsync

**Signature:** `AvatarCreationService:AutoSetupAvatarAsync(player: Player, autoSetupParams: Dictionary, progressCallback: Function?): string`

Automatically sets up a custom [Model](/docs/reference/engine/classes/Model.md) as an avatar asset. This
method returns a `string` generation ID which can be passed to
[LoadGeneratedAvatarAsync()](/docs/reference/engine/classes/AvatarCreationService.md)
to load the generated avatar and return a [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) with
all the generated instances and properties. The load method can be called
on both the server and client, allowing the generated avatar to be loaded
in both places (on the client for previewing, and on the server for saving
the generated avatar to the player's inventory using
[PromptCreateAvatarAsync()](/docs/reference/engine/classes/AvatarCreationService.md)).

Auto-setup has specific model requirements and accepts certain
configurations of models. For more information, see
[Auto-setup requirements](/docs/en-us/avatar-setup/auto-setup-requirements.md).

**Note**: this API requires the `Enable Mesh / Image APIs` setting to be
turned on under Content Settings for your experience.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) that the avatar is being set up for. |
| `autoSetupParams` | `Dictionary` |  | A table containing the arguments. Type: `type AutoSetupAccessory = { AccessoryType: Enum.AccessoryType, IsLayered: bool, Instance: Model, } type AutoSetupParams = { Body: Model?, Accessories: {AutoSetupAccessory}, }` |
| `progressCallback` | `Function?` |  | Optional callback function that will be invoked periodically with a progressInfo table with the overall progress (from 0 to 1). Type: `(progressInfo: { Progress: number }) -> ()` |

**Returns:** `string` — A unique identifier for the generated avatar.

**AutoSetupAvatarAsync**

The following code invokes AutoSetup on the given body Model and layered shirt
Model. The setup avatar is then loaded on the server and an event is sent to
the client to load the avatar for local preview.

```lua
local AvatarCreationService = game:GetService("AvatarCreationService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local LoadAvatarEvent = ReplicatedStorage.LoadAvatarEvent

local generatedAvatars = {}

-- Must be called on the server
local function setupAvatar(player: Player, avatarModel: Model, layeredShirtModel : Model)
	local arguments = {
		Body = avatarModel,
		Accessories = {}
	}
	local accessoryArgument = {
		AccessoryType = Enum.AccessoryType.Shirt,
		IsLayered = true,
		Instance = layeredShirtModel,
	}
	table.insert(arguments.Accessories, accessoryArgument)
	local pcallSuccess, result = pcall(function()
		local generationId = AvatarCreationService:AutoSetupAvatarAsync(
			player,
			arguments,
			function(progressInfo)
				print(`AutoSetup progress: {progressInfo.Progress * 100}%`)
			end
		)
		-- Load and store on the server to use with PromptCreateAvatarAsync
		local humanoidDescription = AvatarCreationService:LoadGeneratedAvatarAsync(generationId)
		generatedAvatars[generationId] = humanoidDescription

		-- Signal the client so it can load the avatar for local preview
		LoadAvatarEvent:FireClient(player, generationId)
	end)

	if not pcallSuccess then
		warn("Avatar setup failed:", result)
	end
end
```

### Method: AvatarCreationService:GenerateAvatar2DPreviewAsync

**Signature:** `AvatarCreationService:GenerateAvatar2DPreviewAsync(avatarGeneration2dPreviewParams: Dictionary, progressCallback: Function?): string`

Creates a 2D avatar image preview, taking as input the FileId from
[PromptSelectAvatarGenerationImageAsync()](/docs/reference/engine/classes/AvatarCreationService.md)
and an optional text prompt. It returns a `previewId` which can be passed
to
[LoadAvatar2DPreviewAsync()](/docs/reference/engine/classes/AvatarCreationService.md)
to retrieve the preview image on the client. This API can only be used on
the game server.

**Note**: this API requires the `Enable Mesh / Image APIs` setting to be
turned on under Content Settings for your experience.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `avatarGeneration2dPreviewParams` | `Dictionary` |  | A table of arguments for 2D preview generation. Type: `avatarGeneration2dPreviewParams: {SessionId: string, FileId: string, TextPrompt: string?}` |
| `progressCallback` | `Function?` |  | Optional callback function that will be invoked periodically with a progressInfo table with the overall progress (from 0 to 1). Type: `(progressInfo: { Progress: number }) -> ()` |

**Returns:** `string` — A string previewId

**Generate Avatar2 D Preview Async**

Demonstrates [AvatarCreationService:GenerateAvatar2DPreviewAsync()](/docs/reference/engine/classes/AvatarCreationService.md).

```lua
local AvatarCreationService = game:GetService("AvatarCreationService")

function generateAvatar2DPreview(sessionId, fileId, textPrompt)
    local pcallSuccess, result = pcall(function()
        local args = {}
        args.SessionId = sessionId
        args.FileId = fileId
        args.TextPrompt = textPrompt
        return AvatarCreationService:GenerateAvatar2DPreviewAsync(args)
    end)

    if not pcallSuccess then
        warn("Generating 2D preview failed: ", result)
    end

    return result
end
```

### Method: AvatarCreationService:GenerateAvatarAsync

**Signature:** `AvatarCreationService:GenerateAvatarAsync(avatarGenerationParams: Dictionary, progressCallback: Function?): string`

Generate an avatar from a preview and return the generationId. The
[LoadGeneratedAvatarAsync()](/docs/reference/engine/classes/AvatarCreationService.md)
method is then called to retrieve the generated
[HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) avatar. This API can only be used on the game
server.

**Note**: this API requires the `Enable Mesh / Image APIs` setting to be
turned on under Content Settings for your experience.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `avatarGenerationParams` | `Dictionary` |  | A table of arguments for generating an avatar. Type: `avatarGenerationParams: {SessionId: string, PreviewId: string}` |
| `progressCallback` | `Function?` |  | Optional callback function that will be invoked periodically with a progressInfo table with the overall progress (from 0 to 1). Type: `(progressInfo: { Progress: number }) -> ()` |

**Returns:** `string` — A string generationId.

**Generate Avatar Async**

Demonstrates [AvatarCreationService:GenerateAvatarAsync()](/docs/reference/engine/classes/AvatarCreationService.md).

```lua
local AvatarCreationService = game:GetService("AvatarCreationService")

function generateAvatar(sessionId, previewId)
    local pcallSuccess, result = pcall(function()
        local args = {}
        args.SessionId = sessionId
        args.PreviewId = previewId
        return AvatarCreationService:GenerateAvatarAsync(args)
    end)

    if not pcallSuccess then
        warn("Generating avatar failed: ", result)
    end

    return result
end
```

### Method: AvatarCreationService:GetBatchTokenDetailsAsync

**Signature:** `AvatarCreationService:GetBatchTokenDetailsAsync(tokenIds: Array): Array`

Gets the avatar creation token details for a list of avatar creation
tokens at once (tokens are generated through the
[token creation](/docs/en-us/production/monetization/avatar-creation-token.md)
process). Returns an array of avatar creation token details; each token
detail is a dictionary with the fields indicated in the example result
below:

```lua
{
	["Name"] = "string",
	["Description"] = "string",
	["UniverseId"] = 0,
	["CreatorId"] = 0,
	["CreatorType"] = Enum.CreatorType.User,
	["OnSale"] = true,
	["Price"] = 0,
	["OffSaleReasons"] = {
		"string",
	}
}
```

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Monetization*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `tokenIds` | `Array` |  | The list of avatar creation token IDs to get details of. |

**Returns:** `Array` — Array of avatar creation token details as outlined above.

### Method: AvatarCreationService:GetValidationRules

**Signature:** `AvatarCreationService:GetValidationRules(): Dictionary`

Gets data regarding rules that assets must abide by to pass UGC
validation. Validation is an essential step before creating avatars and
there are various checks that occur, including mesh triangle limits,
texture sizes, body part size limits, attachment positions, and more.

The returned dictionary of validation rules takes the following form:

```
{
	["MeshRules"] = {
		["BodyPartMaxTriangles"] = {
			Enum.AssetType.DynamicHead: number,
			Enum.AssetType.LeftArm: number,
			Enum.AssetType.RightArm: number,
			Enum.AssetType.Torso: number,
			Enum.AssetType.LeftLeg: number,
			Enum.AssetType.RightLeg: number,
		},
			["AccessoryMaxTriangles"]: number,
			["MeshVertColor"]: Color3,
			["CageMeshMaxDistanceFromRenderMesh"]: number,
	},
	["TextureRules"] = {
		["MaxTextureSize"]: number,
	},
	["BodyPartRules"] = {
		[Enum.AssetType.DynamicHead] = {
			["Bounds"] = {
				["Classic"] = {
					["MinSize"]: Vector3,
					["MaxSize"]: Vector3,
			},
				["ProportionsSlender"] = {
					["MinSize"]: Vector3,
					["MaxSize"]: Vector3,
				},
				["ProportionsNormal"] = {
					["MinSize"]: Vector3,
					["MaxSize"]: Vector3,
				},
			},
			["SubParts"] = {
				["Head"] = {
					["NeckRigAttachment"] = {
						["LowerBound"]: Vector3,
						["UpperBound"]: Vector3,
					},
					["FaceFrontAttachment"] = {
						["LowerBound"]: Vector3,
						["UpperBound"]: Vector3,
					},
					["HatAttachment"] = {
						["LowerBound"]: Vector3,
						["UpperBound"]: Vector3,
					},
					["HairAttachment"] = {
						["LowerBound"]: Vector3,
						["UpperBound"]: Vector3,
					},
					["FaceCenterAttachment"] = {
						["LowerBound"]: Vector3,
						["UpperBound"]: Vector3,
					},
				},
			},
		},
		[Enum.AssetType.LeftArm] = {
			["Bounds"] = {
				["Classic"] = {
					["MinSize"]: Vector3,
					["MaxSize"]: Vector3,
				},
				["ProportionsSlender"] = {
					["MinSize"]: Vector3,
					["MaxSize"]: Vector3,
				},
				["ProportionsNormal"] = {
					["MinSize"]: Vector3,
					["MaxSize"]: Vector3,
				},
			},
			["SubParts"] = {
				["LeftHand"] = {
					["LeftWristRigAttachment"] = {
						["LowerBound"]: Vector3,
						["UpperBound"]: Vector3,
					},
					["LeftGripAttachment"] = {
						["LowerBound"]: Vector3,
						["UpperBound"]: Vector3,
					},
				},
				["LeftUpperArm"] = {
					["LeftShoulderRigAttachment"] = {
						["LowerBound"]: Vector3,
						["UpperBound"]: Vector3,
					},
					["LeftShoulderAttachment"] = {
						["LowerBound"]: Vector3,
						["UpperBound"]: Vector3,
					},
						["LeftElbowRigAttachment"] = {
						["LowerBound"]: Vector3,
						["UpperBound"]: Vector3,
					},
				},
				["LeftLowerArm"] = {
					["LeftElbowRigAttachment"] = {
						["LowerBound"]: Vector3,
						["UpperBound"]: Vector3,
					},
					["LeftWristRigAttachment"] = {
						["LowerBound"]: Vector3,
						["UpperBound"]: Vector3,
					},
				},
			},
		},
		...
	},
	["AccessoryRules"] = {
		[Enum.AssetType.HairAccessory] = {
			["Attachments"] = {
				{
					["Size"]: Vector3,
					["Offset"]: Vector3,
					["Name"]: string,
				},
			},
			["RigidAllowed"]: boolean,
		},
		...
      	},
        ["MakeupRules"] = {
		["ReferenceCageMeshId"]: number,
		["WrapTextureTransferUVBounds"] = {
			["MinBound"]: Vector2,
            		["MaxBound"]: Vector2,
          	},
          	["ExcludeUVBounds"] = {
            		[Enum.AssetType.FaceMakeup] = {
              			["LeftEye"] = {
                			["MinBound"]: Vector2,
                			["MaxBound"]: Vector2,
              			},
              			["RightEye"] = {
                			["MinBound"]: Vector2,
                			["MaxBound"]: Vector2,
              			},
              			["Lips"] = {
                			["MinBound"]: Vector2,
                			["MaxBound"]: Vector2,
              			},
            		},
          	},
          	["IncludeUVBounds"] = {
			[Enum.AssetType.LipMakeup] = {
				["MinBound"]: Vector2,
				["MaxBound"]: Vector2,
		    	},
		    	[Enum.AssetType.EyeMakeup] = {
		      		["MinBound"]: Vector2,
		      		["MaxBound"]: Vector2,
		    	},
          	}
	}
}
```

*Security: None · Thread Safety: Unsafe*

**Returns:** `Dictionary` — Dictionary of validation rules as detailed above.

### Method: AvatarCreationService:LoadAvatar2DPreviewAsync

**Signature:** `AvatarCreationService:LoadAvatar2DPreviewAsync(previewId: string): EditableImage`

Load an AvatarGeneration 2D preview as an [EditableImage](/docs/reference/engine/classes/EditableImage.md) on the
client for the given previewId. This API can only be used on the client.

**Note**: this API requires the `Enable Mesh / Image APIs` setting to be
turned on under Content Settings for your experience.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `previewId` | `string` |  | Load the preview generated from [GenerateAvatar2DPreviewAsync()](/docs/reference/engine/classes/AvatarCreationService.md). |

**Returns:** `EditableImage` — An [EditableImage](/docs/reference/engine/classes/EditableImage.md) containing the preview image.

**Load Avatar2 D Preview Async**

Demonstrates [AvatarCreationService:LoadAvatar2DPreviewAsync()](/docs/reference/engine/classes/AvatarCreationService.md).

```lua
local AvatarCreationService = game:GetService("AvatarCreationService")

function loadAvatar2DPreview(previewId)
    local pcallSuccess, result = pcall(function()
        return AvatarCreationService:LoadAvatar2DPreviewAsync(previewId)
    end)

    if not pcallSuccess then
        warn("Failed to load preview: ", result)
    end

    return result
end
```

### Method: AvatarCreationService:LoadGeneratedAvatarAsync

**Signature:** `AvatarCreationService:LoadGeneratedAvatarAsync(generationId: string): HumanoidDescription`

Loads a generated avatar using an avatar generation ID, as returned by
[AutoSetupAvatarAsync()](/docs/reference/engine/classes/AvatarCreationService.md)
or
[GenerateAvatarAsync()](/docs/reference/engine/classes/AvatarCreationService.md).
The generated avatar will be returned as a [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md)
with all the generated instances and properties. Mesh and texture assets
will be provided as [EditableMesh](/docs/reference/engine/classes/EditableMesh.md) and [EditableImage](/docs/reference/engine/classes/EditableImage.md)
objects, respectively, to allow continued editing of the generated avatar.

This method can be called on both the server and client, allowing the
generated avatar to be loaded in both places (on the client for
previewing, and on the server for saving the generated avatar to the
player's inventory using
[PromptCreateAvatarAsync()](/docs/reference/engine/classes/AvatarCreationService.md)).
Once the method has been invoked on both the client and server, the data
associated with the generation ID will be erased and subsequent calls to
his method with the same generation ID will fail.

**Note**: this API requires the `Enable Mesh / Image APIs` setting to be
turned on under Content Settings for your experience.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `generationId` | `string` |  | A unique string that identifies the generated avatar, as returned by [       AutoSetupAvatarAsync()](/docs/reference/engine/classes/AvatarCreationService.md). |

**Returns:** `HumanoidDescription` — The [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) of the generated avatar, which
includes all the generated instances and properties.

**LoadGeneratedAvatarAsync**

The following code loads a generated avatar using an avatar generation ID
provided by [AvatarCreationService:AutoSetupAvatarAsync()](/docs/reference/engine/classes/AvatarCreationService.md). The result
is returned as a [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).

```lua
local AvatarCreationService = game:GetService("AvatarCreationService")
local Players = game:GetService("Players")

-- Can be called on either the server or client
local function loadAvatar(generationId: string): Model?
	local pcallSuccess, result = pcall(function()
		local humanoidDescription = AvatarCreationService:LoadGeneratedAvatarAsync(generationId)
		local model = Players:CreateHumanoidModelFromDescriptionAsync(humanoidDescription, Enum.HumanoidRigType.R15)
		return model
	end)
	if pcallSuccess then
		return result
	else
		print("Avatar failed to load:", result)
		return nil
	end
end
```

### Method: AvatarCreationService:PrepareAvatarForPreviewAsync

**Signature:** `AvatarCreationService:PrepareAvatarForPreviewAsync(humanoidModel: Model): ()`

Triggers HSR generation and attachment point updating for in-experience
avatar previews. This allows for previewing of avatars created in
experience with layered clothing and accessories in the same way they will
appear when published through
[PromptCreateAvatarAsync()](/docs/reference/engine/classes/AvatarCreationService.md).

When developers use [EditableMesh](/docs/reference/engine/classes/EditableMesh.md) and [WrapDeformer](/docs/reference/engine/classes/WrapDeformer.md) to
modify avatars before publishing, the original HSR data may not accurately
account for the new deformations. This method generates updated HSR data
and corrects attachment points based on the [WrapDeformer](/docs/reference/engine/classes/WrapDeformer.md)
modifications, ensuring consistent preview and published avatar
appearance.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `humanoidModel` | `Model` |  | The [Model](/docs/reference/engine/classes/Model.md) containing [MeshPart](/docs/reference/engine/classes/MeshPart.md) children with [WrapDeformer](/docs/reference/engine/classes/WrapDeformer.md) instances that require HSR data updating for preview. |

**Returns:** `()` — void

### Method: AvatarCreationService:PromptCreateAvatarAssetAsync

**Signature:** `AvatarCreationService:PromptCreateAvatarAssetAsync(tokenId: string, player: Player, assetInstance: Instance, assetType: AvatarAssetType): Tuple`

Prompts a [Player](/docs/reference/engine/classes/Player.md) to purchase and create an avatar asset from an
[Instance](/docs/reference/engine/classes/Instance.md). The price of the creation is dictated by the price
attributed to the avatar creation token. This creation token is required
for the purchasing and creation of the asset and can be generated by
following the
[token creation](/docs/en-us/production/monetization/avatar-creation-token.md)
process.

For accessory creation, the [Instance](/docs/reference/engine/classes/Instance.md) is expected to include a new
accessory to be created. This includes the following types:
[Hat](/docs/reference/engine/enums/AvatarAssetType.md), [Hair](/docs/reference/engine/enums/AvatarAssetType.md),
[FaceAccessory](/docs/reference/engine/enums/AvatarAssetType.md),
[NeckAccessory](/docs/reference/engine/enums/AvatarAssetType.md),
[ShoulderAccessory](/docs/reference/engine/enums/AvatarAssetType.md),
[FrontAccessory](/docs/reference/engine/enums/AvatarAssetType.md),
[BackAccessory](/docs/reference/engine/enums/AvatarAssetType.md),
[WaistAccessory](/docs/reference/engine/enums/AvatarAssetType.md),
[TShirtAccessory](/docs/reference/engine/enums/AvatarAssetType.md),
[ShirtAccessory](/docs/reference/engine/enums/AvatarAssetType.md),
[PantsAccessory](/docs/reference/engine/enums/AvatarAssetType.md),
[JacketAccessory](/docs/reference/engine/enums/AvatarAssetType.md),
[SweaterAccessory](/docs/reference/engine/enums/AvatarAssetType.md),
[ShortsAccessory](/docs/reference/engine/enums/AvatarAssetType.md),
[DressSkirtAccessory](/docs/reference/engine/enums/AvatarAssetType.md),
[EyebrowAccessory](/docs/reference/engine/enums/AvatarAssetType.md), and
[EyelashAccessory](/docs/reference/engine/enums/AvatarAssetType.md).

To support this, the [Instance](/docs/reference/engine/classes/Instance.md) should be an [Accessory](/docs/reference/engine/classes/Accessory.md)
instance or contain an [Accessory](/docs/reference/engine/classes/Accessory.md) child instance. This should
include a [MeshPart](/docs/reference/engine/classes/MeshPart.md) child instance which makes up the accessory.

The avatar asset [MeshPart](/docs/reference/engine/classes/MeshPart.md) will also need to include:

- An [EditableImage](/docs/reference/engine/classes/EditableImage.md).
- An [EditableMesh](/docs/reference/engine/classes/EditableMesh.md).

If creating a layered clothing accessory such as a shirt, the
[MeshPart](/docs/reference/engine/classes/MeshPart.md) should include a [WrapDeformer](/docs/reference/engine/classes/WrapDeformer.md) with an
[EditableMesh](/docs/reference/engine/classes/EditableMesh.md).

This method also supports [FaceMakeup](/docs/reference/engine/enums/AvatarAssetType.md),
[LipMakeup](/docs/reference/engine/enums/AvatarAssetType.md), and
[EyeMakeup](/docs/reference/engine/enums/AvatarAssetType.md). For these types,
`assetInstance` must be a [Decal](/docs/reference/engine/classes/Decal.md) whose [Decal.TextureContent](/docs/reference/engine/classes/Decal.md)
references an [EditableImage](/docs/reference/engine/classes/EditableImage.md), with exactly one
[WrapTextureTransfer](/docs/reference/engine/classes/WrapTextureTransfer.md) child. The accessory and MeshPart requirements
above do not apply to these types.

Finally, the provided [AvatarAssetType](/docs/reference/engine/enums/AvatarAssetType.md) should match the creation
type of the token and the type of asset for upload.

*Yields · Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `tokenId` | `string` |  | The ID of a creation token. The token must be valid in that the universe the method is called from is the same universe the token was created for. Furthermore, the token creator must maintain ID verification and [Roblox Premium](https://www.roblox.com/premium/membership). To create a token for utilization in this API, follow the [token creation](/docs/en-us/production/monetization/avatar-creation-token.md) process. The token's creation type must match the [AvatarAssetType](/docs/reference/engine/enums/AvatarAssetType.md) passed in to the method. |
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) intended to be presented with the creation prompt. |
| `assetInstance` | `Instance` |  | The [Instance](/docs/reference/engine/classes/Instance.md) of the avatar asset intended for creation. |
| `assetType` | `AvatarAssetType` |  | The [AvatarAssetType](/docs/reference/engine/enums/AvatarAssetType.md) of the expected creation. This must match the creation type of the provided token. |

**Returns:** `Tuple` — A tuple containing, in order:

- An [PromptCreateAssetResult](/docs/reference/engine/enums/PromptCreateAssetResult.md) indicating the result of the
  creation prompt.

- A string result. In the case of
  [PromptCreateAssetResult.Success](/docs/reference/engine/enums/PromptCreateAssetResult.md), this will indicate the asset
  ID. In the case of any failure enum, this will indicate the
  resultant error message.

**PromptCreateAvatarAssetAsync**

The following code prompts for avatar asset creation, and responds to the
result.

```lua
local AvatarCreationService = game:GetService("AvatarCreationService")

local function publishAvatarAsset(tokenId: string, player: Player, assetInstance: Accessory, assetType: Enum.AvatarAssetType)
  local pcallSuccess, result, resultMessage = pcall(function()
    return AvatarCreationService:PromptCreateAvatarAssetAsync(tokenId, player, assetInstance, assetType)
  end)
  if pcallSuccess then
    if result == Enum.PromptCreateAssetResult.Success then
      print("Successfully uploaded with AssetId: ", resultMessage)
    else
      print("Unsuccessfully uploaded with error message:", resultMessage)
    end
  else
    print("Avatar asset failed to create.")
  end
end
```

### Method: AvatarCreationService:PromptCreateAvatarAsync

**Signature:** `AvatarCreationService:PromptCreateAvatarAsync(tokenId: string, player: Player, humanoidDescription: HumanoidDescription): Tuple`

Prompts a [Player](/docs/reference/engine/classes/Player.md) to purchase and create an avatar from a
[HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md). The price of the creation is dictated by the
price attributed to the avatar creation token. This avatar creation token
is required for the purchasing and creation of the body and can be
generated by following the
[token creation](/docs/en-us/production/monetization/avatar-creation-token.md)
process.

For avatar creation, the [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) is expected to
include new assets to be created for each of the 6 body parts
([Head](/docs/reference/engine/enums/BodyPart.md), [Torso](/docs/reference/engine/enums/BodyPart.md),
[RightLeg](/docs/reference/engine/enums/BodyPart.md), [LeftLeg](/docs/reference/engine/enums/BodyPart.md),
[RightArm](/docs/reference/engine/enums/BodyPart.md), [LeftArm](/docs/reference/engine/enums/BodyPart.md)).
Optionally, it can also include a new [Hair](/docs/reference/engine/enums/AccessoryType.md)
accessory.

To support this, the [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) should include 6
[BodyPartDescription](/docs/reference/engine/classes/BodyPartDescription.md) children (one for each body part). For each,
the [BodyPartDescription.Instance](/docs/reference/engine/classes/BodyPartDescription.md) property references a
[Folder](/docs/reference/engine/classes/Folder.md) which includes all of the [MeshPart](/docs/reference/engine/classes/MeshPart.md) instances which
make up the body part, for example a `LeftArm` folder which has
`LeftHand`, `LeftUpperArm`, and `LeftLowerArm` [MeshParts](/docs/reference/engine/classes/MeshPart.md).
The [BodyPartDescription.BodyPart](/docs/reference/engine/classes/BodyPartDescription.md) property should also be set to
the relevant [BodyPart](/docs/reference/engine/enums/BodyPart.md).

Each body part [MeshPart](/docs/reference/engine/classes/MeshPart.md) will also need to include:

- An [EditableImage](/docs/reference/engine/classes/EditableImage.md).
- A [WrapDeformer](/docs/reference/engine/classes/WrapDeformer.md) with an [EditableMesh](/docs/reference/engine/classes/EditableMesh.md).

If including an accessory such as hair, the [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md)
should include a child [AccessoryDescription](/docs/reference/engine/classes/AccessoryDescription.md) where:

- The [AccessoryDescription.Instance](/docs/reference/engine/classes/AccessoryDescription.md) property references the
  [Accessory](/docs/reference/engine/classes/Accessory.md) instance.
- The [AccessoryDescription.AccessoryType](/docs/reference/engine/classes/AccessoryDescription.md) property is set to the
  relevant [AccessoryType](/docs/reference/engine/enums/AccessoryType.md).

Finally, the [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) should include the humanoid
scales of [BodyTypeScale](/docs/reference/engine/classes/HumanoidDescription.md),
[HeadScale](/docs/reference/engine/classes/HumanoidDescription.md),
[HeightScale](/docs/reference/engine/classes/HumanoidDescription.md),
[WidthScale](/docs/reference/engine/classes/HumanoidDescription.md), and
[ProportionScale](/docs/reference/engine/classes/HumanoidDescription.md). Be mindful of
the scales that a base body is imported with so that they match the scales
provided to the [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetCreateUpdate, Monetization*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `tokenId` | `string` |  | The ID of an avatar creation token. The token must be valid in that the universe the method is called from is the same universe the token was created for. Furthermore, the token creator must maintain ID verification and [Roblox Premium](https://www.roblox.com/premium/membership). To create a token for utilization in this API, follow the [token creation](/docs/en-us/production/monetization/avatar-creation-token.md) process. |
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) intended to be presented with the creation prompt. |
| `humanoidDescription` | `HumanoidDescription` |  | The [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) of the avatar intended for creation. |

**Returns:** `Tuple` — A tuple containing, in order:

- An [PromptCreateAvatarResult](/docs/reference/engine/enums/PromptCreateAvatarResult.md) indicating the result of the
  creation prompt.

- A string result. In the case of
  [PromptCreateAvatarResult.Success](/docs/reference/engine/enums/PromptCreateAvatarResult.md), this will indicate the
  bundle ID. In the case of any failure enum, this will indicate the
  resultant error message.

- A secondary optional string result. In the case of
  [PromptCreateAvatarResult.Success](/docs/reference/engine/enums/PromptCreateAvatarResult.md), this will indicate the
  outfit ID. In the case of any failure enum, this will be `nil`.

**PromptCreateAvatarAsync**

The following code populates a [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) in the expected
format, prompts for avatar creation, and responds to the result.

```lua
local AvatarCreationService = game:GetService("AvatarCreationService")
export type BodyPartInfo = {
	bodyPart: Enum.BodyPart,
	instance: Instance, --Folder with Created MeshParts
}
export type BodyPartList = { BodyPartInfo }

local function publishAvatar(bodyPartInstances: BodyPartList, player: Player, tokenId: string)
	local humanoidDescription = Instance.new("HumanoidDescription")
	for _, bodyPartInfo in bodyPartInstances do
		local bodyPartDescription = Instance.new("BodyPartDescription")
		bodyPartDescription.Instance = bodyPartInfo.instance
		bodyPartDescription.BodyPart = bodyPartInfo.bodyPart
		bodyPartDescription.Parent = humanoidDescription
	end

	local pcallSuccess, result, resultMessage = pcall(function()
		return AvatarCreationService:PromptCreateAvatarAsync(tokenId, player, humanoidDescription)
	end)
	if pcallSuccess then
		if result == Enum.PromptCreateAvatarResult.Success then
			print("Successfully uploaded with BundleId: ", resultMessage)
		else
			print("Unsuccessfully uploaded with error message:", resultMessage)
		end
	else
		print("Avatar failed to create.")
	end
end
```

### Method: AvatarCreationService:PromptCreateMakeupAsync

**Signature:** `AvatarCreationService:PromptCreateMakeupAsync(player: Player, makeupAssetEntries: Array, thumbnailHeadColor?: Color3?): Tuple`

Prompts a [Player](/docs/reference/engine/classes/Player.md) to create and publish a makeup look from two to
six makeup assets. For example, an in-experience creation tool can use
this method to let a player publish lip and face makeup together as a
single look. This method can only be called from the server and yields
until the operation completes.

Each asset requires a creation token for its asset type and the current
experience. See the
[token creation](/docs/en-us/production/monetization/avatar-creation-token.md)
process. The input entries are checked before the prompt opens. Creation
token and user-generated content validation run while the prompt is
loading; the player can proceed with creation after validation succeeds.

For `FaceMakeup`, `LipMakeup`, and `EyeMakeup`, the asset instance must be
a [Decal](/docs/reference/engine/classes/Decal.md) whose [Decal.TextureContent](/docs/reference/engine/classes/Decal.md) references an
[EditableImage](/docs/reference/engine/classes/EditableImage.md), with exactly one [WrapTextureTransfer](/docs/reference/engine/classes/WrapTextureTransfer.md) child.

The overall [PromptCreateOutfitResult](/docs/reference/engine/enums/PromptCreateOutfitResult.md) describes creation of the
look:

- [Success](/docs/reference/engine/enums/PromptCreateOutfitResult.md) means all submitted
  assets and the makeup look were created.
- [PartialSuccess](/docs/reference/engine/enums/PromptCreateOutfitResult.md) means at
  least one asset was created, but another asset or the makeup look
  composition failed. If the look was created, the second return value is
  its outfit ID; if composition failed, it is an error message instead.
- [CreationFailure](/docs/reference/engine/enums/PromptCreateOutfitResult.md) means no
  assets were created, so no makeup look was created.

Inspect the per-asset results to determine which assets were created. Each
entry contains [Success](/docs/reference/engine/enums/PromptCreateAssetResult.md) and an asset
ID, or [UploadFailed](/docs/reference/engine/enums/PromptCreateAssetResult.md) without an
asset ID. If a failure occurs before asset uploads, the results array may
be empty.

For [PermissionDenied](/docs/reference/engine/enums/PromptCreateOutfitResult.md),
[Timeout](/docs/reference/engine/enums/PromptCreateOutfitResult.md), and
[NoUserInput](/docs/reference/engine/enums/PromptCreateOutfitResult.md), only the result
enum is returned; variables assigned to the other return values receive
`nil`.

This method can raise an error for invalid input, request throttling, or
unexpected failures. Validation failures may raise an error or return
[UGCValidationFailed](/docs/reference/engine/enums/PromptCreateOutfitResult.md)
with an error message and an empty per-asset results array. Use `pcall()`
to handle errors as well as checking the returned result enum.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetCreateUpdate, Monetization*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) who receives the creation prompt and owns the uploaded makeup look. |
| `makeupAssetEntries` | `Array` |  | An array containing between two and six asset-entry dictionaries. Each dictionary contains:  - `TokenId` (string) – The ID of a creation token valid for the   current experience and the entry's `AvatarAssetType`. - `Instance` ([Instance](/docs/reference/engine/classes/Instance.md)) – The makeup asset instance to upload. - `AvatarAssetType` ([AvatarAssetType](/docs/reference/engine/enums/AvatarAssetType.md)) – The asset type.   Supported types are [FaceMakeup](/docs/reference/engine/enums/AvatarAssetType.md),   [LipMakeup](/docs/reference/engine/enums/AvatarAssetType.md),   [EyeMakeup](/docs/reference/engine/enums/AvatarAssetType.md),   [EyebrowAccessory](/docs/reference/engine/enums/AvatarAssetType.md), and   [EyelashAccessory](/docs/reference/engine/enums/AvatarAssetType.md). - `SortOrder` (number) – The asset's ordering within the makeup look. |
| `thumbnailHeadColor` | `Color3?` | `nil` | Optional [Color3](/docs/reference/engine/datatypes/Color3.md) for the head in the makeup look thumbnail. If omitted, the default gray head color is used. |

**Returns:** `Tuple` — A tuple containing, in order:

- An [PromptCreateOutfitResult](/docs/reference/engine/enums/PromptCreateOutfitResult.md) indicating the overall creation
  outcome.

- A string containing the outfit ID when the makeup look is created,
  or an error message otherwise. This value is not returned for
  `PermissionDenied`, `Timeout`, or `NoUserInput`.

- An array of per-asset result dictionaries in the same order as the
  input entries. Each dictionary contains `Result`
  ([PromptCreateAssetResult](/docs/reference/engine/enums/PromptCreateAssetResult.md)) and, for successfully created
  assets, `AssetId` (string). This value is not returned for
  `PermissionDenied`, `Timeout`, or `NoUserInput`.

### Method: AvatarCreationService:PromptSelectAvatarGenerationImageAsync

**Signature:** `AvatarCreationService:PromptSelectAvatarGenerationImageAsync(player: Player): string`

Prompt the [Player](/docs/reference/engine/classes/Player.md) to take a selfie and return the FileId of the
selfie. This FileId is then passed as an argument to
[GenerateAvatar2DPreviewAsync()](/docs/reference/engine/classes/AvatarCreationService.md).
This API can only be used on the game server.

```lua
local AvatarCreationService = game:GetService("AvatarCreationService")

function promptSelectAvatarGenerationImage(player)
    local pcallSuccess, result = pcall(function()
        return AvatarCreationService:PromptSelectAvatarGenerationImageAsync(player)
    end)

    if not pcallSuccess then
        errName, errDesc = unpack(string.split(result, ": "))
        if errName == "SelfieConsentDenied" then
            warn("Player must accept consent to use feature.")
        else
            warn("Failed to prompt for image: ", errDesc)
        end
    end

    return result
end
```

On failure, the result string has the format
`ErrorName: Error description`, allowing the error type to be identified
programmatically.

| Error name | Error description |
| --- | --- |
| `SelfieConsentDenied` | Selfie consent not accepted |
| `QRTooManyRequests` | Failure to generate QR url due to too many requests; please wait and try again later |
| `MediaPermissionsDenied` | Permissions not granted for taking photo |
| `FeatureUnavailable` | Feature not available for player |
| `GenerationInProgress` | Generation already in progress for player |

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: SensitiveInput*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) to prompt for taking a selfie. |

**Returns:** `string` — A string FileId of the selfie on success, or an error string
describing the reason for failure.

### Method: AvatarCreationService:RequestAvatarGenerationSessionAsync

**Signature:** `AvatarCreationService:RequestAvatarGenerationSessionAsync(player: Player, callback: Function): Tuple`

Request an AvatarGeneration session for a [Player](/docs/reference/engine/classes/Player.md). Information
about the session is returned via the callback, including the SessionId
which is passed to the
[GenerateAvatar2DPreviewAsync()](/docs/reference/engine/classes/AvatarCreationService.md)
and
[GenerateAvatarAsync()](/docs/reference/engine/classes/AvatarCreationService.md)
methods. Additional session information includes allowed 2d preview
generations, allowed 3d avatar generations, and the session time. The
method returns a `Tuple` with an [RBXScriptConnection](/docs/reference/engine/datatypes/RBXScriptConnection.md) and
estimated `waitTime`. The [RBXScriptConnection](/docs/reference/engine/datatypes/RBXScriptConnection.md) allows canceling
a session request. The estimated `waitTime` is used to provide the player
an estimated time in seconds until the session will be ready. This API can
only be used on the game server.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) to request an AvatarGeneration session for. |
| `callback` | `Function` |  | Callback function that is invoked with a SessionInfo table, with information about the session. Type: `(SessionInfo: { SessionId: string, Allowed2DGenerations: number, Allowed3DGenerations: number, SessionTime: number }) -> ()` |

**Returns:** `Tuple` — A tuple containing a [RBXScriptConnection](/docs/reference/engine/datatypes/RBXScriptConnection.md) that can be used
to cancel the session request and the estimated wait time in seconds.

**Request Avatar Generation Session Async**

Demonstrates
[AvatarCreationService:RequestAvatarGenerationSessionAsync()](/docs/reference/engine/classes/AvatarCreationService.md).

```lua
local AvatarCreationService = game:GetService("AvatarCreationService")
local playerSessions = {}
local playerSessionRequests = {}

function requestAvatarGenerationSession(player)
    local pcallSuccess, conn, waitTime = pcall(function()
        return AvatarCreationService:RequestAvatarGenerationSessionAsync(player, function(sessionInfo)
            playerSessions[player.UserID] = sessionInfo
            playerSessionRequests[player.UserID] = nil
        end)
    end)

    if not pcallSuccess then
        warn("Failed to request Avatar generation session: ", conn)
    end

    playerSessionRequests[player.UserID] = conn
    print("Wait time for session: ", tostring(waitTime))
end

function cancelAvatarGenerationSessionRequest(player)
    if playerSessionRequests[player.UserID] ~= nil then
        playerSessionRequests[player.UserID]:Disconnect()
    end
end
```

### Method: AvatarCreationService:ValidateUGCAccessoryAsync

**Signature:** `AvatarCreationService:ValidateUGCAccessoryAsync(player: Player, accessory: Instance, accessoryType: AccessoryType): Tuple`

Studio only. Given a [Player](/docs/reference/engine/classes/Player.md) and [Instance](/docs/reference/engine/classes/Instance.md) for an
[AccessoryType](/docs/reference/engine/enums/AccessoryType.md), determines if UGC validation passes.

*Yields · Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) validation is completed for. |
| `accessory` | `Instance` |  | The instance validation is run on. |
| `accessoryType` | `AccessoryType` |  | The [AccessoryType](/docs/reference/engine/enums/AccessoryType.md) the instance is expected to be. |

**Returns:** `Tuple` — A tuple containing, in order:

- A boolean indicating if validation was successful for the accessory.
- An optional table of strings. This includes failure reasons if
  validation was unsuccessful; otherwise `nil` if validation was
  successful.

### Method: AvatarCreationService:ValidateUGCBodyPartAsync

**Signature:** `AvatarCreationService:ValidateUGCBodyPartAsync(player: Player, instance: Instance, bodyPart: BodyPart): Tuple`

Studio only. Given a [Player](/docs/reference/engine/classes/Player.md) and [Instance](/docs/reference/engine/classes/Instance.md) for an
[BodyPart](/docs/reference/engine/enums/BodyPart.md), determines if UGC validation passes. The `instance`
parameter is expected as a [Folder](/docs/reference/engine/classes/Folder.md) in the following example format
with relevant [MeshParts](/docs/reference/engine/classes/MeshPart.md):

- `LeftArm` ([Folder](/docs/reference/engine/classes/Folder.md))
  - `R15ArtistIntent` ([Folder](/docs/reference/engine/classes/Folder.md))
    - `LeftLowerArm` ([MeshPart](/docs/reference/engine/classes/MeshPart.md))
    - `LeftUpperArm` ([MeshPart](/docs/reference/engine/classes/MeshPart.md))
    - `LeftHand` ([MeshPart](/docs/reference/engine/classes/MeshPart.md))

However, if the expected `bodyPart` is [BodyPart.Head](/docs/reference/engine/enums/BodyPart.md), the function
takes a singular `Head` [MeshPart](/docs/reference/engine/classes/MeshPart.md) directly.

*Yields · Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) validation is completed for. |
| `instance` | `Instance` |  | The instance validation is run on. |
| `bodyPart` | `BodyPart` |  | [BodyPart](/docs/reference/engine/enums/BodyPart.md) the instance is expected to be. |

**Returns:** `Tuple` — A tuple containing, in order:

- A boolean indicating if validation was successful for the body part.
- An optional table of strings. This includes failure reasons if
  validation was unsuccessful; otherwise `nil` if validation was
  successful.

### Method: AvatarCreationService:ValidateUGCFullBodyAsync

**Signature:** `AvatarCreationService:ValidateUGCFullBodyAsync(player: Player, humanoidDescription: HumanoidDescription): Tuple`

Studio only. Given a [Player](/docs/reference/engine/classes/Player.md) and [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md), all
instances in the [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) will be validated.

The [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) is expected to include instances set on
[BodyPartDescription](/docs/reference/engine/classes/BodyPartDescription.md) children for each of the six required
[BodyPart](/docs/reference/engine/enums/BodyPart.md) values. Optionally, it can include instances set on
[AccessoryDescription](/docs/reference/engine/classes/AccessoryDescription.md) children for any supported
[AccessoryType](/docs/reference/engine/enums/AccessoryType.md).

*Yields · Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) validation is completed for. |
| `humanoidDescription` | `HumanoidDescription` |  | [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) representing the body that validation is run on. |

**Returns:** `Tuple` — A tuple containing, in order:

- A boolean indicating if validation was successful for the body.
- An optional table of strings. This includes failure reasons if
  validation was unsuccessful; otherwise `nil` if validation was
  successful.

## Events

### Event: AvatarCreationService.AvatarAssetModerationCompleted

**Signature:** `AvatarCreationService.AvatarAssetModerationCompleted(assetId: int64, moderationStatus: ModerationStatus)`

Fires when an in-experience-created avatar asset's moderation status has
been updated from pending. This event provides a streamlined way to know
when an avatar asset created through
[PromptCreateAvatarAssetAsync()](/docs/reference/engine/classes/AvatarCreationService.md)
has completed the moderation process and is ready for use in-experience.

Note that this event only fires for avatar assets created within the
current experience and will trigger when the [ModerationStatus](/docs/reference/engine/enums/ModerationStatus.md)
changes from [NotReviewed](/docs/reference/engine/enums/ModerationStatus.md) to any other
status. The event fires on the client only.

*Security: None · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `assetId` | `int64` | The asset ID of the asset that has completed moderation. |
| `moderationStatus` | `ModerationStatus` | The final [ModerationStatus](/docs/reference/engine/enums/ModerationStatus.md) result after moderation completed. |

**Avatar Asset Moderation Completed**

```lua
local AvatarCreationService = game:GetService("AvatarCreationService")
local conn = AvatarCreationService.AvatarAssetModerationCompleted:Connect(function(assetId, moderationStatus)
	print("Asset, " .. assetId .. ", ready with moderation status: " .. moderationStatus)
end)
```

### Event: AvatarCreationService.AvatarModerationCompleted

**Signature:** `AvatarCreationService.AvatarModerationCompleted(outfitId: int64, moderationStatus: ModerationStatus)`

Fires when an in-experience-created avatar's moderation status has been
updated from pending. This event provides a streamlined way to know when
an avatar created through
[PromptCreateAvatarAsync()](/docs/reference/engine/classes/AvatarCreationService.md)
has completed the moderation process and is ready for use in-experience.

Note that this event only fires for avatars created within the current
experience and will trigger when the [ModerationStatus](/docs/reference/engine/enums/ModerationStatus.md) changes from
[NotReviewed](/docs/reference/engine/enums/ModerationStatus.md) to any other status. The
event fires on the client only.
[GetOutfitDetailsAsync](/docs/reference/engine/classes/AvatarEditorService.md)
can be used on the server to verify the current moderation status if
needed.

*Security: None · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `outfitId` | `int64` | The outfit ID of the avatar that has completed moderation. |
| `moderationStatus` | `ModerationStatus` | The final [ModerationStatus](/docs/reference/engine/enums/ModerationStatus.md) result after moderation completion. |

### Event: AvatarCreationService.AvatarOutfitModerationCompleted

**Signature:** `AvatarCreationService.AvatarOutfitModerationCompleted(outfitId: int64, moderationStatus: ModerationStatus, outfitType: OutfitType)`

Fires on the client when an in-experience-created outfit's moderation
status changes from [NotReviewed](/docs/reference/engine/enums/ModerationStatus.md) to
another status. Use this event for any in-experience-created outfit type.
Current outfit creation flows include
[PromptCreateAvatarAsync()](/docs/reference/engine/classes/AvatarCreationService.md).
Future in-experience outfit types will use this event as well
([AvatarModerationCompleted](/docs/reference/engine/classes/AvatarCreationService.md)
is deprecated).

Use `outfitType` to determine the kind of outfit that completed
moderation. This event is informational: an outfit cannot be used until
its moderation status permits it.

*Security: None · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `outfitId` | `int64` | The outfit ID of the outfit that has completed moderation. |
| `moderationStatus` | `ModerationStatus` | The final [ModerationStatus](/docs/reference/engine/enums/ModerationStatus.md) result after moderation completion. |
| `outfitType` | `OutfitType` | The [OutfitType](/docs/reference/engine/enums/OutfitType.md) of the moderated outfit. |

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