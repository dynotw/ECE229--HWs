import math
from scipy.integrate import quad
from scipy import stats
def false_alarm_probability(thresh):
    assert isinstance(thresh,float)
    assert thresh>=0

    f = lambda x: stats.norm.pdf(x, loc=0, scale=1/10)
    val, error= quad(f,a=thresh, b=math.sqrt(2)) # a is lower bound; b is upper bound

    return val