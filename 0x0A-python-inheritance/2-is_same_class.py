#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ function that returns True if the object is exactly
        an instance of the specified class ; otherwise False
        Args:
            obj: object
            a_class: class
        Return:
            True or false
    """
    return type(obj) is a_class