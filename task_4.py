"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""


# O(n)  сложность
def autorization1(users, user_name, user_password):
    for key, value in users.items():        # in(для списков,кортежей)= O(n)
        if key == user_name:
            if value['password'] == user_password and value['activation']:
                return "Hello."
            elif value['password'] == user_password and not value['activation']:
                return "Access denied"
            elif value['password'] != user_password:
                return "Password incorrect"
    return "Данного пользователя не существует"


# O(1) Наиболее эффективное решение,потому что сложность будет константная
def autorization2(users, user_name, user_password):
    if users.get(user_name):                  # get = o(1)
        if users[user_name]['password'] == user_password and users[user_name]['activation']:
            return "Hello."
        elif users[user_name]['password'] == user_password and not users[user_name]['activation']:
            return "Access denied"
        elif users[user_name]['password']:
            return "Password incorrect"
    else:
        return "Данного пользователя не существует"
