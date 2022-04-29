"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random


SIZE_M = 4
SIZE_N = 4
MIN_ITEM = 1
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)] for _ in range(SIZE_M)]
print(*matrix, sep='\n')


min_row = matrix[0][:]

for line in matrix:
    for index, number in enumerate(line):
        if min_row[index] > number:
            min_row[index] = number

max_number = min_row[0]
for index in range(1, len(min_row)):
    if min_row[index] > max_number:
        max_number = min_row[index]


print(f'Максимальный элемент среди минимальных: {max_number}')
