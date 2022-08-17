import re

class this_is_UNACCEPTABLEEEE(Exception):
    def __init__(self, txt):
        self.txt = txt


list = []
print('Привет. Я программа для записи чисел в список.')
while True:
    num = input('Пожалуйста, введите число для записи: ')
    if num == 'stop':
        print(list)
        break
    try:
        if re.compile(r'[^0-9, .]').search(num):
            raise this_is_UNACCEPTABLEEEE('The words in list are... are... UNACCEPTABLEEEEEE!!!')
    except this_is_UNACCEPTABLEEEE as t:
        print(t)
    else:
        num = float(num)
        list.append(num)
