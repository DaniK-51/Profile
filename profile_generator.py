from cs_change import *
from random import random
import math


def gen_profile(d: float = 1000, min_div: float = -20, max_div: float = 20, step: int = 1, center_div: float = 50):
    # generating ref points every 30 degree
    ref_points = [(d/2 - (random() * (max_div - min_div) + min_div)) for _ in range(12)]
    ref_points.append(ref_points[0])

    # blow other coordinates every "step" degree
    generated_profile = []
    for n in range(12):
        generated_profile.append([ref_points[n], 30 * n * math.pi / 180])
        for ang in range(step, 30, step):
            generated_profile.append([ref_points[n] + (ref_points[n + 1] - ref_points[n]) / 30 * ang,
                                      (30 * n + ang) * math.pi / 180])

    # normalize length of circle
    generated_profile = list(rad_to_dec(rad_cords=generated_profile))

    # find length of circle
    l = 0
    for ang in range(len(generated_profile)):
        dx = (generated_profile[ang][0] - generated_profile[(ang + 1) % len(generated_profile)][0])
        dy = (generated_profile[ang][1] - generated_profile[(ang + 1) % len(generated_profile)][1])
        l += (dx ** 2 + dy ** 2) ** 0.5

    # correct coordinates
    k = math.pi * d / l
    generated_profile = list(map(lambda xy: [xy[0] * k, xy[1] * k], generated_profile))

    # displacement center
    dx, dy = random() * 2 * center_div - center_div, random() * 2 * center_div - center_div
    generated_profile = list(map(lambda xy: [xy[0] - dx, xy[1] - dy], generated_profile))
    generated_profile = list(dec_to_rad(dec_cords=generated_profile))

    return rad_interpolation(generated_profile)


if __name__ == "__main__":
    import turtle
    profile = gen_profile()
    dec_profile = list(rad_to_dec(rad_cords=profile))
    print(*profile, sep='\n')
    t = turtle.Turtle()
    for x, y in dec_profile:
        t.goto(x, y)
    turtle.mainloop()
