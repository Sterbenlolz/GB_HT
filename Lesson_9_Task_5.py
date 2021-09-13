class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки...')

class Pen(Stationery):
    def draw(self):
        print(f'Это ручка {self.title}. Ей пишут, а не рисуют, вообще-то!')

class Pencil(Stationery):
    def draw(self):
        print(f'Сейчас мы будем рисовать карандашом {self.title}!')

class Handle(Stationery):
    def draw(self):
        print(f'Это маркер {self.title}. Им выделяют текст.')

stationery = Stationery('Канцелярочка')
stationery.draw()
print(stationery.title)

pen = Pen('Паркер')
pen.draw()

pencil = Pencil('Белка')
pencil.draw()

handle = Handle('BIC')
handle.draw()