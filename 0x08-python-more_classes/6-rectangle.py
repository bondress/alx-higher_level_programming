#!/usr/bin/python3
"""Define a class named Rectangle."""


class Rectangle:
    """
    Representing a rectangle.

    Attribute:
        number_of_instances (int): number of rectangle instances
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializing a new Rectangle.
        Args:
            width (int): width of the new rectangle.
            height (int): height of the new rectangle.
        Raise:
        TypeError: if the size is not an integer
        ValueError: if the size is less than zero
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        Return printable representation of rectangle

        Shows rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return("")

        n_rect = []
        for x in range(self.__height):
            [n_rect.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                n_rect.append("\n")
        return ("".join(n_rect))

    def __repr__(self):
        """Return string representation of rectangle."""
        n_rect = "Rectangle(" + str(self.__width)
        n_rect += ", " + str(self.__height) + ")"
        return (n_rect)

    def __del__(self):
        """Print a message every time a rectangle is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
