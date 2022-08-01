"""This file implements the arithmetic mean
"""
def m_mean(array):
    """This function implements the arithmetic mean

    :param array: array of elements to find the mean of
    :type array: int, float
    :raises Todo: add error description here
    :return: the arithmetic mean of an array of input values
    :rtype: int,float
    """
    array_len =len(array)
    array_sum = 0
    for i in range(0,array_len):
        array_sum = array_sum + array[i]
    return array_sum/array_len
    