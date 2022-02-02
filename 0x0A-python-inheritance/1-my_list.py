#!/usr/bin/python3
""" module contain class MyList """


class MyList(list):
    """ class MyList that inherits from list """

    def print_sorted(self):
        """ Public instance method, prints the list, sorted
            Args:
                self: first argument to instance methods
            Return:
                no return
        """
        sorted_list = sorted(self)
        print(sorted_list)
