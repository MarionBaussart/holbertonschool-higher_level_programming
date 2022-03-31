#!/usr/bin/python3
"""
module containing class Rectangle
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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter, return the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter, return the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ getter, return the position x of the rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ set the position x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ getter, return the position y of the rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """ set the position y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ Public instance method : area of a rectangle
        Args:
            self: first argument to instance methods
        Return: area value of the rectangle instance
        """
        return self.__height * self.__width

    def display(self):
        """ Public instance method : prints in stdout the Rectangle instance
        with the character #
        Args:
            self: first argument to instance methods
        Return: printable rectangle
        """
        for ordonnee in range(self.__y):
            print()
        for h in range(self.__height):
            for abscisse in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Public instance method
        Args:
            self: first argument to instance methods
        returns: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        Public instance method : assigns a key/value argument to attributes
        Args:
            self: first argument to instance methods
            *args: list of arguments - no-keyworded arguments
            **kwargs: double pointer to a dictionary: key/value
            (keyworded arguments)
        """
        if args is not None and len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Public instance method : dictionary representation of a Rectangle
        Args:
            self: first argument to instance methods
        Return: dictionary
        """
        return self.__dict__