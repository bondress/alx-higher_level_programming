#!/usr/bin/python3
"""This function writes a string to a text file (UTF8)."""


def write_file(filename="", text=""):
    """Return the number of characters written."""
    with open(filename, "w", encoding="utf-8") as fn:
        return fn.write(text)
