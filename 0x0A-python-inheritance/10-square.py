#!/usr/bin/python3
""" Square class inherits from Rectangle """


Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square inherits from Rectangle """

    def __init__(self, size):
        """ Init method with size """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ returns area of square """
        return self.__size ** 2

    def __str__(self):
        """Returns dunder str"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
