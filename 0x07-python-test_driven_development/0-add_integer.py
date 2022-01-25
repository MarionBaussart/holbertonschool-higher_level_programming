#!/usr/bin/python3
"""
Module containing addition function
"""


def add_integer(a, b=98):
    """ function that adds 2 integers
    Args:
        a: first integer or float
        b: second integer or float
    Return: an integer: the addition of a and b
    Raise: TypeError if a or b aren't integers or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
