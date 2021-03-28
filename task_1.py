"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""

import timeit


def func_1(nums):  # Сложность - O(n)
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):  # Решение через генераторы. Сложность - O(n)
    return [index for index, value in enumerate(nums) if value % 2 == 0]


# замеры

nums = [el for el in range(1000)]

print(timeit.timeit("func_1(nums)", globals = globals(), number = 1000))
print(timeit.timeit("func_2(nums)", globals = globals(), number = 1000))

nums = [el for el in range(10000)]

print(timeit.timeit("func_1(nums)", globals = globals(), number = 1000))
print(timeit.timeit("func_2(nums)", globals = globals(), number = 1000))

nums = [el for el in range(100000)]
print(timeit.timeit("func_1(nums)", globals = globals(), number = 1000))
print(timeit.timeit("func_2(nums)", globals = globals(), number = 1000))

"""
У меня получились следующие показатели скорости вычислений:
nums=1000
0.0894122
0.0738292

nums=10000
0.8882075
0.7361501000000001

nums=100000
9.3899862
7.939853900000001

Решение через генераторы будет немного быстрее. Так просисходит,
потому что массив элементов не записывается в память. 
"""
