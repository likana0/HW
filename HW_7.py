from itertools import count
from math import factorial


def generate_fact():

    """Возвращает факториалы равномерно распределенных чисел"""

    for el in count(1):
        yield factorial(el)


generate_numb = generate_fact()

x = 0

for i in generate_numb:
    if x == 4:
        break
    else:
        x += 1
        print(f'Факториал {x}! = {i}')
