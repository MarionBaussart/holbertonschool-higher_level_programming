#!/usr/bin/python3
"""
function that prints an integer.
"""


def safe_print_integer_err(value):

    try:
        print("{:d}".format(value))
        return True
    except:
        print("Exception: {}".format(value))
        return False
