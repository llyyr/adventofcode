#!/usr/bin/env python3.11

inp = open('06.txt').read()

def solve(n):
    for i in range(n, 1+len(inp)):
        if len({*inp[i-n:i]}) == n:
            return i

print(*map(solve, (4, 14)))

