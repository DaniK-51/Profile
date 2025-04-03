import csv

directory = "profiles"
file_name = "file_1.csv"

f = open(f"{directory}/{file_name}")
c = csv.reader(f)
print(*c)
