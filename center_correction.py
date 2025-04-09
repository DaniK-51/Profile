import csv
from center_finder import *
from cs_change import *


def correct(direct: str, name: str):
    with open(f"{direct}\\{name}") as f:
        prof = list(map(lambda x: [float(x[0]), float(x[1])], csv.reader(f)))
    corr = center_finder(prof)

    prof = list(rad_to_dec(rad_cords=prof))
    prof = list(map(lambda x: [x[0] - corr[0], x[1] - corr[1]], prof))
    prof = list(dec_to_rad(dec_cords=prof))

    res_profile = list(rad_interpolation(prof))

    with open(f"{direct}\\{name}", 'w', newline='') as f:
        csv.writer(f).writerows(res_profile)

    corr = (corr[0] ** 2 + corr[1] ** 2) ** 0.5
    corr_new = center_finder(res_profile)
    corr_new = (corr_new[0] ** 2 + corr_new[1] ** 2) ** 0.5
    return [corr, corr_new]


def correct_alt(direct: str, name: str):
    with open(f"{direct}\\{name}") as f:
        prof = list(map(lambda x: [float(x[0]), float(x[1])], csv.reader(f)))
    corr = center_finder_alt(prof)

    prof = list(rad_to_dec(rad_cords=prof))
    prof = list(map(lambda x: [x[0] - corr[0], x[1] - corr[1]], prof))
    prof = list(dec_to_rad(dec_cords=prof))

    res_profile = list(rad_interpolation(prof))

    with open(f"{direct}\\{name}", 'w', newline='') as f:
        csv.writer(f).writerows(res_profile)
    corr = (corr[0] ** 2 + corr[1] ** 2) ** 0.5
    corr_new = center_finder_alt(res_profile)
    corr_new = (corr_new[0] ** 2 + corr_new[1] ** 2) ** 0.5
    return [corr, corr_new]


print(correct("profiles", "file_1.csv"))
print(correct("profiles", "file_2.csv"))
