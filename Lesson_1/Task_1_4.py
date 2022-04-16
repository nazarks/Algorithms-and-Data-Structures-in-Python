"""
Task_1_4
Написать программу, которая генерирует в указанных пользователем границах
● случайное целое число,
● случайное вещественное число,
● случайный символ
"""
import random

print('Введите: \n'
      '1 - для случайного целого числа \n'
      '2 - для случайного вещественного числа \n'
      '3 - для случайного символа')
select = int(input('Выбор: '))
if select == 1:
    print('Введите 2 целых числа a и b, a > b')
    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    c = random.randint(a, b)
elif select == 2:
    print('Введите 2 числа a и b, a > b')
    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    c = random.uniform(a, b)
else:
    print('Введите 2 символа a и b')
    char_a = input('Введите a: ')
    char_b = input('Введите b: ')
    a = ord(char_a)
    b = ord(char_b)
    if a < b:
        c = chr(random.randint(a, b))
    else:
        c = chr(random.randint(b, a))
print(c)
