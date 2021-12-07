#!/usr/bin/env python3.10
inp = list(map(int, next(open(0)).split(',')))

def solve(p2=False):
    out = 0
    for i in range(min(inp), max(inp)+1):
        ans = 0
        for j in inp:
            t = abs(i-j)
            ans += t if not p2 else (t*(t+1))//2
        out = ans if out == 0 else min(out, ans)
    print(out)

solve()
solve(True)

