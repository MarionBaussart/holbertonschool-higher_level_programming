#!/usr/bin/python3
""" module containing class Student
"""


class Student:
    """ class that defines a student """

    def __init__(self, first_name, last_name, age):
        """ Instantiation
        Args:
            self: first argument to instance methods
            first_name: public instance attribute
            last_name: public instance attribute
            age: public instance attribute
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Public method that retrieves a dictionary representation
            of a Student instance
        Args:
            self: first argument to instance methods
        Return: dictionary description
        """
        return self.__dict__
