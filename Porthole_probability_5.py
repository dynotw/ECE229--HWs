from scipy.integrate import quad
from scipy import stats
import math
def true_detection_probability(thresh):
    '''
    :param thresh:
    :return:
    '''

    assert isinstance(thresh,float)
    assert thresh>=0
    assert thresh<=math.sqrt(2)

    def pdf(x):
        if (x >= 0 and x <= 1):
            return (2 / math.pi)
        else:
#             f = lambda x: 2 / math.pi * (math.pi / 2 - math.asin(1 / x) + math.acos(1 / x) - math.sqrt(x ** 2 - 1) + 1)
            return 2/math.pi *(1/(math.sqrt(x**2-1)) * (2/x - x))

    val, error = quad(pdf, a=thresh, b=math.sqrt(2),points=[1])
    return val