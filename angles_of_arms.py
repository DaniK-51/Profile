from cs_change import *


def find_angles(profile: list[list[float]], profile_center: list[float], dx: float, y: float, r1: float, r2: float):
    profile = list(rad_to_dec(rad_cords=profile))

    l_profile = list(map(lambda xy: [xy[0] + profile_center[0] + dx, xy[1] + profile_center[1] - y],
                         filter(lambda xy: xy[0] < 0 and xy[1] < 0, profile)))
    r_profile = list(map(lambda xy: [xy[0] + profile_center[0] - dx, xy[1] + profile_center[1] - y],
                         filter(lambda xy: xy[0] >= 0 and xy[1] < 0, profile)))

    ang_l = []
    for i in range(len(l_profile) - 1):
        try:
            k = (l_profile[i][1] - l_profile[i + 1][1]) / (l_profile[i][0] - l_profile[i + 1][0])
            b = l_profile[i][1] - k * l_profile[i][0]
            b1 = b - r2 * (1 + k ** 2) ** 0.5
            x = -(b1 * k + ((b1 * k) ** 2 - (k ** 2 + 1) * (b1 ** 2 - r1 ** 2)) ** 0.5) / (k ** 2 + 1)
            ang_l.append(abs(math.atan((k * x + b1) / x)))
        except TypeError:
            ang_l.append(0)

    ang_r = []
    for i in range(len(r_profile) - 1):
        try:
            k = (r_profile[i][1] - r_profile[i + 1][1]) / (r_profile[i][0] - r_profile[i + 1][0])
            b = r_profile[i][1] - k * r_profile[i][0]
            b1 = b - r2 * (1 + k ** 2) ** 0.5
            x = (-b1 * k + ((b1 * k) ** 2 - (k ** 2 + 1) * (b1 ** 2 - r1 ** 2)) ** 0.5) / (k ** 2 + 1)
            ang_r.append(abs(math.atan((k * x + b1) / x)))
        except TypeError:
            ang_r.append(0)

    return [max(ang_l), max(ang_r)]
