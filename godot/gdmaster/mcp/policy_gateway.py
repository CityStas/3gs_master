"""Godot Policy Gateway — единственный MCP-сервер, который видит LLM.

Архитектурная роль (§24 спеки): между агентом и реальными серверами
(godot, rag, assets) стоит прокси, который

  * поднимает дочерние MCP-серверы по stdio;
  * фильтрует `tools/list` по allowlist — модель физически не видит
    инструментов, которых нет в списке;
  * фильтрует `tools/call` — вызов неразрешённого имени возвращает TOOL_DENIED;
  * пишет audit log каждого вызова;
  * не даёт достучаться ни до чего, кроме Godot, локального RAG и — если
    возможностью решили воспользоваться — внешних ассетов.

Даже prompt injection из файлов проекта не может добавить capability:
набор инструментов фиксирован в коде гейтвея, а не в промпте.
"""
from __future__ import annotations

import json
import os
import sys
import time
from contextlib import AsyncExitStack
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import mcp.types as types  # noqa: E402
from mcp import ClientSession, StdioServerParameters  # noqa: E402
from mcp.client.stdio import stdio_client  # noqa: E402
from mcp.server.lowlevel import Server  # noqa: E402
from mcp.server.stdio import stdio_server  # noqa: E402

from gdmaster import config  # noqa: E402

AUDIT_LOG = config.LOGS_DIR / "policy_audit.jsonl"

# --------------------------------------------------------------------------
# ALLOWLIST. Единственное место, где описан tool surface агента.
# --------------------------------------------------------------------------
ALLOWED_TOOLS: set[str] = {
    # RAG
    "rag_search",
    "rag_status",
    # Godot: инспекция
    "godot_project_info",
    "godot_list_files",
    "godot_read_file",
    "godot_scene_tree",
    "godot_script_symbols",
    "godot_find_symbol",
    # Godot: мутации
    "godot_write_script",
    "godot_patch_script",
    "godot_scene_create",
    "godot_scene_add_node",
    "godot_scene_remove_node",
    "godot_scene_set_property",
    "godot_scene_attach_script",
    "godot_scene_connect_signal",
    # Godot: настройки проекта
    "godot_input_action_add",
    "godot_project_init",
    # Godot: валидация/runtime
    "godot_validate",
    "godot_run_scene",
    # Godot: показать человеку (окно на экране)
    "godot_play_scene",
    "godot_stop_play",
    "godot_check_project",
}

# --------------------------------------------------------------------------
# ЛОКАЛЬНАЯ ГЕНЕРАЦИЯ АССЕТОВ — ПЕРВЫЙ ЭШЕЛОН, включён всегда.
# Сервер тот же, что у Three (threejs/mcp/assets_mcp_server.py): z-image через
# sd-server :8687, Qwen-Image и BiRefNet через ComfyUI :8188, Real-ESRGAN,
# Pixal3D/TRELLIS.2. Файлы кладутся в <проект Godot>/assets/ (THREE_PROJECT_ASSET_ROOT).
# Поэтому имена здесь совпадают с Three-инструментами.
# --------------------------------------------------------------------------
GEN_TOOLS: set[str] = {
    "asset_generate_pack",
    "assets_scheduler",
    "assets_status",
    "asset_image",
    "asset_edit",
    "asset_remove_bg",
    "asset_to_3d",
    "asset_character",
    "comfy_control",
}
# NB: `asset_list` есть и у генерации, и у веб-набора. Гейтвей маршрутизирует по
# имени, поэтому в GEN_TOOLS его нет: `asset_list` относится к веб-набору и
# доступен только при GDM_ENABLE_ASSET_TOOLS=1.

#: Каталог ассетов внутри Godot-проекта (аналог public/assets у Three).
GODOT_PROJECT_ASSET_ROOT = "assets"

# --------------------------------------------------------------------------
# ВНЕШНИЕ АССЕТЫ — ВТОРОЙ ЭШЕЛОН. Вызывать только если локальной генерации
# не хватает И есть доступ в интернет. Набор восьми asset_* — отдельный,
# осознанно включаемый.
#
# Зачем разделение. Знания о том, как скачивать ассеты, недостаточно: пока
# имён нет в ALLOWED_TOOLS, сетевой capability у модели отсутствует физически
# (§07_gdmaster_integration.md, слой 2). Набор собран, но выключен, и это
# видно в коде одной константой, а не спрятано в тексте промпта.
#
# Включение — РЕШЕНИЕ, а не техническая мелочь: у модели появляется выход в
# интернет и запись бинарников в проект. Поэтому переключатель один и явный.
# --------------------------------------------------------------------------
ASSET_TOOLS: set[str] = {
    "asset_search",
    "asset_inspect",
    "asset_license",
    "asset_download",
    "asset_install",
    "asset_remove",
    "asset_list",
    "asset_manifest",
}

#: Включить внешние ассеты. `GDM_ENABLE_ASSET_TOOLS=1` в окружении.
#: По умолчанию выключено: собрано, но не включено.
ASSETS_ENABLED: bool = os.environ.get("GDM_ENABLE_ASSET_TOOLS", "").strip() in ("1", "true", "yes")

#: Итоговый tool surface. Здесь и только здесь он собирается.
EFFECTIVE_TOOLS: set[str] = ALLOWED_TOOLS | GEN_TOOLS | (ASSET_TOOLS if ASSETS_ENABLED else set())

# Операции, которые считаются необратимо-разрушительными и логируются отдельно.
DESTRUCTIVE_TOOLS = {"godot_scene_remove_node", "godot_check_project", "asset_remove"}

PY = sys.executable


def _children() -> list[tuple[str, StdioServerParameters]]:
    env = dict(os.environ)
    env["PYTHONPATH"] = str(config.GDM_HOME)
    env["PYTHONUNBUFFERED"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"
    kids = [
        ("godot", StdioServerParameters(
            command=PY, args=["-m", "gdmaster.mcp.godot_mcp_server"], env=env)),
        ("rag", StdioServerParameters(
            command=PY, args=["-m", "gdmaster.mcp.rag_mcp_server"], env=env)),
    ]
    # Локальная генерация (первый эшелон) — всегда. Это тот же сервер, что у Three:
    # корень репозитория в PYTHONPATH, вывод в <проект Godot>/assets/.
    gen_env = dict(env)
    gen_env["PYTHONPATH"] = os.pathsep.join(
        [str(config.GDM_HOME.parent), str(config.GDM_HOME)])
    gen_env["THREE_PROJECT_ASSET_ROOT"] = GODOT_PROJECT_ASSET_ROOT
    kids.append(("gen", StdioServerParameters(
        command=PY, args=["-m", "threejs.mcp.assets_mcp_server"], env=gen_env)))
    # Веб-ассеты (второй эшелон) поднимаются ТОЛЬКО при включённом наборе:
    # выключенная возможность не должна даже запускать сетевой код.
    if ASSETS_ENABLED:
        kids.append(("assets", StdioServerParameters(
            command=PY, args=["-m", "gdmaster.mcp.asset_mcp_server"], env=env)))
    return kids


def _audit(event: str, **kw) -> None:
    try:
        with AUDIT_LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": time.time(), "event": event, **kw},
                               ensure_ascii=False)[:2000] + "\n")
    except OSError:
        pass


class Gateway:
    def __init__(self) -> None:
        self.sessions: dict[str, ClientSession] = {}
        self.tool_owner: dict[str, str] = {}
        self.tools: list[types.Tool] = []
        self._stack: AsyncExitStack | None = None
        self.startup_errors: list[str] = []

    async def start(self) -> None:
        self._stack = AsyncExitStack()
        for name, params in _children():
            try:
                read, write = await self._stack.enter_async_context(stdio_client(params))
                session = await self._stack.enter_async_context(ClientSession(read, write))
                await session.initialize()
                self.sessions[name] = session
                listed = await session.list_tools()
                for t in listed.tools:
                    if t.name not in EFFECTIVE_TOOLS:
                        continue  # сервер отдал лишнее — не пропускаем
                    # Дочерние FastMCP-тулы объявляют outputSchema (вывод из аннотации
                    # `-> str`). Гейтвей возвращает обычный текстовый контент, поэтому
                    # схему не переобъявляем — иначе SDK требует structuredContent и
                    # падает с "outputSchema defined but no structured output returned".
                    self.tools.append(types.Tool(
                        name=t.name,
                        title=t.title,
                        description=t.description,
                        inputSchema=t.inputSchema,
                        annotations=t.annotations,
                    ))
                    self.tool_owner[t.name] = name
            except Exception as e:  # noqa: BLE001
                self.startup_errors.append(f"{name}: {e}")
                _audit("child_start_failed", child=name, error=str(e))
        _audit("gateway_started", tools=sorted(self.tool_owner), errors=self.startup_errors)

    async def stop(self) -> None:
        if self._stack:
            await self._stack.aclose()

    async def call(self, name: str, arguments: dict) -> list[types.ContentBlock]:
        if name not in EFFECTIVE_TOOLS:
            _audit("tool_denied", tool=name, reason="not in allowlist")
            # Отдельно объясняем выключенный набор: «нет в списке» и «есть,
            # но выключено» — разные причины, и агент должен уметь сказать
            # пользователю, что именно надо изменить (§07, «что делать»).
            reason = "not in allowlist"
            message = f"Инструмент '{name}' вне разрешённой Godot-only границы."
            if name in ASSET_TOOLS:
                reason = "asset tools disabled"
                message = (
                    f"Инструмент '{name}' существует, но набор внешних ассетов "
                    f"выключен. Включение — решение пользователя: переменная "
                    f"GDM_ENABLE_ASSET_TOOLS=1 в окружении лаунчера. Знания о "
                    f"скачивании ассетов при этом уже загружены — нехватка "
                    f"именно возможности, а не знания."
                )
            return [types.TextContent(type="text", text=json.dumps({
                "ok": False, "error": "TOOL_DENIED", "reason": reason,
                "message": message,
                "allowed": sorted(EFFECTIVE_TOOLS),
            }, ensure_ascii=False, indent=1))]
        owner = self.tool_owner.get(name)
        if owner is None:
            _audit("tool_unavailable", tool=name)
            return [types.TextContent(type="text", text=json.dumps({
                "ok": False, "error": "TOOL_UNAVAILABLE",
                "message": f"Сервер-владелец инструмента '{name}' не запустился.",
                "startup_errors": self.startup_errors,
            }, ensure_ascii=False, indent=1))]
        t0 = time.time()
        try:
            result = await self.sessions[owner].call_tool(name, arguments or {})
        except Exception as e:  # noqa: BLE001
            _audit("tool_error", tool=name, error=str(e))
            return [types.TextContent(type="text", text=json.dumps({
                "ok": False, "error": "TOOL_EXECUTION_FAILED", "message": str(e),
            }, ensure_ascii=False, indent=1))]
        _audit("tool_call", tool=name, owner=owner, ms=int((time.time() - t0) * 1000),
               destructive=name in DESTRUCTIVE_TOOLS)
        out: list[types.ContentBlock] = []
        for block in result.content:
            if isinstance(block, types.TextContent):
                out.append(types.TextContent(type="text", text=block.text))
            elif isinstance(block, types.ImageContent):
                out.append(block)
            elif isinstance(block, types.EmbeddedResource):
                out.append(block)
            else:
                out.append(types.TextContent(type="text", text=str(block)))
        if result.isError and out and isinstance(out[0], types.TextContent):
            out[0] = types.TextContent(type="text", text=out[0].text)
        return out or [types.TextContent(type="text", text=json.dumps({"ok": True}))]


async def _amain() -> None:
    gw = Gateway()
    server = Server("godot-policy")

    @server.list_tools()
    async def list_tools() -> list[types.Tool]:
        return gw.tools

    @server.call_tool()
    async def call_tool(name: str, arguments: dict) -> list[types.ContentBlock]:
        return await gw.call(name, arguments)

    await gw.start()
    try:
        async with stdio_server() as (read, write):
            await server.run(read, write, server.create_initialization_options())
    finally:
        await gw.stop()


def main() -> None:
    import anyio
    anyio.run(_amain)


if __name__ == "__main__":
    main()
