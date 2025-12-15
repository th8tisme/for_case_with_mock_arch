# Python entrypoint layouts

Набор примеров, показывающих разные схемы организации проекта и работы импортов.

## Схема 1. Скрипт без пакета
Директория: `arch_like_script`
- Запуск: `cd arch_like_script && python main.py`
- `sys.path[0]` указывает на директорию с `main.py`, поэтому импорты идут напрямую из соседних модулей.

## Схема 2. Пакет + внешний entrypoint
Директория: `arch_like_outer_entrypoint`
- Запуск: `cd arch_like_outer_entrypoint && python main.py`
- Пакет `project` импортируется из корня, а точка входа лежит рядом.

## Схема 3.A. Чистый пакет, запуск `python -m bot_tg.main`
Директория: `arch_like_package_dot_main`
- Запуск: `cd arch_like_package_dot_main && python -m bot_tg.main`
- Точка входа находится внутри пакета, используются обычные абсолютные или относительные импорты.

## Схема 3.B. Чистый пакет, запуск `python -m bot_tg`
Директория: `arch_like_package_dunder_main`
- Запуск: `cd arch_like_package_dunder_main && python -m bot_tg`
- Пакет содержит `__main__.py`, который делегирует выполнение в `main.py`.
