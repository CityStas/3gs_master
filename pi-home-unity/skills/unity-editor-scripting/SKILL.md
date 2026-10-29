---
name: unity-editor-scripting
description: "Unity Editor automation: Editor scripts under Assets/Editor, MenuItem, CustomEditor/EditorWindow, AssetDatabase, PrefabUtility.SaveAsPrefabAsset, SerializedObject, building scenes and prefabs from code, running an editor method in batch mode (-executeMethod), TextureImporter and asset post-processing. Use whenever a scene, prefab, material or import setting must be created or changed programmatically. Русские триггеры: «editor script», «создай сцену», «создай префаб», «батч», «автоматизация редактора», «импорт настроек»."
---

# Unity Editor scripting

## The one rule

**Never hand-write `.unity` / `.prefab` / `.asset` YAML.** Build the object graph in an editor
script and let Unity serialize it. A hand-written scene imports with no error and is silently
broken (duplicate nodes, dangling `fileID`s, an object that never instantiates) — the same
failure the Godot stack avoids by making Godot save `.tscn` through `ResourceSaver`.

## Where the file goes

`Assets/Editor/` (any folder named `Editor`) makes the assembly editor-only, so `UnityEditor`
is available and the code is stripped from the player build. A script outside an `Editor/`
folder that touches `UnityEditor` breaks the build unless it is wrapped in
`#if UNITY_EDITOR … #endif`. `unity_validate` flags this.

## Menu item + batch entry point in one

```csharp
using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEngine;

namespace MyGame.EditorTools
{
    public static class SceneBuilder
    {
        [MenuItem("MyGame/Rebuild Main Scene")]
        public static void Rebuild() => Build();

        // Unity.exe -batchmode -quit -projectPath <p> -executeMethod MyGame.EditorTools.SceneBuilder.BuildBatch
        public static void BuildBatch() => Build();

        private static void Build()
        {
            var scene = EditorSceneManager.NewScene(NewSceneSetup.EmptyScene, NewSceneMode.Single);

            var ground = GameObject.CreatePrimitive(PrimitiveType.Plane);
            ground.name = "Ground";
            ground.transform.localScale = new Vector3(5f, 1f, 5f);
            ground.isStatic = true;

            var player = new GameObject("Player");
            player.transform.position = new Vector3(0f, 1f, 0f);
            var cc = player.AddComponent<CharacterController>();
            cc.height = 1.8f;
            cc.center = new Vector3(0f, 0.9f, 0f);
            player.AddComponent<PlayerController>();

            var sun = new GameObject("Sun");
            var light = sun.AddComponent<Light>();
            light.type = LightType.Directional;
            light.intensity = 1.1f;
            sun.transform.rotation = Quaternion.Euler(50f, -30f, 0f);

            var camGo = new GameObject("Main Camera");
            camGo.tag = "MainCamera";
            camGo.AddComponent<Camera>();
            camGo.AddComponent<AudioListener>();
            camGo.transform.position = new Vector3(0f, 3f, -6f);

            const string dir = "Assets/Scenes";
            if (!AssetDatabase.IsValidFolder(dir)) AssetDatabase.CreateFolder("Assets", "Scenes");
            const string path = dir + "/Main.unity";
            EditorSceneManager.SaveScene(scene, path);
            EditorBuildSettings.scenes = new[] { new EditorBuildSettingsScene(path, true) };
            AssetDatabase.SaveAssets();
            Debug.Log($"[SceneBuilder] wrote {path}");
        }
    }
}
```

Run it with `unity_run_method("MyGame.EditorTools.SceneBuilder.BuildBatch")`, or from the menu
while the editor is open. A batch method must be `static` and fully qualified; the editor must
not be open on the project.

## Prefabs

```csharp
var go = new GameObject("Enemy");
go.AddComponent<EnemyAI>();
var dir = "Assets/Prefabs";
if (!AssetDatabase.IsValidFolder(dir)) AssetDatabase.CreateFolder("Assets", "Prefabs");
PrefabUtility.SaveAsPrefabAsset(go, $"{dir}/Enemy.prefab");
Object.DestroyImmediate(go);                     // the scene copy is not wanted
```

`PrefabUtility.CreatePrefab` / `ReplacePrefab` / `ConnectPrefabInstance` were replaced in
2018.3 — `SaveAsPrefabAsset` and `SaveAsPrefabAssetAndConnect` are the current API.

## Materials

A `Material` created in a batch run is lost when the process exits unless it is saved:

```csharp
var mat = new Material(Shader.Find("Universal Render Pipeline/Lit"));
mat.SetColor("_BaseColor", Color.red);           // URP; Built-in uses "_Color"
AssetDatabase.CreateAsset(mat, "Assets/Materials/Generated.mat");
```

## Assets and import settings

```csharp
AssetDatabase.Refresh();                                        // after files appear on disk
AssetDatabase.SaveAssets();
AssetDatabase.CreateFolder("Assets", "Generated");              // returns the GUID
var paths = AssetDatabase.FindAssets("t:Texture2D", new[] { "Assets/Generated" });
foreach (var guid in paths)
{
    var path = AssetDatabase.GUIDToAssetPath(guid);
    if (AssetImporter.GetAtPath(path) is TextureImporter ti)
    {
        ti.textureType = TextureImporterType.Sprite;
        ti.spritePixelsPerUnit = 100f;
        ti.alphaIsTransparency = true;
        ti.SaveAndReimport();
    }
}
```

`AssetDatabase.Refresh()` is what the agent needs after writing a `.cs`/asset from outside
Unity while the editor is open — without it the editor does not see the new file.

## SerializedObject — editing assets you cannot touch directly

```csharp
var asset = AssetDatabase.LoadAllAssetsAtPath("ProjectSettings/TagManager.asset")[0];
var so = new SerializedObject(asset);
var tags = so.FindProperty("tags");
tags.InsertArrayElementAtIndex(tags.arraySize);
tags.GetArrayElementAtIndex(tags.arraySize - 1).stringValue = "Enemy";
so.ApplyModifiedProperties();
```

This is how `ProjectSettings/*.asset` is edited safely — never by writing the YAML.

## CustomEditor and EditorWindow

```csharp
[CustomEditor(typeof(Health))]
public class HealthEditor : Editor
{
    public override void OnInspectorGUI()
    {
        DrawDefaultInspector();
        var h = (Health)target;
        if (GUILayout.Button("Damage 10")) h.TakeDamage(10f);   // works in play mode
    }
}

public class LevelToolWindow : EditorWindow
{
    [MenuItem("MyGame/Level Tool")]
    private static void Open() => GetWindow<LevelToolWindow>("Level Tool");
}
```

Editor scripts are not hot-reloaded in play mode: after editing one, the domain reload happens
on the next focus/compile.

## Verification

- `unity_console()` after the editor recompiles.
- `unity_run_method(...)` returns the parsed batch log; `ok:false` with `error CS` means the
  builder itself failed to compile.
- A produced scene must be opened and looked at — a batch run cannot show you the hierarchy.
