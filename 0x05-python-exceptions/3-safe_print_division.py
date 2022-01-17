#!/usr/bin/python3
"""
function that prints the first x elements of a list and only integers
"""


def safe_print_division(a, b):

    try:
        quotient = a / b

    except ZeroDivisionError:
        quotient = None

    finally:
        print("Inside result: {}".format(quotient))
        return quotient
