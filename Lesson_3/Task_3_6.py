"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и
максимальным элементами. Сами минимальный и максимальный элементы в сумму не
включать
"""
import random


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_number = {'index': 0, 'value': array[0]}
max_number = {'index': 0, 'value': array[0]}
for index in range(1, len(array)):
    if array[index] < min_number['value']:
        min_number['value'] = array[index]
        min_number['index'] = index
    elif array[index] > max_number['value']:
        max_number['value'] = array[index]
        max_number['index'] = index

if min_number['index'] > max_number['index']:
    min_number['index'], max_number['index'] = max_number['index'], min_number['index']

sum_numbers = 0
for index in range(min_number['index'] + 1, max_number['index']):
    sum_numbers += array[index]

print(f'Сумма чисел: {sum_numbers}') if sum_numbers else print(f'Числа не найдены')
