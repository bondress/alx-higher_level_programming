#!/usr/bin/python3
"""Creating the MyList class"""


class MyList(list):
    """This class is a subclass of the List class"""
    def __init__(self):
        """Initializing the object"""
        super().__init__()

    def print_sorted(self):
        """Printing the sorted list"""
        print(sorted(self))
