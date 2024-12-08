#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")
G = open(filename).read().splitlines()
R, C = len(G), len(G[0])
nodes = {}
for r, row in enumerate(G):
    for c, ch in enumerate(row):
        if ch != ".":
            nodes.setdefault(ch, []).append((r, c))

p1, p2 = set(), set()
in_bounds = lambda r, c: 0 <= r < R and 0 <= c < C
def walk(r, c, dr, dc):
    if in_bounds(r, c): p1.add((r, c)) # part 1
    while in_bounds(r, c):
        p2.add((r, c))
        r, c = r + dr, c + dc

def solve():
    for v in nodes.values():
        p2.update(v)
        for (r1, c1), (r2, c2) in combinations(v, 2):
            dr, dc = r2 - r1, c2 - c1
            walk(r1 - dr, c1 - dc, -dr, -dc)
            walk(r2 + dr, c2 + dc, dr, dc)
    return len(p1), len(p2)

print(*solve())
