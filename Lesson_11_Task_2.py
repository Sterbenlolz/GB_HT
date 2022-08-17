class le_Error(Exception):
    def __init__(self, txt):
        self.txt = txt


num_1 = input('Привет. Я программа, которая делит числа. Пожалуйста, введите число - делимое: ')
num_2 = input('Теперь введите число - делитель: ')
try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    if num_2 == 0:
        raise le_Error('На ноль делить нельзя!')
except le_Error as err:
    print(err)
except ValueError:
    print('Один из вводов содержит не число.')
else:
    res = num_1 / num_2
    print(f'Результат деления - {res}')
