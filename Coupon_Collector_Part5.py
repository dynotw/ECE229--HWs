import numpy as np

def sim_nxgraph_coupon(probs, nsteps):
    '''
    :param probs: 
    :param nsteps: 
    :return: 
    '''
    
    assert nsteps > 0 and isinstance(nsteps, int)
    assert isinstance(probs, list)
    assert sum(probs) == 1
    for p in probs:
        assert isinstance(p, float) and 0 <= p <= 1

    coupons_get = []
    result = [()]

    coupons = list(range(len(probs)))

    count = nsteps
    while (count != 0):
        count -= 1
        coupon = np.random.choice(coupons, p=np.array(probs))
        if coupon not in coupons_get:
            coupons_get.append(coupon)
            coupons_get.sort()
        result.append(tuple(coupons_get))

    return result