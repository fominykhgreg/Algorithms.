""" Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в
виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

import random
from timeit import timeit

nums_list = [a for a in range(-100, 101)]

print(nums_list)
print("В случайном порядке "+"-" * 70)
random.shuffle(nums_list)
print(nums_list)
print("Сортировка пузырьком "+"-" * 70)


def bubble_sort_func(massive):
    compl_nums = 0
    while compl_nums < len(massive)-1:
        counter = 0
        while counter < len(massive)-1-compl_nums:
            if massive[counter] > massive[counter+1]:
                massive[counter], massive[counter+1] = massive[counter+1], massive[counter]
            counter += 1
        compl_nums += 1


bubble_sort_func(nums_list)
print(nums_list)

# Оптимизированная пузырьковая сортировка.

nums_list2 = [a for a in range(-100, 101)]
random.shuffle(nums_list2)


def bubble_sort_func2(massive):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(massive)-1):
            if massive[i] < massive[i+1]:
                massive[i], massive[i+1] = massive[i+1], massive[i]
                swapped = True


bubble_sort_func(nums_list2)

print('Замеры пузырьковой сортировки: ',
      timeit("bubble_sort_func(nums_list)",
             setup = "from __main__ import bubble_sort_func, nums_list",
             globals = globals(), number = 1000))

print('Замеры оптимизированой пузырьковой сортировки: ',
      timeit("bubble_sort_func2(nums_list2)",
             setup = "from __main__ import bubble_sort_func2, nums_list2",
             globals = globals(), number = 1000))

"""
Резултаты замеров получились следующими при выполнении 1000 раз:
Замеры пузырьковой сортировки:  3.8816213
Замеры оптимизированой пузырьковой сортировки:  0.01698259999999996

Сложность такой сортировки O(n^2), таким образом, при небольшом увеличении количества элементов, 
сложность вычислений увеличивается многократно. 
А так как в оптимизированом варианте пузырьковой сортировки есть преждевременное завершение, 
если перестановок не произошло. По этому и время вычислений значительно сокращается.

"""
