def class_gen(tutor, group):
    dif = len(tutor) - len(group)
    while dif > 0:
        group.append(None)
        dif = len(tutor) - len(group)
    for i, j in zip(tutor, group):
        yield (i, j)


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

le_result = class_gen(tutors, klasses)
print(next(le_result))
print(next(le_result))
print(next(le_result))
print(next(le_result))
print(next(le_result))
print(next(le_result))
print(next(le_result))
