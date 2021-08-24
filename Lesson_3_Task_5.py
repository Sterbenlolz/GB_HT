import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(times, flag):
    """creating a list of jokes from a pregenerated lists of words"""
    jokes_list = []
    nouns_copy = nouns.copy()
    adverbs_copy = adverbs.copy()
    adjectives_copy = adjectives.copy()
    if flag:
        for count in range(0, times):
            i = random.randint(0, len(nouns_copy) - 1)
            j = random.randint(0, len(adverbs_copy) - 1)
            k = random.randint(0, len(adjectives_copy) - 1)
            joke = '{} {} {}'.format(nouns_copy[i], adverbs_copy[j], adjectives_copy[k])
            nouns_copy.remove(nouns_copy[i])
            adverbs_copy.remove(adverbs_copy[j])
            adjectives_copy.remove(adjectives_copy[k])
            jokes_list.append(joke)
    else:
        for count in range(0, times):
            i = random.randint(0, len(nouns_copy) - 1)
            j = random.randint(0, len(adverbs_copy) - 1)
            k = random.randint(0, len(adjectives_copy) - 1)
            joke = '{} {} {}'.format(nouns_copy[i], adverbs_copy[j], adjectives_copy[k])
            jokes_list.append(joke)
    return jokes_list

print(get_jokes(int(input('Введите количество шуток не более 5: ')), bool(input('True - без повторений слов, False - с повторениями: '))))