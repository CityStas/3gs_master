---
name: SecurityCapability
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Identifies a specific permission capability that a sandboxed script container may grant or restrict."
---

# SecurityCapability

Identifies a specific permission capability that a sandboxed script container
may grant or restrict.

**Type:** enum

## Description

`SecurityCapability` is a bitmask-based permission system that controls which
engine APIs and Luau language features are accessible to scripts running
inside sandboxed containers. Each value represents one capability bit that can
be granted or restricted.

When an [Instance](/docs/reference/engine/classes/Instance.md) has its [Sandboxed](/docs/reference/engine/classes/Instance.md) property
enabled, the engine intersects the capabilities of all ancestor containers to
determine the effective permission set of any script that executes within that
container. API members, classes, and Luau built-ins are each annotated with
one or more `SecurityCapability` values; a script's thread must hold every
required capability to call them.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `RunClientScript` | 0 | Indicates that a script container is permitted to execute scripts on the client ([LocalScript](/docs/reference/engine/classes/LocalScript.md)). |
| `RunServerScript` | 1 | Indicates that a script container is permitted to execute scripts on the server ([Script](/docs/reference/engine/classes/Script.md)). |
| `AccessOutsideWrite` | 2 | Grants a script read-write access to instances that live outside its sandboxed container. |
| `AssetRequire` | 3 | Deprecated. Use [SecurityCapability.LoadUnownedAsset](/docs/reference/engine/enums/SecurityCapability.md) instead. |
| `LoadString` | 4 | Allows a script to use the `loadstring()` Luau built-in to compile and execute a string as code. |
| `ScriptGlobals` | 5 | Allows a script to access the `shared` and `_G` shared global variable tables. |
| `CreateInstances` | 6 | Allows a script to create new `Instance` objects using `Instance.new()`. |
| `Basic` | 7 | Guards access to a broad set of general-purpose engine APIs that do not belong to a more specific capability category. |
| `Audio` | 8 | Guards access to audio engine APIs such as [Sound](/docs/reference/engine/classes/Sound.md), [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md), and related classes. |
| `DataStore` | 9 | Guards access to data store APIs such as [DataStoreService](/docs/reference/engine/classes/DataStoreService.md) and its associated objects. |
| `Network` | 10 | Guards access to low-level networking APIs such as [HttpService](/docs/reference/engine/classes/HttpService.md). |
| `Physics` | 11 | Guards access to physics engine APIs such as [Constraint](/docs/reference/engine/classes/Constraint.md) classes and [BasePart](/docs/reference/engine/classes/BasePart.md) physics properties. |
| `UI` | 12 | Guards access to UI engine APIs such as [ScreenGui](/docs/reference/engine/classes/ScreenGui.md), [Frame](/docs/reference/engine/classes/Frame.md), and other [GuiObject](/docs/reference/engine/classes/GuiObject.md) classes. |
| `CSG` | 13 | Guards access to Constructive Solid Geometry (CSG) APIs such as [UnionOperation](/docs/reference/engine/classes/UnionOperation.md) and [NegateOperation](/docs/reference/engine/classes/NegateOperation.md). |
| `Chat` | 14 | Guards access to chat engine APIs such as [TextChatService](/docs/reference/engine/classes/TextChatService.md) and related chat classes. |
| `Animation` | 15 | Guards access to animation engine APIs such as [AnimationController](/docs/reference/engine/classes/AnimationController.md) and related classes. |
| `Avatar` | 16 | Deprecated. Use [SecurityCapability.AvatarAppearance](/docs/reference/engine/enums/SecurityCapability.md) instead. |
| `Input` | 17 | Guards access to user input APIs such as [UserInputService](/docs/reference/engine/classes/UserInputService.md) and [ContextActionService](/docs/reference/engine/classes/ContextActionService.md). |
| `Environment` | 18 | Guards access to environment and world-setting APIs such as [Lighting](/docs/reference/engine/classes/Lighting.md) and [Atmosphere](/docs/reference/engine/classes/Atmosphere.md). |
| `RemoteEvent` | 19 | Guards access to remote event and function APIs such as [RemoteEvent](/docs/reference/engine/classes/RemoteEvent.md) and [RemoteFunction](/docs/reference/engine/classes/RemoteFunction.md). |
| `LegacySound` | 20 | Guards access to the legacy [Sound](/docs/reference/engine/classes/Sound.md) and pre-[VoiceChatService.UseAudioApi](/docs/reference/engine/classes/VoiceChatService.md) sound stack APIs. |
| `Players` | 21 | Guards access to [Players](/docs/reference/engine/classes/Players.md) service APIs that query or manage connected players. |
| `CapabilityControl` | 22 | Guards access to the `Instance.Capabilities` and `Instance.Sandboxed` properties that configure script sandboxing. |
| `Plugin` | 23 | Mirrors the legacy `Plugin` permission level, granting access to Studio plugin APIs. |
| `LocalUser` | 24 | Mirrors the legacy `LocalUser` permission level, granting access to IDE-only and Studio-level APIs. |
| `WritePlayer` | 25 | Mirrors the legacy `WritePlayer` permission level, granting the ability to modify player identity properties such as name and `UserId`. |
| `RobloxScript` | 26 | Mirrors the legacy `RobloxScript` permission level, granting access to `CoreScript` APIs. |
| `RobloxEngine` | 27 | Mirrors the legacy `RobloxEngine` permission level, granting access to internal engine-level APIs. |
| `Unassigned` | 28 | The default capability assigned to API members that have not been explicitly assigned to any other capability category. |
| `InternalTest` | 29 | Restricts access to non-sensitive APIs that are intentionally kept internal. |
| `PluginOrOpenCloud` | 30 | Restricts access to APIs callable only from Studio plugin or Open Cloud Luau execution sessions. |
| `Assistant` | 31 | Restricts access to APIs that may only be called from Studio Assistant execution contexts. |
| `RemoteCommand` | 32 | Restricts access to APIs that are executable only from Studio's `RemoteCommandService` in Team Create sessions. |
| `AssetRead` | 33 | Guards access to APIs that read or query asset metadata from the Roblox catalog. |
| `AssetManagement` | 34 | Guards access to asset management APIs such as [ContentProvider:PreloadAsync()](/docs/reference/engine/classes/ContentProvider.md) and encryption-key registration. |
| `DynamicGeneration` | 35 | Guards access to procedural and AI-driven content generation APIs such as [EditableMesh](/docs/reference/engine/classes/EditableMesh.md) and [AvatarCreationService](/docs/reference/engine/classes/AvatarCreationService.md). |
| `PlatformAvatarEditing` | 36 | Guards access to platform-level avatar editing APIs provided by [AvatarEditorService](/docs/reference/engine/classes/AvatarEditorService.md). |
| `AssetCreateUpdate` | 37 | Guards access to APIs that create or update published Roblox assets. |
| `Capture` | 38 | Guards access to [CaptureService](/docs/reference/engine/classes/CaptureService.md) APIs that take screenshots and record video. |
| `SensitiveInput` | 39 | Guards access to sensitive user input APIs such as those that can read raw keyboard or mouse data beyond normal game input. |
| `Monetization` | 40 | Guards access to in-experience purchase and monetization APIs such as [MarketplaceService](/docs/reference/engine/classes/MarketplaceService.md). |
| `LoadOwnedAsset` | 41 | Allows a script to load assets that are owned by the experience's creator using [InsertService](/docs/reference/engine/classes/InsertService.md) or [LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md). |
| `Social` | 42 | Guards access to social APIs such as [SocialService](/docs/reference/engine/classes/SocialService.md), [FriendPages](/docs/reference/engine/classes/FriendPages.md), and [ExperienceInviteOptions](/docs/reference/engine/classes/ExperienceInviteOptions.md). |
| `ServerCommunication` | 43 | Guards access to server-to-server messaging APIs such as [MessagingService](/docs/reference/engine/classes/MessagingService.md). |
| `Logging` | 44 | Guards access to [LogService](/docs/reference/engine/classes/LogService.md) and logging-related APIs. |
| `PromptExternalPurchase` | 45 | Guards access to APIs that initiate external (non-Roblox) purchase prompts. |
| `Groups` | 46 | Guards access to group-related APIs such as [GroupService](/docs/reference/engine/classes/GroupService.md). |
| `Teleport` | 47 | Guards access to teleportation APIs such as [TeleportService](/docs/reference/engine/classes/TeleportService.md), [TeleportOptions](/docs/reference/engine/classes/TeleportOptions.md), and [TeleportAsyncResult](/docs/reference/engine/classes/TeleportAsyncResult.md). |
| `Consequences` | 48 | Guards access to moderation and player-consequence APIs such as [Players:BanAsync()](/docs/reference/engine/classes/Players.md) and [ModerationService](/docs/reference/engine/classes/ModerationService.md). |
| `Material` | 49 | Guards access to [MaterialService](/docs/reference/engine/classes/MaterialService.md), [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md), and custom material APIs. |
| `AvatarBehavior` | 50 | Guards access to APIs that control avatar locomotion and behavior at runtime. |
| `AvatarAppearance` | 51 | Guards access to APIs that read or modify avatar appearance, such as [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md). |
| `LoadUnownedAsset` | 52 | Allows a script to [LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md) asset IDs or call [InsertService:LoadAsset()](/docs/reference/engine/classes/InsertService.md) for assets not owned by the creator. |