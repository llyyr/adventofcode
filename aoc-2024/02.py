#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace('py', 'txt')
inp = [[int(y) for y in x.split()] for x in open(filename)]

def safe(r):
    trend = {b - a for a, b in pairwise(r)}
    return trend.issubset({1, 2, 3}) or trend.issubset({-1, -2, -3})

print(sum(safe(r) for r in inp))
print(sum(any(safe(r[j] for j in range(len(r)) if j != i) for i in range(len(r))) for r in inp))
