from cs_change import *
import copy
import math


def center_finder(profile:list[list[float]], in_dec:bool=False):
    if in_dec:
        dec_profile = copy.deepcopy(profile)
        profile = list(map(lambda x: dec_to_rad(*x), profile))
    else:
        dec_profile = list(map(lambda x: rad_to_dec(*x), profile))
    n = len(profile)
    dec_profile.append(dec_profile[0])
    profile.append(profile[0])

    cp = [0., 0.]
    summ = 0
    for i in range(n):
        s = profile[i][0] * profile[i + 1][0] * math.sin(abs(profile[i][1] - profile[i + 1][1]))
        summ += s
        cp[0] += (dec_profile[i][0] + dec_profile[i + 1][0]) / 3 * s
        cp[1] += (dec_profile[i][1] + dec_profile[i + 1][1]) / 3 * s

    cp[0] /= summ
    cp[1] /= summ

    return cp
