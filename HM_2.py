numbers_first = int(input("Введи свое любимое целое число до 10 - "))
numbers_list = []

i = 0
el = 0

while i < numbers_first:
    numbers_list.append(input("А теперь введи любое число - "))
    i = i + 1
    print(f'осталось ввести еще значений: {numbers_first - i}')

for elem in range(int(len(numbers_list)/2)):
    numbers_list[el], numbers_list[el + 1] = numbers_list[el + 1], numbers_list[el]
    el = el + 2

print(numbers_list)