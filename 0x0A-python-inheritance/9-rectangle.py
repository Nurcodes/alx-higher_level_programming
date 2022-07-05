#!/usr/bin/python3
"""
Contains definition of class Rectangle that inherits from
BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Create Rectangle class
        this class validates width and height
    """

    def __init__(self, width, height):
        """ Init method for objects i
            Args:
                width: width
                height: height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """ Returns area of validated width and height """
        return self.__width * self.__height

    def __str__(self):
        """ Dunder print/str method to str an object """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
