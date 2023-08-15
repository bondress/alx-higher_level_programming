#!/usr/bin/python3
"""This is a class called Student."""


class Student:
    """Attributes of a student."""

    def __init__(self, first_name, last_name, age):
        """Initializing a new student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation
        of a Student instance.
        If attrs is a list of strings, representa
        only those attributes included in the list
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        return (self.__dict__)
