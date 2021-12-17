#!/usr/bin/env python3.10
from collections import defaultdict
# "target area: x=195..238, y=-93..-67"

def solve():
    xmin, xmax, ymin, ymax = 195, 238, -93, -67 # input
    #xmin, xmax, ymin, ymax = 2000, 2039, -9960, -9956 # smol bigboy
    #xmin, xmax, ymin, ymax = 22000, 22045, -99960, -99956 # bigger bigboy

    print(ymin*(ymin+1)//2)

    y_map = set()
    for y in range(1, -ymin+1):
        for x in range(y):
            if ymin<=x*(x+1)//2 - y*(y+1)//2<=ymax:
                y_map |= {(x, x+y), (-1-x, -1-x+y)}

    x_reversemap = defaultdict(list)
    v_fall = set()
    for x in range(1, xmax+1):
        for y in range(x):
            if xmin<=x*(x+1)//2 - y*(y+1)//2<=xmax:
                x_reversemap[x-y-1] += [x]
                if y == 0:
                    v_fall |= {x}

    valid = set()
    for y, step in y_map:
        if min(v_fall) < step:
            for x in v_fall:
                valid |= {(x, y)}
        for x in x_reversemap[step]:
            valid |= {(x, y)}
    return len(valid)

print(solve())
