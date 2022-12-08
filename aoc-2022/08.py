#!/usr/bin/env python3.11

G = [[*map(int, l.rstrip())] for l in open(0)]
C, R = len(G[0]), len(G)
p1, p2 = 0, 0

for r in range(R):
    for c in range(C):
        vis, sc = 0, 1
        for (dr, dc) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            rr, cc, i = r+dr, c+dc, 0
            while 0<=rr<R and 0<=cc<C:
                i += 1
                if G[rr][cc] >= G[r][c]:
                    break
                rr, cc = rr+dr, cc+dc
            else:
                vis = 1
            sc *= i
        p1 += vis
        p2 = max(p2, sc)

print(p1, p2)
