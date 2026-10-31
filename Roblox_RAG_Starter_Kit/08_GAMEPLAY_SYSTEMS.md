# Gameplay Systems — UI, Input, Physics, Characters, NPCs and Assets

This file is an orientation map. Exact API usage must be verified against the current Engine API Reference.

## 1. User interfaces

Common UI elements and concepts:

- `ScreenGui`: screen-space interface container, usually displayed through `PlayerGui`.
- `Frame`, `TextLabel`, `TextButton`, `ImageLabel`, `ImageButton`: common visual building blocks.
- `UIListLayout`, `UIGridLayout`, `UIPadding`, `UICorner`, `UIStroke`, `UIScale`: layout and styling helpers.
- `UDim2`: combines scale and offset for responsive positioning/sizing.
- `TweenService`: interpolate supported properties over time.

Design for multiple device sizes and input types. Prefer layout constraints and scale where appropriate; test on mobile dimensions. Do not assume mouse hover exists on touch devices.

## 2. Input

Common APIs:

- `UserInputService`: input state and device information.
- `ContextActionService`: bind actions across input devices.
- `GuiService`: GUI navigation and platform UI behavior.
- `ProximityPrompt`: world interaction prompt.

Choose input APIs based on the intended cross-platform behavior. Avoid hard-coding keyboard-only controls for games targeting touch or console.

## 3. Characters and animation

Common components:

- `Players`: player lifecycle.
- `Player.Character`: current character model; it can be replaced on respawn.
- `Humanoid`: common character movement/health state.
- `HumanoidRootPart`: commonly used root part in standard character rigs.
- `Animator` and `AnimationTrack`: animation playback.

Do not assume every character uses the same rig, body scale or exact child hierarchy unless the experience enforces it. Handle character respawn and missing descendants.

## 4. NPC navigation

`PathfindingService` supports path computation. A production NPC needs more than a call to compute a path: it needs state management, path failure handling, waypoint progression, stuck detection, target validation and recomputation strategy. Verify current path status and APIs in the Engine API Reference.

## 5. Physics and world interactions

Common concepts:

- `BasePart`, `Assembly`, `Attachment`.
- Constraints such as `WeldConstraint`, `HingeConstraint`, `SpringConstraint`, `AlignPosition`, `AlignOrientation`.
- `RaycastParams`, raycasts and spatial queries.
- `PhysicsService` collision groups.
- `CollectionService` tags for grouping related Instances.

Use constraints and physics APIs appropriate to the desired simulation. Avoid expensive repeated queries without profiling. Validate important interactions on the server.

## 6. Audio

Use current audio classes and services documented by Roblox. Asset permissions and moderation status matter. Do not assume an arbitrary uploaded audio asset is available to an experience.

## 7. Assets and Creator Store

Roblox's Asset Manager, Toolbox and Importer serve different workflows. Creator Store assets can contain scripts and require inspection. Validate asset source, permissions, dependencies and script contents before inserting into a production project.

Official asset guidance: https://create.roblox.com/docs/projects/assets

## 8. Focused official guides

- Pathfinding: https://create.roblox.com/docs/characters/pathfinding
- Animation: https://create.roblox.com/docs/animation
- Playing animations from scripts: https://create.roblox.com/docs/animation/using
- Physics: https://create.roblox.com/docs/physics
- Raycasting: https://create.roblox.com/docs/workspace/raycasting
- Collision filtering: https://create.roblox.com/docs/workspace/collisions
- ContextActionService API: https://create.roblox.com/docs/reference/engine/classes/ContextActionService

## 9. Monetization-aware gameplay

Roblox supports several monetization systems, including passes, developer products, subscriptions and private servers. Build purchase flows around server-side receipt handling and durable entitlement state; never grant purchasable currency or items solely from a client message. Consult current monetization docs and relevant policy pages before implementation.

Official overview: https://create.roblox.com/docs/production/monetization
