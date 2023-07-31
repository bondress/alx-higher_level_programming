#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0
    for r in range(1, 3):
        try:
            if r > a:
                raise Exception('Too far')
            else:
                res += (a ** b) / r
        except Exception:
            res = (b + a)
            break
    return (res)
