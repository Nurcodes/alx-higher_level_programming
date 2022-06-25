#!/usr/bin/python3
""" Define Square class which takes size """


class Square:
    """ Creating square with size """
    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
