class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_of_asphalt(self):
        return f"{self._length} м * {self._width} м * 25 кг * 5 см = {(self._length * self._width * 25 * 5) / 1000} т"


user_road = Road(123456, 12)
print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна:\n{user_road.mass_of_asphalt()}')

