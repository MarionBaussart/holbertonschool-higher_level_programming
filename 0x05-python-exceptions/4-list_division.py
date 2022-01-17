#!/usr/bin/python3
"""
function that divides element by element 2 lists
"""


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):

        try:
            quotient = my_list_1[i] / my_list_2[i]

        except TypeError:
            quotient = 0
            print("wrong type")

        except ZeroDivisionError:
            quotient = 0
            print("division by 0")

        except IndexError:
            quotient = 0
            print("out of range")

        finally:
            result.append(quotient)

    return result
