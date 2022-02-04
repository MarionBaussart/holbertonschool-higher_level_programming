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

    def to_json(self, attrs=None):
        """ Public method that retrieves a dictionary representation
            of a Student instance
        Args:
            self: first argument to instance methods
        Return: the attribute contained in attrs, if none return all
        """
        all_dictionary = self.__dict__
        dictionary = {}

        if type(attrs) == list:
            for name_attribute in attrs:
                if name_attribute in all_dictionary:
                    dictionary[name_attribute] = all_dictionary[name_attribute]
            return dictionary

        else:
            return all_dictionary
