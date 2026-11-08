# Studio MCP — рантайм-грабли (проверено на практике)

Здесь только то, что **проверено руками** в живой сессии Studio
(`version-7062aec9dbe74b14`). Официальная документация Roblox этого не описывает:
это поведение самого MCP-сервера и песочницы, в которой исполняется `execute_luau`.

Настройка подключения — `10_MCP_SETUP_WINDOWS.md`. Здесь — про то, что ломается
после подключения.

## 1. Генеративные инструменты и play-клиент

`generate_avatar` **требует запущенного play-клиента**. В Edit-режиме вызов падает:

```
Target is closed (INVOKE_AvatarGenTool.generateAvatar_ToRequester, DMN_ID_PLAYCLIENT)
```

Пайплайн Roblox валидирует аватар в живом клиенте и вставляет результат «перед
камерой», поэтому без `DMN_ID_PLAYCLIENT` работать нечему. Пайплайн сам поднимает
playtest, если его нет.

Второй нюанс: **вызов отваливается по `Request timeout` (~2 минуты), но задача в
Studio продолжается**. Таймаут означает обрыв MCP-связи, а не провал генерации.
Правильная реакция — не повторять вызов, а подождать и проверить Workspace:

```lua
for _, c in ipairs(game:GetService("Workspace"):GetChildren()) do
    if c:IsA("Model") and c:FindFirstChildOfClass("Humanoid") then print(c.Name) end
end
```

`auto_setup_avatar` ведёт себя так же: `Request timeout`, результат появляется
(или не появляется) без ответа.

## 2. Песочница `execute_luau`: что нельзя писать

`MeshPart.MeshId` — свойство `ReadOnly` с `write: NotAccessibleSecurity`. Запись из
песочницы падает:

```
The current thread cannot write 'MeshId' (lacking capability NotAccessible)
```

Это не ограничение MCP, а движка: коллизионная геометрия меша не пересчитывается в
рантайме. Правильные способы скопировать меш с одной части на другую:

- `MeshPart:ApplyMesh(sourceMeshPart)` — копирует `MeshContent` (и `MeshId`),
  `TextureContent` (и `TextureID`), `RenderFidelity`, `CollisionFidelity`,
  `FluidFidelity`, `MeshSize` с другой `MeshPart`. Аргумент обязан быть `MeshPart`,
  иначе ошибка.
- `AssetService:CreateMeshPartAsync(content, collisionFidelity)` — создать новую
  часть из контента.

`MeshPart.TextureID` / `TextureContent` при этом **писать можно** — текстура меняется
без перезагрузки меша.

Что писать **можно**: `Script.Source`, обычные свойства частей, атрибуты.

## 3. Геометрия модели: два классических промаха

```lua
local bb = model:GetBoundingBox()
bb.Size  -- ОШИБКА: Size is not a valid member of CFrame
```

`GetBoundingBox()` возвращает **два значения**, а не структуру:

```lua
local cf, size = model:GetBoundingBox()
```

`Model:PivotTo()` двигает **пивот**, а не центр bounding box. Если выставить по
центру bbox, модель уедет по вертикали на разницу между пивотом и центром.
Правильно — считать сдвиг от текущего пивота:

```lua
local cf, size = model:GetBoundingBox()
local shift = Vector3.new(tx - cf.Position.X, ground - (cf.Position.Y - size.Y * 0.5), tz - cf.Position.Z)
local p = model:GetPivot()
model:PivotTo(CFrame.new(p.Position + shift) * (p - p.Position))
```

## 4. Клонирование части из R15-рига

`somePart:Clone()` тащит внутри `Weld`/`WeldConstraint`, у которых `Part0`/`Part1`
ссылаются на **оригинал**. Клон мгновенно притягивается обратно к исходной части —
выглядит как «CFrame не применяется».

Перед парентингом вычистить суставы:

```lua
for _, d in ipairs(clone:GetDescendants()) do
    if d:IsA("JointInstance") or d:IsA("WeldConstraint") or d:IsA("Constraint") then
        d:Destroy()
    end
end
```

И помнить: **зеркалить `MeshPart` нельзя** — отрицательный масштаб в `CFrame`
недопустим. Клон правой ступени на левой ноге выглядит как вывернутая обувь. Если
нужна парная деталь — только `ApplyMesh` из корректного источника либо
перегенерация ассета.

## 5. Современный R15-риг: `Motor6D = 0` — это норма

Аватары, сгенерированные пайплайном Roblox, собраны на `AnimationConstraint` +
`BallSocketConstraint`. `Motor6D` в них нет вообще. Не считать это поломкой рига и
не пытаться «починить» руками.

## 6. Один `StarterCharacter` на место

В `StarterPlayer` может быть только **один** `Model` с именем `StarterCharacter`.
Второго персонажа держат в `Workspace` (или `ServerStorage`) и активируют
переименованием. Роблокс сам подмешивает к нему `Animate` при спавне — idle, ходьба,
прыжок работают без скриптов.

## 7. Idle для модели в Workspace (не персонаж игрока)

Персонаж игрока анимируется автоматически. Модель в Workspace — нет, ей нужен
`Animator` и скрипт:

```lua
local humanoid = script.Parent:FindFirstChildOfClass("Humanoid")
local animator = humanoid:FindFirstChildOfClass("Animator")
if not animator then animator = Instance.new("Animator"); animator.Parent = humanoid end
local a = Instance.new("Animation")
a.AnimationId = "rbxassetid://507766388"  -- R15 idle
local track = animator:LoadAnimation(a)
track.Looped = true
track.Priority = Enum.AnimationPriority.Idle
track:Play(0.3)
```

Три условия, без которых не работает:

1. Скрипт — `Script` с **`RunContext = Server`**. Legacy-скрипт может не подхватиться.
2. Заякоренный `HumanoidRootPart` **не мешает** анимации: суставы двигаются, модель
   стоит на месте. Это удобно для витрины.
3. Проверять надо не «трек числится играющим», а реальное смещение сустава:

```lua
local arm = model:FindFirstChild("LeftUpperArm")
local c1 = arm.CFrame
task.wait(0.8)
print((c1.Position - arm.CFrame.Position).Magnitude)  -- > 0 значит двигается
```

## 8. Моргание требует динамической головы

Моргание — не анимация, а лицевой риг. У головы должны быть `FaceControls` и
лицевые кости (`RootFaceJoint` + суставы век), которые крутит
`FaceAnimatorService`. Обычный `MeshPart`-голова со «нарисованными» глазами моргать
не может — двигать нечего.

Добавить `FaceControls` в существующую статичную голову нельзя. Варианты:

- сгенерировать аватар с `dynamicHead = true`;
- собрать динамическую голову в Blender (см. `art/characters/facial-animation/create-basic-heads`).

## 9. Undo сносит пачку правок

Изменения, сделанные через `execute_luau`, попадают в историю отката Studio. Один
Ctrl+Z может снять сразу несколько шагов, включая созданные части и скрипты — модель
«сама» откатывается к прежнему виду.

Обёртка, чтобы правка была одним шагом:

```lua
local CHS = game:GetService("ChangeHistoryService")
CHS:TryBeginRecording("my change")
-- ... правки ...
CHS:FinishRecording("my change", Enum.FinishRecordingOperation.Commit)
```

## 10. Что даёт `generate_procedural_model`, а что нет

Даёт: модель из примитивов с редактируемыми атрибутами (`ShellRadius`, цвета и т.п.),
работает в Edit-режиме, вставляется сразу.

Не даёт: текстур (`SurfaceAppearance` нет, только `Color`), рига (`Humanoid`,
суставов нет), анимации. Для «персонажа» не годится — это декоративный проп.

Для персонажа: `generate_avatar` (R15 + текстуры, нужен play-клиент) либо
`auto_setup_avatar` поверх готовой модели.
