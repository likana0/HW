name_animal_1 = 'кошка'
name_animal_2 = 'собака'

print('Домашние любимцы бывают разные, например', name_animal_1, 'или', name_animal_2 + '.')

print('А ты любишь пауков?')
user_question = input()
yes_question = ['да', 'Да', 'yes', 'Yes', 'lf', 'Lf']

if user_question in yes_question:
    print(f'Круто!\n(твой ответ:{user_question})')

else:
    print(f'Не все их любят, это да...\n(твой ответ:{user_question})')

print('А сколько у них лапок?')
user_question_spider = input()

if user_question_spider == '8':
    print(f'Ты абсолютно прав!\n(твой ответ:{user_question_spider})')

else:
    print(f'А я думала, что 8...\n(твой ответ:{user_question_spider})')



