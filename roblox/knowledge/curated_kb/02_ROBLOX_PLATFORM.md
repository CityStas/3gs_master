# Roblox Platform Fundamentals

## 1. Experience, universe and place

Roblox content is organized into experiences and places. An experience can contain one or more places; each place contains a DataModel hierarchy. Avoid using `game`, `place`, and `experience` as interchangeable terms.

- **Experience / universe:** the overall game product and its shared configuration, services, permissions and places.
- **Place:** a specific world/level within an experience, with its own DataModel and PlaceId.
- **DataModel:** the live/edit hierarchy of Roblox Instances in a place.

For current details, consult Creator Hub and the relevant Creator Dashboard pages. IDs and publishing workflows can change; do not guess IDs.

## 2. DataModel and Instance

A Roblox place is represented by a hierarchical DataModel. Almost every object in the hierarchy is an `Instance`. Instances have a class, name, parent, properties, methods, events and potentially child Instances.

Common examples:

- `Workspace`: 3D world, parts, terrain and runtime world objects.
- `Players`: connected players and player-related objects.
- `ReplicatedStorage`: objects intended to be available to both server and client.
- `ServerScriptService`: server-side scripts.
- `ServerStorage`: server-only objects and assets.
- `StarterGui`: templates copied into player UI.
- `StarterPlayer`: templates for player scripts and character behavior.
- `Lighting`: lighting and atmosphere configuration.
- `SoundService`: global audio configuration.

These containers have different replication and execution semantics. Always verify the exact container's behavior in current documentation.

## 3. Services

Services are engine-managed Instances usually obtained through `game:GetService("ServiceName")`.

```lua
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local RunService = game:GetService("RunService")
```

Prefer `GetService()` for services rather than searching arbitrary descendants. Do not assume every class is a service.

Common service groups:

- Player/session: `Players`, `Teams`, `TeleportService`.
- World/physics: `Workspace`, `PhysicsService`, `CollectionService`, `PathfindingService`.
- UI/input: `StarterGui`, `UserInputService`, `ContextActionService`, `GuiService`.
- Networking/runtime: `RunService`, `HttpService`, `Debris`, `TweenService`.
- Persistence/cloud: `DataStoreService`, `MemoryStoreService`, `MessagingService`.
- Audio: `SoundService`, audio-related engine classes.

## 4. Instance lifecycle

Typical lifecycle operations:

- Create an instance: `Instance.new("Part")`.
- Configure its properties.
- Parent it into the DataModel.
- Connect to events.
- Clean it up when no longer needed, often with `:Destroy()` or `Debris`.

```lua
local part = Instance.new("Part")
part.Name = "SpawnedPart"
part.Size = Vector3.new(4, 1, 4)
part.Anchored = true
part.Parent = workspace
```

Avoid creating large numbers of Instances every frame. Reuse objects or use pooling where profiling demonstrates a need.

## 5. Properties, methods, events and callbacks

- **Property:** state, e.g. `BasePart.Position`.
- **Method:** operation, e.g. `Instance:Destroy()`.
- **Event:** notification, e.g. `BasePart.Touched`.
- **Callback:** a function property invoked by the engine, e.g. a remote function callback.

RAG should distinguish these types. Search exact identifiers in Engine API Reference before proposing code.

## 6. Common spatial datatypes

- `Vector2`, `Vector3`: 2D/3D vectors.
- `CFrame`: position and orientation transform.
- `UDim`, `UDim2`: UI dimensions combining scale and offset.
- `Color3`: RGB color.
- `Enum`: engine-defined enumerations.
- `RaycastParams`, `OverlapParams`: query configuration types.

Do not treat `CFrame` as only a position; it also represents rotation/orientation.

## 7. Authoritative references

- Data model: https://create.roblox.com/docs/projects/data-model
- Engine API: https://create.roblox.com/docs/reference/engine
- Services: https://create.roblox.com/docs/scripting/services
