# Write a function gen_transition_matrix(init_state=(2,2),pL=0.5) where pL is the probability of selecting the left pocket.
# Remember to use absorbing states to mark the end of the experiment (i.e., no more matches in one of the boxes). The states are tuples.
import numpy as np

def gen_transition_matrix(init_state=(2,2),pL=0.5):
    '''
    :param init_state:
    :param pL:
    :return: a tuple including transition matrix and dict
    '''
    assert (isinstance(init_state, tuple) and len(init_state) == 2)
    for x in init_state:
        assert isinstance(x,int)
        assert x>=0
    assert isinstance(pL,float)
    assert 0<=pL<=1

    states={}
    count = -1
    for i in range(init_state[0] + 1):
        for j in range(init_state[1] + 1):
            state = (i,j)
            states[state] = count
            count += 1
    del states[(0,0)]

    transition_matrix = np.zeros((len(states),len(states)))
    for i in range(init_state[0] + 1):
        for j in range(init_state[1] + 1):
            if i+j==0:
                continue
            elif i*j==0:
                transition_matrix[states[(i,j)],states[(i,j)]] = 1
            else:
                transition_matrix[states[(i,j)],states[(i-1,j)]] = pL
                transition_matrix[states[(i,j)],states[(i,j-1)]] = 1-pL

    return transition_matrix, states

# if __name__ == '__main__':
#     print(gen_transition_matrix(init_state=(3,3),pL=0.5))
