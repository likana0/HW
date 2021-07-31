print('Давай представим, что ты легкоатлет? И вообще за ЗОЖ в отличие от многих =)')

first_sportsman = int(input('Введи количество километров, которое ты сейчас бегаешь в день (больше 0) - '))
second_sportsman = int(input('Введи количество километров, которое ты бы ты хотел бегать в день - '))

percent_day = 0.1
day_success = 1

while second_sportsman > first_sportsman:
    first_sportsman = first_sportsman + (first_sportsman * percent_day)
    day_success = day_success + 1

print(f'Через {day_success} дней ты достигнешь своей цели! Не останавливайся! У тебя все получится!')