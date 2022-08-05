"""This module tests the m_variance function
"""
import unittest
import sys
sys.path.append("..")
import src.math_functions as module


class TestVariancePositive(unittest.TestCase):
    """This class tests the postivie path of the variance function"""
    def test_5_element_a(self):
        """This function tests the variance for 5 elements"""
        test_array_a=[1.89,2.1,1.75,1.98,1.85]
        expected=0.014
        result = round(module.m_variance(test_array_a),3)
        self.assertEqual(result,expected)

    def test_5_element_b(self):
        """This function test the variance fucntion for a different set of 5 elements"""
        test_array_b=[1.94,1.9,1.97,1.89,1.87]
        expected=0.0013
        result = round(module.m_variance(test_array_b),4)
        self.assertEqual(result,expected)

if __name__ == '__main__':
    unittest.main()
