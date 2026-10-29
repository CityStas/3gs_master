---
name: unity-core
description: "Unity 6000.3 core API: GameObject, Component, Transform, MonoBehaviour lifecycle, GameObject/Component lookup, coroutines, Time, Mathf, Vector3/Quaternion, ScriptableObject, Physics, colliders and triggers. Use for any general Unity API question or when you need an exact symbol. Русские триггеры: «сцена», «префаб», «компонент», «повернуть объект», «жизненный цикл», «коллайдер», «триггер»."
---

# Unity Core

Use for `GameObject`, `Component`, `Transform`, `MonoBehaviour`, coroutines, `Physics`,
`ScriptableObject` and the math types. Query `unity_rag_search` with the exact symbol when
possible (`Rigidbody.AddForce`, `CharacterController.Move`, `SceneManager.LoadScene`).

## Lifecycle, in order

```
Awake        -> once, before the object is enabled, all objects exist (wire references here)
OnEnable     -> every time the object is enabled; subscribe to events here
Start        -> once, before the first Update, after all Awake/OnEnable
FixedUpdate  -> every physics step (0.02 s default); Rigidbody movement belongs here
Update       -> every frame; input and gameplay
LateUpdate   -> every frame, after Update; cameras and follow logic belong here
OnDisable    -> unsubscribe here (a missing OnDisable is the classic MissingReferenceException)
OnDestroy    -> last; clear static/singleton references here
```

Rules that come out of that table:
- wire `[SerializeField]` references in `Awake`, not `Start`, when another object's `Start`
  needs them;
- `Rigidbody` forces go in `FixedUpdate`; `CharacterController.Move` and `Input` go in `Update`;
- cameras go in `LateUpdate`.

## Lookup

| Need | Use | Not |
|---|---|---|
| a component on this object | `GetComponent<T>()` | `gameObject.rigidbody` (removed in Unity 5) |
| a component on a child | `GetComponentInChildren<T>()` | `transform.FindChild(...)` (renamed) |
| a single object in the scene | `FindFirstObjectByType<T>()` | `FindObjectOfType<T>()` (obsolete in Unity 6) |
| many objects | `FindObjectsByType<T>(FindObjectsSortMode.None)` | `FindObjectsOfType<T>()` (obsolete) |
| a named object | a `[SerializeField]` reference | `GameObject.Find("X")` in `Update` |

`Find*` is a fallback. The correct answer for a reference between objects is a
`[SerializeField]` field or a reference assigned by the scene builder.

## Instantiating and destroying

```csharp
var go = Instantiate(prefab, position, rotation);      // returns Object
var enemy = Instantiate(prefab, position, rotation);   // generic inference works
enemy.GetComponent<Health>().TakeDamage(10f);
Destroy(go);                 // end of frame
Destroy(go, 3f);             // after 3 s
DestroyImmediate(go);        // EDITOR ONLY - in play mode it corrupts the scene
```

`Instantiate` on a `Prefab` reference in a `MonoBehaviour` field is fine; `Instantiate` on a
`GameObject` in the scene clones the scene object, which is almost never what is wanted.

## Structs are not references

`Vector3`, `Quaternion`, `Color`, `Rect`, `Bounds` are **structs**. `transform.position`
returns a copy:

```csharp
transform.position.x = 5f;        // CS1612 - does not compile
var p = transform.position; p.x = 5f; transform.position = p;   // correct
transform.position += new Vector3(5f, 0f, 0f);                  // correct
```

The same applies to `rect.xMin`, `bounds.min`, and `color.a` when `color` is a property.

## Coroutines

```csharp
private void Start() => StartCoroutine(SpawnLoop());

private IEnumerator SpawnLoop()
{
    while (true)
    {
        Spawn();
        yield return new WaitForSeconds(1.5f);      // scaled time
        // yield return new WaitForSecondsRealtime(1.5f);  // unscaled (works at timeScale 0)
        // yield return null;                               // next frame
    }
}
```

A coroutine stops when its `MonoBehaviour` is destroyed or disabled. `yield break` ends it.
`WaitForSeconds` respects `Time.timeScale`; with `timeScale = 0` it never resumes — that is why
a pause menu needs `WaitForSecondsRealtime`.

## ScriptableObject

Data that lives as an asset, not in a scene:

```csharp
[CreateAssetMenu(fileName = "EnemyStats", menuName = "MyGame/Enemy Stats")]
public class EnemyStats : ScriptableObject
{
    public float maxHealth = 100f;
    public float speed = 3.5f;
}
```

Create via *Assets > Create > MyGame > Enemy Stats*. It is serialized by reference, so a
thousand enemies share one asset — mutate it at runtime and you mutate all of them (use
`Instantiate(stats)` for per-instance state).

## Physics

- `Rigidbody` (3D) / `Rigidbody2D` (2D) — `rb.linearVelocity` in Unity 6 (`velocity` is renamed).
- `Collider` shapes: `BoxCollider`, `SphereCollider`, `CapsuleCollider`, `MeshCollider`
  (convex only for a moving object).
- **Triggers need a Rigidbody.** `OnTriggerEnter` never fires when both colliders are static.
- `OnCollisionEnter` requires a non-kinematic Rigidbody on at least one side.
- Layers: `Physics.Raycast(origin, dir, out hit, dist, layerMask)` — a mask of `0` (Nothing)
  makes every ray miss.
