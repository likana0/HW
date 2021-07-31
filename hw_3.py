user_number = str(input('Введи любое число - '))

print('А давай склеим твое число с точно таким же?')
user_number_2 = user_number + user_number
print(f'Получилось - {user_number_2}')

print('Может быть еще раз?')
user_number_3 = user_number + user_number + user_number
print(f'Теперь получилось - {user_number_3}')

print('А теперь сложим это все вместе не склеивая =)')
user_number_4 = int(user_number) + int(user_number_2) + int(user_number_3)
print(f'Сумма всех наших чисел - {user_number_4}')

