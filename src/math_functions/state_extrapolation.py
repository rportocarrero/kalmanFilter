"""This is an implementation of the state extrapolation equation
"""

def state_extrapolate_1d(prev_range, delta_t, prev_vel):
    """This implements a state estimation for a 1D target with constant velocity
    :param prev_range: Previous range measurement
    :type prev_range: float, int
    :param prev_val: previous velocity measurements
    :type prev_val: float, int
    :param delta_t: time between measurement and prediction
    :type delta_t: float, int
    :return: the current estimate for range and velocity
    :rtype: [float/int, float/int]
    """
    range_est = prev_range + (delta_t * prev_vel)
    vel_est = prev_vel
    return range_est, vel_est

def state_extrapolate_gh(prev_range_est, prev_vel_est, range_measurement, delta_t, alpha, beta):
    """This implements a 1D alpha-beta (g-h) filter
    :param prev_range: previous range estimate
    :param prev_val: previous velocity estimate
    :param range_measurement: current range measurement
    :param delta_t: time between current measurement and last measurement
    :param alpha: alpha parameter
    :param beta: beta parameter
    :type prev_range: float, int
    :type prev_val: float, int
    :type range_measurement: float, int
    :type delta_t: float, int
    :type alpha: float
    :type beta: float
    :return: the current range and velocity estimate
    :rtype: [float/int, float/int]
    """
    range_est = prev_range_est + alpha * (range_measurement - prev_range_est)
    vel_est = prev_vel_est + beta * (range_measurement - prev_range_est) / delta_t
    range_pred = range_est + delta_t * vel_est
    vel_pred = vel_est
    return range_est, vel_est, range_pred, vel_pred
