#!/usr/bin/python3
""" Define a square with properties and private variables"""


class Square:
    """ New Square class. """

    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        """ property size to retrieve it """
        return self.__size

    @size.setter
    def size(self, value):
        """ setting value of size

        Args:
            value (int): size of square

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ return area of square """

        return (self.__size ** 2)
