from cs_change import *


def bin_finder(arr: list[float], target: float):
    l, r = 0, len(arr) - 1
    while l != r:
        c = l + (r - l) // 2 + 1
        if arr[c] > target:
            r = c - 1
        else:
            l = c
    return l


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
            ext_profile.append([profile[i][0] + n3[0] * r, profile[i][1] + n3[1] * r])

    l, r = -dx, dx

    l_profile = list(filter(lambda xy: xy[0] < 0 and xy[1] < 0, ext_profile))
    r_profile = list(filter(lambda xy: xy[0] >= 0 and xy[1] < 0, ext_profile))

    while r - l > .1:
        xl, xr = l + (r - l) / 3, l + (r - l) / 3 * 2
        x0 = xl - dx
        bf = bin_finder(list(map(lambda xy: xy[0], l_profile)), x0)
        x1, x2 = l_profile[bf][0], l_profile[bf + 1][0]
        y1, y2 = l_profile[bf][1], l_profile[bf + 1][1]
        k = (y2 - y1) / (x2 - x1)
        y0 = k * x0 + y1 - k * x1

        x0 = xl + dx
        bf = bin_finder(list(map(lambda xy: xy[0], r_profile)), x0)
        x1, x2 = r_profile[bf][0], r_profile[bf + 1][0]
        y1, y2 = r_profile[bf][1], r_profile[bf + 1][1]
        k = (y2 - y1) / (x2 - x1)
        dyl = abs(y0 - (k * x0 + y1 - k * x1))

        x0 = xr - dx
        bf = bin_finder(list(map(lambda xy: xy[0], l_profile)), x0)
        x1, x2 = l_profile[bf][0], l_profile[bf + 1][0]
        y1, y2 = l_profile[bf][1], l_profile[bf + 1][1]
        k = (y2 - y1) / (x2 - x1)
        y0 = k * x0 + y1 - k * x1

        x0 = xr + dx
        bf = bin_finder(list(map(lambda xy: xy[0], r_profile)), x0)
        x1, x2 = r_profile[bf][0], r_profile[bf + 1][0]
        y1, y2 = r_profile[bf][1], r_profile[bf + 1][1]
        k = (y2 - y1) / (x2 - x1)
        dyr = abs(y0 - (k * x0 + y1 - k * x1))

        if dyl > dyr:
            l = xl
        else:
            r = xr

    center = [(l + r) / 2, 0.]
    x0 = center[0] - dx

    bf = bin_finder(list(map(lambda xy: xy[0], l_profile)), x0)
    x1, x2 = l_profile[bf][0], l_profile[bf + 1][0]
    y1, y2 = l_profile[bf][1], l_profile[bf + 1][1]
    k = (y2 - y1) / (x2 - x1)
    center[1] = k * x0 + y1 - k * x1

    return [-center[0], -center[1]]
