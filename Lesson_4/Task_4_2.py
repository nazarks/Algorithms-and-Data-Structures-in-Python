"""
4.2. Написать два алгоритма нахождения i-го по счёту простого числа.
● Без использования Решета Эратосфена;
● Использовать алгоритм решето Эратосфена
"""
import timeit
import cProfile

from math import log, ceil


def prime_number(position):
    current_number = 2
    count = 1
    while True:
        if count == position:
            return current_number
        current_number += 1
        for number in range(2, current_number):
            if current_number % number == 0:
                break
        else:
            count += 1


def sieve(position):
    if position == 1:
        return 2
    if position == 2:
        return 3

    n = ceil(2 * position * log(position))

    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0
    m = 2
    count = 0

    while m < n:
        if a[m] != 0:
            count += 1
            if count == position:
                return a[m]
            j = m * 2
            while j < n:
                a[j] = 0
                j += m
        m += 1


print(timeit.timeit('prime_number(50)', number=100, globals=globals()))   # 0.0215163000029861
print(timeit.timeit('prime_number(100)', number=100, globals=globals()))  # 0.09090590000414522
print(timeit.timeit('prime_number(200)', number=100, globals=globals()))  # 0.4289050000006682
print(timeit.timeit('prime_number(400)', number=100, globals=globals()))  # 1.9354005999994115
print(timeit.timeit('prime_number(800)', number=100, globals=globals()))  # 8.812833099997079
print(timeit.timeit('prime_number(1600)', number=100, globals=globals()))   # 39.948475600001984
print(timeit.timeit('prime_number(3200)', number=100, globals=globals()))   # 164.3948511000017


print(timeit.timeit('sieve(50)', number=100, globals=globals()))    # 0.005791700001282152
print(timeit.timeit('sieve(100)', number=100, globals=globals()))   # 0.014896299995598383
print(timeit.timeit('sieve(200)', number=100, globals=globals()))   # 0.03626050000457326
print(timeit.timeit('sieve(400)', number=100, globals=globals()))   # 0.08557229999860283
print(timeit.timeit('sieve(800)', number=100, globals=globals()))   # 0.2005494999975781
print(timeit.timeit('sieve(1600)', number=100, globals=globals()))  # 0.42932859999564243
print(timeit.timeit('sieve(3200)', number=100, globals=globals()))  # 0.955917800001771

cProfile.run('prime_number(800)')
cProfile.run('sieve(800)')

"""
Сложность алгоритмов :
Версия c решетом: O(N)
Версия без решета: O(N2)
"""