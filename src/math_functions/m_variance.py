"""This is an implementation of a variance function
"""
def m_variance(array):
    """This function returns the variance of a set of data
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
    