#!/usr/bin/python3
""" module contain function to_json_string
"""
import json


def to_json_string(my_obj):
    """ function that returns the JSON representation of an object (string)
        (Serialize obj to a JSON formatted str)
        Args:
            my_obj: object
        Return:
            JSON representation of an object (string)
    """
    return json.dumps(my_obj)
