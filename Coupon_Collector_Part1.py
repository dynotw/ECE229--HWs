import numpy as np

def sim_avg_coupons(probs, ntrials):
    '''
    simulate average coupons

    '''
    assert isinstance(probs, np.ndarray)
    assert isinstance(ntrials, int) and ntrials >= 1
    assert sum(probs) == 1
    count = 0
    for i in range(ntrials):
        coupon_get = set()
        while (len(coupon_get) < len(probs)):
            count = count + 1
            # np.random.choice(), choose elements based on probability
            pick = np.random.choice(list(range(len(probs))), size=1, p=probs)
            coupon_get.add(pick[0])

    return count / ntrials