"""Читалка сессий pi: превращает JSONL-трейс в историю «запрос → ответ».

Зачем. Ответы модели УЖЕ логируются полностью — `pi-home/sessions/<проект>/*.jsonl`.
Писать рядом второй лог не нужно: это дублирование и рост диска (одна сессия
доходит до 260 КБ). Не хватало не записи, а ЧТЕНИЯ: чтобы разбирать прогон,
не копируя ответы из интерфейса pi руками.

Что достаётся из сессии (проверено на живых файлах):
  * `user`       — запрос;
  * `assistant`  — блоки `thinking` / `text` / `toolCall` (с аргументами),
                   плюс `usage` (input/output/cacheRead/totalTokens) и
                   `stopReason`;
  * `toolResult` — результат вызова и флаг `isError`;
  * служебные    — `session`, `model_change`, `thinking_level_change`.

Режимы:
    python tools/pi_logs.py                      последняя сессия, сводка
    python tools/pi_logs.py --list               список сессий
    python tools/pi_logs.py --session last       то же, что без аргументов
    python tools/pi_logs.py --session <путь>     конкретный файл
    python tools/pi_logs.py --out logs/h.md      сохранить историю в markdown
    python tools/pi_logs.py --errors-only        только ошибки и вызовы вокруг них
    python tools/pi_logs.py --thinking           показывать блоки thinking

Код возврата: 1, если в сессии были ошибки — удобно для скриптов.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

SESSIONS_DIR = ROOT / "pi-home" / "sessions"

#: Маркеры неудачи в тексте результата. `isError` выставляет не каждый сервер,
#: поэтому смотрим и на содержимое: наши MCP-инструменты возвращают
#: {"ok": false, "error": ...} обычным контентом, без флага ошибки.
_FAIL_MARKERS = ('"ok": false', '"ok":false', "TOOL_DENIED", "TOOL_UNAVAILABLE")

#: Маркеры ЛОЖНОГО УСПЕХА: инструмент отчитался `ok: true`, но значение
#: осталось пустым — то есть действие фактически не произошло. Так выглядел
#: прогон, где модель сказала «Сцена полностью рабочa!», а `mesh` у всех
#: MeshInstance3D был NULL: set() со строкой-путём молча ничего не делает.
#: Такие шаги НЕ попадают в счётчик ошибок, и без отдельной проверки провал
#: не виден ни модели, ни читалке логов.
_NO_EFFECT_MARKERS = ('"value": "<Object#null>"', '"value": null', '"value":null')
_OK_TRUE_RE = re.compile(r'"ok"\s*:\s*true')


@dataclass
class Step:
    """Один шаг диалога."""
    kind: str                    # user | assistant | toolResult | meta | compaction
    role: str = ""
    text: str = ""
    thinking: str = ""
    tool_calls: list[dict] = field(default_factory=list)
    tool_name: str = ""
    is_error: bool = False
    usage: dict = field(default_factory=dict)
    stop_reason: str = ""
    timestamp: str = ""
    tokens_before: int = 0       # только для kind="compaction"

    @property
    def tokens_in(self) -> int:
        return int(self.usage.get("input") or 0)

    @property
    def tokens_out(self) -> int:
        return int(self.usage.get("output") or 0)

    @property
    def tokens_cached(self) -> int:
        return int(self.usage.get("cacheRead") or 0)

    @property
    def tokens_total(self) -> int:
        return int(self.usage.get("totalTokens") or 0)


def list_sessions() -> list[Path]:
    if not SESSIONS_DIR.exists():
        return []
    return sorted(SESSIONS_DIR.glob("*/*.jsonl"), key=lambda p: p.stat().st_mtime)


def parse_session(path: Path) -> tuple[dict, list[Step]]:
    """Прочитать сессию. Битые/недописанные строки пропускаются.

    Это не «на всякий случай»: пока модель работает, файл дописывается, и
    последняя строка может оказаться обрезанной. Падать на этом нельзя —
    иначе читалка ломается ровно тогда, когда нужна.
    """
    meta: dict = {}
    steps: list[Step] = []

    with path.open(encoding="utf-8", errors="replace") as f:
        for raw in f:
            raw = raw.strip()
            if not raw:
                continue
            try:
                d = json.loads(raw)
            except json.JSONDecodeError:
                continue

            t = d.get("type")
            if t == "session":
                meta = d
                continue
            if t in ("model_change", "thinking_level_change"):
                steps.append(Step(kind="meta", text=t, timestamp=d.get("timestamp", "")))
                continue
            # Запись компакции — отдельный тип, а не message. Раньше она молча
            # отбрасывалась, и читалка показывала «компакций 0» даже когда
            # компакция была. Считаем по факту, а не по эвристике на токенах.
            if t == "compaction":
                steps.append(Step(
                    kind="compaction",
                    text=d.get("summary") or "",
                    tokens_before=int(d.get("tokensBefore") or 0),
                    timestamp=d.get("timestamp", ""),
                ))
                continue
            if t != "message":
                continue

            m = d.get("message") or {}
            role = m.get("role") or "?"
            content = m.get("content")
            blocks = content if isinstance(content, list) else (
                [{"type": "text", "text": content}] if isinstance(content, str) else [])

            st = Step(kind=role, role=role, timestamp=m.get("timestamp", ""),
                      usage=m.get("usage") or {},
                      stop_reason=m.get("stopReason") or "",
                      is_error=bool(m.get("isError")))

            texts, thinks = [], []
            for b in blocks:
                if not isinstance(b, dict):
                    continue
                bt = b.get("type")
                if bt == "text":
                    texts.append(b.get("text") or "")
                elif bt == "thinking":
                    thinks.append(b.get("thinking") or b.get("text") or "")
                elif bt == "toolCall":
                    st.tool_calls.append({
                        "name": b.get("name") or "",
                        "arguments": b.get("arguments") or {},
                    })

            st.text = "\n".join(x for x in texts if x).strip()
            st.thinking = "\n".join(x for x in thinks if x).strip()

            if role == "toolResult":
                st.tool_name = m.get("toolName") or ""
                if not st.is_error and any(k in st.text for k in _FAIL_MARKERS):
                    st.is_error = True
            if role == "assistant" and not st.text and st.tool_calls:
                st.text = ""

            steps.append(st)
    return meta, steps


def summarize(meta: dict, steps: list[Step]) -> dict:
    """Сводка для быстрого разбора: сколько шагов, ошибок, токенов."""
    assistant = [s for s in steps if s.kind == "assistant"]
    results = [s for s in steps if s.kind == "toolResult"]
    errors = [s for s in results if s.is_error]

    calls: list[str] = []
    for s in assistant:
        calls.extend(c["name"] for c in s.tool_calls)

    # повтор одного и того же вызова с теми же аргументами — признак того,
    # что модель зациклилась (или не поняла отказ)
    seen: dict[str, int] = {}
    for s in assistant:
        for c in s.tool_calls:
            key = f"{c['name']}{json.dumps(c['arguments'], sort_keys=True, ensure_ascii=False)}"
            seen[key] = seen.get(key, 0) + 1
    repeats = {k: v for k, v in seen.items() if v > 1}

    # компакции — по фактическим записям, а не по эвристике
    compactions = [s for s in steps if s.kind == "compaction"]

    # ложные успехи: ok:true при пустом значении. Считаем отдельно от ошибок —
    # это не отказ инструмента, а НЕЗАМЕЧЕННЫЙ провал, и именно он даёт
    # отчёт «всё готово» при пустой сцене.
    false_successes: list[str] = []
    for s in results:
        if s.is_error or not s.text:
            continue
        if any(m in s.text for m in _NO_EFFECT_MARKERS) and _OK_TRUE_RE.search(s.text):
            false_successes.append(s.tool_name or "?")

    # запасной сигнал: падение totalTokens относительно предыдущего шага.
    # Держим отдельно — если он срабатывает, а записей компакции нет, значит
    # контекст «сбросился» по какой-то другой причине и это надо разбирать.
    peak = max((s.tokens_total for s in assistant), default=0)
    drops = sum(1 for a, b in zip(assistant, assistant[1:])
                if a.tokens_total and b.tokens_total and b.tokens_total < a.tokens_total * 0.6)

    return {
        "session_id": meta.get("id", ""),
        "steps": len(steps),
        "assistant_steps": len(assistant),
        "tool_calls": len(calls),
        "tools_used": sorted(set(calls)),
        "errors": len(errors),
        "error_tools": [s.tool_name for s in errors if s.tool_name],
        "false_successes": false_successes,
        "repeated_calls": repeats,
        "peak_context_tokens": peak,
        "compactions": len(compactions),
        "compaction_tokens_before": [s.tokens_before for s in compactions],
        "compactions_suspected": drops,
        "tokens_out_total": sum(s.tokens_out for s in assistant),
        "thinking_chars": sum(len(s.thinking) for s in steps),
    }


def _fmt_usage(s: Step) -> str:
    if not s.usage:
        return ""
    return (f"in={s.tokens_in} out={s.tokens_out} "
            f"cache={s.tokens_cached} total={s.tokens_total}")


def render(meta: dict, steps: list[Step], *, full: bool = True,
           thinking: bool = False, errors_only: bool = False) -> str:
    """История в markdown. Ошибки помечаются явно — их и ищут глазами."""
    out: list[str] = []
    w = out.append

    w("# История прогона pi")
    w("")
    if meta:
        w(f"- session: `{meta.get('id', '?')}`")
        w(f"- started: `{meta.get('timestamp', '?')}`")
    w("")

    summ = summarize(meta, steps)
    w("## Сводка")
    w("")
    w("| Метрика | Значение |")
    w("|---|---|")
    w(f"| шагов всего | {summ['steps']} |")
    w(f"| ответов модели | {summ['assistant_steps']} |")
    w(f"| вызовов инструментов | {summ['tool_calls']} |")
    w(f"| **ошибок** | **{summ['errors']}** |")
    if summ["false_successes"]:
        w(f"| **ложных успехов** | **{len(summ['false_successes'])}** |")
    w(f"| пик контекста | {summ['peak_context_tokens']} токенов |")
    w(f"| сгенерировано токенов | {summ['tokens_out_total']} |")
    w(f"| объём thinking | {summ['thinking_chars']} символов |")
    w(f"| компакций | {summ['compactions']} |")
    if summ["compaction_tokens_before"]:
        w(f"| контекст до компакции | {', '.join(str(t) for t in summ['compaction_tokens_before'])} |")
    w(f"| подозрений на компакцию | {summ['compactions_suspected']} |")
    w("")
    if summ["tools_used"]:
        w(f"Инструменты: {', '.join(f'`{t}`' for t in summ['tools_used'])}")
        w("")
    if summ["repeated_calls"]:
        w("**Повторяющиеся вызовы** (один и тот же инструмент с теми же аргументами):")
        for k, n in sorted(summ["repeated_calls"].items(), key=lambda kv: -kv[1]):
            w(f"- ×{n} `{k[:150]}`")
        w("")
    if summ["false_successes"]:
        w("**Ложные успехи** — инструмент вернул `ok: true`, но значение осталось пустым,")
        w("то есть действие не произошло. В счётчик ошибок такие шаги не попадают,")
        w("поэтому модель считает работу сделанной, а результат пустой:")
        for name in summ["false_successes"]:
            w(f"- `{name}`")
        w("")

    w("---")
    w("")
    w("## Ход диалога")
    w("")

    step_no = 0
    for s in steps:
        if s.kind == "meta":
            w(f"`[{s.text}]`")
            w("")
            continue

        if s.kind == "compaction":
            w("---")
            w("")
            w(f"### ⟳ КОМПАКЦИЯ КОНТЕКСТА  `было {s.tokens_before} токенов`")
            w("")
            w("<details><summary>сводка, которую модель получила вместо истории</summary>")
            w("")
            w("```")
            w(s.text or "(пусто)")
            w("```")
            w("")
            w("</details>")
            w("")
            w("---")
            w("")
            continue

        if s.kind == "user":
            step_no += 1
            w(f"### {step_no}. ЗАПРОС")
            w("")
            w("```")
            w(s.text or "(пусто)")
            w("```")
            w("")
            continue

        if s.kind == "assistant":
            step_no += 1
            u = _fmt_usage(s)
            w(f"### {step_no}. ОТВЕТ МОДЕЛИ" + (f"  `{u}`" if u else ""))
            w("")
            if thinking and s.thinking:
                w("<details><summary>thinking</summary>")
                w("")
                w("```")
                w(s.thinking[:4000])
                w("```")
                w("")
                w("</details>")
                w("")
            if s.text:
                w(s.text)
                w("")
            for c in s.tool_calls:
                args = json.dumps(c["arguments"], ensure_ascii=False)
                w(f"→ **`{c['name']}`** `{args}`")
                w("")
            if s.stop_reason:
                w(f"`stopReason: {s.stop_reason}`")
                w("")
            continue

        if s.kind == "toolResult":
            step_no += 1
            if errors_only and not s.is_error:
                continue
            flag = " ❌ ОШИБКА" if s.is_error else " ✅"
            w(f"### {step_no}. РЕЗУЛЬТАТ `{s.tool_name or '?'}`{flag}")
            w("")
            body = s.text if full else (s.text[:600] + ("…" if len(s.text) > 600 else ""))
            w("```json")
            w(body or "(пусто)")
            w("```")
            w("")
            continue

    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="История запросов и ответов модели из сессий pi")
    ap.add_argument("--session", default="last",
                    help="'last' (по умолчанию), 'all' или путь к .jsonl")
    ap.add_argument("--out", default="", help="сохранить в файл (markdown)")
    ap.add_argument("--list", action="store_true", help="показать список сессий")
    ap.add_argument("--thinking", action="store_true", help="включить блоки thinking")
    ap.add_argument("--errors-only", action="store_true",
                    help="только ошибки и их контекст")
    ap.add_argument("--brief", action="store_true", help="обрезать длинные результаты")
    args = ap.parse_args()

    sessions = list_sessions()
    if not sessions:
        print(f"Сессий не найдено в {SESSIONS_DIR}")
        return 1

    if args.list:
        for p in sessions:
            size = p.stat().st_size
            print(f"  {p.parent.name}/{p.name}  ({size/1024:.0f} КБ)")
        return 0

    if args.session == "all":
        targets = sessions
    elif args.session == "last":
        targets = [sessions[-1]]
    else:
        targets = [Path(args.session)]

    chunks: list[str] = []
    any_error = False
    for path in targets:
        if not path.exists():
            print(f"Нет файла: {path}")
            return 1
        meta, steps = parse_session(path)
        summ = summarize(meta, steps)
        if summ["errors"]:
            any_error = True

        if not args.out:
            # в консоль — сводка, полный текст только при явном запросе
            print(f"\n=== {path.name} ===")
            print(f"  шагов: {summ['steps']} | ответов: {summ['assistant_steps']} | "
                  f"вызовов: {summ['tool_calls']} | ОШИБОК: {summ['errors']}")
            print(f"  пик контекста: {summ['peak_context_tokens']} токенов | "
                  f"out: {summ['tokens_out_total']}")
            if summ["error_tools"]:
                print(f"  упавшие инструменты: {', '.join(summ['error_tools'])}")
            if summ["repeated_calls"]:
                for k, n in sorted(summ["repeated_calls"].items(), key=lambda kv: -kv[1]):
                    print(f"  повтор ×{n}: {k[:110]}")
            if not args.out and (args.errors_only or args.thinking or args.brief):
                print()
                print(render(meta, steps, full=not args.brief,
                             thinking=args.thinking, errors_only=args.errors_only))
        else:
            chunks.append(render(meta, steps, full=not args.brief,
                                 thinking=args.thinking, errors_only=args.errors_only))

    if args.out:
        out_path = Path(args.out)
        if not out_path.is_absolute():
            out_path = ROOT / out_path
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text("\n\n---\n\n".join(chunks), encoding="utf-8")
        print(f"Записано: {out_path}  ({out_path.stat().st_size/1024:.0f} КБ)")

    return 1 if any_error else 0


if __name__ == "__main__":
    raise SystemExit(main())
