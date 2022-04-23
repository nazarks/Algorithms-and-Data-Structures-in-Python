"""
Посчитать четные и нечетные цифры введенного натурального числа. Например, если
введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""
n = int(input('Введите число: '))

even_count = 0
odd_count = 0

while True:
    digit = n % 10
    n //= 10

    if digit % 2:
        odd_count += 1
    else:
        even_count += 1

    if n < 1:
        break

print(f'Количество четных чисел: {even_count}')
print(f'Количество нечетных чисел: {odd_count}')

