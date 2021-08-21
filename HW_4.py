class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} едет'

    def stop(self):
        return f'{self.name} остановилась'

    def show_speed(self):
        return f'{self.speed} км/ч - это выше чем разрешено!'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} - {self.speed}')

        if self.speed > 40:
            return f'{self.speed} км/ч - это выше чем разрешено!'
        else:
            return f'Скорость автомобиля{self.name} нормальная'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} - {self.speed}')

        if self.speed > 60:
            return f'{self.speed} км/ч - это выше чем разрешено!'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - полицейская машина'
        else:
            return f'{self.name} - не полицейская машина'


maserati = SportCar(200, 'Черный', 'Maserati', False)
toyota = TownCar(50, 'Серебристый', 'Toyota', False)
honda = WorkCar(60, 'Красный', 'Honda', True)
mercedes = PoliceCar(110, 'Белый', 'Mercedes', True)

print(f'{maserati.go()} со скоростью {maserati.show_speed()}')
print(f'Цвет автомобиля {toyota.name} - {toyota.color}')
print(f'Автомобиль {toyota.name} - полицейская машина? {toyota.is_police}')
print(mercedes.police())

