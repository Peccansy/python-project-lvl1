"""Игра 'Нечётные числа'."""
from brain_games.utils.rand_actions import pick_number


def _get_expected_ans(question):
    return 'yes' if question % 2 == 0 else 'no'


def get_rules():
    """Описывает правила игры.

    Returns:
        текст правил.
    """
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_q_and_a():
    """Вычисляет следующий вопрос и корректный ответ для него.

    Returns:
        кортеж (вопрос, ответ)
    """
    question = pick_number()
    answer = _get_expected_ans(question)
    return (question, answer)
