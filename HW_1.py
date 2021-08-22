matrix_list_1 = [[1, 1, 1, 1], [3, 3, 3, 3], [4, 4, 4, 4]]
matrix_list_2 = [[9, 9, 9, 9], [7, 7, 7, 7], [6, 6, 6, 6]]


class Matrix:

    def __init__(self, m_list):
        self.m_list = m_list

    def __str__(self):
        return '\n'.join(map(str, self.m_list))

    def __add__(self, other):
        c = []
        for i in range(len(self.m_list)):
            c.append([])
            for el in range(len(self.m_list[0])):
                c[i].append(self.m_list[i][el] + other.m_list[i][el])
        return '\n'.join(map(str, c))


matrix_1 = Matrix(matrix_list_1)
matrix_2 = Matrix(matrix_list_2)

print(f'{matrix_1}\n')
print(f'{matrix_2}\n')
print(f'{matrix_1 + matrix_2}\n')