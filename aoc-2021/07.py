#!/usr/bin/env python3.10
inp = [*map(int, next(open(0)).split(','))]

def solve(p2=False):
    out = float('inf')
    for i in range(min(inp), max(inp)+1):
        ans = 0
        for j in inp:
            t = abs(i-j)
            ans += t if not p2 else (t*(t+1))//2
        out = min(out, ans)
    print(out)

solve()
solve(True)

