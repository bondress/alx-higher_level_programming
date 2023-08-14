#!/usr/bin/python3
"""Creating a subclass of Rectangle class called Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defining a square."""

    def __init__(self, size):
        """Initializing a new square.
        Args:
            size (int): size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
