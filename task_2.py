"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти)
И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...
Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import random
from collections import deque
import itertools

SIZE = 10
LEFT = 0
RIGHT = 50

array = [random.uniform(LEFT, RIGHT - 1) for _ in range(SIZE)]

print(f'Исходный массив:\n{array}')


def sort_func(sort_array):
    if len(sort_array) <= 1:
        return sort_array

    new_size = len(sort_array) // 2

    left = deque(itertools.islice(sort_array, 0, new_size))
    right = deque(itertools.islice(sort_array, new_size, len(sort_array)))

    left = sort_func(left)
    right = sort_func(right)

    for k in range(len(sort_array)):
        if len(left) == 0:
            sort_array[k] = right.popleft()
        elif len(right) == 0:
            sort_array[k] = left.popleft()
        else:
            if left[0] <= right[0]:
                sort_array[k] = left.popleft()
            else:
                sort_array[k] = right.popleft()

    return sort_array


print(f'Отсортированный массив:\n{sort_func(array)}')