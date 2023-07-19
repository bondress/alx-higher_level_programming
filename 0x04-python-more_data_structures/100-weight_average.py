#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)

    scores = 0
    weights = 0

    for score, weight in my_list:
        scores += score * weight
        weights += weight

    return (scores / weights)
