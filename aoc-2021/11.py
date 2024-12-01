#!/usr/bin/env python3.10
G = [[*map(int, l.rstrip())] for l in open(0)]
C, R = len(G[0]), len(G)

def solve(G=G):
    step = 0
    total = 0
    while True:
        step += 1
        flashes = 0
        G = [[x+1 for x in r] for r in G]
        stack = []
        for r in range(R):
            for c in range(C):
                if G[r][c] > 9:
                    stack.append((r, c))
        while stack:
            r, c = stack.pop()
            flashes += 1
            for rr in (r-1, r, r+1):
                for cc in (c-1, c, c+1):
                    if 0<=cc<C and 0<=rr<R:
                        G[rr][cc] += 1
                        if G[rr][cc] == 10:
                            stack.append((rr, cc))
        G = [[0 if x>9 else x for x in r] for r in G]
        total += flashes
        if step == 100:
            print(total)
        if flashes == C*R:
            print(step)
            break

solve()
