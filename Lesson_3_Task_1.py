# Для продвинутой задачи у меня есть идея просто удвоить количество ключей в словаре, но на мой взгляд это не очень хорошее решение
def num_translate(number):
    translation = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                   'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    return translation.get(number)


print(num_translate(input('Введите число от 0 до 10 на английском: ')))
