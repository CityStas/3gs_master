# Unity RAG — полная карта ресурсов и архитектура базы знаний

Цель: собрать локальную базу знаний для AI-агента Unity-разработчика. Агент должен уметь находить документацию и примеры, писать и исправлять C#-код, создавать игровые механики, работать со сценами и ассетами, диагностировать ошибки и помогать со сборкой проекта.

## 1. Основные источники

### 1.1 Официальная документация Unity

- Unity Manual: https://docs.unity3d.com/Manual/index.html
  - Компоненты, сцены, GameObject, физика, освещение, UI, анимации, сборки и настройки проекта.
- Unity Scripting API: https://docs.unity3d.com/ScriptReference/
  - Классы, методы, свойства и события: `MonoBehaviour`, `Transform`, `Rigidbody`, `Collider`, `Animator`, `Camera`, `Physics`, `Input`.
- Unity Learn: https://learn.unity.com/
  - Пошаговые уроки, учебные проекты, игровые механики и примеры.
- Unity Packages: https://docs.unity3d.com/Manual/Packages.html
  - Пакеты и отдельные системы Unity.
- Unity Graphics: https://docs.unity3d.com/Manual/Graphics.html
  - Графика, освещение и рендеринг.
- Unity Input System: https://docs.unity3d.com/Packages/com.unity.inputsystem@latest
  - Современная система ввода.
- Unity Addressables: https://docs.unity3d.com/Packages/com.unity.addressables@latest
  - Управление и загрузка ресурсов.
- Unity AI Navigation: https://docs.unity3d.com/Packages/com.unity.ai.navigation@latest
  - NavMesh и навигация AI-персонажей.
- Offline Documentation: https://docs.unity.com/en-us/engine/7000.0/manual/offline-documentation
  - Официальная офлайн-документация. Проверь соответствие версии документации установленной версии Unity.

**Важно:** URL с `@latest` полезны для поиска актуальных материалов, но в индекс лучше помещать документацию конкретной версии Unity и пакетов, используемых проектом.

### 1.2 Исходный код и sample-проекты

- Unity Technologies на GitHub: https://github.com/Unity-Technologies
- Unity Graphics (SRP, URP/HDRP и графические технологии): https://github.com/Unity-Technologies/Graphics
- Unity ECS Samples: https://github.com/Unity-Technologies/EntityComponentSystemSamples
- Unity Netcode for GameObjects: https://github.com/Unity-Technologies/com.unity.netcode.gameobjects
- Unity Input System: https://github.com/Unity-Technologies/InputSystem
- UnityCsReference: https://github.com/Unity-Technologies/UnityCsReference
- Поиск Unity C# проектов: https://github.com/search?q=Unity+C%23+game+project&type=repositories

Используй реальные примеры для изучения структуры проекта, архитектуры скриптов, использования компонентов, паттернов проектирования и типовых реализаций игровых механик.

### 1.3 Обучение, вопросы и диагностика ошибок

- Unity Discussions: https://discussions.unity.com/
- Stack Overflow — Unity: https://stackoverflow.com/questions/tagged/unity3d
- Unity Issue Tracker: https://issuetracker.unity3d.com/
- Unity Editor releases и архив: https://unity.com/releases/editor/archive

Материалы сообщества полезны для troubleshooting, но проверяй дату ответа, версию Unity и актуальность API. Не считай ответ из форума гарантированно правильным без проверки.

---

## 2. Карта знаний для RAG

Рекомендуется разделить документы на тематические коллекции или хотя бы проставлять им метаданные `topic`, `source_type` и `unity_version`.

### 01 — C# и программирование

- Синтаксис C#, классы, структуры, интерфейсы, наследование.
- События, делегаты, generics, LINQ.
- `MonoBehaviour` и жизненный цикл: `Awake`, `OnEnable`, `Start`, `Update`, `FixedUpdate`, `LateUpdate`, `OnDisable`, `OnDestroy`.
- Coroutines, async/await и управление задачами.
- Управление памятью, GC и производительность.
- SOLID и паттерны проектирования.
- Архитектура игровых систем и разделение ответственности.
- Unity Test Framework, тестирование и debugging.

### 02 — Создание 2D- и 3D-игр

- GameObject, Component, Prefab, Scene, Transform.
- Rigidbody, Collider, триггеры и физические материалы.
- Character Controller и контроллеры персонажа.
- Управление от первого и третьего лица.
- Здоровье, урон, оружие, враги, NPC и диалоги.
- Инвентарь, квесты, сохранения и игровые состояния.
- UI и игровые меню.
- Процедурная генерация уровней и объектов.

### 03 — Графика и ассеты

- URP, HDRP, материалы и шейдеры.
- Shader Graph, свет, тени и постобработка.
- Particle System и VFX Graph.
- Blender → Unity, FBX, текстуры и нормали.
- Риггинг, Animator Controller, Blend Trees и Animation Rigging.
- Terrain, растительность и окружение.
- ProBuilder и процедурное моделирование.
- Оптимизация рендеринга и графических ресурсов.

### 04 — Инструменты редактора и автоматизация

- Editor Scripting и собственные окна Editor.
- `AssetDatabase`, `PrefabUtility`, `SerializedObject`.
- Автоматическое создание GameObject, компонентов, сцен и Prefab.
- Импорт, проверка и пакетная обработка ассетов.
- Генерация и изменение файлов проекта через скрипты.
- Проверка структуры проекта и настроек.
- Editor tools для автоматизации повторяющихся задач.

### 05 — Платформы, сборка и публикация

- Windows, Android, WebGL, iOS и другие целевые платформы.
- Build Profiles, Player Settings, IL2CPP и Mono.
- Addressables и Asset Bundles.
- CPU/GPU profiling, batching, LOD и Occlusion Culling.
- Git и Unity Version Control.
- CI/CD, автоматические сборки и тестирование.
- Платформенные ограничения и диагностика ошибок сборки.

### 06 — Продвинутые системы

- Input System, Cinemachine и Timeline.
- AI Navigation, NavMesh и поведение врагов.
- Netcode for GameObjects, multiplayer и синхронизация.
- ECS, Entity Component System, DOTS, Jobs и Burst.
- UI Toolkit и uGUI.
- Localization и Audio.
- XR, VR и AR — если нужны соответствующие проекты.

---

## 3. Что скачать для локальной базы

### Минимальный первый набор

1. Unity Manual.
2. Unity Scripting API.
3. Документацию пакетов, используемых в выбранной версии Unity.
4. Unity Learn: подходящие учебные проекты и уроки.
5. Несколько официальных sample-проектов на GitHub.
6. Отдельную коллекцию решений ошибок и типовых игровых рецептов.

Официальная страница офлайн-документации:
https://docs.unity.com/en-us/engine/7000.0/manual/offline-documentation

В описаниях Unity встречается архив документации порядка 300 МБ, но фактический размер зависит от версии и формата, а распакованные файлы занимают больше места. Проверяй размер и состав на странице загрузки.

### Что не следует без разбора индексировать

- Текстуры, аудио, видео, модели и прочие бинарные ресурсы.
- `Library/`, временные файлы и кэши Unity.
- Дубликаты одной документации для нескольких версий без метаданных версии.
- Сгенерированные файлы, не содержащие полезных знаний.
- Устаревшие примеры, если их несовместимость не обозначена.

Публичный репозиторий не обязательно разрешает любое переиспользование или распространение его содержимого. Проверяй лицензии исходников, документации и ассетов.

---

## 4. Дополнительные коллекции для AI-агента

### Unity Project Knowledge

Материалы о реальной структуре проектов:

- `Assets/`
- `Packages/manifest.json`
- `Packages/packages-lock.json`
- `ProjectSettings/`
- `.asmdef`
- Scenes, Prefabs и ScriptableObjects.
- Ссылки между объектами, сериализация и организация ресурсов.
- Примеры корректной структуры небольшого и среднего проекта.

### Unity Error Knowledge

Отдельная база troubleshooting:

- Ошибки компиляции C#.
- Missing references и потерянные ссылки на объекты.
- Ошибки импорта ассетов.
- Ошибки пакетов и несовместимости версий.
- Исключения в Play Mode.
- Проблемы с физикой, коллизиями и слоями.
- Ошибки Android/Windows/WebGL build.
- Проблемы производительности и утечки ресурсов.
- Пошаговая диагностика, проверка причины и подтверждение исправления.

Для каждого случая желательно хранить:

- Симптом и полный текст ошибки.
- Версию Unity и связанные версии пакетов.
- Минимальные условия воспроизведения.
- Причину, если она подтверждена.
- Способ исправления.
- Проверку того, что проблема устранена.
- Источник и дату материала.

### Unity Agent Recipes

Практические инструкции, которые описывают целую задачу от начала до проверки:

- Создать персонажа и настроить управление.
- Подключить камеру от третьего лица.
- Реализовать стрельбу, урон и перезарядку.
- Создать врага с NavMesh и простым AI.
- Сделать здоровье, инвентарь и UI.
- Настроить анимации персонажа.
- Создать интерактивные объекты.
- Организовать сохранение игры.
- Настроить импорт модели из Blender.
- Создать сцену и Prefab через Editor scripting.
- Собрать проект под нужную платформу.
- Проверить Console и исправить ошибки после генерации кода.

Каждый рецепт должен содержать предпосылки, шаги, код или настройки, ожидаемый результат и способы проверки.

---

## 5. Архитектура RAG-пайплайна

```text
Источники
  ├── Unity Manual и Scripting API
  ├── Документация пакетов
  ├── Unity Learn
  ├── GitHub sample-проекты
  ├── Ошибки и решения
  └── Unity Agent Recipes
          |
          v
Сбор и обновление материалов
          |
          v
Парсинг и очистка
  ├── HTML -> Markdown / текст
  ├── C# -> структурные блоки
  ├── README и руководства
  └── JSON / manifest / метаданные
          |
          v
Chunking + метаданные
          |
          v
Embeddings + индекс BM25
          |
          v
Гибридный поиск
          |
          v
Reranker (по необходимости)
          |
          v
Контекст для локальной LLM
          |
          v
Unity CLI / MCP / Editor tools
          |
          v
Изменения проекта -> запуск проверок -> Console -> исправление
```

### Метаданные для каждого документа или чанка

Рекомендуемые поля:

- `source`: исходный URL или путь в репозитории.
- `source_type`: `manual`, `api`, `tutorial`, `sample_code`, `issue`, `recipe`.
- `unity_version`: версия Unity, к которой относится материал.
- `package_name`: название пакета, если применимо.
- `package_version`: версия пакета, если известна.
- `topic`: например, `physics`, `animation`, `rendering`, `editor`, `build`.
- `language`: `en`, `ru`, `csharp` или другой подходящий код.
- `symbol`: имя класса, метода или API-элемента.
- `license`: лицензия, если доступна.
- `last_updated`: дата обновления, если известна.

Не выдумывай метаданные, которых нет в источнике. Неизвестные значения оставляй пустыми или помечай как неизвестные.

---

## 6. Начальные параметры индексации

Это отправная точка для тестов, а не универсальные оптимальные значения.

| Тип материала | Начальная стратегия |
|---|---|
| Руководства | Чанки около 400–800 токенов |
| Перекрытие | Около 60–100 токенов |
| API Reference | Один класс или логически связанный раздел |
| C# | Разделение по классам и методам, сохранение сигнатур |
| Tutorials | Разделять по шагам и смысловым заголовкам |
| Ошибки | Один случай ошибки или один сценарий решения на чанк |
| Recipes | Один законченный рабочий процесс на документ |
| Sample-проекты | Индексировать код вместе с README и путём файла |

Для C# не разрезай метод посередине без необходимости. Для больших классов используй отдельные чанки по методам, сохраняя название класса, namespace и нужный контекст.

### Поиск

Для начала сравни:

1. Векторный поиск по embeddings.
2. BM25 или другой лексический поиск.
3. Гибридный поиск, объединяющий оба подхода.
4. Гибридный поиск с reranker.

Лексический поиск особенно полезен для точных названий API, сообщений ошибок и имён методов. Векторный поиск помогает находить материалы по смыслу, даже если запрос сформулирован иначе.

### Проверка качества

Создай тестовый набор запросов, например:

- «Почему персонаж проваливается сквозь пол?»
- «Как реализовать управление персонажем от третьего лица?»
- «Какой API нужен для создания Prefab через Editor script?»
- «Как исправить MissingReferenceException?»
- «Какой способ ввода используется в этом проекте?»
- «Как собрать проект под Android?»

Для каждого вопроса сохраняй ожидаемые источники и критерии корректного ответа. Измеряй качество retrieval отдельно от качества самой модели.

---

## 7. Как подключить RAG к агенту

RAG сам по себе не управляет Unity. Он предоставляет модели релевантные знания. Для работы с проектом агенту дополнительно нужны инструменты.

Рекомендуемые возможности инструментального слоя:

- Читать дерево проекта и файлы C#.
- Искать определения классов и ссылки на символы.
- Читать Unity Console и логи Editor.
- Создавать и редактировать скрипты.
- Выполнять разрешённые команды сборки и тестирования.
- Создавать или изменять сцены и Prefab через Unity Editor API, CLI или специальный MCP-инструмент.
- Проверять результат после внесённых изменений.
- Показывать diff перед рискованными изменениями.

Не позволяй модели считать код правильным только потому, что он сгенерирован. После изменений проверяй компиляцию, Console, тесты и поведение в сцене. Для разрушающих операций и команд с побочными эффектами добавь подтверждение пользователя.

---

## 8. План внедрения по этапам

### Этап 1 — базовый RAG

- [ ] Unity Manual.
- [ ] Unity Scripting API.
- [ ] Документация ключевых пакетов используемой версии.
- [ ] Парсер HTML и Markdown.
- [ ] Метаданные версии.
- [ ] Embeddings и BM25.
- [ ] Набор тестовых запросов.

### Этап 2 — помощь в разработке игр

- [ ] Unity Learn и учебные проекты.
- [ ] Официальные sample-проекты.
- [ ] C#-код, структурно разбитый по классам и методам.
- [ ] Unity Agent Recipes для распространённых механик.
- [ ] Поиск по точным API-символам и сообщениям ошибок.

### Этап 3 — автономный агент

- [ ] Интеграция с Unity Editor/CLI/MCP.
- [ ] Доступ к проектным файлам.
- [ ] Сбор логов и ошибок.
- [ ] Автоматические проверки после изменений.
- [ ] Цикл «изменение → проверка → диагностика → исправление».
- [ ] Логирование действий и возможность отката.

### Этап 4 — расширенные темы

Добавляй по потребности проекта:

- [ ] URP/HDRP и Shader Graph.
- [ ] DOTS/ECS, Jobs и Burst.
- [ ] Multiplayer и Netcode.
- [ ] XR/VR/AR.
- [ ] Оптимизация под конкретные платформы.
- [ ] CI/CD и автоматизированные сборки.

---

## 9. Приоритетный список ссылок

| Ресурс | Назначение | Ссылка |
|---|---|---|
| Unity Manual | Основная документация | https://docs.unity3d.com/Manual/index.html |
| Scripting API | Справочник C# API | https://docs.unity3d.com/ScriptReference/ |
| Unity Learn | Курсы и проекты | https://learn.unity.com/ |
| Unity Packages | Пакеты | https://docs.unity3d.com/Manual/Packages.html |
| Unity Graphics | Рендеринг | https://docs.unity3d.com/Manual/Graphics.html |
| Input System | Ввод | https://docs.unity3d.com/Packages/com.unity.inputsystem@latest |
| Addressables | Управление ресурсами | https://docs.unity3d.com/Packages/com.unity.addressables@latest |
| AI Navigation | NavMesh и навигация | https://docs.unity3d.com/Packages/com.unity.ai.navigation@latest |
| Unity GitHub | Репозитории и примеры | https://github.com/Unity-Technologies |
| Graphics repo | SRP, URP/HDRP | https://github.com/Unity-Technologies/Graphics |
| ECS Samples | DOTS/ECS | https://github.com/Unity-Technologies/EntityComponentSystemSamples |
| Netcode | Сетевая игра | https://github.com/Unity-Technologies/com.unity.netcode.gameobjects |
| Input System repo | Примеры и исходники ввода | https://github.com/Unity-Technologies/InputSystem |
| UnityCsReference | Доступная часть C#-исходников | https://github.com/Unity-Technologies/UnityCsReference |
| Discussions | Форум Unity | https://discussions.unity.com/ |
| Stack Overflow | Ответы и диагностика | https://stackoverflow.com/questions/tagged/unity3d |
| Issue Tracker | Известные ошибки | https://issuetracker.unity3d.com/ |
| Release Archive | Версии Unity | https://unity.com/releases/editor/archive |
| Offline Docs | Офлайн-документация | https://docs.unity.com/en-us/engine/7000.0/manual/offline-documentation |

---

## 10. Итоговая рекомендация

Для первой рабочей версии Unity RAG приоритет такой:

1. **Официальный Manual и Scripting API** — основа знаний.
2. **Документация пакетов конкретной версии Unity** — чтобы не смешивать несовместимые API.
3. **Официальные sample-проекты и Unity Learn** — реальные примеры реализации.
4. **Unity Error Knowledge** — диагностика ошибок.
5. **Unity Agent Recipes** — последовательное выполнение задач.
6. **Unity Editor/CLI/MCP-инструменты** — возможность применять знания в проекте и проверять результат.

Начни с компактного, проверяемого индекса, а затем расширяй его по реальным задачам агента. Качество источников, метаданные версий, гибридный поиск и автоматическая проверка результатов важнее, чем максимальное количество документов.

Перед публикацией или распространением собранной базы проверь лицензии и условия использования каждого источника.
