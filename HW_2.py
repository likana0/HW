with open('HW_2.txt', 'r', encoding='utf-8') as f:
    word_count = []
    for line, count in enumerate(f, 1):
        word_count.append(f'{line}. {" ".join(count.split())} - {len(count.split())} слово(а) в строке')

    print(*word_count, f'Всего строк в файле - {len(word_count)}', sep='\n')
