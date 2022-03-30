#!/usr/bin/python3
"""
module containing class Base
"""


class Base:
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize the base of a class
        Args:
            self: first argument to instance methods
            id: public instance attribute id
        """
        if id is not None:
            self.__id = id
        else:
            Base.__nb_objects += 1
            self.__id = Base.__nb_objects
