#!/usr/bin/env python
"""Корневой сценарий пакета brain_games.

Этот исполняемый файл используется как точка входа
и запускается пользователем напрямую.
"""

from brain_games.cli import welcome_user


def main():
    """Главная функция сценария игры."""
    welcome_user()


if __name__ == '__main__':
    main()
