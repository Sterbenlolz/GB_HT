class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        if self.num >= other.num:
            return self.num - other.num
        else: raise ValueError('Число ячеек первой клетки меньше числа ячеек второй клетки')

    def __mul__(self, other):
        return self.num * other.num

    def __floordiv__(self, other):
        return self.num // other.num

    def make_order(self, row):
        result = ['*' * row for i in range(self.num // row)]
        if self.num % row:
            result.append('*' * (self.num % row))
        return '\n'.join(result)

cell_1 = Cell(20)
cell_2 = Cell(14)
print(cell_1.make_order(7))
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)