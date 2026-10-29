"""Адаптер Kenney — приоритет 3, всё CC0, для 2D и прототипов.

API у Kenney нет, поэтому адаптер разбирает HTML. Проверенная живым запросом
структура (страница `https://kenney.nl/assets/prototype-kit`):

  * ссылка на скачивание:
      https://kenney.nl/media/pages/assets/<slug>/<hash>-<timestamp>/kenney_<slug>.zip
    `<hash>-<timestamp>` УНИКАЛЕН для каждого ассета, поэтому URL нельзя
    сконструировать — его надо извлечь со страницы. Это ровно та причина,
    по которой адаптер нужен, а не «шаблонная ссылка».
  * лицензия подтверждается ссылкой:
      https://creativecommons.org/publicdomain/zero/1.0/   -> CC0
    Если такой ссылки нет, адаптер честно вернёт UNKNOWN, и ассет не поставится.

Разбор HTML — сознательный компромисс: без API другого пути нет. Поэтому
разбор узкий (ищем конкретные шаблоны ссылок) и не «угадывает» лицензию.
"""
from __future__ import annotations

import re
from urllib.parse import urljoin

import httpx

from .. import netguard
from .base import Adapter, Bundle, Candidate, DownloadTarget

BASE = "https://kenney.nl"
UA = "gdmaster-asset-manager/1.0"

#: Ссылка CC0, которой Kenney помечает свои ассеты.
_CC0_LINK = re.compile(r"creativecommons\.org/publicdomain/zero/1\.0", re.I)

#: Ссылка на архив ассета:
#:   https://kenney.nl/media/pages/assets/<slug>/<hash>-<ts>/kenney_<slug>[-<ver>].zip
#: Имя может содержать версию (`kenney_new-platformer-pack-1.1.zip`), поэтому
#: суффикс не фиксирован. `<hash>-<ts>` уникален — URL извлекается со страницы.
_ZIP_RE = re.compile(
    r"https://kenney\.nl/media/pages/assets/([a-z0-9\-]+)/[0-9a-f]+-\d+/(kenney_[a-z0-9\-_.]+\.zip)",
    re.I,
)

#: Карточка ассета. Ссылки абсолютные: https://kenney.nl/assets/<slug>
#: ВАЖНО: Kenney отдаёт атрибуты в ОДИНАРНЫХ кавычках
#: (`href='https://kenney.nl/assets/...'`), поэтому закрывающая кавычка
#: в lookahead обязана включать `'`. Служебные пути page:/category:/tag:/series:
#: отсеиваются отдельно.
_CARD_RE = re.compile(r"""https://kenney\.nl/assets/([a-z0-9][a-z0-9\-]*)(?=["'\s?>]|$)""", re.I)

#: Номер последней страницы пагинации: /assets/page:N?category=...
_PAGE_RE = re.compile(r"/assets/page:(\d+)", re.I)

#: Сколько страниц максимум обходить на категорию — защита от бесконечного цикла.
MAX_PAGES = 40

#: Человекочитаемое название со страницы.
_TITLE_RE = re.compile(r"<title>([^<]+?)\s*(?:&middot;|·|</title>)", re.I)

#: Превью — годится как описание «что это».
_PREVIEW_RE = re.compile(
    r"https://kenney\.nl/media/pages/assets/[a-z0-9\-]+/[0-9a-f]+-\d+/(preview\.(?:png|jpg))",
    re.I,
)


class KenneyAdapter(Adapter):
    name = "kenney"
    display_name = "Kenney"
    priority = 3

    #: Кэш списка slug'ов за время жизни процесса: главная страница
    #: отдаёт только категории, а полный каталог собирается из ?category=
    _slugs: list[str] | None = None

    def _get(self, url: str, timeout: float = 30.0) -> str:
        url = netguard.check_url(url)
        with httpx.Client(timeout=timeout, trust_env=True,
                          headers={"User-Agent": UA}) as c:
            r = c.get(url)
            r.raise_for_status()
            return r.text

    def available(self) -> tuple[bool, str]:
        try:
            self._get(BASE + "/assets", timeout=15.0)
            return True, ""
        except Exception as e:  # noqa: BLE001
            return False, f"kenney.nl недоступен: {e}"

    # ------------------------------------------------------------------
    def _catalog(self) -> list[str]:
        """Список slug'ов ассетов по всем категориям с учётом пагинации.

        Каталог разбит на страницы (`/assets/page:N?category=...`), поэтому
        обход одной первой страницы давал лишь ~10 ассетов из ~350.
        Число страниц берётся из ссылок пагинации самой страницы.
        """
        if self._slugs is not None:
            return self._slugs

        slugs: set[str] = set()
        for cat in ("2D", "3D", "Audio", "Textures"):
            try:
                first = self._get(f"{BASE}/assets?category={cat}")
            except Exception:  # noqa: BLE001
                continue

            pages = {int(m) for m in _PAGE_RE.findall(first)}
            last = max(pages) if pages else 1
            htmls = [first]
            for p in range(2, min(last, MAX_PAGES) + 1):
                try:
                    htmls.append(self._get(f"{BASE}/assets/page:{p}?category={cat}"))
                except Exception:  # noqa: BLE001
                    continue

            for html in htmls:
                for m in _CARD_RE.finditer(html):
                    slug = m.group(1).lower()
                    if slug.startswith(("category", "tag", "series", "page")):
                        continue
                    slugs.add(slug)

        self._slugs = sorted(slugs)
        return self._slugs

    @staticmethod
    def _title(html: str, fallback: str) -> str:
        m = _TITLE_RE.search(html)
        if not m:
            return fallback
        title = m.group(1).strip()
        return title or fallback

    def _page(self, slug: str) -> tuple[str, str, str]:
        """(html, title, license). Одна загрузка вместо трёх."""
        html = self._get(f"{BASE}/assets/{slug}")
        title = self._title(html, slug.replace("-", " ").title())
        lic = "CC0" if _CC0_LINK.search(html) else "UNKNOWN"
        return html, title, lic

    def _candidate(self, slug: str, html: str) -> Candidate:
        title = self._title(html, slug.replace("-", " ").title())
        lic = "CC0" if _CC0_LINK.search(html) else "UNKNOWN"
        fmts: list[str] = []
        if _ZIP_RE.search(html):
            fmts = ["zip"]
        return Candidate(
            source=self.name,
            asset_id=slug,
            name=title,
            url=f"{BASE}/assets/{slug}",
            license=lic,
            author="Kenney",
            formats=fmts,
            tags=[t for t in slug.split("-")],
            description=f"Kenney: {title}",
            godot_compatible=True,
        )

    # ------------------------------------------------------------------
    def search(self, query: str, asset_type: str = "", limit: int = 10) -> list[Candidate]:
        """Поиск по slug'ам каталога.

        Отдельные страницы НЕ грузятся: каталог большой, и проверять лицензию
        каждого кандидата при поиске — лишние десятки запросов. Лицензия
        уточняется на шаге inspect, когда кандидат уже выбран.
        """
        terms = [w for w in query.lower().replace(",", " ").split() if len(w) > 2]
        scored: list[tuple[int, str]] = []
        for slug in self._catalog():
            words = slug.replace("-", " ").lower()
            hits = sum(1 for t in terms if t in words)
            if terms and hits == 0:
                continue
            score = hits * 10
            if any(t == w for t in terms for w in slug.split("-")):
                score += 5
            scored.append((score, slug))
        scored.sort(key=lambda kv: -kv[0])

        out: list[Candidate] = []
        for _s, slug in scored[:limit]:
            out.append(Candidate(
                source=self.name, asset_id=slug,
                name=slug.replace("-", " ").title(),
                url=f"{BASE}/assets/{slug}",
                license="CC0",           # Kenney: весь сайт CC0; уточняется в inspect
                author="Kenney",
                tags=slug.split("-"),
                description=f"Kenney asset pack: {slug.replace('-', ' ')}",
            ))
        return out

    def inspect(self, asset_id: str) -> Candidate:
        html, _title_, _lic = self._page(asset_id)
        return self._candidate(asset_id, html)

    def license(self, asset_id: str) -> str:
        _html, _title_, lic = self._page(asset_id)
        return lic

    def resolve_download(self, asset_id: str, fmt: str = "") -> DownloadTarget:
        return self.resolve_bundle(asset_id, fmt).main

    def resolve_bundle(self, asset_id: str, fmt: str = "", resolution: str = "") -> Bundle:
        html, title, lic = self._page(asset_id)
        m = _ZIP_RE.search(html)
        if not m:
            raise ValueError(
                f"Kenney: не найдена ссылка на архив для '{asset_id}'. "
                f"Возможно, ассет переехал или скачивание идёт через форму."
            )
        url, filename = m.group(0), m.group(2)
        size = None
        try:
            from ..downloader import head_size
            size = head_size(url)
        except Exception:  # noqa: BLE001
            size = None

        t = DownloadTarget(url=url, filename=filename, format="zip", size_bytes=size)
        return Bundle(
            files=[t], main=t,
            note=(f"архив Kenney «{title}», лицензия {lic}. "
                  f"Внутри — файлы в нескольких форматах (png/gltf/svg и др.); "
                  f"лишние форматы отсеиваются при установке."),
        )
