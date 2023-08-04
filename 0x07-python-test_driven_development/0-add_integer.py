#!/usr/bin/python3
"""Defines a function that adds two(2) integers."""


def add_integer(a, b=98):
    """Return the sum of a and b
    (integers or floats, only; returned as integers).

    Raises:
        TypeError: If either a or b is not an integer or a float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
