@echo off
setlocal
rem --- shared paths (GS_ROOT, GS_PROJECTS, PY, NO_PROXY) come from one place ----
call "%~dp0cmd\_env.cmd"
set "PY=%GS_ROOT%.venv\Scripts\python.exe"
if not exist "%PY%" (
  echo [ERROR] Python venv not found: "%PY%"
  echo Create it with:  python -m venv .venv
  exit /b 1
)


rem === 3GS STUDIO — ОДИН ФАЙЛ, ОДИН ДВОЙНОЙ ЩЕЛЧОК =======================
rem --- Студия стартует ПУСТОЙ: без проекта, без консольного меню, без моделей.
rem --- Интерфейс показывает ТОЛЬКО проекты из projects\three\ (это редактор
rem --- three.js-сцен). Здесь же, в UI, можно создать НОВЫЙ проект — студия
rem --- сам разложит канонический стек в projects\three\<имя>.
rem --- После выбора сервер переключает корень на живом соединении и студия
rem --- полностью инициализирует выбранный проект.
rem ---
rem ---   studio.cmd                       пустая студия + выбор проекта в UI
rem ---   studio.cmd three/my_game         (совместимость) сразу открыть проект
rem ---   studio.cmd three/my_game 8788    другой порт
rem ---   studio.cmd --models              + модели для консольного агента pi
rem ---
rem --- Ничего не создаётся: студия только открывает то, что уже лежит в
rem --- projects\. Скелет раскладывает cmd\init.cmd, и только по явной просьбе.
rem --- Сервер (:8777) — ребёнок этого окна: один Ctrl+C гасит всё.
rem --- Подробности: tools\studio.py, tools\web\serve.py (флаг --hub).

"%PY%" "%GS_ROOT%tools\studio.py" %*
set "RC=%errorlevel%"

rem --- Keep the window open on failure: a double click would otherwise close it
rem --- before the error could be read. A normal Ctrl+C exit closes it.
if not "%RC%"=="0" (
  echo.
  echo Exit code: %RC%
  pause
)
exit /b %RC%
