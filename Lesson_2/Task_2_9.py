"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
Задание выполнено с помощью рекурсии
"""


def get_sum(number, sum):
    digit = number % 10
    number //= 10
    sum += digit

    if number >= 1:
        return get_sum(number, sum)
    else:
        return sum


if __name__ == '__main__':
    sum = 0
    number = 0

    while True:
        new_number = int(input('Введите число: '))
        if not new_number:
            break
        new_sum = get_sum(new_number, 0)
        if new_sum > sum:
            sum = new_sum
            number = new_number

    print(f'Наибольшее по сумме цифр число: {number}, сумма: {sum}')
