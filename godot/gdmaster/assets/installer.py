"""Распаковка и раскладка ассета в res://assets/external/<pack>/.

Барьер 3 из четырёх. Здесь два независимых риска, и оба закрыты.

РИСК 1 — zip-slip. Архив содержит имена вида `../../project.godot` или
`C:\\Windows\\...` («path traversal в архиве»). Наивный extractall пишет файл
КУДА УГОДНО — вплоть до автозагрузки. Поэтому имена разбираются вручную,
каждый путь нормализуется и проверяется на принадлежность целевому каталогу.

РИСК 2 — zip-bomb. Маленький архив, разворачивающийся в терабайты. Отсюда
лимиты на суммарный распакованный размер и на коэффициент сжатия, проверяемые
ДО записи файла.

Отдельно: установка пишет ТОЛЬКО под res://assets/external/. Это не «правило
в промпте», а отдельная функция записи со своим корнем. `paths.WRITABLE_EXTS`
намеренно НЕ расширяется — иначе бинарники стали бы доступны для записи в
любую папку проекта, включая перезапись project.godot.
"""
from __future__ import annotations

import shutil
import tarfile
import zipfile
from pathlib import Path

from .. import config
from . import manifest as mf

#: Каталог внешних ассетов внутри проекта. Единственная область бинарной записи.
EXTERNAL_SUBDIR = "assets/external"

#: Что вообще имеет смысл класть в Godot-проект.
ASSET_EXTS: frozenset[str] = frozenset({
    # 3D
    ".glb", ".gltf", ".fbx", ".obj", ".blend", ".dae", ".stl",
    # текстуры и изображения
    ".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tga", ".svg",
    ".exr", ".hdr", ".ktx", ".dds",
    # звук
    ".wav", ".ogg", ".mp3", ".flac",
    # данные/конфиги, которые идут вместе с ассетом
    ".json", ".txt", ".md", ".mtl", ".bin",
    # шрифты
    ".ttf", ".otf", ".fnt",
    # Godot-ресурсы (аддоны, шаблоны)
    ".gd", ".tscn", ".tres", ".godot", ".cfg", ".import",
})

#: Расширения, которые НИКОГДА не попадают в проект, даже если лежат в архиве.
FORBIDDEN_EXTS: frozenset[str] = frozenset({
    ".exe", ".dll", ".so", ".dylib", ".bat", ".cmd", ".ps1", ".sh",
    ".msi", ".scr", ".com", ".jar", ".py", ".pyc", ".vbs", ".js",
})

#: Потолки распаковки.
MAX_UNPACKED_BYTES = 2 * 1024 * 1024 * 1024
MAX_COMPRESSION_RATIO = 200   # распакованное / сжатое
MAX_FILES = 20000


class InstallDenied(PermissionError):
    """Установка ассета отклонена."""


def external_root() -> Path:
    """Корень внешних ассетов в активном Godot-проекте."""
    proj = config.godot_project_root()
    if proj is None:
        raise InstallDenied("Godot-проект не задан — установка невозможна")
    return proj / "assets" / "external"


def _safe_join(base: Path, name: str) -> Path:
    """Безопасно присоединить имя из архива. Бросает при выходе за base."""
    # Windows-разделители и абсолютные пути — сразу отказ
    cleaned = name.replace("\\", "/").lstrip("/")
    if not cleaned:
        raise InstallDenied(f"пустое имя в архиве: {name!r}")
    if len(cleaned) > 1 and cleaned[1] == ":":
        raise InstallDenied(f"абсолютный путь в архиве: {name!r}")

    target = (base / cleaned).resolve()
    try:
        target.relative_to(base.resolve())
    except ValueError as e:
        raise InstallDenied(f"zip-slip: '{name}' выходит за каталог установки") from e
    return target


def _check_ext(name: str) -> None:
    suffix = Path(name).suffix.lower()
    if suffix in FORBIDDEN_EXTS:
        raise InstallDenied(
            f"исполняемый/скриптовый файл в ассете запрещён: {name}"
        )


def extract_zip(archive: Path, target: Path) -> list[Path]:
    """Распаковать zip с защитой от zip-slip и бомб."""
    written: list[Path] = []
    with zipfile.ZipFile(archive) as z:
        infos = z.infolist()
        if len(infos) > MAX_FILES:
            raise InstallDenied(f"в архиве {len(infos)} файлов (> {MAX_FILES})")

        total_unpacked = 0
        total_compressed = 0
        for info in infos:
            if info.is_dir():
                continue
            _check_ext(info.filename)
            out = _safe_join(target, info.filename)

            total_unpacked += info.file_size
            total_compressed += max(info.compress_size, 1)
            if total_unpacked > MAX_UNPACKED_BYTES:
                raise InstallDenied(
                    f"распакованный размер превышает лимит: > {MAX_UNPACKED_BYTES} байт"
                )
            ratio = total_unpacked / total_compressed
            if ratio > MAX_COMPRESSION_RATIO and total_unpacked > 10 * 1024 * 1024:
                raise InstallDenied(
                    f"похоже на zip-бомбу: коэффициент сжатия {ratio:.0f}x"
                )

            out.parent.mkdir(parents=True, exist_ok=True)
            with z.open(info) as src, out.open("wb") as dst:
                shutil.copyfileobj(src, dst, 1 << 16)
            written.append(out)
    return written


def extract_tar(archive: Path, target: Path) -> list[Path]:
    """Распаковать tar/tar.gz. Python 3.12+ умеет filter='data' — он и защищает."""
    written: list[Path] = []
    with tarfile.open(archive) as t:
        safe_members = []
        for m in t.getmembers():
            if m.isdir():
                continue
            _check_ext(m.name)
            _safe_join(target, m.name)   # проверка ДО распаковки
            if m.isfile():
                safe_members.append(m)
        if len(safe_members) > MAX_FILES:
            raise InstallDenied(f"в архиве {len(safe_members)} файлов (> {MAX_FILES})")
        total = sum(m.size for m in safe_members)
        if total > MAX_UNPACKED_BYTES:
            raise InstallDenied(f"распакованный размер превышает лимит")

        try:
            t.extractall(target, members=safe_members, filter="data")
        except TypeError:
            t.extractall(target, members=safe_members)
        written = [target / m.name for m in safe_members]
    return written


def unpack(archive: Path, target: Path) -> list[Path]:
    """Распаковать по расширению. Одиночный файл просто копируется."""
    target.mkdir(parents=True, exist_ok=True)
    name = archive.name.lower()
    if name.endswith(".zip"):
        return extract_zip(archive, target)
    if name.endswith((".tar.gz", ".tgz", ".tar.bz2", ".tar")):
        return extract_tar(archive, target)
    if name.endswith((".gz",)) and not name.endswith(".tar.gz"):
        import gzip
        out = _safe_join(target, archive.stem)
        with gzip.open(archive, "rb") as src, out.open("wb") as dst:
            shutil.copyfileobj(src, dst, 1 << 16)
        return [out]
    if archive.suffix.lower() in FORBIDDEN_EXTS:
        raise InstallDenied(f"тип файла запрещён: {archive.name}")
    # одиночный ассет — копируем как есть
    out = _safe_join(target, archive.name)
    shutil.copy2(archive, out)
    return [out]


def _flatten_if_single_dir(pack_dir: Path) -> None:
    """Убрать лишний уровень вложенности: пак часто распаковывается в одну папку."""
    skip = {mf.MANIFEST_NAME, mf.COMPLETE_MARKER}
    entries = [p for p in pack_dir.iterdir() if p.name not in skip]
    if len(entries) != 1 or not entries[0].is_dir():
        return
    inner = entries[0]
    for child in list(inner.iterdir()):
        shutil.move(str(child), str(pack_dir / child.name))
    inner.rmdir()


def install(archive: Path, pack_name: str, entry: dict,
            project_root: Path | None = None) -> dict:
    """Установить распакованный ассет в res://assets/external/<pack_name>/.

    Порядок: лицензионная проверка -> карантин -> распаковка -> манифест.
    Ассет и его asset.json оказываются в одной папке, поэтому удаление папки
    убирает и ассет, и сведения о его лицензии — не может остаться «сирота».
    """
    from . import licenses

    verdict = licenses.evaluate(entry.get("license"))
    ok, why = licenses.check_installable(verdict)
    if not ok:
        raise InstallDenied(f"установка запрещена: {why}")
    ok, why = licenses.check_attribution_complete(entry)
    if not ok:
        raise InstallDenied(why)

    if not pack_name or "/" in pack_name or "\\" in pack_name or ".." in pack_name:
        raise InstallDenied(f"недопустимое имя пакета: {pack_name!r}")

    root = (project_root / EXTERNAL_SUBDIR) if project_root else external_root()
    pack_dir = root / pack_name
    if pack_dir.exists():
        raise InstallDenied(
            f"пакет '{pack_name}' уже установлен в res://{EXTERNAL_SUBDIR}/{pack_name}"
        )

    staging = pack_dir.parent / (pack_name + ".installing")
    if staging.exists():
        shutil.rmtree(staging, ignore_errors=True)
    staging.mkdir(parents=True, exist_ok=True)

    try:
        files = unpack(archive, staging)
        _flatten_if_single_dir(staging)
        # маркер и манифест — служебные файлы staging, в проект они не едут
        files = [p for p in staging.rglob("*") if p.is_file()
                 and p.name not in (mf.MANIFEST_NAME, mf.COMPLETE_MARKER)]

        asset_files = [p for p in files if p.suffix.lower() in ASSET_EXTS]
        if not asset_files:
            raise InstallDenied(
                "в архиве нет файлов, которые Godot может использовать "
                f"(ожидались {', '.join(sorted(list(ASSET_EXTS))[:8])}…)"
            )

        entry = dict(entry)
        entry["formats"] = sorted({p.suffix.lower().lstrip(".") for p in asset_files})
        mf.write(staging, entry)

        # относительные пути считаем ДО переименования: после replace() файлы
        # уже лежат в pack_dir, но пути, полученные из staging, станут
        # непригодны для relative_to (каталог исчез)
        rel_files = [p.relative_to(staging).as_posix() for p in asset_files]

        staging.replace(pack_dir)
    except Exception:
        shutil.rmtree(staging, ignore_errors=True)
        raise

    return {
        "pack": pack_name,
        "path": f"res://{EXTERNAL_SUBDIR}/{pack_name}",
        "files": len(files),
        "asset_files": rel_files[:50],
        "manifest": f"res://{EXTERNAL_SUBDIR}/{pack_name}/{mf.MANIFEST_NAME}",
        "license": entry.get("license"),
    }


def remove(pack_name: str, project_root: Path | None = None) -> dict:
    """Удалить установленный пакет. Только внутри assets/external."""
    if not pack_name or "/" in pack_name or "\\" in pack_name or ".." in pack_name:
        raise InstallDenied(f"недопустимое имя пакета: {pack_name!r}")
    root = (project_root / EXTERNAL_SUBDIR) if project_root else external_root()
    pack_dir = (root / pack_name).resolve()
    try:
        pack_dir.relative_to(root.resolve())
    except ValueError as e:
        raise InstallDenied(f"пакет вне assets/external: {pack_name!r}") from e
    if not pack_dir.exists():
        raise InstallDenied(f"пакет не найден: {pack_name}")
    entry = mf.read(pack_dir)
    shutil.rmtree(pack_dir)
    return {"removed": pack_name, "license": (entry or {}).get("license"),
            "path": f"res://{EXTERNAL_SUBDIR}/{pack_name}"}
