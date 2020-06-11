import numpy as np
import itertools
def get_coupon_MarkovMatrix(probs):
    '''

    :param probs:
    :return:
    '''
    assert isinstance(probs, list)
    assert 1<= len(probs) <= 10
    assert sum(probs) == 1

    states = []
    all_coupons = list(range(len(probs)))
    for i in range(len(probs) + 1):
        states.extend(list(itertools.combinations(all_coupons, r=i)))

    number = len(states)
    transition_matrix = np.zeros((number, number))

    for i in range(number):
        for j in range(number):
            if i == 0 and len(states[j]) == 1 and sum(states[j]) >= 0:
                transition_matrix[i, j] = probs[states[j][0]]

            # all(): Check if all elements in a list are True:
            elif all(coupon in states[j] for coupon in states[i]) and len(states[i]) == len(states[j]) - 1:
                # np.take(), take elements from np.array based on indices, then construct new np.array
                transition_matrix[i, j] = np.sum(np.take(probs, states[j])) - np.sum(np.take(probs, states[i]))
            elif all(coupon in states[j] for coupon in states[i]) and len(states[i]) == len(states[j]):
                transition_matrix[i, j] = np.sum(np.take(probs, states[j]))

    transition_matrix[0, 0] = 0
    transition_matrix[number - 1, number - 1] = 1

    return transition_matrix
