"""This is an implementation of the state update equation for a one-dimensional kalman filter
"""
def state_update(prev, measurement, k_gain):
    """This is an implementation of a 1-dimentional state update equation for the Kalman Filter

    :param prev: previous estimate
    :type prev: float,int
    :param measurement: current state measurement
    :type measurement: float, int
    :param k_gain: kalman gain value
    :type k_gain: int, float
    :return estimate: current state estimate
    :rvalue: float
    """
    estimate = prev + k_gain * (measurement - prev)
    return estimate
    