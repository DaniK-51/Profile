import csv
from profile_generator import gen_profile

directory = "profiles"
file_name = "file_1.csv"

f = open(f"{directory}/{file_name}", 'w', newline='')
c = csv.writer(f, )
for i in gen_profile():
    c.writerow(i)
