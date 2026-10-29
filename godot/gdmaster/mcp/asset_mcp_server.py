"""MCP-сервер внешних ассетов: восемь инструментов, семь источников внутри.

§9 спеки. Модель не должна получить «download_itch», «download_kenney»,
«download_polyhaven» — семь инструментов значат семь схем в контексте и семь
способов ошибиться. Поэтому наружу видны восемь ЛОГИЧЕСКИХ операций:

    asset_search     найти кандидатов в одном или нескольких источниках
    asset_inspect    подробности одного ассета (включая лицензию)
    asset_license    лицензионное решение — принимает КОД, а не модель
    asset_download   скачать комплект во временную папку (НЕ в проект)
    asset_install    перенести скачанное в res://assets/external/<pack>/
    asset_remove     удалить установленный пакет
    asset_list       что уже установлено
    asset_manifest   манифест одного пакета (автор, лицензия, sha256)

Различие источников живёт в `adapters/`, различие «скачать / поставить» —
в двух отдельных инструментах. Двухшаговость принципиальна: скачивание
проверяется до того, как что-либо появится в проекте.

Про лицензии. Решение принимает `assets.licenses`, а не модель. `CC-BY-SA`
и `GPL` останавливают установку и требуют явного `approve=True`; `UNKNOWN`
не устанавливается вообще. Атрибуция (автор, source_url) для CC-BY
проверяется как УСЛОВИЕ установки: ассет без записанного автора нарушает
лицензию, даже если лежит в проекте.

Состояние. Инструменты stateless по возможности: `asset_download` возвращает
staging-путь, `asset_install` его принимает. Между вызовами живёт только
память о скачанных комплектах в `data/cache/assets/` — она и есть «корзина».
"""
from __future__ import annotations

import json
import shutil
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from mcp.server.fastmcp import FastMCP  # noqa: E402

from gdmaster import config  # noqa: E402
from gdmaster.assets import installer, licenses, manifest as mf, netguard  # noqa: E402
from gdmaster.assets import registry as reg  # noqa: E402
from gdmaster.assets.downloader import (  # noqa: E402
    download_bundle, workspace, write_complete_marker,
)
from gdmaster.godot.paths import PathDenied  # noqa: E402

mcp = FastMCP("assets")

AUDIT_LOG = config.LOGS_DIR / "asset_mcp_audit.jsonl"

#: Сколько источников опрашивать параллельно нельзя: сайт без API (Kenney,
#: Godot Store) не любит залпы запросов, и один поиск уже обходит десятки
#: страниц. Источники обходятся последовательно, зато внутри каждого —
#: собственный кэш на время жизни процесса.
MAX_LIMIT = 40


def _audit(tool: str, args: dict, summary: str, ok: bool) -> None:
    try:
        with AUDIT_LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps({
                "ts": time.time(), "tool": tool, "ok": ok,
                "args": {k: (v if len(str(v)) < 300 else str(v)[:300] + "...")
                         for k, v in args.items()},
                "summary": summary[:400],
            }, ensure_ascii=False) + "\n")
    except OSError:
        pass


def _ok(**kw) -> str:
    return json.dumps({"ok": True, **kw}, ensure_ascii=False, indent=1)


def _err(msg: str, **kw) -> str:
    return json.dumps({"ok": False, "error": msg, **kw}, ensure_ascii=False, indent=1)


def _empty_state() -> dict:
    return {"assets": [], "last_write": 0.0}


def _state_path() -> Path:
    """Учёт установленных внешних ассетов.

    Кэш-файл, а не источник истины: истина — манифесты под res://assets/external.
    Файл нужен, чтобы `asset_list` не обходил дерево проекта при каждом вызове
    и чтобы была видна история установок даже после удаления пакета.
    """
    return config.CACHE_DIR / "assets" / "state.json"


def _load_state() -> dict:
    p = _state_path()
    if not p.exists():
        return _empty_state()
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            return _empty_state()
        data.setdefault("assets", [])
        return data
    except (OSError, json.JSONDecodeError):
        return _empty_state()


def _save_state(state: dict) -> None:
    p = _state_path()
    try:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")
    except OSError:
        pass


# ==========================================================================
# ПОИСК
# ==========================================================================

@mcp.tool()
def asset_search(query: str, asset_type: str = "", source: str = "",
                 limit: int = 10) -> str:
    """Найти внешние ассеты (модели, текстуры, звуки, аддоны) в сети.

    Один вызов — все источники. Не вызывай по источнику на каждый запрос:
    различия скрыты внутри, а `source` нужен только чтобы ограничить поиск
    сознательно.

    Порядок источников — по приоритету (§8): Godot Asset Store (аддоны,
    плагины, шейдеры) -> Poly Haven (3D-модели, PBR-текстуры, HDRI, CC0) ->
    Kenney (2D-спрайты, звук, прототипы, CC0).

    Args:
        query: что искать. Простые существительные работают лучше фраз:
            "crate", "wood floor", "gamepad", "dialogue". По-английски.
        asset_type: необязательный тип: model/3d, texture/pbr, hdri/sky,
            audio, sprite/2d, addon/plugin.
        source: ограничить одним источником (godot_store, polyhaven, kenney).
            Пусто — искать во всех доступных.
        limit: сколько кандидатов вернуть суммарно (макс. 40).

    Дальше: `asset_inspect` по выбранному id -> `asset_license` -> `asset_download`.
    """
    q = (query or "").strip()
    if not q:
        return _err("пустой запрос: укажи, что искать")
    limit = max(1, min(int(limit or 10), MAX_LIMIT))

    if source:
        one = reg.adapter_for(source)
        if one is None:
            return _err(
                f"неизвестный источник: {source!r}",
                available=[a.name for a in reg.get_adapters()],
            )
        adapters, dead = [], []
        ok, why = one.available()
        (adapters.append(one) if ok else dead.append(why))
    else:
        adapters, dead = reg.available_adapters()

    if not adapters:
        return _err(
            "ни один источник недоступен",
            reasons=dead or ["нет адаптеров"],
            hint="Проверь сеть; при офлайн-запуске поиск ассетов невозможен.",
        )

    results: list[dict] = []
    errors: list[str] = []
    # каждый источник получает свою долю лимита: иначе Kenney с сотнями
    # совпадений вытеснит Poly Haven из топа
    per_source = max(3, limit // len(adapters) + 1)
    for a in adapters:
        try:
            for c in a.search(q, asset_type=asset_type, limit=per_source):
                results.append(c.to_dict())
        except netguard.NetworkDenied as e:
            errors.append(f"{a.name}: отказ сети — {e}")
        except Exception as e:  # noqa: BLE001 — один источник не должен ронять поиск
            errors.append(f"{a.name}: {type(e).__name__}: {e}")

    # перемежаем источники, чтобы в топе не оказались одни подряд
    results.sort(key=lambda r: reg.get_adapters().index(
        next((x for x in reg.get_adapters() if x.name == r["source"]),
             reg.get_adapters()[0])) if results else 0)

    out = results[:limit]
    payload = {
        "query": q, "type": asset_type or "(любой)",
        "count": len(out),
        "sources_tried": [a.name for a in adapters],
        "sources_unavailable": dead,
        "results": out,
    }
    if errors:
        payload["errors"] = errors
    if not out:
        payload["hint"] = (
            "Ничего не найдено. Источники англоязычные — попробуй одно "
            "существительное: 'barrel', 'grass', 'footstep'."
        )
    _audit("asset_search", {"query": q, "type": asset_type, "source": source},
           f"{len(out)} результатов", True)
    return _ok(**payload)


@mcp.tool()
def asset_inspect(source: str, asset_id: str) -> str:
    """Подробности одного ассета: лицензия, автор, форматы, размер, теги.

    Вызывай перед скачиванием — именно здесь выясняется лицензия, а она
    решает, можно ли ассет вообще ставить в проект.

    Args:
        source: имя источника из результатов `asset_search`.
        asset_id: id ассета из результатов `asset_search` (поле `id`).
    """
    a = reg.adapter_for(source)
    if a is None:
        return _err(f"неизвестный источник: {source!r}",
                    available=[x.name for x in reg.get_adapters()])
    try:
        cand = a.inspect(asset_id)
    except netguard.NetworkDenied as e:
        return _err(f"отказ сети: {e}")
    except Exception as e:  # noqa: BLE001
        return _err(f"{type(e).__name__}: {e}")

    verdict = licenses.evaluate(cand.license)
    payload = cand.to_dict()
    payload["license_verdict"] = verdict.to_dict()
    payload["next"] = (
        "лицензия позволяет установку — можно asset_download"
        if verdict.automatic_install_allowed
        else f"лицензия {verdict.license}: потребуется явное approve=True"
        if verdict.license in licenses.NEEDS_APPROVAL
        else "лицензия не определена — установка будет заблокирована"
    )
    return _ok(**payload)


@mcp.tool()
def asset_license(source: str, asset_id: str) -> str:
    """Лицензионное решение по ассету: можно ли ставить, нужна ли атрибуция.

    Решение принимает код, а не ты. Не пересказывай лицензию своими словами —
    верни пользователю поля этого ответа. `CC-BY-SA` и `GPL` требуют его
    решения; `UNKNOWN` означает отказ, а не «наверное, можно».

    Args:
        source: имя источника.
        asset_id: id ассета.
    """
    a = reg.adapter_for(source)
    if a is None:
        return _err(f"неизвестный источник: {source!r}\n"
                    f"разрешённые: {sorted(x.name for x in reg.get_adapters())}")
    try:
        raw = a.license(asset_id)
    except netguard.NetworkDenied as e:
        return _err(f"отказ сети: {e}")
    except Exception as e:  # noqa: BLE001
        return _err(f"{type(e).__name__}: {e}")

    verdict = licenses.evaluate(raw)
    return _ok(
        source=source, asset_id=asset_id, license_raw=raw,
        **verdict.to_dict(),
        install_allowed=verdict.automatic_install_allowed,
        need_user_approval=verdict.license in licenses.NEEDS_APPROVAL,
    )


# ==========================================================================
# СКАЧИВАНИЕ (шаг 1 — во временную папку, НЕ в проект)
# ==========================================================================

@mcp.tool()
def asset_download(source: str, asset_id: str, pack_name: str = "",
                   fmt: str = "", resolution: str = "2k") -> str:
    """Скачать ассет во ВРЕМЕННУЮ папку. В проект ничего не попадает.

    Это первый шаг двухшаговой установки. Скачанные файлы лежат вне
    Godot-проекта, поэтому мусорный, битый или нелицензионный ассет не может
    попасть в проект «случайно» — только через явный `asset_install`.

    Для моделей и текстур скачивается КОМПЛЕКТ: у gltf-модели один файл
    бесполезен, ей нужны .bin с геометрией и текстуры. Разрешение по умолчанию
    2k: 8k-текстуры весят сотни мегабайт.

    ВАЖНО — вызывай по одному ассету за раз, не параллельно. Скачивание идёт
    последовательно внутри одного вызова, а вызовы обрабатываются в одном
    процессе: три одновременных `asset_download` складываются по времени и
    упираются в таймаут MCP (проверено на прогоне — три таймаута по 300 с).
    Нужно несколько моделей — вызывай их по очереди в отдельных шагах.

    Повторный вызов с тем же `pack_name` безопасен: если пакет уже скачан
    целиком, вернётся успех с готовым пакетом (не отказ). Недокачанный пакет
    перекачивается заново.

    Args:
        source: имя источника.
        asset_id: id ассета.
        pack_name: как назвать пакет (папка при установке). Пусто — из id.
        fmt: желаемый формат: gltf/glb/fbx/obj, png/jpg, hdr. Пусто — лучший.
        resolution: 1k/2k/4k/8k для текстур и моделей Poly Haven. По умолчанию 2k.

    Возвращает `pack` и путь staging — их передай в `asset_install`.
    """
    a = reg.adapter_for(source)
    if a is None:
        return _err(f"неизвестный источник: {source!r}",
                    available=[x.name for x in reg.get_adapters()])

    pack = pack_name or f"{a.name}-{asset_id}".replace("/", "-")
    try:
        pack = _sanitize(pack)
    except Exception as e:  # noqa: BLE001
        return _err(str(e))

    # Каталог бывает в трёх состояниях, и они означают РАЗНОЕ. Путать их
    # нельзя: именно на этом модель застряла в реальном прогоне — получила
    # таймаут MCP, файлы при этом скачались, а повторный вызов ответил
    # отказом «уже скачан», после чего не работал ни download, ни install.
    state = _staging_state(pack)
    if state == "complete":
        return _already_downloaded(pack)
    if state == "partial":
        # недокачанный (нет маркера) — сносим и качаем заново
        shutil.rmtree(workspace() / pack, ignore_errors=True)
    if _installed_exists(pack):
        return _err(
            f"пакет '{pack}' уже установлен в проект",
            pack=pack,
            hint=f"Скачай под другим именем или сначала asset_remove("
                 f"pack='{pack}', confirm=True).",
        )

    # лицензия проверяется ДО скачивания: качать то, что нельзя поставить, —
    # лишний трафик и лишний риск на ровном месте
    try:
        raw_lic = a.license(asset_id)
    except netguard.NetworkDenied as e:
        return _err(f"отказ сети: {e}")
    except Exception as e:  # noqa: BLE001
        raw_lic = "UNKNOWN"
        _audit("asset_download", {"source": source, "id": asset_id},
               f"лицензия не определена: {e}", False)

    verdict = licenses.evaluate(raw_lic)
    if verdict.license in licenses.REJECT:
        return _err(
            "лицензия не определена — скачивание отменено",
            license_raw=raw_lic,
            reason=verdict.reason,
            hint="Открой страницу ассета, уточни лицензию и повтори.",
        )

    try:
        bundle = a.resolve_bundle(asset_id, fmt=fmt, resolution=resolution)
    except netguard.NetworkDenied as e:
        return _err(f"отказ сети: {e}")
    except Exception as e:  # noqa: BLE001
        return _err(f"не удалось определить файлы ассета: {type(e).__name__}: {e}",
                    source=source, asset_id=asset_id)

    try:
        result = download_bundle(bundle, pack, mark_complete=False)
    except netguard.NetworkDenied as e:
        return _err(f"скачивание отклонено: {e}")
    except Exception as e:  # noqa: BLE001
        return _err(f"скачивание не удалось: {type(e).__name__}: {e}")

    entry = mf.build(
        name=asset_id,
        source=a.name,
        source_url=_page_url(a, asset_id),
        download_url=result.main.url,
        license_raw=raw_lic,
        author=_author_from_source(a.name, asset_id),
        original_filename=result.main.path.name,
        sha256=result.sha256,
    )
    # манифест пишем СРАЗУ в staging: на шаге install он уже готов, а данные
    # о лицензии и происхождении не теряются между двумя вызовами
    try:
        mf.write(result.staging, entry)
    except OSError as e:
        _audit("asset_download", {"pack": pack}, f"манифест не записан: {e}", False)

    # маркер — ПОСЛЕДНИМ. Порядок «файлы -> манифест -> маркер» означает, что
    # маркер есть только у полностью готового пакета. Обрыв на любом шаге
    # оставит каталог без маркера, и он будет перекачан, а не принят за готовый.
    try:
        write_complete_marker(result.staging, result)
    except OSError as e:
        _audit("asset_download", {"pack": pack}, f"маркер не записан: {e}", False)

    payload = result.to_dict(relative_to=workspace())
    payload["source"] = a.name
    payload["asset_id"] = asset_id
    payload["license"] = verdict.license
    payload["license_raw"] = raw_lic
    payload["installable"] = verdict.automatic_install_allowed
    payload["next"] = (
        f"передай pack='{result.pack}' в asset_install"
        if verdict.automatic_install_allowed
        else f"лицензия {verdict.license} требует подтверждения пользователя: "
             f"asset_install(pack='{result.pack}', approve=True) — только после "
             f"явного согласия"
    )
    _audit("asset_download", {"source": source, "id": asset_id, "pack": pack},
           f"{result.total_bytes} байт, {len(result.files)} файл(ов)", True)
    return _ok(**payload)


def _page_url(adapter, asset_id: str) -> str:
    """URL страницы ассета для манифеста. Нужен для атрибуции."""
    try:
        return adapter.inspect(asset_id).url
    except Exception:  # noqa: BLE001
        return ""


def _sanitize(name: str) -> str:
    from gdmaster.assets.downloader import sanitize_pack_name
    return sanitize_pack_name(name)


def _staging_dir(pack: str) -> Path:
    """Каталог готового к установке пакета.

    Требуется маркер `.complete`, и это не придирка: `asset_install` — путь в
    проект. Недокачанный комплекс (нет `.bin` или части текстур) даёт модель
    без геометрии, а заметить это по факту установки невозможно. Лучше отказ.
    """
    p = _sanitize(pack)
    d = workspace() / p
    if not d.exists():
        raise FileNotFoundError(
            f"скачанный пакет '{p}' не найден в staging. Сначала вызови "
            f"asset_download — asset_install ставит только то, что уже скачано."
        )
    if not (d / mf.COMPLETE_MARKER).exists():
        raise FileNotFoundError(
            f"пакет '{p}' недокачан: нет маркера {mf.COMPLETE_MARKER}. "
            f"Скачивание оборвалось (например по таймауту). Повтори "
            f"asset_download — он перекачает пакет целиком."
        )
    return d


def _staging_state(pack: str) -> str:
    """Состояние staging: `none` | `complete` | `partial`."""
    try:
        d = workspace() / _sanitize(pack)
    except Exception:  # noqa: BLE001
        return "none"
    if not d.exists():
        return "none"
    return "complete" if (d / mf.COMPLETE_MARKER).exists() else "partial"


def _already_downloaded(pack: str) -> str:
    """Ответ для уже скачанного комплекта — УСПЕХ, а не отказ.

    Форма ответа та же, что у свежего скачивания: модель не должна различать
    «скачал сейчас» и «скачал раньше», иначе она снова упрётся в тупик.
    """
    d = workspace() / _sanitize(pack)
    entry = mf.read(d) or {}
    marker: dict = {}
    try:
        marker = json.loads((d / mf.COMPLETE_MARKER).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        pass

    files = sorted(
        p for p in d.rglob("*") if p.is_file()
        and p.name not in (mf.MANIFEST_NAME, mf.COMPLETE_MARKER)
    )
    verdict = licenses.evaluate(entry.get("license"))
    total = marker.get("bytes") or 0
    return _ok(
        pack=_sanitize(pack), staging=str(d), cached=True,
        file_count=len(files),
        total_bytes=total or None,
        total_mb=round(total / 1e6, 2) if total else None,
        sha256=marker.get("sha256") or entry.get("sha256") or "",
        source=entry.get("source"), asset_id=entry.get("name"),
        license=verdict.license,
        installable=verdict.automatic_install_allowed,
        files=[{"rel": p.relative_to(d).as_posix()} for p in files],
        note="Пакет уже был скачан ранее и лежит в staging целиком.",
        next=f"передай pack='{_sanitize(pack)}' в asset_install",
    )


def _installed_exists(pack: str) -> bool:
    """Есть ли пакет с таким именем уже в проекте."""
    try:
        root = installer.external_root()
    except installer.InstallDenied:
        return False
    return (root / _sanitize(pack)).exists()


# ==========================================================================
# УСТАНОВКА (шаг 2 — в проект)
# ==========================================================================

@mcp.tool()
def asset_install(pack: str, approve: bool = False) -> str:
    """Установить скачанный ассет в проект: res://assets/external/<pack>/.

    Второй шаг. Материал берётся ИЗ STAGING, а не из сети: между «скачал» и
    «поставил» не должно быть незаметной подмены файла.

    Что проверяется до записи: лицензия (UNKNOWN — отказ, CC-BY-SA/GPL —
    нужен approve=True от пользователя), полнота атрибуции для CC-BY, защита
    от zip-slip и zip-bomb при распаковке. Расширения бинарников лежат в
    отдельном списке: `paths.WRITABLE_EXTS` не расширяется, иначе бинарники
    стали бы доступны для записи в любой угол проекта.

    Args:
        pack: имя пакета из ответа `asset_download` (поле `pack`).
        approve: явное согласие пользователя на лицензию CC-BY-SA/GPL.
            Ставь True ТОЛЬКО получив согласие вслух. Не догадывайся.

    После установки: назначь файлы в сцену и прогони `godot_validate`.
    """
    try:
        staging = _staging_dir(pack)
    except Exception as e:  # noqa: BLE001
        return _err(str(e))

    entry = mf.read(staging)
    if entry is None:
        return _err(f"в staging нет манифеста для '{pack}' — пакет повреждён",
                    hint="Повтори asset_download")

    verdict = licenses.evaluate(entry.get("license"))
    if verdict.license in licenses.REJECT:
        return _err(
            f"установка запрещена: {verdict.reason}",
            license=verdict.license,
            license_raw=entry.get("license"),
            hint="Лицензия не определена. Уточни её на странице ассета "
                 "и запусти asset_download заново.",
        )
    ok, why = licenses.check_installable(verdict, approved_by_user=bool(approve))
    if not ok:
        return _err(why, license=verdict.license,
                    requirements=verdict.requirements,
                    hint="Покажи пользователю requirements и спроси разрешение. "
                         "Только после явного согласия — approve=True.")

    ok, why = licenses.check_attribution_complete(entry)
    if not ok:
        # автор берётся из источника; если его нет — это не «мелочь»,
        # а незакрытое требование лицензии
        if not str(entry.get("author") or "").strip():
            entry["author"] = _author_from_source(entry.get("source", ""),
                                                  entry.get("name", ""))
        ok, why = licenses.check_attribution_complete(entry)
        if not ok:
            return _err(why, license=verdict.license,
                        hint="Заполни author/source_url и повтори.")
    entry["approved_by_user"] = bool(approve)
    try:
        mf.write(staging, entry)
    except OSError:
        pass

    # Архив — единственный файл пакета, и он не .zip? Тогда собираем временный
    # zip: `installer.unpack` умеет копировать одиночный файл, но `install`
    # ждёт архив, а общий путь распаковки сохраняет защиту от zip-slip.
    archive = _pick_archive(staging)
    tmp_archive: Path | None = None
    if archive is None:
        tmp_archive = _direct_copy_target(staging)
        archive = tmp_archive
    try:
        result = installer.install(archive, _sanitize(pack), entry)
    except (installer.InstallDenied, PathDenied) as e:
        return _err(str(e))
    except Exception as e:  # noqa: BLE001
        return _err(f"установка не удалась: {type(e).__name__}: {e}")
    finally:
        # временный zip — служебный, в staging ему делать нечего
        if tmp_archive is not None:
            tmp_archive.unlink(missing_ok=True)

    # staging нужен был только для установки; чистим, чтобы кэш не рос
    shutil.rmtree(staging, ignore_errors=True)

    state = _load_state()
    state["assets"] = [a for a in state.get("assets", [])
                       if a.get("pack") != result["pack"]]
    state.setdefault("assets", []).append({
        "pack": result["pack"], "path": result["path"],
        "license": result.get("license"), "source": entry.get("source"),
        "asset_id": entry.get("name"), "sha256": entry.get("sha256"),
        "installed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    })
    state["last_write"] = time.time()
    _save_state(state)

    result["next"] = (
        "Ассет в проекте: res://" + installer.EXTERNAL_SUBDIR + "/" + result["pack"] +
        ". Запусти godot_check_project, чтобы Godot импортировал ресурсы, "
        "затем используй их в сцене."
    )
    _audit("asset_install", {"pack": pack, "approve": approve},
           f"установлен {result.get('path')}", True)
    return _ok(**result)


def _pick_archive(staging: Path) -> Path | None:
    """Единственный архив в staging, если он там есть."""
    candidates = [p for p in staging.iterdir()
                  if p.is_file() and p.suffix.lower() in (".zip", ".tar", ".gz", ".tgz")]
    if len(candidates) == 1:
        return candidates[0]
    return None


def _direct_copy_target(staging: Path) -> Path:
    """Файлы без архива (одиночный .hdr, .png) ставим через фейковый архив.

    `installer.unpack` умеет копировать одиночный файл, но `install` ждёт
    архив. Проще всего собрать временный zip — тогда путь распаковки тот же,
    что и у остальных источников, и zip-slip-защита остаётся в силе.
    """
    import zipfile
    tmp = staging.parent / f"{staging.name}.bundle.zip"
    if tmp.exists():
        tmp.unlink()
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for p in staging.rglob("*"):
            if p.is_file() and p.name not in (mf.MANIFEST_NAME, mf.COMPLETE_MARKER):
                z.write(p, p.relative_to(staging).as_posix())
    return tmp


def _author_from_source(source: str, asset_id: str) -> str:
    """Автор из адаптера. Нужен для CC-BY: без него установка блокируется.

    Ошибку не глотаем молча: пустой автор для ассета под CC-BY означает, что
    установка будет отклонена на проверке атрибуции, и причина должна попасть
    в лог, иначе разбираться придётся по симптому «установка запрещена» без
    объяснения.
    """
    a = reg.adapter_for(source)
    if a is None:
        return ""
    try:
        return a.inspect(asset_id).author or ""
    except Exception as e:  # noqa: BLE001
        _audit("author_lookup_failed", {"source": source, "id": asset_id},
               f"{type(e).__name__}: {e}", False)
        return ""


@mcp.tool()
def asset_remove(pack: str, confirm: bool = False) -> str:
    """Удалить установленный внешний пакет из проекта.

    Удаляется только содержимое res://assets/external/<pack>/ вместе с его
    asset.json, поэтому «сироты» с неопределённой лицензией остаться не могут.

    Args:
        pack: имя пакета (см. `asset_list`).
        confirm: обязательное подтверждение. Удаление необратимо.
    """
    if not confirm:
        return _err(
            f"удаление '{pack}' требует confirm=True",
            hint="Это необратимая операция. Спроси пользователя и повтори.",
        )
    try:
        result = installer.remove(_sanitize(pack))
    except (installer.InstallDenied, PathDenied) as e:
        return _err(str(e))
    except Exception as e:  # noqa: BLE001
        return _err(f"удаление не удалось: {type(e).__name__}: {e}")

    state = _load_state()
    state["assets"] = [a for a in state.get("assets", [])
                       if a.get("pack") != result.get("removed")]
    _save_state(state)
    _audit("asset_remove", {"pack": pack}, f"удалён {result.get('path')}", True)
    return _ok(**result)


# ==========================================================================
# СОСТОЯНИЕ
# ==========================================================================

@mcp.tool()
def asset_list() -> str:
    """Что уже установлено в проект: пакеты, лицензии, авторы.

    Читается из манифестов под res://assets/external/, а не из кэша: истина —
    файловая система проекта. Кэш нужен только для `asset_search`/дедупликации.
    """
    try:
        root = installer.external_root()
    except installer.InstallDenied as e:
        return _err(str(e))

    entries = mf.scan(root)
    packs = []
    needs_attr: list[str] = []
    for e in entries:
        verdict = licenses.evaluate(e.get("license"))
        item = {
            "pack": e.get("_pack_dir"),
            "name": e.get("name"),
            "source": e.get("source"),
            "license": verdict.license,
            "author": e.get("author") or "",
            "sha256": e.get("sha256") or "",
            "installed_at": e.get("downloaded_at") or "",
            "attribution_required": verdict.attribution_required,
            "attribution_ready": bool(
                (e.get("author") or "").strip() and (e.get("source_url") or "").strip()
            ),
        }
        packs.append(item)
        if verdict.attribution_required and not item["attribution_ready"]:
            needs_attr.append(str(item["pack"]))

    payload = {
        "root": f"res://{installer.EXTERNAL_SUBDIR}",
        "count": len(packs),
        "packs": packs,
    }
    if needs_attr:
        payload["attribution_missing"] = needs_attr
        payload["attribution_hint"] = (
            "У этих пакетов лицензия требует атрибуции, но автор не записан. "
            "Добавь экран благодарностей или титры со ссылками на авторов."
        )
    if not packs:
        payload["hint"] = ("Внешних ассетов нет. Найди через asset_search, "
                           "скачай asset_download, поставь asset_install.")
    return _ok(**payload)


@mcp.tool()
def asset_manifest(pack: str) -> str:
    """Манифест одного установленного пакета: лицензия, автор, sha256, файлы.

    Нужен, когда важно доказать происхождение ассета — например, для раздела
    атрибуции или при проверке перед публикацией игры.

    Args:
        pack: имя пакета (см. `asset_list`).
    """
    try:
        root = installer.external_root()
        pack_dir = (root / _sanitize(pack)).resolve()
        pack_dir.relative_to(root.resolve())
    except (installer.InstallDenied, PathDenied, Exception) as e:  # noqa: BLE001
        return _err(str(e))

    entry = mf.read(pack_dir)
    if entry is None:
        return _err(f"манифест не найден: res://{installer.EXTERNAL_SUBDIR}/{pack}/"
                    f"{mf.MANIFEST_NAME}")
    entry = dict(entry)
    entry["_pack_dir"] = _sanitize(pack)
    entry["_path"] = f"res://{installer.EXTERNAL_SUBDIR}/{_sanitize(pack)}"

    # список файлов, которые реально лежат в пакете, — манифест мог остаться
    # от прежней версии, а файлов на диске уже нет
    entry["_files"] = sorted(
        p.relative_to(pack_dir).as_posix()
        for p in pack_dir.rglob("*") if p.is_file()
    )[:200]
    return _ok(**entry)


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
