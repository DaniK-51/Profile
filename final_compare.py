import csv
import turtle
from cs_change import *
import matplotlib.pyplot as plt

directory = "profiles"
first_file_name = "file_1.csv"
second_file_name = "file_2.csv"

with open(f"{directory}/{first_file_name}") as f:
    profile1 = list(map(lambda x: [float(x[0]), float(x[1])], csv.reader(f)))
with open(f"{directory}/{second_file_name}") as f:
    profile2 = list(map(lambda x: [float(x[0]), float(x[1])], csv.reader(f)))
n = len(profile1)

a = []
for ang in range(n):
    u = 0
    for i in range(n):
        u += abs(profile1[i][0] - profile2[(i + ang) % n][0]) / n
    o = 0
    for i in range(n):
        o += (abs(profile1[i][0] - profile2[(i + ang) % n][0]) - u) ** 2

    o = (o / n) ** 0.5

    a.append(o)

plt.plot(range(n), a)
plt.show()

angle = a.index(min(a)) / n * 2 * math.pi

profile1 = list(rad_to_dec(rad_cords=profile1))
profile2 = list(map(lambda x: [x[0], x[1] + angle], profile2))
profile2 = list(rad_to_dec(rad_cords=profile2))

t = turtle.Turtle()
s = turtle.Screen().getcanvas()
for ang in range(n-1):
    s.create_line(profile1[ang][0], profile1[ang][1], profile1[ang + 1][0], profile1[ang + 1][1])
    s.create_line(profile2[ang][0], profile2[ang][1], profile2[ang + 1][0], profile2[ang + 1][1])
turtle.mainloop()
