"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов
(n) вводится с клавиатуры.
Задание выполнено с помощью рекурсии.
"""


def get_sum(n, sum, current):
    if n == 1:
        return sum

    current = current / 2 * -1
    sum += current
    n -= 1

    return get_sum(n, sum, current)


if __name__ == '__main__':
    n = int(input('Введите число: '))

    sum = 1
    current = 1
    result = get_sum(n, sum, current)

    print(result)
