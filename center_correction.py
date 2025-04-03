import csv
from center_finder import center_finder
from cs_change import *

directory = "profiles"
file_name = "file_1.csv"

with open(f"{directory}/{file_name}") as f:
    prof = list(map(lambda x: [float(x[0]), float(x[1])], csv.reader(f)))

corr = center_finder(prof)

prof = list(map(lambda x: rad_to_dec(*x), prof))
prof = list(map(lambda x: [x[0] - corr[0], x[1] - corr[1]], prof))
prof = list(map(lambda x: dec_to_rad(*x), prof))

res_profile = []
for ang in range(0, 360, 360 // (len(prof) - 1)):
    rotated_profile = list(map(lambda x: [x[0], x[1] - ang * math.pi / 180], prof))
    rotated_profile1 = list(filter(lambda x: x[0] > 0 and x[1] > 0, map(lambda x: rad_to_dec(*x), rotated_profile)))
    rotated_profile2 = list(filter(lambda x: x[0] > 0 and x[1] < 0, map(lambda x: rad_to_dec(*x), rotated_profile)))
    rotated_profile1.sort(key=lambda x: x[1])
    rotated_profile2.sort(key=lambda x: x[1], reverse=True)
    x1, y1 = rotated_profile1[0]
    x2, y2 = rotated_profile2[0]
    res_profile.append([x1 - y1 * (x2 - x1) / (y2 - y1), ang * math.pi / 180])


with open(f"{directory}/{file_name}", 'w', newline='') as f:
    csv.writer(f).writerows(res_profile)

print(corr, center_finder(res_profile))

