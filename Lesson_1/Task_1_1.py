"""
Task_1_1
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

print('Введите трехзначное число')
a = int(input('Число: '))
b = 0

# Первая интерация
d = a % 10
a = a // 10
c = d
b = b + d

# Вторая итерация
d = a % 10
a = a // 10
c = c * d
b = b + d

# Третья итерация
d = a % 10
c = c * d
b = b + d

print(f'Сумма чисел: {b}')
print(f'Произведение чисел: {c}')
