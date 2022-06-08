#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weighted_scores = 0
    weights = 0
    for tup in my_list:
        weighted_scores += tup[0] * tup[1]
        weights += tup[1]
    return weighted_scores / weights
