seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']

seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}

month_user = int(input("Введи номер любимого месяца в году - "))

if month_user == 1 or month_user == 12 or month_user == 2:
    print(f'Твой месяц относится к сезону - {seasons_dict.get(1)} (словарь)')
    print(f'Твой месяц относится к сезону - {seasons_list[0]} (спискок)')

elif month_user == 3 or month_user == 4 or month_user == 5:
    print(f'Твой месяц относится к сезону - {seasons_dict.get(2)} (словарь)')
    print(f'Твой месяц относится к сезону - {seasons_list[1]} (спискок)')

elif month_user == 6 or month_user == 7 or month_user == 8:
    print(f'Твой месяц относится к сезону - {seasons_dict.get(3)} (словарь)')
    print(f'Твой месяц относится к сезону - {seasons_list[2]} (спискок)')

elif month_user == 9 or month_user == 10 or month_user == 11:
    print(f'Твой месяц относится к сезону - {seasons_dict.get(4)} (словарь)')
    print(f'Твой месяц относится к сезону - {seasons_list[3]} (спискок)')
else:
    print("А я думала в году всего 12 месяев...")
