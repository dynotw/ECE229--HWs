import pandas as pd
import numpy as np
from scipy import stats

def sim_triangle(n = 100):
    '''

    :param n: times of stimulation
    :return: probability
    '''
    assert isinstance(n,int)
    assert n > 0

    x1, x2 = stats.uniform().rvs((2, 100))
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
#     print(sim_triangle())