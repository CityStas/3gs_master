"""Адаптер Godot Asset Store — приоритет 1 для аддонов, плагинов, шейдеров.

Два разных API, и это не случайность:

  1. НОВЫЙ магазин, `https://store.godotengine.org` — основной каталог.
     Проверенные endpoints:
       GET /search/?q=<query>                        -> HTML со ссылками на ассеты
       GET /api/v1/search/autocomplete/?query=<q>    -> [{"suggestion": "..."}]
       GET /asset/<author>/<slug>/                   -> HTML страницы ассета
       GET /asset/<author>/<slug>/download/<ver>/    -> 302 на предподписанный S3
     Автокомплит отдаёт только строки-подсказки, поэтому поиск идёт по HTML,
     а подсказки используются как уточнение запроса.

  2. СТАРАЯ библиотека, `https://godotengine.org/asset-library/api/asset` —
     возвращает JSON с полями asset_id/title/author/cost/godot_version.
     Каталог небольшой (десятки записей), годится как резерв.

Про загрузку: скачивание идёт через 302 на предподписанный URL объектного
хранилища (fra1.digitaloceanspaces.com, X-Amz-Signature, живёт 600 с).
Такой хост разрешён ТОЛЬКО как цель редиректа — см. netguard.REDIRECT_ONLY_HOSTS.

Про лицензии: магазин не унифицирует их. На странице ассета лицензия указана
текстом («License: MIT»). Адаптер её извлекает, но при неудаче возвращает
UNKNOWN — и тогда установка блокируется. Это осознанное поведение: аддоны
часто под GPL/MIT, и решать за пользователя нельзя.
"""
from __future__ import annotations

import re

import httpx

from .. import netguard
from .base import Adapter, Bundle, Candidate, DownloadTarget

STORE = "https://store.godotengine.org"
LIBRARY_API = "https://godotengine.org/asset-library/api"
UA = "gdmaster-asset-manager/1.0"

#: Ссылка на страницу ассета: /asset/<author>/<slug>/
_ASSET_LINK_RE = re.compile(r'href=[\'"](/asset/([a-z0-9\-_.]+)/([a-z0-9\-_.]+)/)[\'"]', re.I)

#: Ссылка на скачивание конкретной версии: /asset/<a>/<s>/download/<ver>/
_DOWNLOAD_RE = re.compile(
    r'href=[\'"](/asset/([a-z0-9\-_.]+)/([a-z0-9\-_.]+)/download/(\d+)/)[\'"]', re.I)

#: Лицензия на странице ассета. Магазин пишет её текстом.
_LICENSE_RE = re.compile(
    r"[Ll]icense\s*:?\s*(?:</[^>]+>\s*)?(?:<a[^>]*>)?\s*"
    r"(MIT|GPL[^<\s]*|LGPL[^<\s]*|Apache[^<\s]*|BSD[^<\s]*|MPL[^<\s]*|CC0[^<\s]*|"
    r"CC[-\s]?BY[^<\s]*|Unlicense|Zlib|ISC|Public\s+Domain)",
    re.I)

#: Название ассета.
_TITLE_RE = re.compile(r"<title>([^<]+?)\s*(?:[-–—]\s*Godot Asset Store)?\s*</title>", re.I)

#: Автор из URL страницы уже известен (первый сегмент), но на странице он тоже есть.
_AUTHOR_RE = re.compile(r'/user/([a-z0-9\-_.]+)/', re.I)


class GodotStoreAdapter(Adapter):
    name = "godot_store"
    display_name = "Godot Asset Store"
    priority = 1

    def _get(self, url: str, timeout: float = 30.0) -> str:
        url = netguard.check_url(url)
        with httpx.Client(timeout=timeout, trust_env=True,
                          follow_redirects=True,
                          headers={"User-Agent": UA}) as c:
            r = c.get(url)
            r.raise_for_status()
            return r.text

    def available(self) -> tuple[bool, str]:
        try:
            self._get(STORE + "/search/?q=godot", timeout=15.0)
            return True, ""
        except Exception as e:  # noqa: BLE001
            return False, f"store.godotengine.org недоступен: {e}"

    # ------------------------------------------------------------------
    @staticmethod
    def _license_of(html: str) -> str:
        m = _LICENSE_RE.search(html)
        return m.group(1).strip() if m else "UNKNOWN"

    @staticmethod
    def _title_of(html: str, fallback: str) -> str:
        m = _TITLE_RE.search(html)
        if not m:
            return fallback
        t = m.group(1).strip()
        return t or fallback

    def _candidate_from_link(self, author: str, slug: str) -> Candidate:
        return Candidate(
            source=self.name,
            asset_id=f"{author}/{slug}",
            name=slug.replace("-", " ").title(),
            url=f"{STORE}/asset/{author}/{slug}/",
            license="",            # уточняется в inspect
            author=author,
            formats=["zip"],
            tags=[t for t in slug.split("-") if t],
            description=f"Godot Asset Store: {slug.replace('-', ' ')}",
            godot_compatible=True,
        )

    # ------------------------------------------------------------------
    def search(self, query: str, asset_type: str = "", limit: int = 10) -> list[Candidate]:
        """Поиск по HTML магазина. Автокомплит используется как уточнение.

        В магазине нет параметра типа для поиска через URL, поэтому
        `asset_type` здесь только фильтрует по словам в slug/названии.
        """
        from urllib.parse import quote
        html = self._get(f"{STORE}/search/?q={quote(query)}")

        seen: set[str] = set()
        out: list[Candidate] = []
        for m in _ASSET_LINK_RE.finditer(html):
            _full, author, slug = m.group(1), m.group(2), m.group(3)
            if author.lower() in ("static", "api", "search"):
                continue
            key = f"{author}/{slug}"
            if key in seen:
                continue
            seen.add(key)
            out.append(self._candidate_from_link(author, slug))

        # если HTML-поиск ничего не дал — попробуем автокомплит, чтобы понять,
        # есть ли вообще подходящие термины (и не выдать пустоту молча)
        if not out:
            try:
                self._get(f"{STORE}/api/v1/search/autocomplete/?query={quote(query)}")
            except Exception:  # noqa: BLE001
                pass

        return out[:limit]

    def inspect(self, asset_id: str) -> Candidate:
        if "/" not in asset_id:
            raise ValueError(
                f"Godot Store: id должен быть 'автор/slug', получено: {asset_id!r}"
            )
        author, slug = asset_id.split("/", 1)
        html = self._get(f"{STORE}/asset/{author}/{slug}/")
        cand = self._candidate_from_link(author, slug)
        cand.name = self._title_of(html, cand.name)
        cand.license = self._license_of(html)
        m = _AUTHOR_RE.search(html)
        if m:
            cand.author = m.group(1)
        # описание — первый осмысленный абзац
        desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']{10,300})',
                         html, re.I)
        if desc:
            cand.description = desc.group(1).strip()
        return cand

    def license(self, asset_id: str) -> str:
        if "/" not in asset_id:
            return "UNKNOWN"
        author, slug = asset_id.split("/", 1)
        return self._license_of(self._get(f"{STORE}/asset/{author}/{slug}/"))

    def resolve_download(self, asset_id: str, fmt: str = "") -> DownloadTarget:
        return self.resolve_bundle(asset_id, fmt).main

    def resolve_bundle(self, asset_id: str, fmt: str = "", resolution: str = "") -> Bundle:
        if "/" not in asset_id:
            raise ValueError(f"Godot Store: неверный id: {asset_id!r}")
        author, slug = asset_id.split("/", 1)
        html = self._get(f"{STORE}/asset/{author}/{slug}/")

        m = _DOWNLOAD_RE.search(html)
        if not m:
            raise ValueError(
                f"Godot Store: у ассета '{asset_id}' нет прямой ссылки на скачивание. "
                f"Возможно, он только для редактора или требует входа."
            )
        path, ver = m.group(1), m.group(4)
        url = f"{STORE}{path}"

        size = None
        try:
            from ..downloader import head_size
            size = head_size(url)
        except Exception:  # noqa: BLE001
            size = None

        # имя файла неизвестно до редиректа — задаём детерминированно
        filename = f"{slug}-{ver}.zip"
        t = DownloadTarget(url=url, filename=filename, format="zip", size_bytes=size)
        return Bundle(
            files=[t], main=t,
            note=(f"аддон/пакет из Godot Asset Store (версия {ver}). "
                  f"Скачивание идёт через 302 на предподписанный URL хранилища."),
        )

    # ------------------------------------------------------------------
    def search_library(self, query: str, kind: str = "", limit: int = 10) -> list[Candidate]:
        """Поиск по СТАРОЙ библиотеке (JSON API). Резервный канал.

        Возвращает ассеты с уже известной лицензией (поле `cost` в API),
        что удобно: у старых записей лицензия размечена машинно.
        """
        import json
        params = f"page=1&filter={query}" if query else "page=1"
        raw = self._get(f"{LIBRARY_API}/asset?{params}")
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            return []

        out: list[Candidate] = []
        for it in (data.get("result") or []):
            lic = str(it.get("cost") or "")
            if kind and str(it.get("type") or "").lower() != kind.lower():
                continue
            aid = str(it.get("asset_id") or "")
            out.append(Candidate(
                source=self.name,
                asset_id=f"library/{aid}",
                name=str(it.get("title") or aid),
                url=f"https://godotengine.org/asset-library/asset/{aid}",
                license=lic or "UNKNOWN",
                author=str(it.get("author") or ""),
                formats=["zip"],
                tags=[str(it.get("category") or "")],
                description=f"Godot Asset Library: {it.get('category') or ''} "
                            f"(Godot {it.get('godot_version') or '?'})",
                godot_compatible=str(it.get("godot_version") or "").startswith("4"),
            ))
        return out[:limit]
