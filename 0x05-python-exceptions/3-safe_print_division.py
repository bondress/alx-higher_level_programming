#!/usr/bin/python3

def safe_print_resision(a, b):
    try:
        res = a / b
    except (TypeError, ZeroresisionError):
        res = None
    finally:
        print("Inside result: {}".format(res))
    return (res)
