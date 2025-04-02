from cs_change import *
from random import random


def gen_profile(d: float = 1000, min_div: float = -20, max_div: float = 20, step: int = 1, center_div: float = 50):
    # создание референстых точек каждые 30 градусов
    ref_points = [(d/2 - (random() * (max_div - min_div) + min_div)) for _ in range(12)]
    ref_points.append(ref_points[0])

    # заполнение остальных координат каждые step градусов
    generated_profile = []
    for n in range(12):
        generated_profile.append([ref_points[n], 30 * n * math.pi / 180])
        for ang in range(step, 30, step):
            generated_profile.append([ref_points[n] + (ref_points[n + 1] - ref_points[n]) / 30 * ang,
                                      (30 * n + ang) * math.pi / 180])

    # смещение центра ск
    generated_profile = list(map(lambda x: rad_to_dec(*x), generated_profile))
    dx, dy = random() * 2 * center_div - center_div, random() * 2 * center_div - center_div
    generated_profile = list(map(lambda x: [x[0] - dx, x[1] - dy], generated_profile))
    generated_profile = list(map(lambda x: dec_to_rad(*x), generated_profile))

    # интерполяция правильных цилиндрических координат
    res_profile = []
    for ang in range(0, 360, step):
        rotated_profile = list(map(lambda x: [x[0], x[1] - ang * math.pi / 180], generated_profile))
        rotated_profile1 = list(filter(lambda x: x[0] > 0 and x[1] > 0, map(lambda x: rad_to_dec(*x), rotated_profile)))
        rotated_profile2 = list(filter(lambda x: x[0] > 0 and x[1] < 0, map(lambda x: rad_to_dec(*x), rotated_profile)))
        rotated_profile1.sort(key=lambda x: x[1])
        rotated_profile2.sort(key=lambda x: x[1], reverse=True)
        x1, y1 = rotated_profile1[0]
        x2, y2 = rotated_profile2[0]
        res_profile.append([x1 - y1 * (x2 - x1) / (y2 - y1), ang * math.pi / 180])
    return res_profile


if __name__ == "__main__":
    import turtle
    profile = gen_profile()
    dec_profile = list(map(lambda x: rad_to_dec(*x), profile))
    print(*profile, sep='\n')
    t = turtle.Turtle()
    for x, y in dec_profile:
        t.goto(x, y)
    turtle.mainloop()
