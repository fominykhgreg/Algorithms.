"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""

from collections import deque
from timeit import timeit

lst = [1, 2, 3, 4, 5]
de = deque([1, 2, 3, 4, 5])

print(de)
print(lst)


def lst_append():
    lst.append(3)


def deque_append():
    de.append(3)


def lst_pop():
    lst.pop()


def deque_pop():
    de.pop()


def list_appendleft(num):
    my_list = []
    for i in range(num):
        my_list.insert(0, i)


def deque_appendleft():
    de.appendleft(6)


def lst_popleft(lst):
    for i in range(len(lst)):
        a = lst.pop(0)


def deque_popleft():
    de.popleft()


print('_' * 50, '\n')
print('Append.List:  ', timeit("lst_append()", globals = globals()))
print('Append.Deque: ', timeit("deque_append()", globals = globals()))
print('_' * 50, '\n')
print('Appendleft.List:  ', timeit("list_appendleft(3)", globals = globals()))
print('Appendleft.Deque: ', timeit("deque_appendleft()", globals = globals()))
print('_' * 50, '\n')
print('Pop.List:  ', timeit("lst_pop()", globals = globals()))
print('Pop.Deque: ', timeit("deque_pop()", globals = globals()))
print('_' * 50, '\n')
print('Popleft.List:  ', timeit("lst_popleft(lst)", globals = globals()))
print('Popleft.Deque: ', timeit("deque_popleft()", globals = globals()))

"""
Получились следующие замеры. Результаты получились примерно одинаковые. 
Но в некоторых примерах есть некоторая разница в скорости а именно вставка и удаление
в начало (appendleft и popleft).

Append.List:   0.13879750000000002
Append.Deque:  0.11343479999999997
__________________________________________________ 

Appendleft.List:   0.4870348
Appendleft.Deque:  0.11306640000000001
__________________________________________________ 

Pop.List:   0.11521570000000003
Pop.Deque:  0.11675110000000011
__________________________________________________ 

Popleft.List:   0.22087299999999987
Popleft.Deque:  0.117178
__________________________________________________ 


"""
