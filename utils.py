"""Вспомогательные функции для статистики оценок."""


def average(numbers):
    """Среднее значение; для пустого списка — 0."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def max_value(numbers):
    """Наибольшее значение списка."""
    result = numbers[0]
    for n in numbers:
        if n > result:
            result = n
    return result


def min_value(numbers):
    """Наименьшее значение списка."""
    result = numbers[0]
    for n in numbers:
        if n < result:
            result = n
    return result
