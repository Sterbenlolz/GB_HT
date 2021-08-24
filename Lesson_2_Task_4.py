data_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']
print(id(data_list))
for elem in data_list:
    if elem.count(' ') > 1:
        res = elem.replace(' ', '', elem.count(' ') - 1)
        data_list.insert(data_list.index(elem), res)
        data_list.remove(elem)
for elem in data_list:
    name_list = list(elem)
    for i in list(elem):
        if i != ' ':
            name_list.remove(i)
        else:
            name_list.remove(i)
            break
    name_str = "".join(name_list)
    data_list.insert(data_list.index(elem), name_str)
    data_list.remove(elem)
for elem in data_list:
    cap_str = elem.capitalize()
    data_list.insert(0, cap_str)
    data_list.remove(elem)
data_list.reverse()
print(id(data_list))
print(data_list)
for elem in data_list:
    print('Привет, {}!'.format(elem))
