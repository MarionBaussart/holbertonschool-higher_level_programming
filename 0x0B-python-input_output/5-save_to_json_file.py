#!/usr/bin/python3
""" module contain function save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file,
        using a JSON representation
        Args:
            my_obj: object
            filename: file
        Return:
            no return
    """
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
