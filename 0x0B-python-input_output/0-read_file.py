#!/usr/bin/python3
"""This function reads a text file."""


def read_file(filename=""):
    """Print the contents of the text file(UTF8) to stdout."""
    with open(filename, encoding="utf-8") as fn:
        print(fn.read(), end="")
