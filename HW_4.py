def my_func(x, y):

    """Принимает 2 позиционных аргумента x и y.
    x - действительное положительное число.
    y - целое отрицательное число.
    Возводит x в степень y.
    Предусмотрена проверка на тип вводимых данных
    """

    try:
        result = x ** y
        return result

    except TypeError:
        return "Это же не число..."


def my_func_2(x, y):

    """Принимает 2 позиционных аргумента x и y.
        x - действительное положительное число.
        y - целое отрицательное число.
        Возводит x в степень y.
        Если y == 0, возвращает 1.
        """

    return 1 if y == 0 else my_func_2(x, y + 1) * 1 / x


x = int(input('Введи действительное положительное число - '))
y = float(input('Введи целое отрицательное число - '))

print(f'1 вариант решения: - {my_func(x, y)}')
print(f'2 вариант решения: - {my_func_2(x, y)}')