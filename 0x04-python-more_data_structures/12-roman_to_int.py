#!/usr/bin/python3
def roman_to_int(roman_str):
    if (not isinstance(roman_str, str) or
            roman_str is None):
        return (0)

    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    n = 0

    for i in range(len(roman_str)):
        if romans.get(roman_str[i], 0) == 0:
            return (0)
        if (i != (len(roman_str) - 1) and
                romans[roman_str[i]] < romans[roman_str[i + 1]]):
            n += romans[roman_str[i]] * -1
        else:
            n += romans[roman_str[i]]
    return (n)
