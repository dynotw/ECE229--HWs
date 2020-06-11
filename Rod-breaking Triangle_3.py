# Rod-breaking Triangle
# A rod of unit length is broken in two places uniformly at random.
#
# Part 3: Beta distribution numerical result
# Write a function beta_obj(a,b) to numerically evaluate the probability of a valid triangle for 1<= a <= 20 and 1<=b<=20 over integers. This is not a simulation. Your beta_obj(a,b) should return the numerical probability of a valid triangle as a floating-point number given a and b. Your results here should align with your previous sim_triangle_beta simulation.
#
# Note: Use any or all of Numpy, Scipy, Pandas.
#
#
# Please put your Python code in a Python script file and upload it. Please retain your submitted source files! Remember to use all the best practices we discussed in class. You can use any module in the Python standard library, but third-party modules (e.g., Numpy, Pandas) are restricted to those explicitly mentioned in the problem description.
#
# After you have submitted your file, do not use the browser back or reload buttons to navigate or open the page in multiple browser tabs, as this may cause your attempts to decrease unexpectedly. It may take up to thirty seconds for your code to be processed, so please be patient.
#
# Good luck!

import pandas as pd
import numpy as np
from scipy import stats
from scipy.integrate import quad, dblquad
from scipy import stats

# 1st method
def beta_obj(a,b):
    '''
    :param a:
    :param b:
    :return:
    '''
    assert isinstance(a,int)
    assert 1<=a<=20
    assert isinstance(b,int)
    assert 1<=b<=20

# 二重积分
    f = lambda y, x: stats.beta.pdf(x, a, b) * stats.beta.pdf(y, a, b)
    val, error = dblquad(f,  # 函数
                   0.5,  # x下界
                   1,  # x上界
                   lambda x: x - 0.5,  # y下界
                   lambda x: 0.5)  # y 上界

    return val * 2

# 2nd method
def beta_obj2(a,b):
    '''
    :param a:
    :param b:
    :return:
    '''

    assert isinstance(a,int)
    assert 1<=a<=20
    assert isinstance(b,int)
    assert 1<=b<=20

    result = stats.beta.expect(lambda x : stats.beta.cdf(0.5,a,b) - stats.beta.cdf(x-0.5,a,b), args=(a, b),lb = 0.5, ub = 1)
    return result * 2

if __name__ == '__main__':
    print(beta_obj(5,6))