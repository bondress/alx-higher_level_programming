#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    tot_elems = 0
    for i in range(r):
        try:
            print("{}".format(my_list[i]), end="")
            tot_elems += 1
        except IndexError:
            break
    print()
    return(tot_elems)
