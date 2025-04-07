import csv
from profile_generator import gen_profile
import copy


def save(direct: str, name: str | list[str]):
    if name is str:
        f = open(f"{direct}\\{name}", 'w', newline='')
        c = csv.writer(f)
        c.writerows(gen_profile())
    else:
        gen = list(gen_profile())
        for i in name:
            f = open(f"{direct}\\{i}", 'w', newline='')
            c = csv.writer(f)
            c.writerows(gen)


save("profiles", ["file_1.csv", "file_1_alt.csv"])
save("profiles", ["file_2.csv", "file_2_alt.csv"])
