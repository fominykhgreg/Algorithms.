"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, /
- условие завершения рекурсии - введена операция 0

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def calculator():
    operation = input("Введите знак вычисления:")
    if operation == "0":
        return print("Bye")
    else:
        if operation in "+-*/":
            try:
                number1 = int(input("Введите первое число:"))
                number2 = int(input("Введите второе число:"))
                if operation == "+":
                    calculate = number1+number2

                elif operation == "-":
                    calculate = number1-number2

                elif operation == "*":
                    calculate = number1 * number2

                elif operation == "/":
                    calculate = number1 / number2
                print(f'Ваш результат : {calculate}')

            except ValueError:
                print("Введите число")
            return calculator()
        else:
            print("Введен неверный символ, попробуйте еще раз")
            return calculator()


calculator()





# Черновик
# def calculator(a, b, c):
#     a = int(input("Введите первое число:"))
#     b = int(input("Введите второе число:"))
#     c = input("Введите знак вычисления:")
#     if c == "0":
#         return print("Пока")
#
#     if c == "+":
#         calculate = a+b
#     elif c == "-":
#         calculate = a-b
#     elif c == "*":
#         calculate = a * b
#     elif c == "/":
#         calculate = a / b
#     print(calculate)
#
#     return calculator(a, b, c)
#
# calculator(1, 1, 1)
