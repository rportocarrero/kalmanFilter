"""This is an implementation of a variance function
"""
def m_variance(array):
    """This function returns the variance of a set of data

    :param array: Array of elements to find the variance of
    :type arry: int,float
    :return: the variance of the array
    :rtype: float
    """
    array_len=len(array)
    array_sum = 0
    for val in array:
        array_sum = array_sum + val
    array_mean = array_sum/array_len
    mean_dist = []
    for val in array:
        mean_dist.append((val-array_mean)**2)
    array_sum=0
    for val in mean_dist:
        array_sum=array_sum+val
    return array_sum/array_len
    