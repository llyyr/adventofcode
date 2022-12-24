#!/usr/bin/env python3.11

from aochelper import *

inp = [r[1:-1] for r in open('24.txt').read().splitlines()[1:-1]]
G = {(r, c): point for r, l in enumerate(inp) for c, point in enumerate(l)}
R = len(inp)
C = len(inp[0])
start = (-1, 0)
goal = (R, C - 1)

def solve(start, goal, t):
    occlusion = lambda r, c, t: G[((r - t) % R, c)] == 'v' or \
                                G[((r + t) % R, c)] == '^' or \
                                G[(r, (c - t) % C)] == '>' or \
                                G[(r, (c + t) % C)] == '<'
    seen = set()
    Q = deque([(start, t)])
    while Q:
        state = Q.popleft()
        if state in seen:
            continue
        seen.add(state)
        (r, c), t = state
        if (r, c) == goal:
            break
        for rr, cc in ((r, c), (r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if (rr, cc) == goal or (rr, cc) == start or \
                    ((rr,cc) in G and not occlusion(rr, cc, t+1)):
                Q.append(((rr, cc), t+1))
    return t

r1 = solve(start, goal, 0)
print(r1)
r2 = solve(goal, start, r1)
r3 = solve(start, goal, r2)
print(r3)

