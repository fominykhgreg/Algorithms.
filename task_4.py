"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
from collections import OrderedDict

mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 4}
orddict = OrderedDict(mydict)

print(mydict, orddict)


# items
def dict_func():
    for k, v in mydict.items():
        return k, v


def ordered_func():
    for k, v in orddict.items():
        return k, v


# Dict
def dict_keys_func():
    for key in mydict.keys():
        return key


def ordered_keys_func():
    for key in orddict.keys():
        return key


# Ordered_dict
def dict_values_func():
    for value in mydict.values():
        return value


def ordered_values_func():
    for value in orddict.values():
        return value


# Sorted
def dict_sorting_func(mydict):
    a = sorted(mydict.items(), key = lambda item: item[1])


def ordered_sorting_func(orddict):
    a = sorted(orddict.items(), key = lambda item: item[1])


print('\n', 'Items', '_' * 50)

print('Dict:         ', timeit("dict_func()", globals = globals()))
print('OrderedDict:  ', timeit("ordered_func()", globals = globals()))

print('\n', 'Keys', '_' * 50)

print('Dict:         ', timeit("dict_keys_func()", globals = globals()))
print('OrderedDict:  ', timeit("ordered_keys_func()", globals = globals()))

print('\n', 'Values', '_' * 50)

print('Dict:         ', timeit("dict_values_func()", globals = globals()))
print('OrderedDict:  ', timeit("ordered_values_func()", globals = globals()))

print('\n', 'Sorting', '_' * 50)

print('Dict:         ', timeit("dict_sorting_func(mydict)", globals = globals()))
print('Dict:         ', timeit("ordered_sorting_func(orddict)", globals = globals()))

"""В моей версии Python(3.9) результаты замеров получились примерно одинаковые,но по всем позициям OrderedDict 
немного уступает обычному словарю,работает медленнее.

Items __________________________________________________
Dict:          0.2499233
OrderedDict:   0.27157349999999997

 Keys __________________________________________________
Dict:          0.18784220000000007
OrderedDict:   0.20555580000000007

 Values __________________________________________________
Dict:          0.19469150000000013
OrderedDict:   0.21402739999999998

 Sorting __________________________________________________
Dict:          0.8780628999999998
Dict:          1.0365659999999997
"""
