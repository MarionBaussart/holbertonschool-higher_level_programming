#!/usr/bin/python3
"""
Write a class Square that defines a square
"""


class Square:
    """ class Square that defines a square """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the size of the square
        @size: private instance attribute, size of the square
        @position: private instance attribute, position to print the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        returns the size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set the size of a square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        returns the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        set the position of the square
        """
        if not instance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not instance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not instance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Public instance method
        returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Public instance method : prints in stdout the square
        with the character # at a given position
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
