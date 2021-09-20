# Не совсем понятно, что имеется в виду, когда говорится, что дата вводится в формате день-месяц-год.
# Это дд-мм-гг или дд-мм-гггг? Нужна ли тут проверка на формат даты? Я на всякий сделяль
# Надеюсь, я правильно понял, что вообще требуется от меня в задании

import re


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def parse(cls, date):
        if re.compile(r'(\d{2}-){2}\d{4}').search(date):
            day = int(date[0:2])
            month = int(date[3:5])
            year = int(date[6:10])
        else:
            raise ValueError('Неправильный формат даты')
        return day, month, year

    @staticmethod
    def validate(day, month, year):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if month == 2:
                if day <= 29:
                    return True
                else:
                    return False
        elif month == 2:
            if day <= 28:
                return True
            else:
                return False
        elif month in [4, 7, 9, 11]:
            if day <= 30:
                return True
            else:
                return False
        elif month <= 12:
            if day <= 31:
                return True
            else:
                return False
        else:
            return False


d_1 = '29-02-2021'
d_2 = '32-09-2030'
d_3 = '15-13-1678'
d_4 = '13-08-1997'
d_5 = 'fl-1g-2uf5'
print(Date.validate(Date.parse(d_1)[0], Date.parse(d_1)[1], Date.parse(d_1)[2]))
print(Date.validate(Date.parse(d_2)[0], Date.parse(d_2)[1], Date.parse(d_2)[2]))
print(Date.validate(Date.parse(d_3)[0], Date.parse(d_3)[1], Date.parse(d_3)[2]))
print(Date.validate(Date.parse(d_4)[0], Date.parse(d_4)[1], Date.parse(d_4)[2]))
print(Date.parse(d_1))
print(Date.parse(d_2))
print(Date.parse(d_3))
print(Date.parse(d_4))
print(Date.parse(d_5))
