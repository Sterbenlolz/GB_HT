class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self. position = position
        self._income = {'Wage': wage, 'Bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'
    def get_full_income(self):
        return f'{sum(self._income.values())}'

le_worker = Position('Иван', 'Иванов', 'Погромист', 50000, 10000)
print(le_worker.get_full_name())
print(le_worker.position)
print(le_worker.get_full_income())
