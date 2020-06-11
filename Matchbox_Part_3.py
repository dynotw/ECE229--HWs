
from functools import lru_cache
@lru_cache(maxsize=None)
def get_Smk(m,n,k):
    '''
    :param m: m matches in the left pocket
    :param n: n matches in the right pocket
    :param k:
    :return: probability
    '''

    assert isinstance(m,int)
    assert m>=0
    assert isinstance(n,int)
    assert n>=0
    assert isinstance(k,int)
    assert k >= 0

    if ((n == 0 and m==k) or (m==0 and n==k)):
        return 1
    elif (n == 0 or m==0):
        return 0
    # elif (n < 0 or m < 0):
    #     return 0
    return 0.5 * get_Smk(m-1,n,k) + 0.5 * get_Smk(m,n-1,k)
