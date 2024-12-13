#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")
inp = open(filename).read().split("\n\n")
N = 10000000000000
stupid_fucking_puzzle = lambda s: math.isclose(round(s), s, rel_tol=0.0)

def solve_linear(x1, y1, x2, y2, xp, yp, part):
    determinant = x1 * y2 - y1 * x2
    eq1 = (xp * y2 - yp * x2) / determinant
    eq2 = (yp * x1 - xp * y1) / determinant

    if all(x >= 0 and stupid_fucking_puzzle(x) and (part or x <= 100) for x in (eq1, eq2)):
        return 3 * round(eq1) + round(eq2)
    return 0

def solve(inp, N):
    ans = [0, 0]
    for l in inp:
        x1, y1, x2, y2, xp, yp = ints(l)
        for part in range(2):
            ans[part] += solve_linear(x1, y1, x2, y2, xp, yp, part)
            xp += N
            yp += N
    return ans

print(*solve(inp, N))
