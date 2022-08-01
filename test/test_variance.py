import unittest
import sys
sys.path.append("..")

import src.math_functions as module


class test_variance_positive(unittest.TestCase):
    def test_5_element_A(self):
        A=[1.89,2.1,1.75,1.98,1.85]
        expected=0.014
        result = round(module.m_variance(A),3)
        self.assertEqual(result,expected)

    def test_5_element_B(self):
        B=[1.94,1.9,1.97,1.89,1.87]
        expected=0.0013
        result = round(module.m_variance(B),4)
        self.assertEqual(result,expected)

if __name__ == '__main__':
    unittest.main()