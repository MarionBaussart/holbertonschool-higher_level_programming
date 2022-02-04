#!/usr/bin/python3
""" module contain function class_to_json """


def class_to_json(obj):
    """ function that returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    Args:
        obj: object
    Return: dictionary description
    """
    return obj.__dict__
