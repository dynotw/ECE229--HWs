# Given a set of discrete probability distributions represented as a dictionary such as the following,
# p1 = {'00':1/2, '01':1/4, '10':1/4}
#  p2 = {'0':1/3, '01':1/3, '10':1/3}
#  p3 = {'00':1/8, '01':1/4, '0':3/8,'1010':2/8}
# and a string sequence of bits such as
# '10011001'
# Find the maximum likelihood solution for this sequence amoung the given dictionaries. Here is your function signature: get_ML_seq(seq,plist) where plist is a list of probability dictionaries and seq is a string of bits. You can use numpy, pandas, and networkx for this problem if you wish. If your maximum likelihood analysis returns a tie, then return any one of the ties. For this example, p2 is the maximum likelihood solution and the return value for get_ML_seq(seq,plist) is the p2 dictionary. If none of the input dictionaries are viable for the seq input, then assert False. Note that the input bitstring can be any length and there can be any number of input dictionaries. The dictionary keys may also be bitstrings of any length.
# Example 1:
# For p1 above, the likelihood is 1/4**4. This is because the only valid sequence that consumes the entire observed string given p1 is 10,01,10,01, each of which as probability of 1/4.
# Likewise, consider p2 above. The only valid sequence there is 10,01,10,01. Each of these terms has 1/3 probability so the likelihood for p2 is 1/3**4. The p3 dictionary cannot produce a valid sequence for the observed string, so its corresponding likelihood is zero.
# Example 2:
# Given the same dictionaries as above, consider the new observed sequence 10101010100. It is not possible for p1 to generate this sequence so the likelihood for this dictionary is zero. For p2, we have 10,10,10,10,10,0 with corresponding likelihood 1/3**5 * 1/3. For p3 we have zero because there is no way to generate the sequence from the keys of p3.

def get_ML_seq(seq,plist):
    '''

    :param seq:
    :param plist:
    :return: Maximum Likelihood p
    '''
    assert isinstance(seq, str)
    for i in seq:
        assert i in ['0','1']
    assert isinstance(plist, list)
    for j in plist:
        assert isinstance(j, dict)
        assert sum(j.values()) == 1
        for prob in j.values():
            assert 0 <= prob <= 1
        for i in j.keys():
            assert isinstance(i,str)
            for a in i:
                assert a in ['0','1']

    max_prob = 0
    temp = 0
    # call find_prob for each p, to get the maximum probability and responding index
    for i in range(len(plist)):
        prob = find_prob(seq, plist[i])
        if prob > max_prob:
            max_prob = prob
            temp = i

    # ensure there's valid p in plist
    assert max_prob > 0

    return plist[temp]

# Use recursion to get the probability, based on p
def find_prob(seq, p):
    '''
    :param seq: Bit String
    :param p: Dictionary about probability of each coupon
    :return: probability
    '''

    prob = 0
    if len(seq) == 0:
        return 1

    # Divide
    substrings = [seq[len(s):] for s in p.keys() if seq.startswith(s)]
    # each (key + value) = seq, in combinations
    combinations = {s: seq[len(s):] for s in p.keys() if seq.startswith(s)}

    # Conquer
    if len(substrings) == 0:
        return 0

    for i in range(len(substrings)):
        prob += p[list(combinations.keys())[i]] * find_prob(substrings[i], p)

    return prob