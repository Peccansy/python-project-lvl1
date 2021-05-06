#!/usr/bin/env python
"""Сценарий запускающий игру "Проверка на чётность"."""

import prompt

from brain_games.cli import welcome_user
from brain_games.games.even import get_q_and_a, get_rules


def _get_user_ans():
    return prompt.string('Your answer: ')


def main():
    """Главная функция сценария игры."""
    name = welcome_user()
    print(get_rules())

    succ_count = 3

    while succ_count != 0:
        (question, expected_ans) = get_q_and_a()
        print('Question:', question)
        user_ans = _get_user_ans()

        if user_ans == expected_ans:
            print('Correct!')
            succ_count -= 1
        else:
            print("'{0}' is wrong answer ;(.".format(user_ans), end='')
            print("Correct answer was '{0}'.".format(expected_ans))
            print("Let's try again, {0}!".format(name))
            return

    print('Congratulations, {0}!'.format(name))


if __name__ == '__main__':
    main()
