#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """ function that returns if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False
        Args:
            obj: object
            a_class: class
        Return:
            True or false
    """
    return isinstance(obj, a_class)
