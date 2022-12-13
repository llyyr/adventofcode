#!/usr/bin/env python3.11

from functools import cmp_to_key
from json import loads

inp = open('13.txt').read().split('\n\n')
packets = []

def cmp(l, r):
    match l, r:
        case int(), int(): return (l > r) - (l < r)
        case int(), list(): return cmp([l], r)
        case list(), int(): return cmp(l, [r])
        case list(), list():
            return next((x for x in map(cmp, l, r) if x), cmp(len(l), len(r)))

p1 = 0
for i, p in enumerate(([*map(loads, x.split())] for x in inp), 1):
    packets.extend(p)
    if cmp(*p) == -1:
        p1 += i
print(p1)

packets.extend([[2], [6]])
packets.sort(key=cmp_to_key(cmp))
print((packets.index([2]) + 1) * (packets.index([6]) + 1))
