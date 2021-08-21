from time import sleep


class TrafficLight:
    __color = "Цвет"

    @staticmethod
    def running():
        while True:
            print(f'\r\033[1m\033[31mКрасный сигнал светофора! Стой!', end="")
            sleep(7)
            print(f'\r\033[1m\033[33mЖелтый сигнал светофора! Жди!', end="")
            sleep(2)
            print(f'\r\033[1m\033[32mЗеленый сигнал светофора! Вперёд!', end="")
            sleep(10)
            print(f'\r\033[1m\033[33mЖелтый сигнал светофора! Жди!', end="")
            sleep(2)


traffic_light = TrafficLight()
traffic_light.running()
