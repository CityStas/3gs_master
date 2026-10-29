"""Скачивание ассетов. Каждый запрос проходит через `netguard.check_url`.

Про прокси. В этом окружении выставлен HTTP_PROXY. Для запросов к ЛОКАЛЬНЫМ
серверам (LLM, embeddings) прокси надо обходить — это уже сделано в
`rag/embedder.py`. Для скачивания из интернета всё наоборот: прокси нужен,
иначе запрос может не уйти. Поэтому здесь opener строится ЯВНО из переменных
окружения, а не «как получится» — иначе поведение зависит от версии Python.

Поток одного скачивания:

    1. check_url(url)                      — домен, схема, приватные адреса
    2. GET с allow_redirects=False         — редиректы проверяем сами,
                                             а не отдаём httpx на самотёк
    3. на каждом шаге 3xx — check_redirect  — новый хост тоже проверяется
    4. Content-Length -> check_size        — ранний отказ по размеру
    5. поток в файл + счёт байт            — точный контроль по факту
    6. sha256                              — целостность и дедупликация
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import httpx

from .. import config
from . import manifest as mf
from . import netguard
from .netguard import FetchBudget, NetworkDenied

USER_AGENT = "gdmaster-asset-manager/1.0 (+local; Godot-only agent)"
CHUNK = 1 << 16


@dataclass
class DownloadResult:
    path: Path
    url: str
    final_url: str
    bytes: int
    sha256: str
    content_type: str

    def to_dict(self) -> dict:
        return {
            "path": str(self.path),
            "url": self.url,
            "final_url": self.final_url,
            "bytes": self.bytes,
            "mb": round(self.bytes / 1e6, 2),
            "sha256": self.sha256,
            "content_type": self.content_type,
        }


def _client(timeout: float = 60.0) -> httpx.Client:
    """HTTP-клиент. Прокси берётся из окружения (trust_env=True): в этой сети
    выход в интернет идёт через прокси, и отключать его нельзя.
    Редиректы НЕ следуются автоматически — их проверяет netguard.
    """
    return httpx.Client(
        timeout=httpx.Timeout(timeout, read=timeout),
        follow_redirects=False,
        headers={"User-Agent": USER_AGENT},
        trust_env=True,
    )


def head_size(url: str) -> int | None:
    """Размер файла по HEAD. Не критично, если не поддержан — вернём None."""
    try:
        with _client(timeout=20.0) as c:
            r = c.head(netguard.check_url(url))
            if r.status_code >= 400:
                return None
            cl = r.headers.get("content-length")
            return int(cl) if cl and cl.isdigit() else None
    except (httpx.HTTPError, NetworkDenied, ValueError, OSError):
        return None


def download(url: str, dest_dir: Path, filename: str,
             budget: FetchBudget | None = None,
             max_bytes: int = netguard.MAX_FILE_BYTES) -> DownloadResult:
    """Скачать один файл. Возвращает результат с sha256 и реальным размером."""
    budget = budget or FetchBudget()
    dest_dir.mkdir(parents=True, exist_ok=True)

    # filename может содержать относительный путь (textures/model_diff.jpg):
    # так его ожидает .gltf внутри себя, поэтому структуру сохраняем.
    # Отсюда две проверки ниже — она же и точка возможного выхода за каталог.
    rel = filename.replace("\\", "/").lstrip("/")
    if ".." in rel.split("/") or (len(rel) > 1 and rel[1] == ":"):
        raise NetworkDenied(f"недопустимое имя файла: {filename!r}")

    target = dest_dir / rel
    try:
        target.resolve().relative_to(dest_dir.resolve())
    except ValueError as e:
        raise NetworkDenied(f"имя файла выходит за каталог: {filename!r}") from e
    target.parent.mkdir(parents=True, exist_ok=True)

    part = target.with_name(target.name + ".part")

    hops = 0
    current = netguard.check_url(url)

    with _client() as c:
        while True:
            r = c.get(current)
            if r.is_redirect:
                loc = r.headers.get("location", "")
                hops += 1
                current = netguard.check_redirect(current, loc, hops)
                r.close()
                continue
            if r.status_code >= 400:
                r.close()
                raise NetworkDenied(
                    f"источник вернул HTTP {r.status_code} для {current}"
                )
            break

        declared = r.headers.get("content-length")
        size = int(declared) if declared and declared.isdigit() else None
        netguard.check_size(size, budget)

        written = 0
        # пишем в .part: оборванное скачивание не оставляет «целый» файл
        with part.open("wb") as f:
            for block in r.iter_bytes(CHUNK):
                written += len(block)
                if written > max_bytes:
                    f.close()
                    part.unlink(missing_ok=True)
                    raise NetworkDenied(
                        f"файл превысил лимит по факту: > {max_bytes} байт"
                    )
                f.write(block)
        content_type = r.headers.get("content-type", "").split(";")[0].strip()
        r.close()

    netguard.check_size(written, FetchBudget())  # финальная сверка с общим потолком
    budget.spend(written)

    from .manifest import sha256_file
    digest = sha256_file(part)
    part.replace(target)  # атомарная подмена: файла наполовину не бывает

    return DownloadResult(path=target, url=url, final_url=current, bytes=written,
                          sha256=digest, content_type=content_type)


def workspace() -> Path:
    """Временная папка для скачивания — ВНЕ Godot-проекта.

    Принципиально: сначала скачиваем и проверяем, и только потом переносим
    в res://assets/external/. Иначе мусорный или оборванный файл окажется
    в проекте раньше, чем мы узнаем, что он из себя представляет.
    """
    d = config.CACHE_DIR / "assets"
    d.mkdir(parents=True, exist_ok=True)
    return d


# --------------------------------------------------------------------------
# Комплекты. Один ассет — не всегда один файл.
# --------------------------------------------------------------------------

@dataclass
class BundleResult:
    """Результат скачивания комплекта."""
    pack: str
    staging: Path
    main_path: Path
    files: list[DownloadResult]
    bundle_note: str = ""

    @property
    def main(self) -> DownloadResult:
        return self.files[0]

    @property
    def total_bytes(self) -> int:
        return sum(f.bytes for f in self.files)

    @property
    def sha256(self) -> str:
        """Хеш комплекта. Один файл — его хеш, иначе хеш конкатенации.

        Так дедупликация работает и для комплектов: повторное скачивание
        той же модели с тем же набором текстур даёт тот же хеш.
        """
        if len(self.files) == 1:
            return self.files[0].sha256
        import hashlib
        h = hashlib.sha256()
        for f in sorted(self.files, key=lambda x: x.path.name):
            h.update(f.sha256.encode())
        return h.hexdigest()

    def to_dict(self, relative_to: Path | None = None) -> dict:
        def rel(p: Path) -> str:
            if relative_to is None:
                return str(p)
            try:
                return p.relative_to(relative_to).as_posix()
            except ValueError:
                return str(p)

        return {
            "pack": self.pack,
            "staging": str(self.staging),
            "main": rel(self.main_path),
            "file_count": len(self.files),
            "total_bytes": self.total_bytes,
            "total_mb": round(self.total_bytes / 1e6, 2),
            "sha256": self.sha256,
            "files": [
                {**f.to_dict(), "rel": rel(f.path), "path": rel(f.path)}
                for f in self.files
            ],
            "note": self.bundle_note,
        }


def sanitize_pack_name(raw: str) -> str:
    """Имя пакета для каталога назначения. Только безопасный набор символов.

    Имя приходит от модели, поэтому оно не может содержать ни разделителей,
    ни `..`, ни расширений: `pack_name` — это КАТАЛОГ, а не путь к файлу.

    Разделители и `..` отклоняются ЯВНО, а не «затираются» заменой на дефис.
    Разница принципиальная: `../../etc` после молчаливой замены становится
    безобидным `etc`, и вызов «проходит» — но это скрывает, что модель
    пыталась выйти за каталог. Отказ с внятной причиной полезнее: он виден
    в аудите и в ответе, а не превращается в тихий успех с другим именем.
    """
    import re

    name = (raw or "").strip()
    if not name:
        raise NetworkDenied(f"пустое имя пакета: {raw!r}")
    if "/" in name or "\\" in name:
        raise NetworkDenied(
            f"имя пакета не может содержать разделители пути: {raw!r}"
        )
    if ".." in name:
        raise NetworkDenied(f"имя пакета не может содержать '..': {raw!r}")

    name = re.sub(r"[^A-Za-z0-9._-]+", "-", name).strip("-._")[:64]
    if not name or name in (".", ".."):
        raise NetworkDenied(f"недопустимое имя пакета: {raw!r}")
    return name


def download_bundle(bundle, pack: str, dest_root: Path | None = None,
                    budget: FetchBudget | None = None,
                    resolution: str = "",
                    mark_complete: bool = True) -> BundleResult:
    """Скачать ВСЕ файлы комплекта в один staging-каталог.

    Зачем отдельная функция, а не вызов download() в цикле: у комплекта общий
    бюджет на сессию. Иначе десять файлов по 300 МБ каждый пройдут поштучную
    проверку и вместе выйдут за лимит на порядок.

    Каждый файл пишется атомарно (`.part` -> rename), относительные пути
    внутри комплекта сохраняются: `.gltf` ссылается на `model.bin` и
    `textures/*.jpg` ровно так, как они названы в include-блоке API.

    `mark_complete=False` — для случая, когда вызывающий сам дописывает
    манифест и хочет поставить маркер последним (см. `write_complete_marker`).
    """
    staging = (dest_root or workspace()) / sanitize_pack_name(pack)
    if staging.exists():
        import shutil
        shutil.rmtree(staging, ignore_errors=True)
    staging.mkdir(parents=True, exist_ok=True)

    shared = budget or FetchBudget()
    results: list[DownloadResult] = []
    try:
        for target in bundle.files:
            results.append(download(
                target.url, staging, target.filename,
                budget=shared, max_bytes=netguard.MAX_FILE_BYTES,
            ))
    except Exception:
        import shutil
        shutil.rmtree(staging, ignore_errors=True)
        raise

    result = BundleResult(
        pack=sanitize_pack_name(pack),
        staging=staging,
        main_path=results[0].path,
        files=results,
        bundle_note=getattr(bundle, "note", "") or "",
    )
    if mark_complete:
        write_complete_marker(staging, result)
    return result


def write_complete_marker(staging: Path, result: BundleResult) -> None:
    """Отметить комплект как целый. Вызывать ПОСЛЕ записи манифеста.

    Порядок важен: маркер — последний файл в каталоге. Если между записью
    файлов и маркером что-то упадёт, пакет останется без маркера, то есть
    будет считаться недокачанным — и это правильное поведение, потому что
    манифеста в нём действительно нет.
    """
    import json
    (staging / mf.COMPLETE_MARKER).write_text(
        json.dumps({
            "pack": result.pack,
            "files": len(result.files),
            "bytes": result.total_bytes,
            "sha256": result.sha256,
        }, ensure_ascii=False, indent=1),
        encoding="utf-8",
    )


def is_complete(staging: Path) -> bool:
    """Целый ли комплект в каталоге."""
    return (staging / mf.COMPLETE_MARKER).exists()
