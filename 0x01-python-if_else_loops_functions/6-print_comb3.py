#!/usr/bin/python3
for y in range(0, 10):
    for z in range(y + 1, 10):
        if y == 8 and z == 9:
            print("{}{}".format(y, z))
        else:
            print("{}{}".format(y, z), end=", ")
