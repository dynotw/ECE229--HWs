import itertools
import functools


def get_mean_boxes(probs):
    '''
    :param probs:
    :return:
    '''

    assert isinstance(probs, list)
    assert 2 <= len(probs) <= 10
    assert sum(probs) == 1

    mean_boxes = 0
    for i in range(1, len(probs) + 1):
        # states represents all states (we have i coupons)
        states = list(itertools.combinations(probs, r=i))

        sub_sum = 0

        for state in states:
            prob_state = 1 / sum(state)  # 1/pi
            sub_sum += prob_state  # sum of 1/pi

        mean_boxes += (-1) ** (i + 1) * sub_sum
    #         print(mean_boxes)
    #         for state in states:
    #             probs_state = functools.reduce(lambda x,y:x*y,state) / sum_probs_state
    #             probs_same_state = sum([j for j in state])
    #             # print("已有Coupon的概率", probs_state)
    #             prob = probs_state * (sum(probs) - probs_same_state) * (probs_same_state / (1-probs_same_state)**2) / probs_same_state
    #             # print(prob)
    #             mean_boxes += prob

    return mean_boxes