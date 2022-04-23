"""
Посчитать, сколько раз встречается определенная цифра в введенной последовательности
чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом
с клавиатуры.
Числа целые.
"""


def get_count(number, digit):
    count = 0

    while True:
        _digit = number % 10
        number //= 10
        if digit == _digit:
            count += 1

        if number < 1:
            break
    return count


if __name__ == '__main__':
    n = int(input('Сколько чисел будет всего? '))
    digit = int(input('Какую цифру будем искать? '))

    result = 0

    while n >= 1:
        number = int(input(f'Введите число: '))
        result += get_count(number, digit)
        n -= 1

    print(f'Найдено цифр всего: {result}')
