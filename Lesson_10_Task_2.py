from abc import ABC, abstractmethod

class Clothes(ABC):
    expenses_count = 0

    @abstractmethod
    def expence(self):
        pass

class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Coat.expenses_count += self.expence

    def __str__(self):
        return f'Пальто размера {self.size} требует расхода ткани {self.expence}, общий расход ткани {Coat.expenses_count}'

    @property
    def expence(self):
        calc = self.size / 6.5 + 0.5
        return float(calc)

class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        Suit.expenses_count += self.expence

    def __str__(self):
        return f'Костюм роста {self.height} требует расхода ткани {self.expence}, общий расход ткани {Suit.expenses_count}'

    @property
    def expence(self):
        calc = self.height * 2 + 0.3
        return float(calc)

itm_1 = Coat(65)
print(itm_1)
itm_2 = Suit(185)
print(itm_2)
itm_3 = Coat(78)
print(itm_3)
itm_4 = Suit(177)
print(itm_4)