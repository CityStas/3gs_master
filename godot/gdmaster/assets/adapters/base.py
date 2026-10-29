"""Общий интерфейс адаптера источника.

§9 спеки: модель не должна видеть семь разных инструментов скачивания.
Все различия источников спрятаны ЗДЕСЬ, за одним интерфейсом. Модель работает
с `asset_search`, а не с «itch_adapter» и «kenney_adapter» по отдельности.

Адаптер обязан уметь четыре вещи:

  search(query, type, limit)      -> список кандидатов
  inspect(asset_id)               -> подробности одного ассета
  license(asset_id)               -> строка лицензии из источника
  resolve_download(asset_id, fmt) -> прямой URL + имя файла

`resolve_download` не скачивает: он только возвращает URL, который дальше
обязательно пройдёт через `netguard.check_url`. Разделение важное — адаптер
не должен иметь возможности обойти сетевой барьер.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Candidate:
    """Один ассет-кандидат. Формат согласован с §10 спеки."""
    source: str
    asset_id: str
    name: str
    url: str                       # страница ассета
    license: str = ""
    author: str = ""
    formats: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    description: str = ""
    size_bytes: int | None = None
    polycount: int | None = None
    godot_compatible: bool = True

    def to_dict(self) -> dict:
        return {
            "source": self.source,
            "id": self.asset_id,
            "name": self.name,
            "url": self.url,
            "license": self.license,
            "author": self.author,
            "formats": self.formats,
            "tags": self.tags,
            "description": self.description[:400],
            "size_bytes": self.size_bytes,
            "polycount": self.polycount,
            "godot_compatible": self.godot_compatible,
        }


@dataclass
class DownloadTarget:
    """Где лежит файл. Путь проверяется netguard'ом перед скачиванием."""
    url: str
    filename: str
    format: str
    size_bytes: int | None = None

    def to_dict(self) -> dict:
        return {
            "url": self.url,
            "filename": self.filename,
            "format": self.format,
            "size_bytes": self.size_bytes,
            "mb": round(self.size_bytes / 1e6, 2) if self.size_bytes else None,
        }


@dataclass
class Bundle:
    """Набор файлов одного ассета.

    Нужен там, где один ассет — это не один файл. Пример, на котором это
    выяснилось: модель Poly Haven в формате gltf — это `.gltf` на 5 КБ,
    который ссылается на `.bin` с геометрией и на текстуры в соседних
    папках. Скачать только `.gltf` — получить в Godot битую модель.

    Поэтому адаптер возвращает комплект: главный файл первым, плюс всё,
    без чего он не откроется.
    """
    files: list[DownloadTarget]
    main: DownloadTarget
    note: str = ""

    @property
    def total_bytes(self) -> int | None:
        sizes = [f.size_bytes for f in self.files]
        if any(s is None for s in sizes):
            return None
        return sum(sizes)  # type: ignore[arg-type]

    def to_dict(self) -> dict:
        return {
            "main": self.main.to_dict(),
            "files": [f.to_dict() for f in self.files],
            "file_count": len(self.files),
            "total_bytes": self.total_bytes,
            "total_mb": round(self.total_bytes / 1e6, 2) if self.total_bytes else None,
            "note": self.note,
        }


class Adapter:
    """Базовый адаптер. Наследники переопределяют все четыре метода."""

    name: str = "base"
    display_name: str = "Base"
    #: Приоритет источника (§8 спеки). Меньше — раньше.
    priority: int = 99

    def available(self) -> tuple[bool, str]:
        """Готов ли адаптер работать. По умолчанию — да."""
        return True, ""

    def search(self, query: str, asset_type: str = "", limit: int = 10) -> list[Candidate]:
        raise NotImplementedError

    def inspect(self, asset_id: str) -> Candidate:
        raise NotImplementedError

    def license(self, asset_id: str) -> str:
        raise NotImplementedError

    def resolve_download(self, asset_id: str, fmt: str = "") -> DownloadTarget:
        raise NotImplementedError

    def resolve_bundle(self, asset_id: str, fmt: str = "", resolution: str = "") -> Bundle:
        """Комплект файлов ассета. По умолчанию — один файл через resolve_download.

        Адаптеры, где одного файла мало (Poly Haven), переопределяют этот метод.
        """
        t = self.resolve_download(asset_id, fmt)
        return Bundle(files=[t], main=t)
