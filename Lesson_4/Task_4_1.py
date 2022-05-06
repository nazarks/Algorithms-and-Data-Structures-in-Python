"""
4.1. Определить, какое число в массиве встречается чаще всего
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
"""
import random
import timeit
import cProfile


SIZE = 10000
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


def get_max_counts_version_1(array):
    temp_dict = {}
    max_freq = 0
    for number in array:
        temp_dict.setdefault(number, 0)
        temp_dict[number] += 1
        if temp_dict[number] > max_freq:
            max_freq = temp_dict[number]

    result = (number for number, count in temp_dict.items() if count == max_freq)
    return result


def get_max_counts_version_2(array):
    temp_dict = {}

    for number in array:
        temp_dict[number] = array.count(number)
    max_freq = max(temp_dict.values())

    result = [key for key, value in temp_dict.items() if value == max_freq]
    return result


def get_max_counts_version_3(array):
    max_freq = 1
    result = []
    for i in range(len(array)):
        freq = 1
        for j in range(i + 1, len(array)):
            if array[j] == array[i]:
                freq += 1
        if freq > max_freq:
            result = [array[i]]
            max_freq = freq
        elif freq == max_freq:
            result.append(array[i])

    return result


# print(timeit.timeit('get_max_counts_version_1(array)', number=100, globals=globals()))  # 0.0013441999999486143, SIZE = 100
# print(timeit.timeit('get_max_counts_version_1(array)', number=100, globals=globals()))  # 0.011685399998896173,   SIZE = 1_000
# print(timeit.timeit('get_max_counts_version_1(array)', number=100, globals=globals()))  # 0.05641469999864057,   SIZE = 5_000
# print(timeit.timeit('get_max_counts_version_1(array)', number=100, globals=globals()))  # 0.1130646000001434,   SIZE = 10_000

# print(timeit.timeit('get_max_counts_version_2(array)', number=100, globals=globals()))  # 0.008599400000093738, SIZE = 100
# print(timeit.timeit('get_max_counts_version_2(array)', number=100, globals=globals()))  # 0.7736364000011235,   SIZE = 1_000
# print(timeit.timeit('get_max_counts_version_2(array)', number=100, globals=globals()))  # 19.2272551000005,   SIZE = 5_000
# print(timeit.timeit('get_max_counts_version_2(array)', number=100, globals=globals()))  # 76.69657700000062,   SIZE = 10_000

# print(timeit.timeit('get_max_counts_version_3(array)', number=100, globals=globals()))  # 0.020590699999956996, SIZE = 100
# print(timeit.timeit('get_max_counts_version_3(array)', number=100, globals=globals()))  # 2.06184679999933,   SIZE = 1_000
# print(timeit.timeit('get_max_counts_version_3(array)', number=100, globals=globals()))  # 51.2645893999997,   SIZE = 5_000
# print(timeit.timeit('get_max_counts_version_3(array)', number=100, globals=globals()))  # 205.13712449999912,   SIZE = 10_000


print('Вариант 1. Максимальное количество раз встречаются:', end=' ')
for number in get_max_counts_version_1(array):
    print(number, end=' ')
print()

print('Вариант 2. Максимальное количество раз встречаются:', end=' ')
for number in get_max_counts_version_2(array):
    print(number, end=' ')
print()

print('Вариант 3. Максимальное количество раз встречаются:', end=' ')
for number in get_max_counts_version_3(array):
    print(number, end=' ')
print()


"""
cProfile.run('get_max_counts_version_1(array)')

      10006 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.002    0.002    0.003    0.003 Task_4_1.py:16(get_max_counts_version_1)
        1    0.000    0.000    0.000    0.000 Task_4_1.py:25(<genexpr>)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
    10000    0.001    0.000    0.001    0.000 {method 'setdefault' of 'dict' objects}
"""
"""
cProfile.run('get_max_counts_version_2(array)')

10008 function calls in 0.773 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.773    0.773 <string>:1(<module>)
        1    0.002    0.002    0.773    0.773 Task_4_1.py:29(get_max_counts_version_2)
        1    0.000    0.000    0.000    0.000 Task_4_1.py:36(<listcomp>)
        1    0.000    0.000    0.773    0.773 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
    10000    0.771    0.000    0.771    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}

"""
"""
cProfile.run('get_max_counts_version_3(array)')

10005 function calls in 2.225 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    2.225    2.225 <string>:1(<module>)
        1    2.224    2.224    2.225    2.225 Task_4_1.py:40(get_max_counts_version_3)
        1    0.000    0.000    2.225    2.225 {built-in method builtins.exec}
    10001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
"""
Сложность алгоритмов :
Версия 1: O(N)
Версия 2: O(N2)
Версия 3: O(N2)

Версия 1 работает быстрее всего, сложность алгоритма наименьшая.
"""
