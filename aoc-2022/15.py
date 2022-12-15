#!/usr/bin/env python3.11

from aochelper import *
from z3 import Or, Ints, Solver, sat

def solve(p2=4000000, p1=2000000):
    S = set()
    B = set()
    x, y = Ints('x y')
    s = Solver()
    s.add(0 <= x)
    s.add(x <= p2)
    s.add(0 <= y)
    s.add(y <= p2)
    for line in open('15.txt').read().splitlines():
        sx, sy, bx, by = ints(line)
        dist = abs(sx - bx) + abs(sy - by)
        lim = dist - abs(sy - p1)
        if by == p1:
            B.add(bx)
        for sensor in range(sx - lim, sx + lim + 1):
            S.add(sensor)
        s.add(Or((x + y > dist + sx + sy),
                 (x + y < -dist + sx + sy),
                 (x - y > dist + sx - sy),
                 (x - y < -dist + sx - sy)))

    assert s.check() == sat
    m = s.model()
    return len(S-B), m[x].as_long() * p2 + m[y].as_long()

print(*solve())
