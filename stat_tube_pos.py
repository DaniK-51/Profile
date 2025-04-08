from cs_change import *
import math
import turtle
from profile_generator import *
import csv


def stat_tube_pos(profile: list[list[float]], dx: float, r: float, angle: float = 0):
    if angle:
        profile = list(map(lambda xy: [xy[0], (xy[1] + angle) % (math.pi * 2)], profile))

    profile = list(rad_to_dec(rad_cords=profile))

    ext_profile = []
    n = len(profile)
    for i in range(n):
        i2, i1 = (i + 1) % n, (i - 1) % n

        k1 = (profile[i][1] - profile[i1][1]) / (profile[i][0] - profile[i1][0])
        k2 = (profile[i][1] - profile[i2][1]) / (profile[i][0] - profile[i2][0])
        k3 = (profile[i1][1] - profile[i2][1]) / (profile[i1][0] - profile[i2][0])

        b1 = profile[i][1] - k1 * profile[i][0]
        b2 = profile[i][1] - k2 * profile[i][0]
        b3 = profile[i1][1] - k3 * profile[i1][0]

        n1 = [math.cos(math.atan(-1 / k1)), math.sin(math.atan(-1 / k1))]
        if (b1 > 0 and n1[1] < 0) or (b1 < 0 and n1[1] > 0):
            n1 = [-n1[0], -n1[1]]

        n2 = [math.cos(math.atan(-1 / k2)), math.sin(math.atan(-1 / k2))]
        if (b2 > 0 and n2[1] < 0) or (b2 < 0 and n2[1] > 0):
            n2 = [-n2[0], -n2[1]]

        xn = (b2 - b1) / (k1 - k2)
        yn = k1 * xn + b1

        if (b3 < 0 and yn < k3 * xn + b3) or (b3 > 0 and yn > k3 * xn + b3):
            ext_profile.append([profile[i][0] + n1[0] * r, profile[i][1] + n1[1] * r])
            ext_profile.append([profile[i][0] + n2[0] * r, profile[i][1] + n2[1] * r])

        else:
            n3 = [n1[0] + n2[0], n1[1] + n2[1]]
            l3 = (n3[0] ** 2 + n3[1] ** 2) ** .5
            n3 = [n3[0] / l3 * (2 / (1 + (n1[0] * n2[0] + n1[1] * n2[1]))) ** 0.5,
                  n3[1] / l3 * (2 / (1 + (n1[0] * n2[0] + n1[1] * n2[1]))) ** 0.5]
            print(n3)
            ext_profile.append([profile[i][0] + n3[0] * r, profile[i][1] + n3[1] * r])

    t = turtle.Turtle()
    s = turtle.Screen().getcanvas()
    k = 0.5
    for i in range(len(ext_profile)):
        s.create_line(ext_profile[i-1][0] * k, -ext_profile[i-1][1] * k, ext_profile[i][0] * k, -ext_profile[i][1] * k, fill="blue")
    for i in range(n):
        s.create_line(profile[i-1][0] * k, -profile[i-1][1] * k, profile[i][0] * k, -profile[i][1] * k)
    s.mainloop()


directory = "profiles"
file_name = "file_1.csv"

f = open(f"{directory}/{file_name}")
c = list(csv.reader(f))
c = list(map(lambda x: [float(x[0]), float(x[1])], c))

stat_tube_pos(c, 0, 20)
