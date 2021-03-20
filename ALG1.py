# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

def zadacha():
    a = input("Введите число : ")

    j = 0
    m = 1

    for i in a:
        j = j+int(i)

    for i in a:
        m = m * int(i)

    sumsum = (f'Сумма цифр будет равна - {j}.\n'
          f'Произведение - {m}.')
    return print(sumsum)

zadacha()
