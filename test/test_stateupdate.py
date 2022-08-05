"""This module tests the state_update method
"""
import unittest
import sys
sys.path.append("..")
import src.math_functions as module

class TestStaticSystemPostive(unittest.TestCase):
    """Tests the positive path of the 1D kalman filter state update method
    """
    def test_initial_estimate(self):
        """Tests an initial prediction with kalman gain of 1
        """
        initial = 1000
        measurement = 1030
        prediction = module.state_update(initial,measurement,1)
        self.assertEqual(prediction,1030)

    def test_single_iteration(self):
        """Tests single iteration of the state_update equation
        """
        previous_estimate = 1030
        measurement = 989
        gain=1/2
        prediction = module.state_update(previous_estimate,measurement,gain)
        self.assertEqual(prediction,1009.5)

    def test_series_estimate(self):
        """Tests a series of values that represent noisy measurements of a
        static, one-dimensional system.
        """
        initial = 1000
        prediction = initial
        gain_log = []
        measurements = [1030, 989, 1017, 1009, 1013, 979, 1008, 1042, 1012, 1011]
        estimate_log = []


        for i,val in enumerate(measurements):
            prediction = module.state_update(prediction,val,1/(i+1))
            estimate_log.append(round(prediction,2))
            gain_log.append(1/(i+1))

        gain_log_expected = [1,1/2,1/3,1/4,1/5,1/6,1/7,1/8,1/9,1/10]
        self.assertEqual(gain_log, gain_log_expected)
        estimate_log_expected = [1030.00,1009.50,1012.00,1011.25,1011.60, \
            1006.17,1006.43,1010.88,1011.00,1011.00]
        self.assertEqual(estimate_log, estimate_log_expected)

if __name__ == '__main__':
    unittest.main()
