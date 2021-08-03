user_text = input('Введи слова через пробелы - ')
user_word = []
num = 1
for el in range(user_text.count(' ') + 1):
    user_word = user_text.split()
    if len(str(user_word)) <= 10:
        print(f" {num} {user_word [el]}")
        num += 1
    else:
        print(f" {num} {user_word [el] [0:10]}")
        num += 1