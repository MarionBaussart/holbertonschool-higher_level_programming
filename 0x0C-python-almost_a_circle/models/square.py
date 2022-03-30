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

    def __str__(self):
        """
        Public instance method
        Args:
            self: first argument to instance methods
        returns: [Square] (<id>) <x>/<y> - <size>
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width))
