#!/usr/bin/env python3.10
def solve():
    points, inst = open(0).read().split('\n\n')
    dots = set()
    for l in points.splitlines():
        dots.add((*map(int, l.split(',')),))
    part1 = True
    for l in inst.splitlines():
        start, end = l.split('=')
        axis = start[-1]
        val = int(end)
        if axis == 'x':
            dots = {(val-abs(x-val), y) for x, y in dots}
        elif axis == 'y':
            dots = {(x, val-abs(y-val)) for x, y in dots}
        if part1:
            part1 = False
            print(len(dots))
    mx = max(x for x, y in dots)
    my = max(y for x, y in dots)
    for y in range(my+1):
        for x in range(mx+1):
            print('#' if (x, y) in dots else ' ', end=' ')
        print()

solve()

