rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open('HW_4_1.txt', 'w', encoding='utf-8') as f_1:
    with open('HW_4.txt', 'r', encoding='utf-8') as f:
        f_1.write(str([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in f]))