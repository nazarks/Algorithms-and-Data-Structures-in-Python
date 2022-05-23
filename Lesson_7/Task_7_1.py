"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный
случайными числами на промежутке [-100; 100). Выведите на экран исходный и
отсортированный массивы. Сортировка должна быть реализована в виде функции. По
возможности доработайте алгоритм (сделайте его умнее).

Улучшения:
1) Нет нужды проверять каждый раз весь массив.
При первом проходе на последнем месте всегда будет минимальное число, и т.д. Поэтому проверяем до: len(array) - n
2) Добавим флаг который указывает что перестановок не было, а значит массив уже отсортирован.
"""

import random
SIZE = 10
MIN_RANDOM = -100
MAX_RANDOM = 100
data = [random.randrange(MIN_RANDOM, MAX_RANDOM) for _ in range(SIZE)]


def sort(array):
    n = 1
    need_sort = True
    while n < len(array) and need_sort:
        need_sort = False
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                need_sort = True

        n += 1
    return array


if __name__ == '__main__':
    print(data)
    print(sort(data))

