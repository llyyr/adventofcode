#!/usr/bin/env python3.11

from aochelper import *

inp = hash2coords(open('23.txt').read())

t = 0
try_dirs = list(range(4))
while t:=t+1:
    moves = defaultdict(list)
    for x, y in inp:
        if any(d in inp for d in neighbours(x, y, 8)):
            directions = [
                    ((x-1, y-1), (x,y-1), (x+1, y-1)), # north
                    ((x-1, y+1), (x, y+1), (x+1, y+1)), # south
                    ((x-1, y-1), (x-1, y), (x-1, y+1)), # west
                    ((x+1, y-1), (x+1, y), (x+1, y+1)), # east
                    ]
            goto = ((0, -1), (0, 1), (-1,0), (1,0))
            for dir in try_dirs:
                if all(adj not in inp for adj in directions[dir]):
                    dx, dy = goto[dir]
                    moves[(x+dx, y+dy)].append((x, y))
                    break
    moves = {k: v[0] for k, v in moves.items() if len(v) == 1}
    inp = (inp - set(moves.values())) | moves.keys()
    if not moves:
        print(t)
        break

    try_dirs.append(try_dirs.pop(0))

    if t == 10:
        min_x = max_x = min_y = max_y = 0
        for x, y in inp:
            min_x = min(x, min_x)
            max_x = max(x, max_x)
            min_y = min(y, min_y)
            max_y = max(y, max_y)
        
        print(sum((x, y) not in inp
                  for x in range(min_x, max_x+1)
                  for y in range(min_y, max_y+1)))

