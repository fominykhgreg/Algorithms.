"""Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке."""


def count_subs(string):
    result = set()

    for i in range(1, len(string)):
        for j in range(len(string)-i+1):
            h = hash(string[j:i+j])
            result.add(h)

    return len(result)


strng = input('Введите строку: ')

print(f'В данной строке {count_subs(strng)} подстрок.')
print("*" * 100)
