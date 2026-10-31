# Roblox Studio — Workspace and Workflow

## 1. What Studio is

Roblox Studio is the primary integrated development environment for building, scripting, testing and publishing Roblox experiences. Its core panels include the 3D viewport, Explorer, Properties, Toolbox/Creator Store, Output, Script Editor and test controls.

Official overview: https://create.roblox.com/docs/studio

## 2. Core panels

- **Explorer:** hierarchical view of the current DataModel. Use it to inspect parent-child relationships and script placement.
- **Properties:** inspect and change properties of the selected Instance.
- **Script Editor:** Luau editing with autocomplete, diagnostics, type checking and API hints.
- **Output:** runtime messages, warnings and errors. Capture the full error and stack trace when debugging.
- **Command Bar:** execute short Luau snippets in the current Studio context. Treat it as a powerful tool; confirm the target place and data model before destructive operations.
- **Toolbox / Creator Store:** browse creator assets, models and plugins. Third-party assets can contain scripts; inspect them before using.
- **Asset Manager:** manage assets imported into the currently opened experience.

## 3. Recommended development loop

1. Inspect the existing project structure and identify relevant scripts/Instances.
2. State the intended behavior and acceptance criteria.
3. Make the smallest coherent change.
4. Run static checks/type analysis where available.
5. Start a Studio playtest and inspect Output.
6. Test both server and client behavior when relevant.
7. Test at least one alternate device/resolution for UI/input work.
8. Review the diff/change set and save/publish only when explicitly intended.

## 4. Test modes

Studio provides Test, Test Here, Run, Server & Clients, device simulation and network simulation. Multi-client testing is important for multiplayer behavior because a solo client test cannot expose all synchronization and race conditions.

Common controls documented by Roblox include Test (F5), Run (F8), stopping a simulation (Shift+F5), and multi-client simulation from the Test controls. Shortcuts may vary; consult the current Studio UI/docs.

Official guide: https://create.roblox.com/docs/studio/testing-modes

## 5. Saving, publishing and environments

Keep development/test experiences separate from production where practical. Never enable API access in Studio against production DataStores just to test a feature. Use a dedicated test version and test data.

Distinguish:

- Save to local/Studio project state.
- Publish changes to Roblox.
- Publish a new version of an experience/place.

An AI agent must not publish, overwrite live data, delete assets, or change permissions without explicit user authorization.

## 6. External file workflow

For source-controlled development, Roblox documents tools such as Rojo and Rokit. These are optional. Studio MCP and Rojo solve different problems:

- Studio MCP: AI client interacts with an open Studio session.
- Rojo: synchronizes local files with the Studio DataModel.
- Git: tracks code/project history and supports review/rollback.

Official external tools overview: https://create.roblox.com/docs/projects/external-tools
