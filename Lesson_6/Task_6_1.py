"""
6.1 Подсчитать, сколько было выделено памяти под переменные в
программах, разработанных на первых трех уроках.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Подсчитывем на примере задачи:
Определить, какое число в массиве встречается чаще всего
"""
import sys
import random

SIZE = 1000
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


def get_size(data):
    size_of_data = 0
    size_of_data += sys.getsizeof(data)
    if hasattr(data, '__iter__'):
        if hasattr(data, 'items'):
            for key, value in data.items():
                size_of_data += get_size(key)
                size_of_data += get_size(value)
        elif not isinstance(data, str):
            for item in data:
                size_of_data += get_size(item)
    return size_of_data


def get_function_vars_size(functions_vars, exclude):
    return sum(map(get_size, (value for var, value in functions_vars.items() if var not in exclude)))


def get_max_counts_version_1(array):
    """
    Функция определяет, какие числа в массиве встречаются чаще всего.
    Для промежуточного хранения используется словарь.
    """

    temp_dict = {}
    max_freq = 0
    for number in array:
        temp_dict.setdefault(number, 0)
        temp_dict[number] += 1
        if temp_dict[number] > max_freq:
            max_freq = temp_dict[number]

    result = [number for number, count in temp_dict.items() if count == max_freq]

    print(f"Размер переменных функции {sys._getframe().f_code.co_name}:"
          f" {get_function_vars_size(functions_vars=locals(), exclude=('array',))} байт")

    return result


def get_max_counts_version_2(array):
    """
    Функция определяет, какие числа в массиве встречаются чаще всего.
    Для промежуточного хранения данных используется список состоящий из кортежей.
    """

    temp_list = []  # list of tuples (number, count)
    max_freq = 1
    freq = 1
    for number in array:
        for i in range(len(temp_list)):
            if number == temp_list[i][0]:
                temp_list[i] = (temp_list[i][0], temp_list[i][1] + 1)
                freq = temp_list[i][1]
                break
        else:
            temp_list.append((number, 1))
        if freq > max_freq:
            max_freq = freq

    result = [number for number, count in temp_list if count == max_freq]

    print(f"Размер переменных функции {sys._getframe().f_code.co_name}:"
          f" {get_function_vars_size(functions_vars=locals(), exclude=('array',))} байт")

    return result


def get_max_counts_version_3(array):
    """
    Функция определяет, какие числа в массиве встречаются чаще всего.
    Для промежуточного хранения данных используется 2 списка и сет.
    """

    number_list = []
    count_list = []
    temp_set = set()
    max_freq = 1
    freq = 1
    for number in array:
        if number in temp_set:
            for i in range(len(number_list)):
                if number == number_list[i]:
                    count_list[i] += 1
                    freq = count_list[i]
                    break
        else:
            number_list.append(number)
            count_list.append(1)
            temp_set.add(number)
        if freq > max_freq:
            max_freq = freq

    result = [number_list[i] for i in range(len(number_list)) if count_list[i] == max_freq]

    print(f"Размер переменных функции {sys._getframe().f_code.co_name}:"
          f" {get_function_vars_size(functions_vars=locals(), exclude=('array',))} байт")

    return result


def get_max_counts_version_4(array):
    """
    Функция определяет, какие числа в массиве встречаются чаще всего.
    Для промежуточного хранения данных используется список.
    """

    max_freq = 1
    result = []
    max_size = 0

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

        # Размер массива меняется динамически, в конце работы функции данные для него не корректны
        size = get_size(result)
        if size > max_size:
            max_size = size

    print(f"Размер переменных функции {sys._getframe().f_code.co_name}: "
          f"{get_function_vars_size(functions_vars=locals(), exclude=('array', 'result')) + max_size}"
          f" байт")

    return result


if __name__ == '__main__':
    max_count_numbers = get_max_counts_version_1(array)
    print('Вариант 1. Максимальное количество раз встречаются числа:', end=' ')
    for number in max_count_numbers:
        print(number, end=' ')
    print('\n')

    max_count_numbers = get_max_counts_version_2(array)
    print('Вариант 2. Максимальное количество раз встречаются числа:', end=' ')
    for number in max_count_numbers:
        print(number, end=' ')
    print('\n')

    max_count_numbers = get_max_counts_version_3(array)
    print('Вариант 3. Максимальное количество раз встречаются числа:', end=' ')
    for number in max_count_numbers:
        print(number, end=' ')
    print('\n')

    max_count_numbers = get_max_counts_version_4(array)
    print('Вариант 4. Максимальное количество раз встречаются числа:', end=' ')
    for number in max_count_numbers:
        print(number, end=' ')


"""
Python 3.10, x64
Результат работы : 

Размер переменных функции get_max_counts_version_1: 10548 байт
Вариант 1. Максимальное количество раз встречаются числа: 62 21 

Размер переменных функции get_max_counts_version_2: 12484 байт
Вариант 2. Максимальное количество раз встречаются числа: 62 21 

Размер переменных функции get_max_counts_version_3: 18980 байт
Вариант 3. Максимальное количество раз встречаются числа: 62 21 

Размер переменных функции get_max_counts_version_4: 344 байт
Вариант 4. Максимальное количество раз встречаются числа: 62 21 
Process finished with exit code 0

Вывод: наиболее эффективным с точки зрения потребления памяти является вариант номер 4.
К сожалению, с точки зрения процессорного времени он не применим для большого количества входных данных.
Для вариантов 1-3 в качестве входных данных можно использовать генератор вместо списка, это экономит память. 
"""
