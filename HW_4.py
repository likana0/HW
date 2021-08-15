from random import randint


random_list = [randint(0, 10) for _ in range(15)]
list_without_repeats = [el for el in random_list if random_list.count(el) == 1]

print(f'Случайный список из чисел - {random_list}')
print(f'Список, в котором убраны повторы - {list_without_repeats}')

