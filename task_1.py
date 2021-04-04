"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.
Можно взять задачи с курса Основ
или с текущего курса Алгоритмов
Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from timeit import timeit
import sys
import inspect
from memory_profiler import profile
from collections import deque

N = []
IND = [10, 100, 1000, 10000]
for ind in IND:
    num = [1234567890] * (ind // 10)
    N.append(int("".join(map(str, num))))

memory = {}


@profile
def show_size(x):
    size = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                size += show_size(key)
                size += show_size(value)
        elif not isinstance(x, str):
            for item in x:
                size += show_size(item)

    return size


def rev_func(n):
    n_num = N[n]

    def rev(a, a_rev):
        for loc in locals().values():
            memory[inspect.stack()[-2][3]] += show_size(loc)

        if a == 0:
            return a_rev
        else:
            return rev(a // 10, a_rev * 10+a % 10)

    memory[inspect.stack()[0][3]] = 0
    for loc in locals().values():
        memory[inspect.stack()[0][3]] += show_size(loc)

    return rev(n_num, 0)


def rev_func_1(n):
    n_num = N[n]
    memory[inspect.stack()[0][3]] = 0
    n_rev = 0
    while n_num > 0:
        n_rev = n_rev * 10+n_num % 10
        n_num = n_num // 10

    for loc in locals().values():
        memory[inspect.stack()[0][3]] += show_size(loc)

    return n_rev


def rev_func_2(n):
    n_num = N[n]

    memory[inspect.stack()[0][3]] = 0
    n_rev = ''
    n_num = str(n_num)
    for i in n_num:
        n_rev = i+n_rev

    for loc in locals().values():
        memory[inspect.stack()[0][3]] += show_size(loc)

    return int(n_rev)


def rev_func_slice(n):
    n_num = N[n]
    n_rev = str(n_num)[::-1]

    memory[inspect.stack()[0][3]] = 0
    for loc in locals().values():
        memory[inspect.stack()[0][3]] += show_size(loc)

    return int(n_rev)


def rev_func_deque(n):
    n_num = N[n]

    n_rev = deque(str(n_num))
    n_rev.reverse()

    memory[inspect.stack()[0][3]] = 0
    for loc in locals().values():
        memory[inspect.stack()[0][3]] += show_size(loc)

    return int(''.join(n_rev))


rev_func(0)
rev_func_1(0)
rev_func_2(0)
rev_func_slice(0)
rev_func_deque(0)

for name in memory:
    print(f'Функция {name} для разворота числа из 10 цифр,занимает {memory[name]} байт.')

"""
# Выводы:
Функция rev_func для разворота числа из 10 цифр,занимает 2296 байт.
Функция rev_func_1 для разворота числа из 10 цифр,занимает 76 байт.
Функция rev_func_2 для разворота числа из 10 цифр,занимает 192 байт.
Функция rev_func_slice для разворота числа из 10 цифр,занимает 115 байт.
Функция rev_func_deque для разворота числа из 10 цифр,занимает 1180 байт.


Больше всего памяти занимает решение через рекурсию. 
Так же довольно много (по сравнению с другими), 
занимает решение через очередь. 
Самый оптимальный вариант получился через деление на 10.


"""
