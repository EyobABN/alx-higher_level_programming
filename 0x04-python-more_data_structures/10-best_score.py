#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    score_exists = False
    for key in a_dictionary:
        if a_dictionary[key]:
            score_exists = True
    if score_exists is False:
        return None
    return max(a_dictionary, key=a_dictionary.get)
