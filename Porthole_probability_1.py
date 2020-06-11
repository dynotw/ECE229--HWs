import numpy as np
from scipy import stats
import math
def gen_length_samples(n=1):
    '''
    :param n:
    :return:
    '''

    assert isinstance(n,int)
    assert n>=1

    x = stats.uniform.rvs(loc=0, scale=1, size=n)
    angle = stats.uniform.rvs(loc=0, scale=180, size=n) # should turn to radius when use it
    result = np.ones(n)
    for i in range(n):
        if (angle[i] >= 90):
            result[i] = x[i] / -math.cos(math.radians(angle[i]))
        else:
            if (1 / math.sin(math.radians(angle[i]))) <= math.sqrt(2) and 0 <= (1 / math.sin(math.radians(angle[i]))):
                result[i] = (1 / math.sin(math.radians(angle[i])))
            else:
                result[i] = (1 - x[i]) / math.cos(math.radians(angle[i]))

    return result