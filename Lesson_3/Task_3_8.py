"""
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа
должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю
ячейку строки. В конце следует вывести полученную матрицу.
M - строки
N - столбцы
"""

SIZE_M = 5
SIZE_N = 3


matrix = []
STEP = 10


for i in range(SIZE_M):
    line = []
    sum_line = 0
    for j in range(SIZE_N):
        number = int(input(f'Введите число, строка {i + 1}, столбец {j + 1}: '))
        sum_line += number
        line.append(number)

    line.append(sum_line)
    matrix.append(line)

for line in matrix:
    for number in line:
        print(f'{number:>{STEP}}', end='')
    print()
