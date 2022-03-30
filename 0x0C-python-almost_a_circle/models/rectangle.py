#!/usr/bin/python3
"""
module containing class Base
"""
from models.base import Base

class Rectangle(Base):
    """ class Rectangle inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize a rectangle
        Args:
            self: first argument to instance methods
            width: private instance attribute width
            height: private instance attribute height
            x: private instance attribute
            y: private instance attribute
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ getter, return the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width """
        self.__width = value

    @property
    def height(self):
        """ getter, return the height of the rectangle """
        return self.__height

    @height.setter
    def heigth(self, value):
        """ set the height """
        self.__height = value

    @property
    def x(self):
        """ getter, return the position x of the rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ set the position x """
        self.__x = value

    @property
    def y(self):
        """ getter, return the position y of the rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """ set the position y """
        self.__y = value
