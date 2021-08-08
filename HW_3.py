def my_func(user_numb1, user_numb2, user_numb3):

    """Принимает 3 позиционных аргумента user_numb1, user_numb2, user_numb3.
    Выбирает 2 самых больших числа и складывает их.
    Выводит 2 самых больших числа и сумму этих чисел.
    """

    numbers = [user_numb1, user_numb2, user_numb3]

    try:

        max_number1 = max(numbers)
        numbers.pop(numbers.index(max_number1))
        max_number2 = max(numbers)

        print(f'2 самых больших числа из введенных тобой - {max_number1}, {max_number2}')
        print(f'Сумма двух самых больших чисел - {max_number1 + max_number2}')

    except TypeError:

        return "Enter only a numbers"


print('Введи 3 числа:')

user_numb1 = int(input("Введи первое число - "))
user_numb2 = int(input("Введи второе число - "))
user_numb3 = int(input("Введи третье число - "))

my_func(user_numb1, user_numb2, user_numb3)