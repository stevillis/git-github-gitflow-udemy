from enum import Enum
from typing import Union


class SumType(Enum):
    ODD = 1
    EVEN = 2


def is_even(num: int) -> bool:
    """Check if a given num is even.

    Parameters:
    num (int): An integer to be evaluated as even or not.

    Returns:
    bool: True if num is even, False otherwise.
   """
    return num % 2 == 0


def sum_range_integers(start: int, end: int, sum_type: SumType) -> int:
    """Sum integers between start and end parameters.

    Parameters:
    start (int): Start range of odd integer sum.
    end (int): End range of odd integer sum.
    type (SumType): Sum odd or even integers between the given range.

    Returns:
    int: Sum of odd numbers between start and end.
   """
    result = 0
    if sum_type == SumType.ODD:
        for num in range(start, end + 1):
            if not is_even(num):
                result += num
        return result
    elif sum_type == SumType.EVEN:
        for num in range(start, end + 1):
            if is_even(num):
                result += num
        return result
    return result


if __name__ == '__main__':
    print('-' * 5, 'Sum of odd integers between `start` and `end` values', '-' * 5)

    sum_type = -1
    while sum_type not in (1, 2):
        sum_type = int(
            input('What kind of sum do you want? (1) - Even, (2) - Odd: '))
        if sum_type not in (1, 2):
            print('Choose a valid choice!\n')

    start = int(input('Type the `start` integer: '))
    end = int(input('Type the `end` integer: '))

    sum_type_str = SumType(sum_type).name.lower()
    result = sum_range_integers(start, end, SumType(sum_type))

    print(
        f'The sum of {sum_type_str} integers between `{start}` and `{end}` is: {result}')
