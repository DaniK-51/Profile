from cs_change import *
from random import random
import turtle


def gen_profile(d: float = 1000, min_div: float = -20, max_div: float = 20, step: int = 1, center_div: float = 50):
    ref_points = [(d/2 - (random() * (max_div - min_div) + min_div)) for _ in range(12)]
    ref_points.append(ref_points[0])

    generated_profile = []
    for n in range(12):
        generated_profile.append([ref_points[n], 30 * n * math.pi / 180])
        for ang in range(step, 30, step):
            generated_profile.append([ref_points[n] + (ref_points[n + 1] - ref_points[n]) / 30 * ang,
                                      (30 * n + ang) * math.pi / 180])

    generated_profile = list(map(lambda x: rad_to_dec(*x), generated_profile))
    dx, dy = random() * 2 * center_div - center_div, random() * 2 * center_div - center_div
    generated_profile = list(map(lambda x: [x[0] - dx, x[1] - dy], generated_profile))
    generated_profile = list(map(lambda x: dec_to_rad(*x), generated_profile))
    return generated_profile


profile = gen_profile()
dec_profile = list(map(lambda x: rad_to_dec(*x), profile))
print(*profile, sep='\n')
t = turtle.Turtle()
for x, y in dec_profile:
    t.goto(x/2, y/2)
turtle.mainloop()
