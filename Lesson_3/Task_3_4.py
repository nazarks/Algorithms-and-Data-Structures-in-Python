"""
4. Определить, какое число в массиве встречается чаще всего
"""
import random


SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

temp_dict = {}
max_freq = 0
for number in array:
    temp_dict.setdefault(number, 0)
    temp_dict[number] += 1
    if temp_dict[number] > max_freq:
        max_freq = temp_dict[number]

result = (number for number, count in temp_dict.items() if count == max_freq)

print('Максимальное количество раз встречаются:', end=' ')
for number in result:
    print(number, end=' ')
