class Exclusion:
    def __init__(self, *args):
        self.user_list = []

    def input_numbers(self):

        while True:

            try:
                val = int(input('Введи значение и нажми Enter - '))
                self.user_list.append(val)
                print(f'Текущий список - {self.user_list} \n ')

            except:
                print(f"Недопустимое значение (вводи только числа)!")
                question = input(f'Будешь вводить еще числа? (y/n) ')

                if question == 'Y' or question == 'y':
                    print(try_except.input_numbers())
                elif question == 'N' or question == 'n':
                    return f'Конец программы'
                else:
                    return f'Конец программы'


try_except = Exclusion(1)
print(try_except.input_numbers())
