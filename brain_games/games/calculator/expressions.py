"""Модуль выражений.

Реализует математические выражения для игры "Калькулятор".
"""

from brain_games.games.calculator.evaluators import mul, subtract, summ
from brain_games.utils.rand_actions import pick_item, pick_number

_OPERATORS = '+-*'


def get_expression():
    """Формирует выражение.

    Returns:
        кортеж (операнд, оператор, операнд)
    """
    return (pick_number(), pick_item(_OPERATORS), pick_number())


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
