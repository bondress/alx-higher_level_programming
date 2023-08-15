#!/usr/bin/python3
"""This is a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file"""
    with open(filename) as fn:
        return json.load(fn)
