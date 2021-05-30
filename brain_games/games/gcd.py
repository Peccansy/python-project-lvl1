"""Игра 'НОД'."""
from brain_games.utils.rand_actions import pick_number


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
    left = pick_number()
    right = pick_number()
    answer = _get_answer(left, right)

    return ('{0} {1}'.format(left, right), str(answer))
