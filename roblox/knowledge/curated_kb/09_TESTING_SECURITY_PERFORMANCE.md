# Testing, Security, Performance and Release

## 1. Testing strategy

Test the same feature at multiple levels:

- **Static review:** syntax, Luau type checking, lints, unused variables and API validity.
- **Playtest:** core happy path and expected failure states.
- **Server/client test:** confirm client visuals and server-owned state remain consistent.
- **Multi-client test:** multiplayer synchronization, join/leave, trading, combat and round state.
- **Device test:** touch, keyboard/mouse, gamepad, viewport dimensions and safe UI placement.
- **Network test:** latency, jitter and packet loss where relevant.
- **Regression test:** ensure existing mechanics still work after a change.

Official Studio testing guide: https://create.roblox.com/docs/studio/testing-modes

## 2. Security baseline

Treat all client-originated values and actions as untrusted. Important state changes must be validated and calculated on the server. Review:

- RemoteEvent/RemoteFunction handlers.
- ProximityPrompt and touch-triggered actions.
- Shop, currency, reward, inventory and trade flows.
- Movement, combat hit claims and physics ownership.
- DataStore input, serialization and schema migration.
- Secrets, API keys and server-only configuration.

Security references:

- https://create.roblox.com/docs/scripting/security/client-server-boundary
- https://create.roblox.com/docs/scripting/security/security-tactics

## 3. Performance loop

Use a measurement-driven cycle:

1. Reproduce and measure a performance problem.
2. Identify whether the bottleneck is CPU/script, physics, rendering, memory, network or loading.
3. Inspect with Studio profiling/developer tools.
4. Change one likely cause.
5. Measure again under comparable conditions.
6. Monitor after release.

Common areas to investigate:

- Too many active Instances or expensive per-frame loops.
- Excessive physics simulation and unanchored assemblies.
- Repeated raycasts/spatial queries.
- Large textures/meshes/audio or excessive loading.
- Unbounded event connections/tasks.
- Excessive network traffic or oversized remote payloads.
- UI/layout work that scales poorly.

Official guide: https://create.roblox.com/docs/performance-optimization

## 4. Release checklist

- No unresolved severe errors in Output.
- Core gameplay tested on server and client.
- Multiplayer flows tested where relevant.
- Data persistence tested in a separate test environment.
- Remote requests validated and rate-limited.
- UI and controls tested on target devices.
- Performance checked on a lower-end device profile.
- Assets, permissions and moderation compliance reviewed.
- Monetization and purchase flows tested without granting items from client claims.
- Change set reviewed; rollback path understood.
- Publishing/live changes explicitly approved by the project owner.

## 5. Agent restrictions

An AI coding agent should not publish, overwrite live experience data, alter access permissions, rotate credentials, delete large asset sets, or change production DataStores without explicit confirmation from the user. Prefer reversible edits and test places.
