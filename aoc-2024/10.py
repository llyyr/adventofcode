#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")
inp = [[int(ch) for ch in row.strip()] for row in open(filename)]
R, C = len(inp), len(inp[0])

@cache
def explore(di, r, c, S):
    N = []
    for dr, dc in DIRS:
        rr, cc = r + dr, c + dc
        if 0 <= rr < R and 0 <= cc < C and inp[rr][cc] == di + 1:
            N.append((S, (di + 1, rr, cc)))
    return N

stack = [n for r, row in enumerate(inp) for c, ch in enumerate(row) if ch == 0
    for n in explore(0, r, c, (0, r, c))]
ans = []
while stack:
    S, (di, r, c) = stack.pop()
    if di == 9:
        ans.append((S, (9, r, c)))
    else:
        stack.extend(explore(di, r, c, S))

print(len(set(ans)), len(ans))
