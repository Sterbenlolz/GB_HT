class Matrix():
    def __init__(self, data):
        self.data = data
        for line in self.data[:-1]:
            if not len(line) == len(self.data[self.data.index(line) + 1]):
                raise ValueError('Количество элементов в строках не совпадает')

    def __str__(self):
        return '\n'.join('\t'.join(str(num) for num in line) for line in self.data)

    def __add__(self, other):
        if not len(self.data) == len(other.data):
            raise ValueError('Размерности матриц не совпадают')
        else:
            for i in range(len(self.data)):
                if not len(self.data[i]) == len(other.data[i]):
                    raise ValueError('Размерности матриц не совпадают')
            item = [[int(self.data[line][num]) + int(other.data[line][num]) for num in
                 range(len(self.data[line]))] for line in range(len(self.data))]
            return Matrix(item)

# Если написать проверку через IndexError, размерность первой матрицы может быть меньше размерности второй матрицы и коду будет нормально,
# поэтому я написал проверку на совпадение размерностей до всего суммирования

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
mtr1 = Matrix(m1)
mtr2 = Matrix(m2)
print(mtr1)
print(mtr2)
print(mtr1 + mtr2)

m3 = [[1, 2], [3, 4], [5, 6]] # Здесь пример того, о чем я говорил: матрицы 2 * 3 и 3 * 3 складывать нельзя,
m4 = [[4, 5, 6], [6, 7, 8], [8, 9, 10]] # но IndexError это пропускает
mtr3 = Matrix(m3)
mtr4 = Matrix(m4)
print(mtr3)
print(mtr4)
print(mtr3 + mtr4)

# Вот код с IndexError:
# def __add__(self, other):
#     try:
#         item = [[int(self.data[line][num]) + int(other.data[line][num]) for num in
#                  range(len(self.data[line]))] for line in range(len(self.data))]
#         return Matrix(item)
#     except IndexError:
#         raise ValueError('Размерность матриц не совпадает')
# Можно вставить его вместо той логики, что я написал, и проверить на тех же примерах, что с ним ошибки не возникает
