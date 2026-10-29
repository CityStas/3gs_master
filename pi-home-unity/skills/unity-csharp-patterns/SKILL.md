---
name: unity-csharp-patterns
description: "C# idioms for Unity: events and delegates, null-safe references to destroyed objects, singletons, object pooling, serialization, async/await vs coroutines, interfaces for damageable/interactable, ScriptableObject data, state machines. Use when writing or reviewing Unity C# beyond a single script. Русские триггеры: «паттерн», «события», «синглтон», «пул объектов», «архитектура», «рефакторинг»."
---

# Unity C# patterns

## Events, not polling

```csharp
public class Health : MonoBehaviour
{
    public event Action<float, float> Changed;    // current, max
    public event Action Died;

    private void Raise() => Changed?.Invoke(_current, _max);
}
```

Subscribe in `OnEnable`, unsubscribe in `OnDisable`. A subscriber that never unsubscribes
keeps a destroyed object in the delegate list — `MissingReferenceException` on the next scene
load. This is the single most common runtime bug in generated Unity code.

For a value that many systems read every frame, a property is fine. For a value that changes
rarely and drives UI, an event is the correct shape.

## Interfaces keep systems decoupled

```csharp
public interface IDamageable { void TakeDamage(float amount, GameObject source = null); }
public interface IInteractable { string Prompt { get; } void Interact(GameObject actor); }

// usage - no dependency on a concrete class
if (other.TryGetComponent(out IDamageable d)) d.TakeDamage(12f);
```

`TryGetComponent` is the Unity-6-friendly form (it allocates nothing, unlike
`GetComponent<T>() != null`). It works with interfaces.

## Singleton — only when it is genuinely global

```csharp
public class GameManager : MonoBehaviour
{
    public static GameManager Instance { get; private set; }

    private void Awake()
    {
        if (Instance && Instance != this) { Destroy(gameObject); return; }
        Instance = this;
        // DontDestroyOnLoad(gameObject);   // only if it must survive a scene load
    }

    private void OnDestroy() { if (Instance == this) Instance = null; }
}
```

The `OnDestroy` clear is not optional: without it the static field points at a destroyed
object after a scene reload. `DontDestroyOnLoad` on many objects produces duplicates.

## Object pooling

`Instantiate`/`Destroy` per bullet is the classic frame-time spike.

```csharp
public class BulletPool : MonoBehaviour
{
    [SerializeField] private GameObject prefab;
    [SerializeField] private int initial = 32;

    private readonly Queue<GameObject> _free = new();

    private void Awake()
    {
        for (int i = 0; i < initial; i++) _free.Enqueue(Create());
    }

    private GameObject Create()
    {
        var go = Instantiate(prefab, transform);
        go.SetActive(false);
        return go;
    }

    public GameObject Rent(Vector3 pos, Quaternion rot)
    {
        var go = _free.Count > 0 ? _free.Dequeue() : Create();
        go.transform.SetPositionAndRotation(pos, rot);
        go.SetActive(true);
        return go;
    }

    public void Return(GameObject go)
    {
        go.SetActive(false);
        go.transform.SetParent(transform);
        _free.Enqueue(go);
    }
}
```

Unity 6 also ships `UnityEngine.Pool.ObjectPool<T>` if a hand-rolled queue is not wanted.

## Serialization rules

- `[SerializeField] private float speed = 5f;` — the Inspector field for a private value.
- **`[SerializeField]` on a public field is redundant** (public fields serialize by default).
- Only fields serialize: **properties are silently skipped**. If it must be saved, it must be
  a field.
- `[Serializable]` is required on every custom class nested in a component or in `JsonUtility`
  data.
- `[NonSerialized] public float runtimeOnly;` for state that must not persist.
- A reference to a `GameObject`/`Component` in a scene serializes as a fileID — moving the
  asset without its `.meta` breaks it.

## Coroutines vs async/await

| Use coroutine | Use async/await |
|---|---|
| frame-by-frame work, `yield return null` | I/O: `UnityWebRequest`, file reads |
| timed sequences | waiting on an external service |
| anything that must run on the main thread per frame | `Task` composition (`WhenAll`) |

`async void` is only for an event handler; use `async Task` elsewhere. `await` returns to the
main thread by default in Unity (a `SynchronizationContext` is installed), so touching
`transform` after an `await` is safe.

## State machines

For anything past two states, an explicit enum + switch beats boolean flags:

```csharp
private enum State { Idle, Chase, Attack, Dead }
private State _state = State.Idle;

private void Update()
{
    switch (_state)
    {
        case State.Idle:   TickIdle();   break;
        case State.Chase:  TickChase();  break;
        case State.Attack: TickAttack(); break;
        case State.Dead:   return;
    }
}

private void SetState(State next) { if (_state == next) return; OnExit(_state); _state = next; OnEnter(next); }
```

Two booleans (`isJumping`, `isGrounded`) already encode four states, two of which are
impossible — that is where the bug lives.

## Composition over inheritance

A `Player : Character : Actor : MonoBehaviour` chain is unmaintainable in Unity because
components are the composition unit. Prefer small components (`Health`, `Mover`, `Looker`,
`DamageDealer`) that talk through events and interfaces, with a thin coordinator if needed.
