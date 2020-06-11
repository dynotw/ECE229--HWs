import numpy as np
def get_auc():
    '''
    :return:
    '''
    x = np.linspace(-math.sqrt(2),math.sqrt(2),200)
    pd = np.array([true_detection_probability(i) for i in x])
    pfa = np.array([false_alarm_probability(i) for i in x])

    return float(-np.trapz(pd, x=pfa))

from scipy.integrate import dblquad

def true_detection_probability(thresh):
    '''
    :param thresh:
    :return:
    '''
    assert isinstance(thresh,(float,int))

    f = lambda y,x: (10/(math.sqrt(2*math.pi)) * math.exp(-50 * (x-y)**2)) * 2/math.pi *(1/(math.sqrt(y**2-1)) * (2/y - y)) if (1<y and y<= math.sqrt(2)) else ((10/(math.sqrt(2*math.pi)) * math.exp(-50 * (y-x)**2))*2/math.pi if (0<=y and y<=1) else 0)
    val, error = dblquad(f,  thresh,  math.sqrt(2), lambda x: 0,  lambda x: math.sqrt(2))

    return val

import math
from scipy import stats
def false_alarm_probability(thresh):
    '''
    :param thresh: thresh
    :return: float
    '''
    assert isinstance(thresh,(float,int))

    return float(1 - stats.norm.cdf(thresh, loc=0, scale=1/10))