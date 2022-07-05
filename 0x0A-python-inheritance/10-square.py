#!/usr/bin/python3
""" Square class inherits from Rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square inherits from Rectangle """

    def __init__(self, size):
        """ Init method with size """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ returns area of square """
        return self.__size ** 2
