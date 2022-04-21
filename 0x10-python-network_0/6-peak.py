#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ find a peak """

    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    middle = int(length / 2)

    if length == 1:
        return list_of_integers[0]
    if length == 2:
        return max(list_of_integers)
    if list_of_integers[middle] >= list_of_integers[middle - 1] and\
       list_of_integers[middle] >= list_of_integers[middle + 1]:
        return list_of_integers[middle]
    if list_of_integers[middle - 1] and list_of_integers[middle] < list_of_integers[middle - 1]:
        return find_peak(list_of_integers[:middle])
    if list_of_integers[middle + 1] and list_of_integers[middle] < list_of_integers[middle + 1]:
        return find_peak(list_of_integers[middle:])
