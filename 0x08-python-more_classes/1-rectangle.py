#!/usr/bin/python3
"""
class Rectangle that defines a rectangle
"""


class Rectangle:
    """ class that defines a rectangle """

    def __init__(self, width=0, height=0):
        """ Initialize the size of a rectangle
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ return width of a rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of a rectangle
        Args:
            value: width
        Return: No return.
        Raise:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ return height of a rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height of a rectangle
        Args:
            value: height
        Return: No return.
        Raise:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
