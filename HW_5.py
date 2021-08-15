from functools import reduce


def multiply_numbers(num_1, num_2):

    """Принимает 2 значения. Возвращает их умножение."""

    return num_1 * num_2


list_of_numbers = [el for el in range(100, 1001, 2)]
print(f'Список четных чисел от 100 до 1000 - {list_of_numbers}')
print(f'А если все числа умножить, то получится - {reduce(multiply_numbers, list_of_numbers)}')



