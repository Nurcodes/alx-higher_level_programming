#!/usr/bin/python3
""" Define a square with properties and private variables"""


class Square:
    """ New Square class. """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ property size to retrieve it """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ property position to retrieve it """

        return (self.__position)

    @position.setter
    def position(self, value):
        """ setting postion values """
        if not isinstance(value, tuple >= (0, 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ return current area of square."""

        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""

        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
