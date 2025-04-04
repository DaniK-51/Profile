import csv
from cs_change import *

# directory = "profiles"
# file_name = "file_1.csv"
#
# f = open(f"{directory}/{file_name}")
# c = list(csv.reader(f))
# c = list(map(lambda x: [float(x[0]), float(x[1])], c))
#
# print(c)
# print(list(rad_to_dec(rad_cords=c)))

print(list(dec_to_rad(dec_cords=[[1, 1], [1, 2]])))