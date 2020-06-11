
def get_odds_ratio_overall():
    '''
    :return:
    '''

    return 0.6848365884777702


def get_odds_ratio_by_age():
    '''
    :return:
    '''

    result = {
        "18-24": 122 / 53,
        "25-34": 456 / 605,
        "35-44": 12 / 5,
        '45-54': 297 / 206,
        '55-64': (51 * 81) / (40 * 64),
        '65-74': 116 / 101

    }

    return result