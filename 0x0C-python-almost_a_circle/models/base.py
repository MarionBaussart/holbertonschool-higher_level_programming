#!/usr/bin/python3
"""
module containing class Base
"""


class Base:
    """ Base class
    private class attribute __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize the base of a class
        Args:
            self: first argument to instance methods
            id: public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
