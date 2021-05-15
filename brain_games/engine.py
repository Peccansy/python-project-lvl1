"""Игровой движок.

Данный модуль содержит общую логику по запуску игр.
Экспортирует функцию run, которая принимает в качестве аргумента игру.
"""
import prompt

TRIES_NUMBER = 3


def _welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    return name


def _get_user_ans():
    return prompt.string('Your answer: ')


def run(get_rules, get_q_and_a):
    """Запускает игру, переданную как аргумент.

    Args:
        get_rules: функция, возвращающая текст правил игры
        get_q_and_a: функция, возвращающая вопрос и правильный ответ
    """
    name = _welcome_user()
    print(get_rules())

    succ_count = TRIES_NUMBER

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
