#!/usr/bin/python3
""" Define Square class with size and area method """


class Square:
    """ init a new square """

    def __init__(self, size=0):
        """ init a new square

        Args:
            size (int): The size of the new squre.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Return the area of the ___size """
        return (self.__size ** 2)
