"""this module tests a ghk filter"""
import unittest
import sys
sys.path.append("..")
import src.math_functions as module

class TestGHKStateExtrapolation(unittest.TestCase):
    """This class tests the positive path of the ghk filter modules"""
    def test_ghk_extrapolation(self):
        """Tests single extrapolate response"""
        # simulation constants
        delta_t = 5 #(s)
        range_est = 30000 #(m)
        vel_est = 50 #(m/s)
        acc_est = 0 #(m/s^2)

        range_est, vel_est, acc_est = \
            module.ghk_state_extrapolation(range_est, vel_est, acc_est, delta_t)

        exp_range_est =30250
        exp_vel_est = 50
        exp_acc_est = 0

        self.assertEqual(range_est, exp_range_est)
        self.assertEqual(vel_est, exp_vel_est)
        self.assertEqual(acc_est, exp_acc_est)

    def test_ghk_extrapolation_2(self):
        """second single pass through ghk filter extrapolation"""
        delta_t = 5
        curr_range_est = 30205
        curr_vel_est = 42.8
        curr_acc_est = -0.7

        range_pred, vel_pred, acc_pred = module.ghk_state_extrapolation(curr_range_est, curr_vel_est, curr_acc_est, delta_t)

        self.assertEqual(range_pred, 30410.2)
        self.assertEqual(vel_pred, 39.3)
        self.assertEqual(acc_pred, -0.7)

    def test_ghk_update_equation(self):
        """test single iteration of update equation"""
        alpha = 0.5
        beta = 0.4
        gamma = 0.1
        delta_t = 5
        range_est = 30250
        vel_est = 50
        acc_est = 0
        measurement = 30160

        curr_range_est, curr_vel_est, curr_acc_est = module.ghk_state_update(alpha, beta, gamma, range_est, vel_est, acc_est, delta_t, measurement)
    
        self.assertEqual(curr_range_est, 30205)
        self.assertEqual(curr_vel_est, 42.8)
        self.assertEqual(curr_acc_est,-0.7)
    
    def test_accel_target_series(self):
        """Tests ghk filter for series of range measurements in 1d"""
        # filter constants
        alpha = 0.5
        beta = 0.4
        gamma = 0.1

        # simulation constants
        delta_t = 5 #(s)

        curr_range_est_list = []
        curr_vel_est_list = []
        curr_acc_est_list = []

        range_pred_list = []
        vel_pred_list = []
        acc_pred_list = []

        # initial values
        range_est = 30250.0 #(m)
        vel_est = 50.0 #(m/s)
        acc_est = 0 #(m/s^2)

        measurements = [30160, 30365, 30890, 311050, 31758, 32215, 33130, \
            34510, 36010, 37265]

        for value in measurements:
            curr_range_est, curr_vel_est, curr_acc_est = \
                module.ghk_state_update(alpha, beta, gamma ,\
                range_est, vel_est, acc_est, delta_t, value)

            curr_range_est_list.append(round(curr_range_est,1))
            curr_vel_est_list.append(round(curr_vel_est,1))
            curr_acc_est_list.append(round(curr_acc_est,1))

            range_est, vel_est, acc_est = \
                module.ghk_state_extrapolation(curr_range_est, curr_vel_est, \
                    curr_acc_est, delta_t)

            range_pred_list.append(round(range_est,1))
            vel_pred_list.append(round(vel_est,1))
            acc_pred_list.append(round(acc_est,1))

        # Expected test results
        exp_curr_range_est = [30205.0, 30387.5, 30721.0, 31038.8, \
            31591.1, 32201.7, 33032.5, 34250.7, 35822.9, 37465.4]
        exp_curr_vel_est = [42.8, 35.6, 57.2, 67.2, 107.2, 133.9, 175.1, \
            250.0, 334.0, 371.1]
        exp_curr_acc_est = [-0.7, -1.1, 1.6, 1.8, 4.9, 5.1, 6.7, 10.8, \
            13.8, 10.6]

        exp_range_pred = [30410, 30552, 31027.5, 31397.1, 32188.5, 32935.1, \
            33991.3, 35635.8,37665.8, 39453.5]
        exp_vel_pred = [39.2, 30.2, 65.4, 76.2, 131.7, 159.5, 208.5, 304.1, \
            403.1, 424.2]
        exp_acc_pred = [-0.7, -1.1, 1.6, 1.8, 4.9, 5.1, 6.7, 10.8, 13.8, 10.6]

        self.assertEqual(curr_range_est_list, exp_curr_range_est)
        self.assertEqual(curr_vel_est_list, exp_curr_vel_est)
        self.assertEqual(curr_acc_est_list, exp_curr_acc_est)

        self.assertEqual(range_pred_list, exp_range_pred)
        self.assertEqual(vel_pred_list, exp_vel_pred)
        self.assertEqual(acc_pred_list, exp_acc_pred)
