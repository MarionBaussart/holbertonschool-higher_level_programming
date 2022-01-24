#!/usr/bin/python3
"""
class Rectangle that defines a rectangle
"""


class Rectangle:
    """ class that defines a rectangle """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initialize the size of a rectangle
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ return private instance attribute width of a rectangle """
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
        """ return private instance attribute height of a rectangle """
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

    def area(self):
        """
        Public instance method
        returns the rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Public instance method
        returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """
        Public instance method
        returns a printable string representing the rectangle
        """
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        else:
            for i in range(self.__height):
                rectangle += ("#" * self.__width) + "\n"
            return rectangle

    def __repr__(self):
        """
        Public instance method
        returns the rectangle caracteristiques
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Public instance method
        Print the message Bye rectangle...
        when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
