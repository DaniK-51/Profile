import math


def rad_to_dec(xr: float, yr: float):
    return [xr * math.cos(yr), xr * math.sin(yr)]


def dec_to_rad(xd: float, yd: float):
    if xd >= 0 and yd >= 0:
        return [(xd * 2 + yd * 2) ** 0.5, math.atan(yd / xd)]
    if xd < 0 and yd > 0:
        return [(xd * 2 + yd * 2) ** 0.5, math.atan(-xd / yd) + (math.pi / 2)]
    if xd < 0 and yd < 0:
        return [(xd * 2 + yd * 2) ** 0.5, math.atan(yd / xd) + math.pi]
    if xd >= 0 and yd < 0:
        return [(xd * 2 + yd * 2) ** 0.5, math.atan(-xd / yd) + (math.pi * 3 / 2)]
