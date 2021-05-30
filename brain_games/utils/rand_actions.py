"""Утилитарные функции, производящие псевдо-случайные операции."""

from random import randint

_MIN_NUMBER = 1
_MAX_NUMBER = 100


def pick_number(min_num=_MIN_NUMBER, max_num=_MAX_NUMBER):
    """Генерирует произвольное число.

    По умолчанию возвращает число от _MIN_NUMBER до _MAX_NUMBER

    Args:
        min_num: минимально допустимое число
        max_num: максимально допустимое число

    Returns:
        Число
    """
    return randint(min_num, max_num)  # noqa: S311


def pick_index(collection):
    """Генерирует произвольный индекс коллекции.

    Args:
        collection: коллекция для которой выбирается index

    Returns:
        Число
    """
    return pick_number(0, len(collection) - 1)


def pick_item(collection):
    """Выбирает произвольный элемент коллекции.

    Args:
        collection: коллекция из которой выбирается элемент

    Returns:
        Элемент коллекции
    """
    return collection[pick_index(collection)]
