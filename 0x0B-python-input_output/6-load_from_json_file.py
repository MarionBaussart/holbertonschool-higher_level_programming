#!/usr/bin/python3
""" module contain function load_from_json_file
"""
import json


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file”
        Args:
            filename: file
        Return:
            Object from a “JSON file”
    """
    with open(filename) as file:
        return json.load(file)
