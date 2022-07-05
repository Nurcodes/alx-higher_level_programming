#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" Module for Rectangle """


class Rectangle(BaseGeometry):
    """ Create Rectangle class """

    def __init__(self, width, height):
        """ Init method for objects """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
