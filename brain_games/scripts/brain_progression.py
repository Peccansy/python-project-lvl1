#!/usr/bin/env python
"""Сценарий запускающий игру "Арифметическая прогрессия"."""

from brain_games.engine import run
from brain_games.games.progression import get_q_and_a, get_rules


def main():
    """Главная функция сценария игры."""
    run(get_rules, get_q_and_a)


if __name__ == '__main__':
    main()
