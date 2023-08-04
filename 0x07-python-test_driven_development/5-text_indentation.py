#!/usr/bin/python3
"""Defines a function that indents texts."""


def text_indentation(text):
    """This function prints a text with two
    new lines after each ".", "?", or ":"

    Args:
        text (str): The text to be printed

    Raises:
        TypeError: If the text is not a string

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cnt = 0
    while cnt < len(text) and text[cnt] == " ":
        cnt = cnt + 1

    while cnt < len(text):
        print(text[cnt], end="")
        if text[cnt] == "\n" or text[cnt] in ".?:":
            if text[cnt] in ".?:":
                print("\n")
            cnt = cnt + 1
            while cnt < len(text) and text[cnt] == " ":
                cnt = cnt + 1
            continue
        cnt = cnt + 1
