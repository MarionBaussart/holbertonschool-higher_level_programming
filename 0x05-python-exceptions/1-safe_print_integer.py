#!/usr/bin/python3
"""
function that prints an integer with "{:d}".format().
"""


def safe_print_integer(value):

    try:
        if isinstance(value, int):
            print("{}".format(value))
            return True
    except:
        return False
