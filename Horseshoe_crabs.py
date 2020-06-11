import pandas as pd
import statsmodels.api as sm
def horseshoe1(data):
    '''
    :param data:
    :return:
    '''
    assert isinstance(data,pd.DataFrame)

    temp1 = data['width']
    temp2 = data['y']
    model = sm.GLM(temp2,temp1,family=sm.families.Poisson())
    res = model.fit()
    return res.deviance

def horseshoe2(data):
    '''
    :param data:
    :return:
    '''
    assert isinstance(data,pd.DataFrame)

    temp1 = data[['width','weight']]
    temp2 = data['y']
    model = sm.GLM(temp2,temp1,family=sm.families.Poisson())
    res = model.fit()
    return res.deviance

def horseshoe3(data):
    '''
    :param data:
    :return:
    '''
    assert isinstance(data,pd.DataFrame)

    temp1 = data[['width','weight']]
    temp2 = data['y']
    model = sm.GLM(temp2,temp1,family=sm.families.NegativeBinomial())
    res = model.fit()
    return res.deviance

