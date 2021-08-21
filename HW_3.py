class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"{sum(self._income.values())}"


worker_first = Position("Иван", 'Петров', "слесарь", 50000, 5000)
worker_second = Position("Александр", 'Сидоров', "директор", 200000, 30000)

print(f'Имя сотрудника: {worker_first.get_full_name()}\nДолжность: {worker_first.position}\nЗарплата: '
      f'{worker_first.get_total_income()} руб.\n')

print(f'Имя сотрудника: {worker_second.get_full_name()}\nДолжность: {worker_second.position}\nЗарплата: '
      f'{worker_second.get_total_income()} руб.')

