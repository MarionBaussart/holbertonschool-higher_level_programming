#!/usr/bin/python3
""" module contain function from_json_string
"""
import json


def from_json_string(my_str):
    """ function that returns an object (Python data structure)
        represented by a JSON string
        (Deserialize a JSON string to a Python object)
        Args:
            my_str: JSON string
        Return:
            an object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
