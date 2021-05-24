"""Игра 'НОД'."""
from random import randint

_MIN_QUESTION_VALUE = 1
_MAX_QUESTION_VALUE = 100


def _get_number():
    return randint(_MIN_QUESTION_VALUE, _MAX_QUESTION_VALUE)  # noqa: S311


def _get_answer(param1, param2):
    left = param1
    right = param2

    while left != 0 and right != 0:
        if left > right:
            left %= right
        else:
            right %= left

    return left + right


def get_rules():
    """Описывает правила игры.

    Returns:
        текст правил.
    """
    return 'Find the greatest common divisor of given numbers.'


def get_q_and_a():
    """Вычисляет следующий вопрос и корректный ответ для него.

    Returns:
        кортеж (вопрос, ответ)
    """
    left = _get_number()
    right = _get_number()
    answer = _get_answer(left, right)

    return ('{0} {1}'.format(left, right), str(answer))
