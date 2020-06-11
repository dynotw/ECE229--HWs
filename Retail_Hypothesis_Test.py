# Nationwide Promotion or Not?
# Your client is a retailer with many storefront outlets that sell these pants, shirts, and socks across three regions (West, North, South, East). The retailer wants to know if the probability of buying these items is the same regardless of region because they want to launch an expensive nationwide promotion. If it turns out that the probability of buying these items is particular to the specific region, then the nationwide promotion, although less expensive than a region-by-region promotion, will fail.
#
# Solve the problem using hypothesis testing and write a function compute_p_value(data) that returns the p-value given input data like the following dataframe.
#
# shirt	socks	pants
# West	7	24	19
# South	10	21	19
# East	5	24	21
# North	32	5	13
import pandas as pd
from scipy.stats import multinomial
def compute_p_value(data):
    '''
    :param data:
    :return:
    '''
    assert isinstance(data,pd.DataFrame)

    res = 1
    for i in range(3):
        temp = list(data.iloc[:,i])
        print(temp)
        res = res * multinomial.pmf(temp,sum(temp),p=[1/4, 1/4, 1/4, 1/4])

    return res