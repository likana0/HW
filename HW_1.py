with open('HW_1.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Введи данные (чтобы закрыть программу-ничего не вводи) - ')
        if not line:
            break

        f.write(f'{line}\n')
        