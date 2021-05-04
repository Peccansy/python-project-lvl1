#!/usr/bin/env python
"""Корневой сценарий пакета brain_games.

Этот исполняемый файл используется как точка входа
и запускается пользователем напрямую.
"""

from brain_games.cli import welcome_user


def _main():
    welcome_user()


if __name__ == '__main__':
    _main()
