#!/usr/bin/python3
"""
function that that divides 2 integers and prints the result
"""


def safe_print_division(a, b):

    try:
        quotient = a / b

    except ZeroDivisionError:
        quotient = None

    finally:
        print("Inside result: {}".format(quotient))
        return quotient
