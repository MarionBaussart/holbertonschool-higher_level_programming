#!/usr/bin/python3
""" module contain function read_file
"""


def read_file(filename=""):
    """ function that reads a text file (UTF8) and prints it to stdout
        Args:
            filename: name of the file
        Return:
            no return
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
