from scipy.integrate import dblquad
from scipy import stats
from scipy.integrate import quad
import math
def conditional_prob_H1(x):
    '''
    :param x:
    :return:
    '''

    assert isinstance(x,(float,int))
    assert x>=0
    assert x<=math.sqrt(2)

    f = lambda y: (10/(math.sqrt(2*math.pi)) * math.exp(-50 * (x-y)**2)) * 2/math.pi *(1/(math.sqrt(y**2-1)) * (2/y - y)) if (1<y and y<= math.sqrt(2)) else ((10/(math.sqrt(2*math.pi)) * math.exp(-50 * (x-y)**2))*2/math.pi if (0<=y and y<=1) else 0)
    val, error = quad(f,0,math.sqrt(2))

    return val

def conditional_prob_H0(x):
    '''
    :param x:
    :return:
    '''
    assert isinstance(x,(float,int))
    return stats.norm.pdf(x, loc=0, scale=1/10)