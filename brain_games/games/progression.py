"""Логика игры "Арифметическая прогрессия"."""

from brain_games.utils.rand_actions import pick_index, pick_number

_PROGRESSION_LENGTH = 10


def _make_progression():
    start = pick_number()
    step = pick_number()
    stop = start + step * _PROGRESSION_LENGTH

    return list(range(start, stop, step))


def _stringify_progression(progression, index):
    progression_str = ''
    last_index = len(progression) - 1
    for idx, el in enumerate(progression):
        if idx == index:
            progression_str = '{0}..'.format(progression_str)
        else:
            progression_str = '{0}{1}'.format(progression_str, el)

        if idx != last_index:
            progression_str = '{0} '.format(progression_str)

    return progression_str


def get_rules():
    """Описывает правила игры.

    Returns:
        текст правил.
    """
    return 'What number is missing in the progression?'


def get_q_and_a():
    """Вычисляет следующий вопрос и корректный ответ для него.

    Returns:
        кортеж (вопрос, ответ)
    """
    progression = _make_progression()
    picked_idx = pick_index(progression)
    answer = str(progression[picked_idx])
    question = _stringify_progression(progression, picked_idx)

    return (question, answer)
