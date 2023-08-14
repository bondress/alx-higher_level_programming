#!/usr/bin/python3
"""Defines a function that checks if an object is an instance or
inherited instance of a class."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class or an inherited instance.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True - If obj is an instance or inherited instance of a_class.
        Otherwise - False.
    """
    return (isinstance(obj, a_class))
