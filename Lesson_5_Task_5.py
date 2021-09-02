src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique = set()
temp = set()
for elem in src:
    if elem not in temp:
        unique.add(elem)
    else:
        unique.discard(elem)
    temp.add(elem)
print([elem for elem in src if elem in unique])