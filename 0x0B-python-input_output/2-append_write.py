#!/usr/bin/python3
"""This appends a string at the end of a text file (UTF8)."""


def append_write(filename="", text=""):
    """Return the number of characters added"""
    with open(filename, "a", encoding="utf-8") as fn:
        return fn.write(text)
