"""
5.2 Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое
число представляется как коллекция, элементы которой это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import defaultdict, deque


HEX_LIST = '0123456789ABCDEF'


def get_digit(hex_number):
    for key, value in numbers_dict.items():
        if value == hex_number:
            return key


def sum_hex(num_1, num_2):
    hex_1 = num_1.copy()
    hex_2 = num_2.copy()
    hex_summa = deque()

    diff = abs(len(hex_1) - len(hex_2))
    for _ in range(diff):
        if len(hex_1) > len(hex_2):
            hex_2.appendleft('0')
        elif len(hex_2) > len(hex_1):
            hex_1.appendleft('0')

    hex_1 = list(hex_1)
    hex_2 = list(hex_2)
    transfer = 0
    for i in range(len(hex_1) - 1, -1, -1):
        digit = get_digit(hex_1[i]) + get_digit(hex_2[i]) + transfer
        transfer = 0
        if digit > 15:
            transfer = 1
            digit -= 16
        hex_summa.appendleft(HEX_LIST[digit])
    if transfer:
        hex_summa.appendleft(1)
    return hex_summa


def mul_hex(num_1, num_2):
    hex_1 = list(num_1.copy())
    hex_2 = list(num_2.copy())
    hex_mul = deque()
    hex_1.reverse()
    hex_2.reverse()
    transfer = 0
    i = 0
    j = 0
    row = []
    all_row = []
    while j < len(hex_2):
        mul = get_digit(hex_1[i]) * get_digit(hex_2[j]) + transfer
        transfer = mul // 16
        if transfer:
            digit = mul - 16 * transfer
        else:
            digit = mul
        row.append(digit)

        i += 1
        if i == len(hex_1) and j < len(hex_2):
            i = 0
            j += 1
            if transfer:
                row.append(transfer)
                transfer = 0
            all_row.append(row)
            row = list([0] * j)

    transfer = 0
    for i in range(len(max(all_row, key=len))):
        digit = 0
        digit += transfer
        for row in all_row:
            try:
                digit += row[i]
            except IndexError:
                pass
        transfer = digit // 16
        if transfer:
            digit = digit - 16 * transfer
        hex_mul.appendleft(HEX_LIST[digit])

    return hex_mul


if __name__ == '__main__':
    numbers_dict = defaultdict(int)
    for i in range(16):
        numbers_dict[i] = HEX_LIST[i]

    num1 = deque(input('Введите первое число: ').upper())
    num2 = deque(input('Введите второе число: ').upper())

    print(f'Сумма двух чисел: {sum_hex(num1, num2)}')
    print(f'Умножение двух чисел: {mul_hex(num1, num2)}')

