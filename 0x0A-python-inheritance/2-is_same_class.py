#!/usr/bin/python3
"""Defines a function that checks if an
object is exactly an instance of a specified class."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specified class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True - If obj is exactly an instance of a_class.
        Otherwise - False.
    """
    return (type(obj) == a_class)
