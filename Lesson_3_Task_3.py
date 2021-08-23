def thesaurus(names_list):
    thesaurus_names = {}
    used_letters = []
    lettername_list = []
    for name in names_list:
        letter = name[0]
        if used_letters.count(letter) == 0:
            for name_2 in names_list:
                letter_2 = name_2[0]
                if letter_2 == letter:
                    lettername_list.append(name_2)
            used_letters.append(letter)
            thesaurus_names.update({letter: lettername_list})
            lettername_list = []
    return thesaurus_names


print(thesaurus(["Иван", "Мария", "Петр", "Илья"]))
