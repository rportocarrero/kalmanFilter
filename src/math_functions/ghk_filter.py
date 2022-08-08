"""This module implements the state update and state extrapolation equations of a ghk filter"""
def ghk_state_update(alpha, beta, gamma, range_est, vel_est, acc_est, delta_t, measurement):
    """ghk filter state update equation
    :param alpha: alpha parameter of filter
    :type alpha: float
    :param beta: beta parameter of filter
    :type beta: float
    :param gamma: gamm parameter of filter
    :type gamma: float
    :param range_est: previous range estimate
    :type range_est: float
    :param vel_est: previous velocity estimate
    :type vel_est: float
    :param acc_est: previous acceleration estimate
    :type acc_est: float
    :param delta_t: time between measurements
    :type delta_t, float/int
    :param measurement: range measurement
    :type measurement: flost
    :return: the updated estimates for range, velocity, and acceleration
    :rtype: float, float, float"""
    updated_range = range_est + alpha * (measurement - range_est)
    updated_vel = vel_est + beta * ((measurement - range_est) / delta_t)
    updated_acc = acc_est + gamma * ((measurement - range_est) / ((delta_t**2)*0.5))
    return round(updated_range,1), round(updated_vel,1), round(updated_acc,1)

def ghk_state_extrapolation(range_est, vel_est, acc_est, delta_t):
    """ghk filter state extrapolation equation
    :param range_est: estimated range
    :type range_est: float
    :param vel_est: estimated velocity
    :type vel_est: float
    :param acc_est: estimated acceleration
    :type acc_est: float
    :param delta_t: time between measurements
    :type delta_t: float
    :return: predictions for next state range, velocity, and acceleration
    :rtype: float, float, float"""
    updated_range = range_est + (vel_est * delta_t) + (acc_est * (delta_t**2) / 2)
    updated_vel = vel_est + acc_est * delta_t
    updated_acc = acc_est
    return round(updated_range,1), round(updated_vel,1), round(updated_acc,1)
