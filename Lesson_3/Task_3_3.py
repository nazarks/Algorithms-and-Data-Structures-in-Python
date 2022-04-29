"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный
элементы
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

array[min_number['index']], array[max_number['index']] = array[max_number['index']], array[min_number['index']]
print(array)
