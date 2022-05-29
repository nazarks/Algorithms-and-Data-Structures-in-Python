"""
1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9
"""

import hashlib


def unique_sub(s: str) -> int:

    substring_list = []
    for i in range(len(s)):
        temp = [s[i: i + j + 1] for j in range(len(s) - i) if len(s[i: i + j + 1]) < len(s)]
        substring_list.extend(temp)

    unique = set()
    answer = 0
    for sub in substring_list:
        if hashlib.sha1(sub.encode('utf-8')).hexdigest() not in unique:  # В учебных целях. Требование ТЗ.
            unique.add(hashlib.sha1(sub.encode('utf-8')).hexdigest())    # Можно просто применить set(substring_list).
            answer += 1

    return answer


if __name__ == '__main__':

    print(unique_sub('papa'))
    print(unique_sub('sova'))
