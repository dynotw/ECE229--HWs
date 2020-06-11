# Rod-breaking Triangle
# # A rod of unit length is broken in two places uniformly at random.
# #
# # Part 2: Breaking using Beta distribution
# # Write a simulation sim_triangle_beta(n=100,a=1,b=1) to change from breaking according to a uniform distribution to breaking according to a Beta distribution with parameters a,b. See scipy.stats.beta for more details. Note that we are only interested in positive integer values for the Beta distribution parameters a,b.
# #
# # You can use Numpy, Scipy, Pandas as needed.
# #
# # Please put your Python code in a Python script file and upload it. Please retain your submitted source files! Remember to use all the best practices we discussed in class. You can use any module in the Python standard library, but third-party modules (e.g., Numpy, Pandas) are restricted to those explicitly mentioned in the problem description.
# #
# # After you have submitted your file, do not use the browser back or reload buttons to navigate or open the page in multiple browser tabs, as this may cause your attempts to decrease unexpectedly. It may take up to thirty seconds for your code to be processed, so please be patient.
# #
# # Good luck!

import pandas as pd
import numpy as np
from scipy import stats

def sim_triangle_beta(n=100,a=1,b=1):
    '''

    :param n: times of stimulation
    :param a:
    :param b:
    :return:
    '''
    assert isinstance(n,int)
    assert n > 0
    assert isinstance(a,int)
    assert a > 0
    assert isinstance(b,int)
    assert b > 0

    x1, x2 = stats.beta(a,b).rvs((2,100))
    # x1, x2 = stats.beta.rvs(a, b, scale=2, size=100)
    # x1 and x2 is splited points
    df = pd.DataFrame(columns=["x1", 'x2', 'l1', 'l2', 'l3'])
    df.x1 = x1
    df.x2 = x2
    # x1 < x2
    df.loc[df.x1 < df.x2, 'l1'] = df.x1
    df.loc[df.x1 < df.x2, 'l2'] = df.x2 - df.x1
    df.loc[df.x1 < df.x2, 'l3'] = 1 - df.x2
    # x1 > x2
    df.loc[df.x1 > df.x2, 'l1'] = df.x2
    df.loc[df.x1 > df.x2, 'l2'] = df.x1 - df.x2
    df.loc[df.x1 > df.x2, 'l3'] = 1 - df.x1
    # x1 = x2
    df.loc[df.x1 == df.x2, 'l1'] = df.x1
    df.loc[df.x1 == df.x2, 'l2'] = df.x2 - df.x1
    df.loc[df.x1 == df.x2, 'l3'] = 1 - df.x2

    y1 = df.query('l1 < 0.5 and l2 < 0.5 and l3 < 0.5 ')

    return (y1.shape[0]/df.shape[0])

# if __name__ == '__main__':
#     print(sim_triangle_beta())