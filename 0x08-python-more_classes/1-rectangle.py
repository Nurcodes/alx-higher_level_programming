#!/usr/bin/python3
""" Define a rectangle class """


class Rectangle:
    """ New rectangle class """

    def __init__(self, width=0, height=0):
        """ initialize a new rectancle instance

        Args:
            width (int): width of rectangle object
            height (int): height of rectangle object
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Get/set the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle"""
        return self.height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
