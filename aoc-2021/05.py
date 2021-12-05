#!/usr/bin/env python3.10
inp = [(*map(int, l.replace('->', ',').split(',')),) for l in open(0)]

def solve(p2=False):
    grid = {}
    for x1, y1, x2, y2 in inp:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[(x1, y)] = 1 if (x1, y) not in grid else grid[(x1, y)] + 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[(x, y1)] = 1 if (x, y1) not in grid else grid[(x, y1)] + 1
        elif p2 and abs(x1-x2) == abs(y1-y2):
            dx = -1 if x1 > x2 else 1
            dy = -1 if y1 > y2 else 1
            for i in range(abs(x1-x2) + 1):
                xy = (x1 + (dx*i), y1 + (dy*i))
                grid[xy] = 1 if xy not in grid else grid[xy] + 1
    return sum(val > 1 for val in grid.values())

print(solve())
print(solve(True))

