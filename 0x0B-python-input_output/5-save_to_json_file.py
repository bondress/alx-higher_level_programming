#!/usr/bin/python3
"""This is a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file, using a JSON representation."""
    with open(filename, "w") as fn:
        json.dump(my_obj, fn)
