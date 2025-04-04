import csv
from center_finder import *
from cs_change import *

directory = "profiles"
file_name = "file_2.csv"

with open(f"{directory}/{file_name}") as f:
    prof = list(map(lambda x: [float(x[0]), float(x[1])], csv.reader(f)))
corr = center_finder(prof)

prof = list(rad_to_dec(rad_cords=prof))
prof = list(map(lambda x: [x[0] - corr[0], x[1] - corr[1]], prof))
prof = list(dec_to_rad(dec_cords=prof))

res_profile = list(rad_interpolation(prof))

with open(f"{directory}/{file_name}", 'w', newline='') as f:
    csv.writer(f).writerows(res_profile)

print(corr, center_finder(res_profile))

