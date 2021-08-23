print(type(15 * 3), type(15 / 3), type(15 // 2), type(15 ** 2))

data_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+6', 'градусов']
print(id(data_list))
for i in data_list[:]:
    if i.isdigit() == False:
        element = list(i)
        result = list(i)
        for j in element:
            if j.isdigit() == False:
                element.remove(j)
        if len(element) == 1:
            element.insert(0, '0')
            for k in result:
                if k.isdigit(): result.remove(k)
            result = result + element
            data_list.insert(data_list.index(i), "".join(result))
            data_list.insert(data_list.index(i) - 1, '"')
            data_list.insert(data_list.index(i), '"')
            data_list.remove(i)
    else:
        data_list.insert(data_list.index(i) + 1, '"')
        data_list.insert(data_list.index(i), '"')
        if len(list(i)) == 1:
            digit = list(i)
            digit.insert(0, '0')
            data_list.insert(data_list.index(i) + 1, "".join(digit))
            data_list.remove(i)
print(data_list)
data_str = " ".join(data_list)
for i in range(0, data_list.count('"') // 2):
    data_str = data_str.replace(' " ', ' "', 1)
    data_str = data_str.replace(' " ', '" ', 1)
print(id(data_list))
print(data_str)
