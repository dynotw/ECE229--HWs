from scipy.integrate import dblquad
from scipy import stats
import numpy as np
import math


def compute_cdf(d):
    '''
    :param d:
    :return:
    '''
    assert isinstance(d, (float, int))
    assert d >= 0

    # pdf_pdf = pdf(delta_x) * pdf(delta_y)
    pdf_pdf = lambda delta_x, delta_y: 2 * (1 - delta_x) * 2 * (
                1 - delta_y) if 0 <= delta_x <= 1 and 0 <= delta_y <= 1 else 0

    val, error = dblquad(pdf_pdf,
                         -math.sqrt(d),  # delta_x lower bound
                         math.sqrt(d),  # delta_y upper bound
                         lambda x: - math.sqrt(d - x ** 2),  # delta_y lower bound
                         lambda x: math.sqrt(d - x ** 2))  # delta_y upper bound
    return val


def compute_test_pvalue(X):
    '''
    :param X:
    :return:
    '''
    assert isinstance(X, np.ndarray)
    assert X.shape[1] == 2
    rvs_distance = []

    np.random.shuffle(X)

    point1 = X[:len(X) // 2]
    point2 = X[len(X) // 2:]
    for i in range(len(point1)):
        rvs_distance.append((point1[i][0] - point2[i][0]) ** 2 + (point1[i][1] - point2[i][1]) ** 2)

    #  cdf = [compute_cdf(i) for i in d]
    error, p_value = stats.kstest(rvs_distance, get_cdf)
    return p_value


def get_cdf(x):
    x = np.atleast_1d(x)
    pdf_pdf = lambda delta_x, delta_y: 2 * (1 - delta_x) * 2 * (
                1 - delta_y) if 0 <= delta_x <= 1 and 0 <= delta_y <= 1 else 0

    cdf = [dblquad(pdf_pdf,
                   -math.sqrt(d),  # delta_x lower bound
                   math.sqrt(d),  # delta_y upper bound
                   lambda x: - math.sqrt(d - x ** 2),  # delta_y lower bound
                   lambda x: math.sqrt(d - x ** 2))[0] for d in x]  # delta_y upper bound

    return np.array(cdf)