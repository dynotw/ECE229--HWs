# Part 1: Simulation
# Write a function sim_ngon(n=3,ns=100) to simulate breaking the unit length rod in n pieces uniformly at random and returning the corresponding probability of using the so-generated fragments to create a valid (i.e., non-zero area) n+1 polygon using ns simulation trials.
#
# Part 2: Numerical result
# Write the following function (not a simulation):
#
#     def prob_n_breaks(n=4):
#          '''
#          compute the probability of forming a nonzero area polygon with `n` breaks.
#
#          Note that `n` breaks creates a `n+1` polygon.
#
#          Example:
#          --------
#          >>> prob_n_breaks(3) # rectangle
#          0.5
#          >>> prob_n_breaks(4) # Pentagon
#          0.6875
#          >>> prob_n_breaks(5) # hexagon
#          0.812501
#          '''
#
# Note: Use any or all of Numpy, Scipy, Sympy, Pandas.

import numpy as np
from scipy import stats

def sim_ngon(n=3,ns=100):
    '''
    :param n: points number
    :param ns: stimulation times
    :return: probability
    '''
    assert isinstance(n,int)
    assert 2<= n
    assert isinstance(ns,int)
    assert 1<= ns

    data = stats.uniform().rvs((n,ns))
    # sort by elements in each column, then elements of each row change
    data.sort(axis = 0)
    # prepend = x1, append = x2: 就是在array的顶部补足x1，在底部补足x2， diff(axis=0)就是计算data[i+1]-data[i]
    result = np.diff(data, axis=0,prepend=0, append=1)
    # get the maximum element of each column
    column_max = np.max(result, axis=0)
    valid_number = sum(column_max < 0.5)

    return valid_number/ns

def prob_n_breaks(n=4):
    '''
    :param n:
    :return:
    '''
    assert isinstance(n,int)
    assert 2<= n

    invalid_probability = (n+1) * ((0.5)**n)

    return 1 - invalid_probability


def sim_ngon2(n=3, ns=100):
    '''
    simulate breaking the unit length rod in n pieces uniformly
    at random and returning the corresponding probability of
    using the so-generated fragments to create a valid (i.e.,
    non-zero area) n+1 polygon using ns simulation trials.
    '''
    assert isinstance(n, int) and isinstance(ns, int)
    assert n >= 2 and ns >= 1

    r = uniform.rvs(size=(n, ns))
    r.sort(axis=0)
    r = np.concatenate((r, np.array([[1]])))
    r[1:n] = r[1:n] - r[:n - 1]

    return sum(np.max(r, axis=0) < 0.5) / ns


def prob_n_breaks2(n=4):
    '''
    compute the probability of forming a nonzero area polygon with `n` breaks.

    Note that `n` breaks creates a `n+1` polygon.

    Example:
    --------
    >>> prob_n_breaks(3) # rectangle
    0.5
    >>> prob_n_breaks(4) # Pentagon
    0.6875
    >>> prob_n_breaks(5) # hexagon
    0.812501
    '''
    assert isinstance(n, int)
    assert n >= 2

    p = 1 << n  #位运算
    return 1.0 - (n + 1) / p

# if __name__ == '__main__':
#     print(sim_ngon(n=4,ns=1000))
#     print(prob_n_breaks(n=4))
