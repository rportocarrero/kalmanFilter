import unittest
import sys
sys.path.append("..")

import src.math_functions as module

class test_mean_positive(unittest.TestCase):
    def test_one_element(self):
        A = [1]
        self.assertEqual(module.m_mean(A),1)

    def test_5_elements(self):
        A=[5,5,10,10,10]
        self.assertEqual(module.m_mean(A), 8)

    def test_5_floats(self):
        A=[79.8,80,80.1,79.8,80.2]
        result = module.m_mean(A)
        result = round(result, 2)
        self.assertEqual(result,79.98)

if __name__ == '__main__':
    unittest.main()