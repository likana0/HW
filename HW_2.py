def parameters(**kwargs):

    """Функция - словарь. Принимает именованные аргументы (**kwargs).
    return: вывод значений ключей словаря через пробел.
    """

    return ' '.join(kwargs.values())


question_to_the_user = input('Привет! Добавим нового пользователя? (да/нет) - ').lower()

if question_to_the_user.startswith('д'):

    name = input("Введи имя - ")
    surname = input("Введи фамилию - ")
    year_birthday = input("Введи год своего рождения - ")
    city = input("Введи город, где ты живешь - ")
    email = input("Введи свой email - ")
    phone = input("Введи номер телефона - ")

    print(f'Данные о пользователе: {parameters(name=name, surname=surname, year_birthday=year_birthday, city=city, email=email, phone=phone)}')

else:
    print("Тогда я завершаю свою работу.")
