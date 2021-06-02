"""Игра "Простое ли число?"."""

from math import ceil, sqrt

from brain_games.utils.rand_actions import pick_number


def _is_prime(number):
    """Определяет простое ли число.

    Args:
        number: число, подлежащее проверке

    Returns:
        Boolean
    """
    # мы можем не искать делители, большие чем корень из number.
    # Хорошее объяснение почему так есть тут:
    # https://ru.khanacademy.org/computing/computer-science/cryptography/comp-number-theory/a/trial-division
    stop = ceil(sqrt(number)) + 1
    start = 2  # на единицу нет смысла делить
    for divider in range(start, stop):
        if number % divider == 0:
            return False

    return True


def get_rules():
    """Описывает правила игры.

    Returns:
        текст правил.
    """
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_q_and_a():
    """Вычисляет следующий вопрос и корректный ответ для него.

    Returns:
        кортеж (вопрос, ответ)
    """
    number = pick_number(2)
    question = str(number)
    answer = 'yes' if _is_prime(number) else 'no'
    return (question, answer)
