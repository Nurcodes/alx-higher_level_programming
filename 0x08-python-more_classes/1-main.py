#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(0, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 0
my_rectangle.height = 0
print(my_rectangle.__dict__)
