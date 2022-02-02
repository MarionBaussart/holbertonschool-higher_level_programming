#!/usr/bin/python3
""" module contain function lookup """


def lookup(obj):
    """ function that returns the list of available attributes
    and methods of an object
    Args:
        obj: object
    Return: list of attributes and methods
    """
    return dir(obj)
