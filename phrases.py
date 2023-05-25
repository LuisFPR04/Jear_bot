from random import randint

def ran_phrase(key):
    arch = open("citas_famosas.csv", "r", encoding='utf_8')
    phrase_list = []
    for i in arch:
        phrase = tuple(i.replace("\n", "").rsplit(";"))
        phrase_list.append(phrase)
    #print(phrase_list)

    filtered_phrases = list(filter(lambda x: x[2] == key.lower(), phrase_list))
    filtered_phrases_range = len(filtered_phrases)
    phrase_index = randint(0, filtered_phrases_range-1)
    print(phrase_index)
    #print(phrase_index)
    arch.close()
    return filtered_phrases[phrase_index]
