from scipy.integrate import dblquad
from scipy import stats
import math
def true_detection_probability(thresh):
    '''
    :param thresh:
    :return:
    '''
    assert isinstance(thresh,(float,int))
    assert thresh>=0
    assert thresh<=math.sqrt(2)

    f = lambda y,x: (10/(math.sqrt(2*math.pi)) * math.exp(-50 * (x-y)**2)) * 2/math.pi *(1/(math.sqrt(y**2-1)) * (2/y - y)) if (1<y and y<= math.sqrt(2)) else ((10/(math.sqrt(2*math.pi)) * math.exp(-50 * (y-x)**2))*2/math.pi if (0<=y and y<=1) else 0)
    val, error = dblquad(f,  # 函数
                       thresh,  # x下界
                       math.sqrt(2),  # x上界
                       lambda x: 0,  # y下界
                       lambda x: math.sqrt(2))  # y 上界

    return val