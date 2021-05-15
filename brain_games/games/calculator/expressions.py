"""Модуль выражений.

Реализует математические выражения для игры "Калькулятор".
"""

from random import randint

from brain_games.games.calculator.evaluators import mul, subtract, summ

_OPERATORS = '+-*'
_MIN_OPERAND = 1
_MAX_OPERAND = 100


def _pick_operand():
    return randint(_MIN_OPERAND, _MAX_OPERAND)  # noqa: S311


def _pick_operator():
    return _OPERATORS[randint(0, len(_OPERATORS) - 1)]  # noqa: S311


def get_expression():
    """Формирует выражение.

    Returns:
        кортеж (операнд, оператор, операнд)
    """
    return (_pick_operand(), _pick_operator(), _pick_operand())


def eval_expression(expression):
    """Вычисляет выражение для операндов, перечисленных в _OPERATORS.

    Args:
        expression: выражение

    Returns:
        результат выражения
    """
    (left, operator, right) = expression

    answer = None
    if operator == _OPERATORS[0]:
        answer = summ(left, right)
    elif operator == _OPERATORS[1]:
        answer = subtract(left, right)
    elif operator == _OPERATORS[2]:
        answer = mul(left, right)

    return answer


def stringify_expression(expression):
    """Приводит выражение к строке.

    Args:
        expression: выражение

    Returns:
        Строковое представление выражения
    """
    (left, operator, right) = expression

    return '{0} {1} {2}'.format(left, operator, right)
