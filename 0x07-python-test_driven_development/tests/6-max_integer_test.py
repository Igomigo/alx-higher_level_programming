#!/usr/bin/python3
"""unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unittest class for the max_integer function"""
    def test_module_docstring(self):
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        func = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(func) > 1)

    def test_all_positive_integer_list(self):
        result = max_integer([1, 3, 5, 7, 4])
        self.assertEqual(result, 7)

    def test_positive_negative_integer_list(self):
        result = max_integer([1, -3, 4, -5,])
        self.assertEqual(result, 4)

    def test_all_negative_integer_list(self):
        result = max_integer([-1, -2, -2, -3, -5])
        self.assertEqual(result, -1)

    def test_no_argument_passed(self):
        result = max_integer()
        self.assertEqual(result, None)

    def test_single_integer_list(self):
        result = max_integer([1])
        self.assertEqual(result, 1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_None_argument_passed(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_string_and_integers_args(self):
        with self.assertRaises(TypeError):
            max_integer([1, "a", 3, 4, 5])

    def test_string(self):
        self.assertEqual(max_integer(["a", "z"]), "z")

    def test_neg_float(self):
        self.assertEqual(max_integer([-5.55, -66.66, -111.1]), -5.55)

if __name__ == '__main__':
    unittest.main()
