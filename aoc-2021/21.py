#!/usr/bin/env python3.10
from itertools import cycle, product
from functools import cache

def part1(p1, p2):
    rolls = s1 = s2 = 0
    die = cycle(range(1, 101))
    while True:
        rolls += 3
        r = sum(next(die) for _ in range(3))
        p1 = (p1 + r) % 10 or 10
        s1 += p1
        if s1 >= 1000:
            break
        p1, p2, s1, s2 = p2, p1, s2, s1
    return s2*rolls

@cache
def part2(p1, p2, s1=0, s2=0):
    if s2 >= 21:
        return 0, 1
    wins1, wins2 = 0, 0
    for r in product((1,2,3), repeat=3):
        np1 = (p1 + sum(r)) % 10 or 10
        dy, dx = part2(p2, np1, s2, s1+np1)
        wins1 += dx
        wins2 += dy
    return wins1, wins2

inp = [int(l[-1]) for l in open(0).read().splitlines()]
print(part1(*inp))
print(max(part2(*inp)))
