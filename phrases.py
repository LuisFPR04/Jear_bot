from random import randint

def phrase_arch():
    arch = open("citas_famosas.csv", "r", encoding='utf_8')
    phrase_list = []
    for i in arch:
        phrase = tuple(i.replace("\n", "").rsplit(";"))
        phrase_list.append(phrase)
    arch.close()
    return phrase_list

def ran_phrase_from(key):

    phrase_list = phrase_arch()
    filtered_phrases = list(filter(lambda x: x[2] == key.lower(), phrase_list))
    filtered_phrases_range = len(filtered_phrases)
    phrase_index = randint(0, filtered_phrases_range-1)

    return filtered_phrases[phrase_index]

def random_phrase():
    
    phrase_list = phrase_arch()
    list_index_range = len(phrase_list)
    phrase_list_index = randint(0, list_index_range-1)
    
    return phrase_list[phrase_list_index]


