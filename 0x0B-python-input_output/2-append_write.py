#!/usr/bin/python3
""" module contain function append_write
"""


def append_write(filename="", text=""):
    """ function that appends a string at the end of a text file (UTF8)
        and returns the number of characters added
        Args:
            filename: name of the file
            text: text to append
        Return:
            number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        nb_char_added = file.write(text)

    return nb_char_added
