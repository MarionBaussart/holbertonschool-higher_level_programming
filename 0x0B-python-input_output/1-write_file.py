#!/usr/bin/python3
""" module contain function write_file
"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file (UTF8) and
        returns the number of characters written
        Args:
            filename: name of the file
            text: text to write
        Return:
            number of characters written
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        nb_char_written = file.write(text)

    return nb_char_written
