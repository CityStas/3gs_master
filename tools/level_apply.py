#!/usr/bin/env python3
"""Наложить ручные правки на `web3d/level.json` (родной уровень level_0).

Зачем отдельный инструмент, а не `level_build.py`: тот СОБИРАЕТ level_1 из
таблиц арта, а `level.json` больше ниоткуда не собирается — это и есть исходник.
Значит, для правок нужен не «сборщик с наложением», а «наложение и всё»:

    web3d/level_edit.json  --(этот скрипт)-->  web3d/level.json

Сам разбор конверта (`nodes` + `add` + `remove`) живёт в `tools/level_edits.py` и
общий с `level_build.py`: правки пишет один и тот же редактор, и вторая копия
логики разошлась бы с первой молча.

Идемпотентно: повторный запуск с теми же правками не меняет файл. Правки
накладываются на ЗАНОВО прочитанный level.json, поэтому «сбросить одну правку»
нельзя — удалите её из level_edit.json.

usage: python tools/level_apply.py [--check]
       --check — показать, что изменится, но не писать
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import level_edits  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEVEL = os.path.join(ROOT, "web3d", "level.json")
EDIT = os.path.join(ROOT, "web3d", "level_edit.json")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    if not os.path.isfile(LEVEL):
        sys.exit(f"нет {LEVEL} — сначала tools/level_native.py")
    if not os.path.isfile(EDIT):
        print("правок руками нет (web3d/level_edit.json не найден)")
        sys.exit(0)

    with open(LEVEL, encoding="utf-8") as fh:
        data = json.load(fh)
    with open(EDIT, encoding="utf-8") as fh:
        spec = json.load(fh)

    # Пустой `nodes` больше не значит «правок нет»: добавление и удаление живут в
    # отдельных секциях, и файл с одним лишь `remove` — совершенно нормальный.
    if not (spec.get("nodes") or spec.get("add") or spec.get("remove")):
        print("правок руками нет (файл пуст)")
        sys.exit(0)

    counts = level_edits.apply(data["tree"], spec, os.path.basename(EDIT))

    if a.check:
        print(f"будет применено: позиций {counts['nodes']} "
              f"(сдвинут {counts['moved']}), добавлено {counts['added']}, "
              f"обновлено {counts['updated']}, удалено {counts['removed']}")
        sys.exit(0)

    with open(LEVEL, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)

    print(f"level.json: позиций {counts['nodes']} (сдвинуто {counts['moved']}), "
          f"добавлено {counts['added']}, обновлено {counts['updated']}, "
          f"удалено {counts['removed']}")
    print(f"-> {LEVEL}")


if __name__ == "__main__":
    main()
