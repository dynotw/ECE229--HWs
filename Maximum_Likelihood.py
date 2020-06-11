import pandas as pd

def get_ML_seq(seq, plist):
    assert isinstance(seq, str)
    for i in seq:
        assert i is 0 or 1
    assert isinstance(plist, list)
    for j in plist:
        assert isinstance(j, dict)
        assert sum(j.values()) == 1
        for prob in j.values():
            assert 0 <= prob <= 1

    prob_all = []
    plist_temp = plist[:]
    seq = ''.join(["%s " % j for j in seq])
    seq = seq.strip()
    combinations = split(seq)

    for i in range(len(combinations)):
        for j in range(len(combinations[i])):
            combinations[i][j] = ''.join(combinations[i][j].split())
        combinations[i] = pd.value_counts(combinations[i])
    for i in range(len(plist_temp)):
        plist_temp[i] = pd.Series(plist_temp[i])
        probability = 0
        for j in combinations:
            temp = pd.concat([j, plist_temp[i]], axis=1)
            if (temp[1].isnull().any()):
                continue

            else:
                temp = temp.dropna(axis=0, how='any')
                temp[3] = temp.apply(lambda x: x[1] ** x[0], axis=1)
                prob = temp.prod(axis=0)[3]

                probability += prob

        prob_all.append(probability)

    assert len(prob_all)
    max_index=prob_all.index(max(prob_all))

    return plist[max_index]


def split(s, i=0):
    if len(s) == i:
        return [[s]]
    elif s[i] == " ":
        return [[s[0:i]] + acc for acc in split(s[i + 1:])] + split(s, i + 1)
    else:
        return split(s, i + 1)
