import numpy as np
from scipy import stats
from scipy.misc import derivative
import math
def conditional_prob_H1(x):
    '''
    :param x:
    :return:
    '''

    assert isinstance(x,float)
    assert x>=0
    assert x<=math.sqrt(2)

    if (x>=0 and x<=1):
        return (2/math.pi)
    else:
        f = lambda x: 2 / math.pi * (math.pi / 2 - math.asin(1 / x) + math.acos(1 / x) - math.sqrt(x ** 2 - 1) + 1)
        return derivative(f, x, dx=1e-6)

def conditional_prob_H0(x):
    '''
    :param x:
    :return:
    '''
    assert isinstance(x,float)
    return stats.norm.pdf(x, loc=0, scale=1/10)
