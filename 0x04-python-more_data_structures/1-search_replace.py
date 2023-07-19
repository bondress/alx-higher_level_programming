#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_l = []
    for it in my_list:
        if it == search:
            new_l.append(replace)
        else:
            new_l.append(it)
    return (new_l)
