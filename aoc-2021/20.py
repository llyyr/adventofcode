#!/usr/bin/env python3.10
from collections import defaultdict

def solve(iterations):
    inp = [l.strip() for l in open('20.txt')]
    rule = inp[0]
    inp = inp[2:]
    R = range(len(inp))
    C = range(len(inp[0]))
    G = defaultdict(lambda: '.')

    for r in R:
        for c in C:
            G[(r, c)] = inp[r][c]

    for i in range(iterations):
        new_G = defaultdict(lambda: (rule[-1], rule[0])[i%2])
        for r in G:
            new_G[r] = G[r]
        R = range(R[0]-2, R[-1]+2)
        C = range(C[0]-2, C[-1]+2)
        for r in R:
            for c in C:
                s = ''
                for rr in (r-1, r, r+1):
                    for cc in (c-1, c, c+1):
                        s += G[(rr, cc)]
                s = s.replace('.', '0').replace('#', '1')
                new_G[(r, c)] = rule[int(s, 2)]
        G = new_G
    print(sum(1 for c in G if G[c] == '#'))

solve(2)
solve(50)
