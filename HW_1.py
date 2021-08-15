from sys import argv


def pay():
    try:
        hours, rate_per_hour, prize = map(float, argv[1:])
        print(f"Зарплата работника - {hours * rate_per_hour + prize}")

    except ValueError:
        print("Надо ввести 3 числа!")

pay()
