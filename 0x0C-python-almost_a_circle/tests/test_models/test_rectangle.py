#!/usr/bin/python3
""" Rectangle testing """
import unittest

from models.base import Base
from models.rectangle import Rectangle


class rectangle_t(unittest.TestCase):
    """ Testing """
    def Test_normal(self):
        rect1 = Rectangle(1,1)
        self.assertEqual(rect1.width, 1)
        self.assertEqual(rect1.height, 1)
        self.assertEqual(rect1.x, 0)
        self.assertEqual(rect1.y, 0)

        rect2 = Rectangle(1, 2, 1)
        self.assertEqual(rect2.width, 1)
        self.assertEqual(rect2.height, 2)
        self.assertEqual(rect2.x, 1)
        self.assertEqual(rect2.y, 0)

        rect3 = Rectangle(1, 2, 2, 3)
        self.asserEqual(rect3.width, 1)
        self.assertEqual(rect3.height, 2)
        self.assertEqual(rect3.x, 2)
        self.assertEqual(rect3.y, 3)

        rect4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect4.width, 1)
        self.assertEqual(rect4.height, 2)
        self.assertEqual(rect4.x, 3)
        self.assertEqual(rect4.y, 4)
        self.assertEqual(rect4.id, 5)

    def Test_missing_args(self):

        with self.assertRaises(TypeError) as cm:
            rect_1 = Rectangle()
        msg = "__init__() missing 2 required positional arguments: 'width' and 'height'"
        self.assertEqual(str(cm.exception), msg)

        with self.assertRaises(TypeError) as cm:
            rect_1 = Rectangle(1)
        msg = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(cm.exception), msg)
