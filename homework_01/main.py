"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** 2 for num in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num: int) -> bool:
    """
    :param num: an integer
    :return: True if num is a prime number, otherwise returns falls; 1 is considered to be non-prime
    """
    num = abs(num)
    if num == 0 or num == 1:
        return False
    for n in range(1, num):
        if n == 1:
            continue
        if not num % n:
            return False
    return True


def filter_numbers(int_nums_lst: list, num_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    filter_action = {
        ODD: lambda num: num % 2,
        EVEN: lambda num: not num % 2,
        PRIME: is_prime,
    }
    return list(filter(filter_action[num_type], int_nums_lst))




