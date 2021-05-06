"""Игра 'Нечётные числа'."""
from random import randint

_MIN_QUESTION_VALUE = 1
_MAX_QUESTION_VALUE = 100


def _get_question():
    return randint(_MIN_QUESTION_VALUE, _MAX_QUESTION_VALUE)  # noqa: S311


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
    question = _get_question()
    answer = _get_expected_ans(question)
    return (question, answer)
