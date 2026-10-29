---
name: unity-performance
description: "Unity performance: GetComponent and Find in Update, per-frame allocations and GC spikes, object pooling, batching/instancing, LOD, occlusion culling, Profiler and Frame Debugger, physics settings, texture and mesh budget. Use when a Unity project stutters, drops frames or allocates every frame. Русские триггеры: «тормозит», «лаги», «fps», «производительность», «оптимизация», «gc», «профайлер»."
---

# Unity performance

## Measure before changing

- **Profiler**: *Window > Analysis > Profiler* (`com.unity.profiling.core`), or
  `Profiler.BeginSample("X")` / `Profiler.EndSample()` around a suspect block.
- **Frame Debugger**: *Window > Analysis > Frame Debugger* shows why draw calls are not batched.
- **Memory Profiler** package for a snapshot with retained sizes.
- In a build, `-profiler-enable` and `-deepprofiling` are the batch equivalents.

Optimising without a profile is guessing; the wrong guess costs a session.

## The three things that actually cost frames

1. **Per-frame allocations** → GC spikes. `foreach` over a `List<T>` is fine, but a `foreach`
   over a collection that returns an interface, `string` concatenation, `new Vector3` in a tight
   loop, LINQ, and `GetComponent<T>()` in `Update` all allocate.
   ```csharp
   private Transform _target;
   private void Awake() => _target = GameObject.FindWithTag("Player").transform;
   private void Update() { /* use _target, not GetComponent */ }
   ```
   `TryGetComponent` allocates nothing; `GetComponent` + null check does not either, but both are
   slow in `Update`. Cache in `Awake`.
2. **Draw calls / batching**. Static batching for non-moving geometry (`isStatic`), GPU
   instancing for many copies of one mesh (enable `Enable GPU Instancing` on the material, or use
   `Graphics.RenderMeshInstanced`). A URP project batches poorly when materials differ per object
   — share a material and use a `MaterialPropertyBlock` for per-instance colour.
3. **Overdraw and fill rate** — transparent particles and UI stacked over each other. Cull the
   particle count, shrink the screen area.

## The usual suspects, in order

| Suspect | Fix |
|---|---|
| `GetComponent`/`Find*` in `Update` | cache in `Awake`; `FindFirstObjectByType` once |
| `Instantiate`/`Destroy` per bullet | object pool |
| `Camera.main` in `Update` | it is a `FindGameObjectsWithTag` in older versions; cache it |
| `string` concat in `Update` | cache, or use a `StringBuilder` |
| `foreach` over a dictionary/list in `Update` | iterate a cached array |
| too many `Update` methods | one manager tick, or a `List<ITickable>` |
| `SendMessage`/`BroadcastMessage` | direct call or an event |
| a `MeshCollider` that is not convex on a moving object | primitive collider or a convex hull |
| thousands of small objects | combine meshes, or ECS/DOTS for the extreme case |
| a texture with `Read/Write Enabled` | turn it off unless the CPU needs the pixels |
| `Resources.Load` | move to Addressables / direct references |

## Physics

- `Physics.simulationMode` and `Time.fixedDeltaTime`: lowering `fixedDeltaTime` (0.02 → 0.01)
  doubles the physics cost. Raise it for slow-moving puzzles instead.
- `Physics.autoSimulation`/`Physics.Simulate` when physics is not needed every frame.
- A large `Rigidbody` count with continuous collision detection is expensive — `Collision
  Detection = Discrete` unless tunnelling is real.
- `Physics.queriesHitBackfaces` off (default) and layer masks narrow on every raycast.

## Rendering budget (rough, for a 60 fps desktop target)

- Draw calls: a few hundred, not thousands. URP SRP Batcher covers the rest if materials are
  compatible.
- Triangles: 1–3 M on screen is a comfortable desktop budget; 3 M in one asset is not (the
  generated GLB in `test_scene` is 3.08 M — decimate it).
- Real-time shadow casters: shadow distance is the lever, not the light count.
- LOD groups for anything with more than ~10 k triangles that can be seen far away.

## Verification

- Frame time before/after, with the same scene and the same camera path. A change that "feels
  faster" without a number is not a result.
- `Profiler` GC Alloc column: a steady per-frame allocation of more than a few KB is the bug.
- The player build, not the editor — the editor's numbers are always worse, but the *relative*
  comparison holds.
