# Start Program
"""
""
Program: test_inner_function.py
Author: Paul Thairu
Last date modified: 06/017/2020

Write a function multiply_string() that takes a string message
and a number n and returns the string with message printed n times.
"""

import unittest

from area_perimeter import inner_functions_assignment as ass


class MyTestCase(unittest.TestCase):
    def test_measurement_rectangle(self):
        self.assertEqual(ass.measurements([2.1, 3.4]), "Perimeter = 11.0 Area = 7.14")

    def test_measurements_square(self):
        self.assertEqual(ass.measurements([3.5]), "Perimeter = 14.0 Area = 12.25")


if __name__ == '___main___':
    unittest.main()

