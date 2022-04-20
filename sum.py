def is_even(num: int) -> bool:
    """Check if a given num is even.

    Parameters:
    num (int): An integer to be evaluated as even or not.

    Returns:
    bool: True if num is even, False otherwise.
   """
    return num % 2 == 0


def odd_sum(start: int, end: int) -> int:
    """Sum odd integers between start and end parameters.

    Parameters:
    start (int): Start range of odd integer sum.
    end (int): End range of odd integer sum.

    Returns:
    int: Sum of odd numbers between start and end.
   """
    sum = 0
    for num in range(start, end + 1):
        if not is_even(num):
            sum += num
    return sum


if __name__ == '__main__':
    print('Sum of odd integers between `start` and `end` values')
    start = int(input('Type the `start` integer: '))
    end = int(input('Type the `end` integer: '))

    print(
        f'The sum of odd integers between `{start}` and `{end}` is: {odd_sum(start, end)}')
