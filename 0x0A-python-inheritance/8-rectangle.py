#!/usr/bin/python3
"""Creates a class called Rectangle that
inherits from the BaseGeometry class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intializing a new Rectangle.
        Args:
            width (int): the width of the new rectangle.
            height (int): height of the new rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
