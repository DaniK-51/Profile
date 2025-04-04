import math


def rad_to_dec(rad_cord:list[float]=None, rad_cords:list[list[float]]=None):
    """
    Function generate coordinates in decart system. Use only rad_cord or only rad_cords
    :param rad_cord: list[x:float, y:float]
    :param rad_cords: list[list[x:float, y:float]]
    :return: list[x:float, y:float] or Generator[list[x:float, y:float]]
    """
    if rad_cord:
        xr, yr = rad_cord
        return [xr * math.cos(yr), xr * math.sin(yr)]
    if rad_cords:
        for cord in rad_cords:
            xr, yr = cord
            yield [xr * math.cos(yr), xr * math.sin(yr)]


def dec_to_rad(dec_cord:list[float]=None, dec_cords:list[list[float]]=None):
    """
    Function generate coordinates in radial system. Use only dec_cord or only dec_cords
    :param dec_cord: list[x:float, y:float]
    :param dec_cords: list[list[x:float, y:float]]
    :return: list[x:float, y:float] or Generator[list[x:float, y:float]]
    """
    if dec_cord:
        xd, yd = dec_cord
        if xd >= 0 and yd >= 0:
            return [(xd ** 2 + yd ** 2) ** 0.5, math.atan(yd / xd)]
        if xd < 0 and yd > 0:
            return [(xd ** 2 + yd ** 2) ** 0.5, math.atan(-xd / yd) + (math.pi / 2)]
        if xd < 0 and yd < 0:
            return [(xd ** 2 + yd ** 2) ** 0.5, math.atan(yd / xd) + math.pi]
        return [(xd ** 2 + yd ** 2) ** 0.5, math.atan(-xd / yd) + (math.pi * 3 / 2)]
    if dec_cords:
        for cord in dec_cords:
            xd, yd = cord
            if xd >= 0 and yd >= 0:
                return [(xd ** 2 + yd ** 2) ** 0.5, math.atan(yd / xd)]
            if xd < 0 and yd > 0:
                return [(xd ** 2 + yd ** 2) ** 0.5, math.atan(-xd / yd) + (math.pi / 2)]
            if xd < 0 and yd < 0:
                return [(xd ** 2 + yd ** 2) ** 0.5, math.atan(yd / xd) + math.pi]
            yield [(xd ** 2 + yd ** 2) ** 0.5, math.atan(-xd / yd) + (math.pi * 3 / 2)]


def rad_interpolation(rad_cords:list[list[float]]):
    """
    Function recalculates coordinates with the same angular step using interpolation
    :param rad_cords: list[list[x:float, y:float]]
    :return: list[list[x:float, y:float]]
    """
    for ang in range(0, 360, 360 // len(rad_cords)):
        rotated_profile = list(map(lambda x: [x[0], x[1] - ang * math.pi / 180], rad_cords))
        rotated_profile1 = list(filter(lambda x: x[0] > 0 and x[1] > 0, rad_to_dec(rad_cords=rotated_profile)))
        rotated_profile2 = list(filter(lambda x: x[0] > 0 and x[1] < 0, rad_to_dec(rad_cords=rotated_profile)))
        rotated_profile1.sort(key=lambda x: x[1])
        rotated_profile2.sort(key=lambda x: x[1], reverse=True)
        x1, y1 = rotated_profile1[0]
        x2, y2 = rotated_profile2[0]
        yield [x1 - y1 * (x2 - x1) / (y2 - y1), ang * math.pi / 180]
