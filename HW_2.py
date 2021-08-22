from abc import abstractmethod


class Сlothes:
    def __init__(self, vh):
        self.vh = vh

    @property
    def get_sq_full(self):
        return str(f'Площадь общая ткани - {(self.vh / 6.5 + 0.5) + (self.vh * 2 + 0.3)}')

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Сlothes):

    @property
    def consumption(self):
        return round(self.vh / 6.5) + 0.5

    def __str__(self):
        return f'Расход ткани на пальто - {self.consumption} м2'


class Costume(Сlothes):

    @property
    def consumption(self):
        return round(2 * self.vh + 0.3)

    def __str__(self):
        return f'Расход ткани на костюм - {self.consumption} м2'


coat = Coat(10)
costume = Costume(10)
sum = coat + costume

print(coat)
print(costume)
print(f'Общий расход ткани - {sum} м2')
