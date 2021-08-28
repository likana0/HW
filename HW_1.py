class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        user_date = []

        for i in day_month_year.split():
            if i != ' ': user_date.append(i)

        return int(user_date[0]), int(user_date[1]), int(user_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 1900:
                    return f'Все верно'
                else:
                    return f'Введите год в диапазоне: от 1900 до 2021'
            else:
                return f'Введите месяц в диапазоне: от 1 до 12'
        else:
            return f'Введите день в диапазоне: от 1 до 31'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('28 8 2021')
print(today)
print(Data.valid(32, 8, 2021))
print(today.valid(28, 15, 2021))
print(today.valid(28, 8, 1200))
print(Data.extract('28 8 2021'))
print(today.extract('27 7 2020'))
print(Data.valid(28, 8, 2021))
