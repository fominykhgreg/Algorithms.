"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш
Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
from uuid import uuid4
import hashlib

file_1 = open("file.txt", "w")


def pass_func():
    salt = uuid4().hex
    print(salt)
    pass_word = input("Введите свой пароль!:")

    pass_encode = pass_word.encode()
    print(pass_encode)
    hash_obj = hashlib.sha256(pass_encode)
    print(hash_obj)
    complete = hash_obj.hexdigest()+": "+salt
    print(f'Хэш пароля с использование соли: {complete}')
    file_1.write(complete)
    file_1.close()

    pass_word_validate = input("Введите еще раз пароль для проверки: ")
    pass_encode2 = pass_word_validate.encode()
    hash_obj2 = hashlib.sha256(pass_encode2)
    complete2 = hash_obj2.hexdigest()+": "+salt

    if complete == complete2:
        return print("Вы ввели верный пароль.")
    else:
        return print("Пароль не верный.")


pass_func()
