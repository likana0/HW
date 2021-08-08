# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
#
def division(user_numb1, user_numb2):

    """Получает позиционные аргументы и выолняет их деление.
    Аргументы: user_numb1, user_numb2.
    Предусмотрена проверка деления на 0.
    return: деление двух чисел.
    """

    try:
        user_numb1, user_numb2 = int(user_numb1), int(user_numb2)
        result = user_numb1 / user_numb2

    except ValueError:
        return 'Это же не число...'

    except ZeroDivisionError:
        return 'Давай не будем делить на 0?)'

    return result


print('Давай поделим 2 числа?')

user_numb1 = int(input("Введи первый позицонный аргумент - "))
user_numb2 = int(input("Введи второй позицонный аргумент - "))

print(f'Результат деления - {division(user_numb1, user_numb2)}')