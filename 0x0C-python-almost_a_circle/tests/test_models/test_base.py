#!/usr/bin/python3
"""
module that contains the unit test cases for each classes
and methods here"""


import unittest
from models.base import Base


class Test_Base_Class_Instaniation(unittest.TestCase):
    """Test the Base class instances"""

    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_3_instances_without_args(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)
        self.assertEqual(b2.id, b3.id - 1)

    def test_None_arg_passed(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_one_instance_with_arg(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_zero_args_passed_in_two_instances(self):
        b1 = Base(0)
        b2 = Base(0)
        self.assertEqual(b1.id, b2.id)
