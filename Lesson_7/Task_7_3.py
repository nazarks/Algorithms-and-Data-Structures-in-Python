"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану.
Медианой называется элемент ряда,
делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки,
который не рассматривался на уроках (сортировка слиянием также недопустима).
"""
import random


M = 5
MIN_RANDOM = 1
MAX_RANDOM = 100
data = [random.randint(MIN_RANDOM, MAX_RANDOM) for _ in range((M * 2) + 1)]


def search_median(array, index):
    if len(array) == 1:
        return array[0]

    pivot = random.choice(array)

    left = [item for item in array if item < pivot]
    right = [item for item in array if item > pivot]
    pivots = [item for item in array if item == pivot]

    if index < len(left):
        return search_median(left, index)
    elif index < len(left) + len(pivots):
        return pivots[0]
    else:
        return search_median(right, index - len(left) - len(pivots))


def median(array):
    search_index = len(array) // 2

    return search_median(array, search_index)


if __name__ == '__main__':
    print(data)

    my_median = median(data)
    print(f'Медианна: {my_median}')
    assert sorted(data)[len(data) // 2] == my_median, 'Ошибка нахождения медианны!'
