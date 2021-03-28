"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""

import random
from timeit import timeit

array = [random.randint(0, 10) for el in range(10)]


# Алгоритм 1
def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


# Алгоритм 2
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


print(func_1())
print(func_2())

print(timeit("func_1()", globals = globals()))
print(timeit("func_2()", globals = globals()))

"""
Согластно замерам, второй вариант решения получился медленней,
так как, при таком решении создается несколкьо массивов,
с перебором элементов каждого,что негативно сказывается 
на скорости вычислений.

Мои замеры
2.4416742
3.0524077
"""
