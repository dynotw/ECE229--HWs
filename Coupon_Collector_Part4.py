import networkx as nx
import itertools
def get_coupon_Markov_graph(probs):
    '''

    :param probs:
    :return:
    '''

    assert isinstance(probs, list)
    for i in probs:
        assert 0<=i<=1
    assert sum(probs) == 1, 'probs should sum up to 1'

    states = []
    G1 = nx.DiGraph()
    all_coupons = list(range(len(probs)))
    for i in range(len(probs) + 1):
        G1.add_nodes_from(list(itertools.combinations(all_coupons, r=i)))
        states.append(list(itertools.combinations(all_coupons, r=i)))

    for i in range(len(probs)):
        for state1 in states[i]:
            for state2 in states[i + 1]:
                if set(state1).issubset(set(state2)):
                    G1.add_edge(state1, state2)

    for i in states:
        for j in i:
            G1.add_node(j, position ="the state is j")
            G1.add_edge(j,j)

    G1.remove_edge(states[0][0],states[0][0])

    return G1