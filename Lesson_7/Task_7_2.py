"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный
случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный
массивы.
"""
import random
SIZE = 10
MAX_RANDOM = 50
data = [round(random.random() * MAX_RANDOM, 2) for _ in range(SIZE)]


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(array):
    if len(array) < 2:
        return array

    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge(left, right)


if __name__ == '__main__':
    print(data)
    print(merge_sort(data))



