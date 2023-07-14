#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mults = []

    for n in my_list:
        if n % 2 == 0:
            mults.append(True)
        else:
            mults.append(False)
    return (mults)
