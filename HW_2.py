class Divide_by_null:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.denominator = second_number

    @staticmethod
    def divide_by_null(first_number, second_number):

        try:
            return (first_number / second_number)

        except:
            return (f"Давай не будем делить на ноль?")


div = Divide_by_null(15, 5)
print(Divide_by_null.divide_by_null(15, 5))
print(Divide_by_null.divide_by_null(15, -3))
print(div.divide_by_null(15, 0))
