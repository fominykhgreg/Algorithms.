"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""

from uuid import uuid4
import hashlib

salt = uuid4().hex
hash_table = dict(
)


def cash_func(url):
    # hash_table[url]=complete_hash

    if hash_table.get(url):
        print(f'Такая страница уже есть в кэшэ:{url}')
        print(hash_table)
    else:
        url_encode = url.encode()

        hash_obj = hashlib.sha256(url_encode)

        complete_hash = hash_obj.hexdigest()+": "+salt

        hash_table[url] = complete_hash
        print(hash_table)


cash_func("https://github.com/")
cash_func("https://youtube.com/")
cash_func("https://github.com/")
