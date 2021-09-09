names_list = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]


def thesaurus_adv(names_list):
    full_thesaurus = {}
    inner_thesaurus = {}
    inner_thesaurus_list = []
    name_fletter_list = []
    surname_fletter_list = []
    for name in names_list:
        surname_fletter = name[name.index(' ') + 1]
        surname_fletter_list.append(surname_fletter)
        name_fletter = name[0]
        name_fletter_list.append(name_fletter)
    for i in name_fletter_list:
        if name_fletter_list.count(i) > 1:
            name_fletter_list.remove(i)
    for i in surname_fletter_list:
        if surname_fletter_list.count(i) > 1:
            surname_fletter_list.remove(i)
    for surname_letter in surname_fletter_list:
        for name_letter in name_fletter_list:
            for name in names_list:
                if name[name.index(' ') + 1] == surname_letter:
                    if name[0] == name_letter:
                        inner_thesaurus_list.append(name)
            if len(inner_thesaurus_list) > 0:
                inner_thesaurus.update({name_letter: inner_thesaurus_list.copy()})
                inner_thesaurus_list.clear()
        full_thesaurus.update({surname_letter: inner_thesaurus.copy()})
        inner_thesaurus.clear()
    return full_thesaurus

for key, value in thesaurus_adv(names_list).items():
    print(key, ":", value)
