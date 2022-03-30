#!/usr/bin/python3
"""
module containing class Square
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a square
        Args:
            self: first argument to instance methods
            size: private instance attribute size of square
            x: private instance attribute
            y: private instance attribute
            id: public instance attribute
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter, return the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ set the size """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        """
        Public instance method
        Args:
            self: first argument to instance methods
        returns: [Square] (<id>) <x>/<y> - <size>
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width))

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
                self.width = args[1]
                self.height = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
