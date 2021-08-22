class Cell:
    def __init__(self, count: int):
        self._count = count

    def __add__(self, other):
        return Cell(self._count + other._count)

    def __sub__(self, other):
        if self._count > other._count:
            return Cell(self._count - other._count)

        print(f"{self._count} - {other._count} - недопустимо!")

    def __mul__(self, other):
        return Cell(self._count * other._count)

    def __truediv__(self, other):
        return Cell(self._count // other._count)

    def cells_in_row(self, per_row: int) -> str:
        rows, cells = self._count // per_row, self._count % per_row
        return '\n'.join(['*' * per_row] * rows + (['*' * cells] if cells else []))

    def __str__(self) -> str:
        return f"Клетка состоит из {self._count} ячеек"


if __name__ == '__main__':
    c1 = Cell(3)
    print(c1)
    c2 = Cell(5)
    print(c2)

    print(c1 + c2)
    print(c1 - c2)
    print(c2 - c1)
    print(c2 - c2)
    print(c1 * c2)
    print(c1 / c2)
    print((c1 * c2).cells_in_row(23))