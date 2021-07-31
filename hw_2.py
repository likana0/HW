user_second = int(input('Введи время в секундах - '))

minute = user_second // 60
if minute > 59:
    hours = minute // 60
    minute = minute % 60

else:
    hours = 0

second = user_second % 60

print(f'У нас получилось: {hours}ч:{minute}м:{second}с')

print('Теперь давай посчитаем сколько тебе лет в днях =)')
user_day = int(input('Введи свой возраст - '))

print(f'{user_day * 365} - столько тебе дней!')
