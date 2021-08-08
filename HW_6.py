def int_func(word):
    """Принимает слова из маленьких латинских букв.
    Печатает принятые слова с заглавной буквы.
    Если ввести цифры или кириллицу - выдаст негативное сообщение.
    """

    latin_letter = 'qazwsxedcrfvtgbyhnujmikolp'

    if not set(word).difference(latin_letter):

        return word.title()

    else:
        print('Это не подходит.')


words = input('Введи слово или несколько слов разделенных пробелами - ').split()

for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), ' ')