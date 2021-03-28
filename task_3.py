"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""

import cProfile
from timeit import timeit


# Алгоритм 1
def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num+num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


# Алгоритм 2
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num+num / 10) * 10
        enter_num //= 10
    return revers_num


# Алгоритм 3
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


enter_num = int(input('Введите число: '))
revers_1(enter_num, revers_num = 0)
revers_2(enter_num, revers_num = 0)
revers_3(enter_num)

print('Замеры для алгоритма 1: ', timeit(f'revers_1({enter_num})', globals = globals(), number = 10000))
print('Замеры для алгоритма 2: ', timeit(f'revers_2({enter_num})', globals = globals(), number = 10000))
print('Замеры для алгоритма 3: ', timeit(f'revers_3({enter_num})', globals = globals(), number = 10000))

cProfile.run('revers_1(10000000000)')
cProfile.run('revers_2(10000000000)')
cProfile.run('revers_3(10000000000)')

"""
Быстрее всего вычисляется Алгоритм 3,потому что он решается через
встроенную функцию,которая максимально оптимизирована,
а так же третий алгорит не имеет арифметических операций.
"""
