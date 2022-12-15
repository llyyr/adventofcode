#!/usr/bin/env python3.11

from aochelper import ints, timer
from itertools import combinations

sensors = [ints(line) for line in open('15.txt')]
dist = lambda x1, y1, x2, y2: abs(y2 - y1) + abs(x2 - x1)

def diag(sx, sy, bx, by, diagonal):
    r = dist(sx, sy, bx, by) + 1
    d = sx + sy if diagonal == "diag" else sx - sy
    return (d + r, d - r)

@timer
def p2(n=4000000):
    for s1, s2 in combinations(sensors, 2):
        for m, perp in zip(diag(*s1, "diag"), diag(*s2, "perp")):
            x = (m + perp) // 2
            y = m - x
            if not (0 <= x <= n and 0 <= y <= n):
                continue
            if all(dist(*p[:2], x, y) > dist(*p) for p in sensors):
                return x * n + y

print(p2())

