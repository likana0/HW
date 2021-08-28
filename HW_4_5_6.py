class Equipment_warehouse:

    def __init__(self, name, price, quantity, number_of_lists):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):

        try:
            unit = input(f'Введи наименование - ')
            unit_p = int(input(f'Введи цену за шт. - '))
            unit_q = int(input(f'Введите общее количество - '))
            unique = {'Модель устройства': unit, 'Цена за шт.': unit_p, 'Общее количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n{self.my_store}')
        except:
            return f'Вводи число!\nНачинаем заново:'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return Equipment_warehouse.reception(self)


class Printer(Equipment_warehouse):
    def to_print(self):
        return f'Уникально - {self.numb}'


class Scanner(Equipment_warehouse):
    def to_scan(self):
        return f'Или уникально - {self.numb}'


class Copier(Equipment_warehouse):
    def to_copier(self):
        return f'А может быть - {self.numb}'


unit_1 = Printer('Kyocera', 34999, 10, 15)
unit_2 = Scanner('Epson', 7849, 10, 15)
unit_3 = Copier('Xerox', 12099, 10, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())
