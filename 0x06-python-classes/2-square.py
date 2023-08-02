#!/usr/bin/python3
"""Define a class named Square."""


class Square:
    """Representing a square."""

    def __init__(self, size=0):
        """Initializing a new Square.
        Args:
            size (int): shows the size of the new square.
        Raise:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
