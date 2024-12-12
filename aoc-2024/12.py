#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")
L = [list(x) for x in open(filename).read().split()]
R, C = len(L), len(L[0])
DIAGS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

def dfs(r, c, n, G, seen):
    stack = [(r, c)]
    while stack:
        rr, cc = stack.pop()
        if (rr, cc) in seen:
            continue
        seen.add((rr, cc))
        G[(rr, cc)] = n
        for dr, dc in DIRS:
            nr, nc = rr + dr, cc + dc
            if (nr, nc) in seen or not (0 <= nr < R and 0 <= nc < C):
                continue
            if L[nr][nc] == L[rr][cc]:
                stack.append((nr, nc))

def flood():
    seen, G, n = set(), {}, 0
    for r in range(R):
        for c in range(C):
            if (r, c) not in seen:
                n += 1
                dfs(r, c, n, G, seen)
    return G

def solve(area, perim, corners):
    G = flood()
    for r in range(R):
        for c in range(C):
            cur = G[(r, c)]
            area[cur] += 1
            perim[cur] += sum(cur != G.get((r + dr, c + dc)) for dr, dc in DIRS)
            for dr, dc in DIAGS:
                di = G.get((r + dr, c))
                dj = G.get((r, c + dc))
                dk = G.get((r + dr, c + dc))
                if (cur != di and cur != dj) or (cur == di == dj and cur != dk):
                    corners[cur] += 1

    return (sum(area[x] * perim[x] for x in area),
            sum(area[x] * corners[x] for x in area))

print(*solve(defaultdict(int), defaultdict(int), defaultdict(int)))
