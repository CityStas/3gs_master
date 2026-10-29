#!/usr/bin/env python3
"""Нарезка character-sheet на 4 вида под `Pixal3DMultiViewConditioning`.

Зачем отдельный инструмент. Multiview-нода жёстко требует двух вещей, и обе
ломаются тихо - меш просто выходит перекошенным, без единой ошибки в логе:

1. **Квадрат**, объект на альфе или на чёрном, ~1/1.1 кадра по широкой стороне.
2. **Одинаковый масштаб во всех видах.** Это главное. Если резать каждую
   панель по её собственному bounding box, вид спереди (широкий) и вид сбоку
   (узкий) отмасштабируются по-разному, и нода, которая считает, что все камеры
   стоят на одной орбите, получит четыре разных масштаба. Меш выходит сплющенным.

Общим должен быть **масштаб**, а не прямоугольник. Разница видна на числах: у
нашего листа вертикальные центры панелей совпали до пикселя (268..269), а
горизонтальные разъехались на 184..290. Если применить ко всем один и тот же
прямоугольник, профиль (центр 184) окажется в кадре слева, а не по центру - это
боковой сдвиг камеры на ~15 % кадра, то есть ровно то рассогласование, из-за
которого меш выходит перекошенным. Поэтому сторона кропа общая (максимум по
панелям), а центрируется каждая панель по своему содержимому. Масштаб остаётся
общим по построению, а объект в каждом виде - в центре.

    python tools/split_sheet.py sheet.png                  # 1x4 -> view_*.png рядом
    python tools/split_sheet.py sheet.png --layout 2x2
    python tools/split_sheet.py sheet.png --out assets/3d/views
    python tools/split_sheet.py sheet.png --align union    # старый режим: один прямоугольник
    python tools/split_sheet.py sheet.png --dry-run        # только показать боксы

Порядок панелей слева-направо (сверху-вниз для 2x2) - это порядок `--order`,
по умолчанию `front,left,back,right`. Первый вид становится «передом», к
которому нода ставит меш, так что порядок - это контракт, а не украшение.

Код возврата 1, если лист не удалось разобрать (нет содержимого, панели не
квадратные и т.п.).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:  # pragma: no cover - Pillow есть в .venv проекта
    raise SystemExit("нужен Pillow: ./.venv/Scripts/python.exe -m pip install Pillow")

#: Панели идут в этом порядке, если пользователь не переопределил `--order`.
DEFAULT_ORDER = ["front", "left", "back", "right"]
#: Запас вокруг объекта. 1.1 - ровно то, что ждёт нода («объект занимает ~1/1.1»).
DEFAULT_PAD = 1.1


def _content_bbox(panel: Image.Image, black_threshold: int = 8) -> tuple[int, int, int, int] | None:
    """Bounding box содержимого панели.

    Альфа, если она есть и не полностью непрозрачная; иначе - не-чёрные пиксели
    (пайплайн кладёт объект на чёрный фон, `ImageCropToMask.background`).
    """
    if panel.mode in ("RGBA", "LA"):
        alpha = panel.getchannel("A")
        if alpha.getextrema()[0] < 255:
            return alpha.getbbox()
    rgb = panel.convert("RGB")
    # getbbox() у Pillow считает по непустым (не 0,0,0) пикселям только для L/1;
    # для RGB используем point() как бинаризацию по порогу.
    mask = rgb.convert("L").point(lambda v: 255 if v > black_threshold else 0)
    return mask.getbbox()


def _split(panel_source: Image.Image, cols: int, rows: int) -> list[Image.Image]:
    w, h = panel_source.size
    if w % cols or h % rows:
        # Не фатально: последний пиксель уйдёт в округление. Предупреждаем, потому
        # что неровная сетка - это почти всегда не тот лист, что имелся в виду.
        print(f"! {w}x{h} не делится на {cols}x{rows} нацело - панели будут неровными", file=sys.stderr)
    pw, ph = w // cols, h // rows
    panels = []
    for r in range(rows):
        for c in range(cols):
            panels.append(panel_source.crop((c * pw, r * ph, (c + 1) * pw, (r + 1) * ph)))
    return panels


def _common_crop_box(boxes: list[tuple[int, int, int, int]], pad: float) -> tuple[int, int, int, int]:
    """Один общий прямоугольник на все панели: объединение содержимого + запас.

    Оставлен для `--align union`. Годится, только если генератор поставил все
    фигуры в одну и ту же точку кадра; на реальных листах это не так (у нас
    горизонтальные центры разъехались на 106 px), и тогда профиль уезжает к краю.
    """
    x0 = min(b[0] for b in boxes)
    y0 = min(b[1] for b in boxes)
    x1 = max(b[2] for b in boxes)
    y1 = max(b[3] for b in boxes)
    w, h = x1 - x0, y1 - y0
    side = max(w, h)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    half = side * pad / 2
    return (round(cx - half), round(cy - half), round(cx + half), round(cy + half))


def _centred_boxes(boxes: list[tuple[int, int, int, int]],
                   pad: float) -> list[tuple[int, int, int, int]]:
    """Общая сторона кропа (масштаб) + индивидуальное центрирование по содержимому.

    Сторона берётся как максимум по панелям: так содержимое каждой панели заведомо
    влезает в свой кроп, а поскольку сторона одна и та же, масштаб у всех видов
    одинаковый. Центр - свой у каждой панели, поэтому объект стоит в кадре по
    центру независимо от того, куда его поставил генератор.
    """
    side = max(max(b[2] - b[0], b[3] - b[1]) for b in boxes)
    half = side * pad / 2
    out = []
    for b in boxes:
        cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
        out.append((round(cx - half), round(cy - half), round(cx + half), round(cy + half)))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Нарезать character-sheet на виды для Pixal3D multiview.")
    ap.add_argument("sheet", help="PNG-лист с видами (4 панели)")
    ap.add_argument("--layout", default="1x4", help="1x4 (в строку), 4x1 (в столбец) или 2x2")
    ap.add_argument("--order", default=",".join(DEFAULT_ORDER),
                    help="имена ВСЕХ панелей сетки по порядку (по умолчанию "
                         "front,left,back,right). --panels выбирает из них подмножество")
    ap.add_argument("--out", default="", help="каталог для view_*.png (по умолчанию <лист>-views/)")
    ap.add_argument("--pad", type=float, default=DEFAULT_PAD, help="запас вокруг объекта (1.1 = контракт ноды)")
    ap.add_argument("--align", choices=("center", "union"), default="center",
                    help="center: общий масштаб, каждый вид центрируется по своему "
                         "содержимому (по умолчанию). union: один общий прямоугольник на все")
    ap.add_argument("--size", type=int, default=1024, help="сторона выходного квадрата")
    ap.add_argument("--panels", default="",
                    help="подмножество панелей сетки, например 0,1,2 (по умолчанию все). "
                         "Нужно, когда один ракурс из листа негоден: нода принимает и "
                         "меньше четырёх видов, а подсунуть ей дубль хуже, чем пропустить - "
                         "она поставит дубль на свою орбитальную станцию и меш сплющится")
    ap.add_argument("--dry-run", action="store_true", help="только показать боксы, ничего не писать")
    args = ap.parse_args()

    sheet_path = Path(args.sheet).expanduser()
    if not sheet_path.is_file():
        print(f"нет файла: {sheet_path}", file=sys.stderr)
        return 1

    try:
        # `1x4` - это СТРОКА из четырёх панелей: сначала строки, потом столбцы.
        rows, cols = (int(v) for v in args.layout.lower().split("x"))
    except ValueError:
        print(f"плохой --layout '{args.layout}': ожидается вид 1x4, 4x1 или 2x2", file=sys.stderr)
        return 1

    total = cols * rows
    if args.panels:
        try:
            picked = [int(v) for v in args.panels.split(",") if v.strip() != ""]
        except ValueError:
            print(f"плохой --panels '{args.panels}': ожидается список номеров, например 0,1,2",
                  file=sys.stderr)
            return 1
        bad = [p for p in picked if not 0 <= p < total]
        if bad:
            print(f"--panels: номеров нет в раскладке {args.layout} ({total} панелей): {bad}",
                  file=sys.stderr)
            return 1
    else:
        picked = list(range(total))

    names = [n.strip() for n in args.order.split(",") if n.strip()]
    if len(names) != total:
        print(f"--order даёт {len(names)} имён, а раскладка {args.layout} - {total} панелей",
              file=sys.stderr)
        return 1
    names = [names[i] for i in picked]

    source = Image.open(sheet_path)
    source.load()
    panels = [_split(source, cols, rows)[i] for i in picked]
    print(f"панели сетки: {picked} из {total} -> виды {names}")

    boxes = []
    for i, name, panel in zip(picked, names, panels):
        box = _content_bbox(panel)
        if box is None:
            print(f"панель {i + 1} ({name}) пустая - нет ни альфы, ни не-чёрных пикселей",
                  file=sys.stderr)
            return 1
        boxes.append(box)

    if args.align == "union":
        crop_boxes = [_common_crop_box(boxes, args.pad)] * len(panels)
    else:
        crop_boxes = _centred_boxes(boxes, args.pad)
    print(f"лист        : {sheet_path.name}  {source.size[0]}x{source.size[1]}  {args.layout}")
    print(f"панели      : {', '.join(f'{n}={b}' for n, b in zip(names, boxes))}")
    side = crop_boxes[0][2] - crop_boxes[0][0]
    print(f"кроп        : сторона {side}px у всех видов (масштаб общий), "
          f"режим {args.align}")
    for n, b in zip(names, crop_boxes):
        print(f"  {n:<5s}: {b}")

    if args.dry_run:
        print("--dry-run: ничего не записано")
        return 0

    out_dir = Path(args.out).expanduser() if args.out else sheet_path.with_name(sheet_path.stem + "-views")
    out_dir.mkdir(parents=True, exist_ok=True)

    has_alpha = source.mode in ("RGBA", "LA")
    background = (0, 0, 0, 0) if has_alpha else (0, 0, 0)
    written = []
    for name, panel, box in zip(names, panels, crop_boxes):
        canvas = Image.new("RGBA" if has_alpha else "RGB", panel.size, background)
        canvas.paste(panel, (0, 0))
        crop = canvas.crop(box)
        crop = crop.resize((args.size, args.size), Image.LANCZOS)
        path = out_dir / f"view_{name}.png"
        crop.save(path)
        written.append(path)

    print(f"записано    : {len(written)} файлов в {out_dir}")
    for path in written:
        print(f"  {path.name}  {path.stat().st_size // 1024} КБ")
    print()
    print("дальше: передать их в порядке front,left,back,right:")
    print(f"  asset_to_3d_multiview {' '.join(p.name for p in written)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
