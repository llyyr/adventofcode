#!/usr/bin/env python3.11

from aochelper import *

inp = set(tuple(map(int, line.split(','))) for line in open('18.txt'))

def adjacent3d(x, y, z):
    for d in (-1, 1):
        yield x + d, y, z
        yield x, y + d, z
        yield x, y, z + d

print(sum(n not in inp for c in inp for n in adjacent3d(*c)))

min_pt = tuple(min(a[i] - 1 for a in inp) for i in range(3))
max_pt = tuple(max(a[i] + 1 for a in inp) for i in range(3))
seen = set()
Q = deque([min_pt])
while Q:
    cur = Q.popleft()
    if cur in seen:
        continue
    seen.add(cur)
    for new_pt in (set(adjacent3d(*cur)) - seen - inp):
        if all(min_pt[i] <= new_pt[i] <= max_pt[i] for i in range(3)):
            Q.append(new_pt)

print(sum(s in seen for c in inp for s in adjacent3d(*c)))

