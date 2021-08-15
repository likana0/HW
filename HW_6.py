from itertools import count, cycle


print('Скрипт генерирует целые числа, начиная с указанного и до 10.')
for numb in count(int(input('Введи первое число - '))):
    print(numb)

    if numb == 10:
        break

print('Скрипт повторяет введенные числа. Для генерации следующего повторения необходимо нажать Enter (выход - "q")')
user_numb = input('Введи числа через пробел - ').split()
iter_ = cycle(user_numb)
compl_script = None

while compl_script != 'q':
    print(next(iter_), end='')
    compl_script = input()

