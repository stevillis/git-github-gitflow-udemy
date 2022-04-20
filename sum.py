def is_even(num):
    return num % 2 == 0


def odd_sum(start, end):
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
