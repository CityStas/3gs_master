# Roblox / Luau Glossary

| Term | Meaning |
|---|---|
| Experience | Overall Roblox game/product, potentially containing multiple places |
| Universe | Platform-level representation of an experience |
| Place | A specific world/level within an experience |
| DataModel | Hierarchical collection of Instances making up a place |
| Instance | Base object type for objects in the Roblox DataModel |
| Service | Engine-managed Instance accessed commonly through `game:GetService()` |
| Luau | Roblox scripting language derived from Lua 5.1 |
| Script | Script Instance commonly used for server execution in supported server contexts |
| LocalScript | Script Instance used for client execution in supported client contexts |
| ModuleScript | Reusable code module loaded through `require()` |
| Server | Authoritative simulation for shared game state |
| Client | Player-side runtime responsible for local interaction/presentation |
| Replication | Synchronization of relevant state between server and clients |
| RemoteEvent | Asynchronous one-way communication across client/server boundary |
| RemoteFunction | Request-response communication across client/server boundary |
| UnreliableRemoteEvent | Remote event for non-critical/continuous data where reliability/order can be traded |
| BindableEvent | Event communication within the same side/context, not across client/server |
| DataStore | Persistent key-value storage across sessions |
| MemoryStore | Short-lived, high-throughput storage for temporary shared state |
| Open Cloud | Roblox REST API platform for external tools/services |
| Creator Hub | Roblox developer portal and official documentation |
| Engine API Reference | Reference for Roblox classes, datatypes, enums, properties, methods and events |
| MCP | Model Context Protocol; standard for connecting AI clients to tools/apps |
| Studio MCP | Built-in Roblox Studio MCP server for agent interaction with an open Studio session |
| Rojo | Third-party tool for syncing local files with Roblox Studio DataModel |
| Rokit | Toolchain manager used to pin/manage versions of tools such as Rojo/Wally/Lune |
| Wally | Luau package manager |
| Playtest | Run a simulation of a place inside Studio |
| DataStore budget | Available request allowance for DataStore operations; check current API guidance |
| Network ownership | Which machine simulates physics for a networked assembly |
| `--!strict` | Luau script directive enabling strict type checking |
