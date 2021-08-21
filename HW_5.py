from random import randint


with open('HW_5.txt', mode='w+', encoding='utf-8') as f:
    f.write(" ".join([str(randint(1, 10)) for _ in range(10)]))
    f.seek(0)

    print(sum(map(int, f.readline().split())))