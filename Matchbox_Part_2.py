import numpy as np
import random as rd
def sim_chain(init_state=(2,2),pL=1/2):
    '''
    :param init_state:
    :param pL:
    :return:
    '''
    assert (isinstance(init_state, tuple) and len(init_state) == 2)
    for x in init_state:
        assert isinstance(x,int)
        assert x>=0
    assert 0<=pL<=1

    state = init_state
    while (state[0] != 0 and state[1] != 0):
        if rd.random() <= pL:
            state = (state[0]-1, state[1])
        else:
            state = (state[0], state[1]-1)
        yield state

# def sim_chain2(init_state=(2,2),pL=1/2):  # 生成器函数 - 斐波那契
#     '''
#     :param init_state:
#     :param pL:
#     :return: a tuple including transition matrix and dict
#     '''
#     assert (isinstance(init_state, tuple) and len(init_state) == 2)
#     for x in init_state:
#         assert isinstance(x,int)
#         assert x>=0
#     assert isinstance(pL,float)
#     assert 0<=pL<=1
#
#     state = np.array(init_state, dtype = float)
#     while True:
#         if (np.min(state) <= 0):
#             return
#         state = state @ transition_matrix
#         yield tuple(state)

# if __name__ == '__main__':
#     list(sim_chain(init_state=(2,2),pL=1/2))  # f 是一个迭代器，由生成器返回生成