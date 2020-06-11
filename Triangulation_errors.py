import math
from scipy import optimize
from scipy import stats
import numpy as np


def get_corrections(h1, h2, h3, theta1, theta2, theta3):
    '''
    :param h1:
    :param h2:
    :param h3:
    :param theta1:
    :param theta2:
    :param theta3:
    :return:
    '''
    assert isinstance(h1,(float,int))
    assert isinstance(h2,(float,int))
    assert isinstance(h3,(float,int))
    assert isinstance(theta1,(float,int))
    assert isinstance(theta2,(float,int))
    assert isinstance(theta3,(float,int))

    def f(X):
        return X[0] ** 2 + X[1] ** 2 + X[2] ** 2

    def observe_1(X):
        return h1 + X[3] * math.tan(theta1 + X[0]) - X[4]

    def observe_2(X):
        return h2 + X[3] * math.tan(theta2 + X[1]) - X[4]

    def observe_3(X):
        return h3 + X[3] * math.tan(theta3 + X[2]) - X[4]

    cons = (dict(type='eq', fun=observe_1), dict(type='eq', fun=observe_2), dict(type='eq', fun=observe_3))
    res = optimize.minimize(f, [0, 0, 0, 1, 1], method='SLSQP', constraints=cons)
    return (res.x[0], res.x[1], res.x[2])


def get_xz(h1, h2, h3, theta1, theta2, theta3):
    '''
    :param h1:
    :param h2:
    :param h3:
    :param theta1:
    :param theta2:
    :param theta3:
    :return:
    '''
    assert isinstance(h1,(float,int))
    assert isinstance(h2,(float,int))
    assert isinstance(h3,(float,int))
    assert isinstance(theta1,(float,int))
    assert isinstance(theta2,(float,int))
    assert isinstance(theta3,(float,int))

    def f(X):
        return X[0] ** 2 + X[1] ** 2 + X[2] ** 2

    def observe_1(X):
        return h1 + X[3] * math.tan(theta1 + X[0]) - X[4]

    def observe_2(X):
        return h2 + X[3] * math.tan(theta2 + X[1]) - X[4]

    def observe_3(X):
        return h3 + X[3] * math.tan(theta3 + X[2]) - X[4]

    cons = (dict(type='eq', fun=observe_1), dict(type='eq', fun=observe_2), dict(type='eq', fun=observe_3))
    res = optimize.minimize(f, [0, 0, 0, 1, 1], method='SLSQP', constraints=cons)
    return res.x[3], res.x[4]


def get_stats_x(h1, h2, h3, phi1, phi2, phi3, sigma):
    '''
    :param h1:
    :param h2:
    :param h3:
    :param phi1:
    :param phi2:
    :param phi3:
    :param sigma:
    :return:
    '''
    assert isinstance(h1,(float,int))
    assert isinstance(h2,(float,int))
    assert isinstance(h3,(float,int))
    assert isinstance(phi1,(float,int))
    assert isinstance(phi2,(float,int))
    assert isinstance(phi3,(float,int))


    x = []

    for i in range(100):
        correction_1, correction_2, correction_3 = stats.norm(0, sigma).rvs(3)
        x1, z1 = get_xz(h1, h2, h3, phi1 + correction_1, phi2 + correction_2, phi3 + correction_3)
        x.append(x1)

    return (np.mean(x), np.var(x))


def get_stats_z(h1, h2, h3, phi1, phi2, phi3, sigma):
    '''
    :param h1:
    :param h2:
    :param h3:
    :param phi1:
    :param phi2:
    :param phi3:
    :param sigma:
    :return:
    '''

    assert isinstance(h1,(float,int))
    assert isinstance(h2,(float,int))
    assert isinstance(h3,(float,int))
    assert isinstance(phi1,(float,int))
    assert isinstance(phi2,(float,int))
    assert isinstance(phi3,(float,int))

    z = []
    for i in range(100):
        correction_1, correction_2, correction_3 = stats.norm(0, sigma).rvs(3)
        x1, z1 = get_xz(h1, h2, h3, phi1 + correction_1, phi2 + correction_2, phi3 + correction_3)

        z.append(z1)
    return (np.mean(z), np.var(z))