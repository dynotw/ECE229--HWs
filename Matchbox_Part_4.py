import numpy as np
def get_Smn(m, n, i, j, pL=0.5):
    '''
    :param m:
    :param n:
    :param i:
    :param j:
    :param pL:
    :return:
    '''
    assert isinstance(m, int) and m >= 0
    assert isinstance(n, int) and n >= 0
    assert isinstance(i, int) and 0 <= i <= m
    assert isinstance(j, int) and 0 <= j <= n
    assert 0 <= pL <= 1

    # index of column represent n,
    states = np.zeros((m + 1, n + 1))
    states[i, 0] = states[0, j] = 1
    # a,b represents recursive equation m and n
    for a in range(1, m + 1):
        for b in range(1, n + 1):
            states[a, b] = pL * states[a - 1, b] + (1 - pL) * states[a, b - 1]
    return states[m, n]

def get_Smn2(m,n,i,j,pL=0.5):
    '''
    :param m:
    :param n:
    :param i:
    :param j:
    :param pL:
    :return:
    '''
    assert isinstance(m,int)
    assert m >= 0
    assert isinstance(n,int)
    assert n >= 0
    assert isinstance(i,int)
    assert 0 <= i
    assert isinstance(j, int)
    assert 0 <= j
    assert 0<=pL<=1

    if (n == j and i==m):
        return 1
    elif ( m ==0 or n == 0 ):
        return 0

    return pL * get_Smn2(m-1,n,i,j) + (1-pL) * get_Smn2(m,n-1,i,j)