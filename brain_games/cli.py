"""Модуль реализует функции по работе с пользовательским вводом."""

import prompt


def welcome_user():
    """Поприветствовать пользователя и предложить ввести имя."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
