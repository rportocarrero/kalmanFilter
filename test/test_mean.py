"""This module tests the m_mean function
"""
import unittest
import sys
sys.path.append("..")
import src.math_functions as module

class TestMeanPositive(unittest.TestCase):
    """This class tests the positive case for the mean function
    """
    def test_one_element(self):
        """tests the mean if there is only 1 element in the list
        """
        test_array = [1]
        self.assertEqual(module.m_mean(test_array),1)

    def test_5_elements(self):
        """tests the mean if there are 5 elements in the list
        """
        test_array=[5,5,10,10,10]
        self.assertEqual(module.m_mean(test_array), 8)

    def test_5_floats(self):
        """tests the mean if there are 5 float elements
        """
        test_array=[79.8,80,80.1,79.8,80.2]
        result = module.m_mean(test_array)
        result = round(result, 2)
        self.assertEqual(result,79.98)

if __name__ == '__main__':
    unittest.main()
