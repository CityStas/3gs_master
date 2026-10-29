"""Реестр адаптеров: одно место, где перечислены источники.

Правило восьми инструментов (§9 спеки) держится на этой таблице: модель видит
один `asset_search`, а внутри — N адаптеров. Добавление источника в v2/v3
сводится к регистрации класса здесь и домена в `netguard.ALLOWED_HOSTS`;
инструменты, схемы и текст ошибок при этом не меняются.

Реестр НЕ проверяет сеть. Проверка доступности — отдельно (`available_adapters`),
потому что `search` не должен падать из-за одного недоступного источника:
пользователю нужны результаты из тех, что живы, а не отказ целиком.
"""
from __future__ import annotations

from .adapters.base import Adapter

#: Классы источников. Ленивый импорт: адаптер v2 можно оставить в файле,
#: не подключая его к v1 — тогда он не грузится и не проверяется.
_SOURCES: dict[str, tuple[str, str]] = {
    # имя -> (модуль, класс), импорт выполняется в get_adapters()
    "godot_store": (".adapters.godot_store", "GodotStoreAdapter"),
    "polyhaven": (".adapters.polyhaven", "PolyHavenAdapter"),
    "kenney": (".adapters.kenney", "KenneyAdapter"),
}

#: Порядок v1 (07_gdmaster_integration.md): аддоны -> 3D-окружение -> 2D.
V1_SOURCES: tuple[str, ...] = ("godot_store", "polyhaven", "kenney")


def get_adapters(names: list[str] | tuple[str, ...] | None = None) -> list[Adapter]:
    """Собрать адаптеры. По умолчанию — все зарегистрированные.

    Порядок — по приоритету источника (§8 спеки), а не по алфавиту: модель
    должна видеть аддоны от Godot Store раньше, чем текстуры Poly Haven.
    """
    import importlib

    wanted = list(names) if names else list(_SOURCES)
    out: list[Adapter] = []
    for key in wanted:
        spec = _SOURCES.get(key)
        if spec is None:
            continue
        module_name, class_name = spec
        module = importlib.import_module(module_name, __package__)
        out.append(getattr(module, class_name)())
    out.sort(key=lambda a: a.priority)
    return out


def adapter_for(source: str) -> Adapter | None:
    """Адаптер по имени источника — для `asset_inspect`/`asset_download`.

    `source` приходит от модели, поэтому это не «поиск по ключу», а поиск
    среди уже собранных адаптеров: неизвестное имя даёт None, а не падение
    и не создание адаптера по строке.
    """
    key = (source or "").strip().lower()
    for a in get_adapters():
        if a.name == key:
            return a
    return None


def available_adapters() -> tuple[list[Adapter], list[str]]:
    """(живые адаптеры, причины отказа остальных).

    Причина отказа попадает в ответ поиска: молча пустой результат хуже,
    чем «Poly Haven недоступен: таймаут», потому что второе модель может
    сообщить пользователю, а первое — нет.
    """
    alive: list[Adapter] = []
    dead: list[str] = []
    for a in get_adapters():
        ok, why = a.available()
        (alive.append(a) if ok else dead.append(why or f"{a.name}: недоступен"))
    return alive, dead
