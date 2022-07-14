"""Test for base.py"""

import unittest
from models.base import Base

class base_t(unittest.TestCase):
    """ test the id """
    def test_base_id(self):
        """ first test method """
        i1 = Base()
        i2 = Base()
        i3 = Base()
        i4 = Base(500)
        i5 = Base(100)
        i6 = Base(None)
        i7 = Base(id=80)
        self.assertEqual(i1.id, 1)
        self.assertEqual(i2.id, 2)
        self.assertEqual(i3.id, 3)
        self.assertEqual(i4.id, 500)
        self.assertEqual(i5.id, 100)
        self.assertEqual(i6.id, 4)
        self.assertEqual(i7.id, 80)
