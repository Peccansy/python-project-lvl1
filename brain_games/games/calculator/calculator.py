"""Модуль 'Калькулятор'.

Реализует интерфейс игры.
"""
from brain_games.games.calculator.expressions import (
    eval_expression,
    get_expression,
    stringify_expression,
)


def get_q_and_a():
    """Позволяет получить вопрос и ответ.

    Returns:
        кортеж (вопрос, ответ)
    """
    expression = get_expression()
    question = stringify_expression(expression)
    answer = eval_expression(expression)

    return (question, str(answer))


def get_rules():
    """Содержит правила игры.

    Returns:
        Строка правил игры.
    """
    return 'What is the result of the expression?'
