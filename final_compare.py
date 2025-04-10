import csv
import turtle
from cs_change import *
# import matplotlib.pyplot as plt
from stat_tube_pos import stat_tube_pos
from angles_of_arms import find_angles

directory = "profiles"
first_file_name = "file_1.csv"
second_file_name = "file_2.csv"
dx1, r = 300, 150
dx2, dy, r1, r2 = 300, 0, 150, 100

with open(f"{directory}\\{first_file_name}") as f:
    profile1 = list(map(lambda x: [float(x[0]), float(x[1])], csv.reader(f)))
with open(f"{directory}\\{second_file_name}") as f:
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

angle = a.index(min(a)) * math.pi / 180

print(f"angle\t = {angle.__format__('.3')} at {min(a):.3}")

# plt.plot(range(n), a)
# plt.plot(range(n), a1, '--')
# plt.show()

dec_profile1 = list(rad_to_dec(rad_cords=profile1))
profile2 = list(map(lambda x: [x[0], x[1] + angle], profile2))
dec_profile2 = list(rad_to_dec(rad_cords=profile2))

s = turtle.Screen().getcanvas()
k = 0.5

for ang in range(n):
    s.create_line(dec_profile1[ang][0] * k, -dec_profile1[ang][1] * k, dec_profile1[ang - 1][0] * k, -dec_profile1[ang - 1][1] * k)
    s.create_line(dec_profile2[ang][0] * k, -dec_profile2[ang][1] * k, dec_profile2[ang - 1][0] * k, -dec_profile2[ang - 1][1] * k)

center = stat_tube_pos(profile1, dx1, r)

s.create_oval(-(center[0] + dx1 + r) * k, (center[1] - r) * k, -(center[0] + dx1 - r) * k, (center[1] + r) * k)
s.create_oval(-(center[0] - dx1 + r) * k, (center[1] - r) * k, -(center[0] - dx1 - r) * k, (center[1] + r) * k)

s.create_oval(-(center[0] + dx2 + r1) * k, (center[1] - r1) * k, -(center[0] + dx2 - r1) * k, (center[1] + r1) * k)
s.create_oval(-(center[0] - dx2 + r1) * k, (center[1] - r1) * k, -(center[0] - dx2 - r1) * k, (center[1] + r1) * k)

angles = find_angles(profile2, center, dx2, dy, r1, r2)
print(f"left angle = {angles[0].__format__('.3')}, right angle = {angles[1].__format__('.3')}")

s.create_oval(k * (math.cos(math.pi - angles[0]) * r1 - r2 - center[0] - dx2), -k * (math.sin(math.pi - angles[0]) * r1 - r2 - center[1]), k * (math.cos(math.pi - angles[0]) * r1 + r2 - center[0] - dx2), -k * (math.sin(math.pi - angles[0]) * r1 + r2 - center[1]))
s.create_oval(k * (math.cos(angles[1]) * r1 - r2 - center[0] + dx2), -k * (math.sin(angles[1]) * r1 - r2 - center[1]), k * (math.cos(angles[1]) * r1 + r2 - center[0] + dx2), -k * (math.sin(angles[1]) * r1 + r2 - center[1]))

turtle.mainloop()
