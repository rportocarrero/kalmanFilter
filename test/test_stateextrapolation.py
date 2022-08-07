"""This module tests the state extrapolation equations.
"""
import unittest
import sys
sys.path.append("..")
import src.math_functions as module

class TestStateExtrapolationPositive(unittest.TestCase):
    """This class tests the positive path of the state extrapolation equations
    """
    def test_1d_prediction(self):
        """tests the range/val prediction of a target moving at
        a constant velocity in 1D"""
        curr_range = 30000 #(m)
        velocity = 40 #(m/s)
        delta_t = 5 #(s)
        result_range, result_vel = module.state_extrapolate_1d(curr_range,delta_t,velocity)
        self.assertEqual(result_range,30200)
        self.assertEqual(result_vel,40)

    def test_1d_gh_vel_estimation_high_beta(self):
        """test the range/val prediction of a g-h filter with most likely
        error source being target velocity change
        """
        prev_range = 30200 #(m)
        prev_vel = 40 #(m/s)
        delta_t = 5 #(s)
        range_measurement = 30110 #(m)
        alpha = 1
        beta = 0.9
        _, curr_vel_est, _, _ = \
            module.state_extrapolate_gh(prev_range, prev_vel, \
                range_measurement, delta_t, alpha, beta)
        self.assertEqual(curr_vel_est,23.8)

    def test_1d_gh_vel_estimation_low_beta(self):
        """test the range/val prediction of a g-h filter with the most likely
        error source being measurment variance
        """
        prev_range = 30200
        prev_vel = 40
        delta_t = 5
        range_measurement = 30110
        alpha = 1
        beta = 0.1
        _, curr_vel_est, _, _ = \
            module.state_extrapolate_gh(prev_range, prev_vel, \
                range_measurement, delta_t, alpha, beta)
        self.assertEqual(curr_vel_est, 38.2)

    def test_1d_gh_vel_estimate_series(self):
        """tests the range/val predictions of a series of range measurements
        """
        alpha = 0.2
        beta = 0.1
        delta_t = 5 #(5)
        curr_range_est = 30200
        curr_vel_est = 40
        result_ranges = []
        result_vels = []
        range_measurements = [30110, 30265, 30740, 30750, 31135, 31015,31180, \
            31610, 31960, 31865]

        for vel in range_measurements:
            curr_range_est, curr_vel_est, range_pred, vel_pred = \
                module.state_extrapolate_gh(curr_range_est, curr_vel_est, \
                    vel, delta_t, alpha, beta)
            result_ranges.append(round(curr_range_est,1))
            result_vels.append(round(curr_vel_est,1))
            curr_range_est = range_pred
            curr_vel_est = vel_pred

        expected_result_ranges = [30182.0, 30351.4, 30573.3, 30769.5, \
            31001.5, 31176.4, 31333.2, 31529.4, 31764.3, 31952.9]
        expected_result_vels = [38.2, 36, 40.2, 39.7, 43.1, 39, 35.2, 37.2, \
            42.1, 39.9]

        self.assertEqual(result_ranges, expected_result_ranges)
        self.assertEqual(result_vels, expected_result_vels)

    def test_1d_gh_accelerating(self):
        """test the g-h filter estimation for sequence of a accelerating
        target measurements"""
        # Target model
        initial_vel = 50 #(m/s)
        initial_range = 30000
        target_accel = [0, 0, 8, 8, 8, 8, 8, 8, 8, 8] #(m/s^2)
        target_vel = [] #(m/s)
        curr_target_vel = initial_vel
        curr_target_pos = initial_range
        target_pos = []
        delta_t = 5 #(s)
        for acc in target_accel:
            curr_target_vel = curr_target_vel + acc
            target_vel.append(curr_target_vel)
        for vel in target_vel:
            curr_target_pos = curr_target_pos + delta_t * vel
            target_pos.append(curr_target_pos)

        ## Measurements
        measurements = [30160, 30365, 30890, 31050, 31785, 32215, 33130, \
            34510, 36010, 37265]

        ## initial values
        alpha = 0.2
        beta = 0.1
        curr_range_est = 30250
        curr_vel_est = 50

        ## result values
        curr_range_est_vals = []
        curr_vel_est_vals = []
        range_pred_vals = []
        vel_pred_vals = []

        ## filter sequence
        for target_range in measurements:
            curr_range_est, curr_vel_est, range_pred, vel_pred = \
                module.state_extrapolate_gh(curr_range_est, curr_vel_est, \
                    target_range, delta_t, alpha, beta)
            curr_range_est_vals.append(round(curr_range_est,1))
            curr_vel_est_vals.append(round(curr_vel_est,1))
            range_pred_vals.append(round(range_pred,1))
            vel_pred_vals.append(round(vel_pred,1))
            curr_range_est = range_pred
            curr_vel_est = vel_pred

        ## Expected values
        exp_curr_range_est_vals = [30232.0, 30451.4, 30723.3, 30989.5, \
            31355.5, 31777.2, 32341.4, 33147.6, 34228.8, 35522.9]
        exp_curr_vel_est_vals = [48.2, 46, 50.2, 51.7, 62.5, 73.4, 93.1, \
            127.2, 171.7, 215.3]
        exp_range_pred_vals = [30473.0, 30681.6, 30974.3, 31248.1, 31667.8, \
            32144.2, 32807.0, 33783.5, 35087.4, 36599.2]
        exp_vel_pred_vals = [48.2, 46, 50.2, 51.7, 62.5, 73.4, 93.1, 127.2, \
            171.7, 215.3]

        ## Checks
        self.assertEqual(curr_range_est_vals, exp_curr_range_est_vals)
        self.assertEqual(curr_vel_est_vals, exp_curr_vel_est_vals)
        self.assertEqual(range_pred_vals, exp_range_pred_vals)
        self.assertEqual(vel_pred_vals, exp_vel_pred_vals)
if __name__ == '__main__':
    unittest.main()
