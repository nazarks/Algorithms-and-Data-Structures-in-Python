"""
В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть
как равны между собой (оба являться минимальными), так и различаться.
"""

import random


SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


min_number_1, min_number_2 = array[0], array[1]

for index in range(2, len(array)):
    if array[index] < min_number_1 or array[index] < min_number_2:
        if min_number_1 < min_number_2:
            min_number_2 = array[index]
        else:
            min_number_1 = array[index]

print(f'Минимальные числа: {min_number_1} {min_number_2}')

