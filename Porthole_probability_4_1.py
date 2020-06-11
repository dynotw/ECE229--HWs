import math
from scipy.integrate import quad
from scipy import stats
def false_alarm_probability(thresh):
    '''
    :param thresh: thresh
    :return: float
    '''
    assert isinstance(thresh,(float,int))

    return float(1 - stats.norm.cdf(thresh, loc=0, scale=1/10))