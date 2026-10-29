"""Адаптер Poly Haven — приоритет 2, всё CC0, официальный API.

Единственный источник, у которого есть настоящий API (спека прямо требует
использовать его вместо скрапинга). Эндпоинты, проверенные живыми запросами:

  GET https://api.polyhaven.com/types                     -> ["hdris","textures","models"]
  GET https://api.polyhaven.com/assets?t=models&categories=props
  GET https://api.polyhaven.com/info/<id>
  GET https://api.polyhaven.com/files/<id>                -> дерево файлов с URL и md5

Файлы отдаются с dl.polyhaven.org (разрешён в netguard).

Лицензия: всё CC0. Атрибуция не требуется, но автор записывается всё равно —
это стоит ноль усилий и сохраняет provenance.
"""
from __future__ import annotations

import httpx

from ... import config
from .. import netguard
from .base import Adapter, Bundle, Candidate, DownloadTarget

API = "https://api.polyhaven.com"

#: Карта «тип запроса агента» -> параметр t в API.
TYPE_MAP = {
    "model": "models", "models": "models", "3d": "models",
    "texture": "textures", "textures": "textures", "pbr": "textures",
    "hdri": "hdris", "hdris": "hdris", "environment": "hdris", "sky": "hdris",
}

#: Предпочтение форматов для 3D-моделей (см. 05_search_and_scoring.md).
MODEL_FMT_ORDER = ("gltf", "glb", "fbx", "obj", "blend")
TEX_FMT_ORDER = ("png", "jpg", "jpeg", "exr")


class PolyHavenAdapter(Adapter):
    name = "polyhaven"
    display_name = "Poly Haven"
    priority = 2

    def _get(self, path: str, timeout: float = 30.0):
        url = netguard.check_url(API + path)
        with httpx.Client(timeout=timeout, trust_env=True,
                          headers={"User-Agent": "gdmaster-asset-manager/1.0"}) as c:
            r = c.get(url)
            r.raise_for_status()
            return r.json()

    def available(self) -> tuple[bool, str]:
        try:
            self._get("/types", timeout=15.0)
            return True, ""
        except Exception as e:  # noqa: BLE001
            return False, f"Poly Haven API недоступен: {e}"

    # ------------------------------------------------------------------
    def search(self, query: str, asset_type: str = "", limit: int = 10) -> list[Candidate]:
        t = TYPE_MAP.get((asset_type or "").lower(), "")
        path = f"/assets?t={t}" if t else "/assets"
        data = self._get(path)
        if not isinstance(data, dict):
            return []

        q = query.lower().strip()
        terms = [w for w in q.replace(",", " ").split() if len(w) > 2]

        scored: list[tuple[int, Candidate]] = []
        for asset_id, meta in data.items():
            if not isinstance(meta, dict):
                continue
            tags = [str(x).lower() for x in (meta.get("tags") or [])]
            cats = [str(x).lower() for x in (meta.get("categories") or [])]
            name = str(meta.get("name") or asset_id)
            haystack = " ".join([name.lower(), asset_id.lower(), *tags, *cats])

            hits = sum(1 for term in terms if term in haystack)
            if terms and hits == 0:
                continue
            score = hits * 10
            # лёгкий бонус за совпадение в тегах — они точнее описания
            score += sum(3 for term in terms if term in tags)
            scored.append((score, self._candidate(asset_id, meta)))

        scored.sort(key=lambda kv: -kv[0])
        return [c for _s, c in scored[:limit]]

    def _candidate(self, asset_id: str, meta: dict) -> Candidate:
        authors = meta.get("authors") or {}
        author = ", ".join(authors.keys()) if isinstance(authors, dict) else str(authors)
        return Candidate(
            source=self.name,
            asset_id=asset_id,
            name=str(meta.get("name") or asset_id),
            url=f"https://polyhaven.com/a/{asset_id}",
            license="CC0",
            author=author,
            formats=[],
            tags=[str(x) for x in (meta.get("tags") or [])][:12],
            description=str(meta.get("description") or "")[:400],
            polycount=meta.get("polycount"),
        )

    def inspect(self, asset_id: str) -> Candidate:
        meta = self._get(f"/info/{asset_id}")
        if not isinstance(meta, dict):
            raise ValueError(f"Poly Haven: ассет не найден: {asset_id}")
        cand = self._candidate(asset_id, meta)
        try:
            cand.formats = self._formats(self._get(f"/files/{asset_id}"))
        except Exception:  # noqa: BLE001 — формат не критичен для inspect
            pass
        return cand

    def license(self, asset_id: str) -> str:
        return "CC0"   # весь Poly Haven — CC0, отдельных исключений нет

    # ------------------------------------------------------------------
    @staticmethod
    def _formats(tree: dict) -> list[str]:
        found: set[str] = set()

        def walk(node, depth: int = 0):
            if depth > 5 or not isinstance(node, dict):
                return
            for key, val in node.items():
                if isinstance(val, dict):
                    if "url" in val and isinstance(val["url"], str):
                        ext = val["url"].split("?")[0].rsplit(".", 1)[-1].lower()
                        if 1 < len(ext) <= 5:
                            found.add(ext)
                    else:
                        walk(val, depth + 1)
                elif isinstance(val, str) and key in ("format", "ext"):
                    found.add(val.lower())

        walk(tree)
        return sorted(found)

    def resolve_download(self, asset_id: str, fmt: str = "") -> DownloadTarget:
        """Главный файл ассета. Для моделей gltf это .gltf, но одного его мало —
        используй resolve_bundle, иначе получишь битую модель."""
        return self.resolve_bundle(asset_id, fmt).main

    def resolve_bundle(self, asset_id: str, fmt: str = "", resolution: str = "") -> Bundle:
        """Комплект файлов ассета.

        Почему комплект, а не файл: у модели Poly Haven `.gltf` весит ~5 КБ и
        ссылается на `.bin` с геометрией и на текстуры в соседних подпапках.
        Скачав только `.gltf`, мы получим в Godot модель без геометрии.
        Поэтому берём главный файл + все include-файлы + текстуры выбранного
        разрешения.

        Разрешение по умолчанию — 2k. 8k-текстуры весят сотни мегабайт
        (проверено: Diffuse/8k/png = 230 МБ на один ящик) и для прототипа
        бессмысленны. 2k достаточно и по размеру разумно.
        """
        info = self._get(f"/info/{asset_id}")
        kind = ""
        if isinstance(info, dict):
            kind = {0: "hdri", 1: "texture", 2: "model"}.get(info.get("type"), "")
        tree = self._get(f"/files/{asset_id}")

        if kind == "model":
            return self._bundle_model(tree, asset_id, fmt, resolution)
        if kind == "texture":
            return self._bundle_texture(tree, asset_id, fmt, resolution)
        return self._bundle_hdri(tree, asset_id, fmt, resolution)

    # ------------------------------------------------------------------
    @staticmethod
    def _res_of(key: str, preferred: str) -> int:
        """Оценка разрешения: чем ближе к предпочтительному, тем больше.

        `preferred` пустой -> считаем 2k разумным значением по умолчанию.
        """
        want = preferred or "2k"
        order = ["1k", "2k", "4k", "8k", "16k"]
        low = key.lower()
        for i, r in enumerate(order):
            if r in low:
                return 100 - abs(i - order.index(want)) * 15
        return 50   # разрешение не указано — нейтрально

    def _bundle_model(self, tree: dict, asset_id: str, fmt: str,
                      resolution: str) -> Bundle:
        """Собрать комплект модели.

        Структура gltf-узла в API (проверена живым запросом):

          gltf -> "2k" -> { "gltf": { "url": "...gltf", "size": N,
                                      "include": {
                                         "model.bin": {...},
                                         "textures/model_diff_2k.jpg": {...},
                                      } } }

        Ключевой момент — блок `include`. Именно он описывает, ЧТО нужно
        для открытия модели, и сохраняет относительные пути (`textures/…`),
        которых ждёт .gltf. Поэтому комплект строится по `include`, а не
        обходом всего дерева: обход давал дубли текстур (они же есть на
        верхнем уровне дерева) и терял относительные пути.
        """
        order = [fmt.lower()] if fmt else list(MODEL_FMT_ORDER)

        chosen_fmt = next((f for f in order if f in tree), "")
        if not chosen_fmt:
            for f in MODEL_FMT_ORDER:
                if f in tree:
                    chosen_fmt = f
                    break
        if not chosen_fmt:
            raise ValueError(f"Poly Haven: у модели {asset_id} нет поддерживаемых форматов")

        variants = tree[chosen_fmt]
        if not isinstance(variants, dict) or not variants:
            raise ValueError(f"Poly Haven: пустой набор файлов для {asset_id}/{chosen_fmt}")

        # выбираем вариант по разрешению (ключи 1k/2k/4k/8k)
        best_key = max(variants.keys(), key=lambda k: self._res_of(k, resolution))
        node = variants[best_key]

        from urllib.parse import unquote

        def target_of(url: str, size, name: str = "") -> DownloadTarget:
            fn = name or unquote(url.split("?")[0].rsplit("/", 1)[-1])
            return DownloadTarget(url=url, filename=fn,
                                  format=fn.rsplit(".", 1)[-1].lower(),
                                  size_bytes=size)

        # главный файл: у gltf он лежит в node["gltf"], у fbx/obj — прямо в node
        main_node = node.get(chosen_fmt) if isinstance(node.get(chosen_fmt), dict) else node
        if not isinstance(main_node, dict) or not main_node.get("url"):
            main_node = node
        main_url = main_node.get("url")
        if not main_url:
            raise ValueError(f"Poly Haven: нет главного файла для {asset_id}/{chosen_fmt}")

        main = target_of(main_url, main_node.get("size"))
        files: list[DownloadTarget] = [main]

        include = main_node.get("include")
        if isinstance(include, dict):
            for rel_name, entry in include.items():
                if not isinstance(entry, dict) or not entry.get("url"):
                    continue
                # имя сохраняем КАК В include: относительный путь (textures/...)
                # именно его ожидает .gltf внутри себя
                files.append(target_of(entry["url"], entry.get("size"), rel_name))

        return Bundle(
            files=files, main=main,
            note=(f"комплект {chosen_fmt}/{best_key}: главный файл + {len(files) - 1} "
                  f"файл(ов) из include (геометрия .bin и текстуры). "
                  f"Скачать только .gltf нельзя — получится модель без геометрии."),
        )

    def _bundle_texture(self, tree: dict, asset_id: str, fmt: str,
                        resolution: str) -> Bundle:
        files: list[DownloadTarget] = []
        for map_name, variants in tree.items():
            if not isinstance(variants, dict):
                continue
            best_key = max(variants.keys(), key=lambda k: self._res_of(k, resolution))
            variant = variants[best_key]
            if not isinstance(variant, dict):
                continue
            want = fmt.lower() if fmt else ""
            candidates = [want] if want else ["png", "jpg", "exr"]
            for ext in candidates + [k for k in variant.keys() if k not in candidates]:
                entry = variant.get(ext)
                if isinstance(entry, dict) and entry.get("url"):
                    from urllib.parse import unquote
                    url = entry["url"]
                    fn = unquote(url.split("?")[0].rsplit("/", 1)[-1])
                    files.append(DownloadTarget(
                        url=url, filename=f"{map_name}_{fn}", format=ext,
                        size_bytes=entry.get("size")))
                    break
        if not files:
            raise ValueError(f"Poly Haven: не найдено файлов текстуры {asset_id}")
        return Bundle(files=files, main=files[0],
                      note=f"комплект PBR-карт, разрешение {resolution or '2k'}")

    def _bundle_hdri(self, tree: dict, asset_id: str, fmt: str,
                     resolution: str) -> Bundle:
        hdri = tree.get("hdri") or {}
        if not isinstance(hdri, dict) or not hdri:
            raise ValueError(f"Poly Haven: нет hdri для {asset_id}")
        best_key = max(hdri.keys(), key=lambda k: self._res_of(k, resolution))
        variant = hdri[best_key] or {}
        want = (fmt.lower() if fmt else "hdr")
        entry = variant.get(want) or variant.get("hdr") or variant.get("exr")
        if not isinstance(entry, dict) or not entry.get("url"):
            raise ValueError(f"Poly Haven: нет файла {want} для {asset_id}")
        from urllib.parse import unquote
        url = entry["url"]
        fn = unquote(url.split("?")[0].rsplit("/", 1)[-1])
        t = DownloadTarget(url=url, filename=fn,
                           format=fn.rsplit(".", 1)[-1].lower(),
                           size_bytes=entry.get("size"))
        return Bundle(files=[t], main=t, note=f"HDRI {best_key}")
