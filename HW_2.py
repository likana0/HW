import random


def generate_items():

    """Создает список случайных чисел [0;100) и возвращает 6 значений"""

    numbers = range(0, 100)
    return random.sample(numbers, 6)


items_more = generate_items()
larger_number = [items_more[num] for num in range(1, len(items_more)) if items_more[num] > items_more[num - 1]]

print(f'Сегодня случайными числами будут - {items_more}')
print(f'Элементы, значения которых больше предыдущего элемента - {larger_number}')
