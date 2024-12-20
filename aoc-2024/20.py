#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")
G = open(filename).read().strip().splitlines()
R, C = len(G), len(G[0])
S, E = [(r, c) for r in range(R) for c in range(C) if G[r][c] in 'SE']

def is_open(r, c):
    return 0 <= r < R and 0 <= c < C and G[r][c] in ('.', 'S', 'E')

def floodfill(cell):
    dist = {cell: 0}
    Q = deque([cell])
    while Q:
        r, c = Q.popleft()
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if is_open(nr, nc) and (nr, nc) not in dist:
                dist[nr, nc] = dist[r, c] + 1
                Q.append((nr, nc))
    return dist

dist_from_S, dist_to_E = floodfill(S), floodfill(E)
time = dist_from_S[E]

def solve():
    p1, best_cheats = 0, {}
    for sr in range(R):
        for sc in range(C):
            if not is_open(sr, sc) or (sr, sc) not in dist_from_S:
                continue
            for rr, cc in ((sr + dr1 + dr2, sc + dc1 + dc2) for dr1, dc1 in DIRS for dr2, dc2 in DIRS):
                if is_open(rr, cc):
                    d_e = dist_to_E.get((rr, cc))
                    if d_e is not None:
                        if time - (dist_from_S[sr, sc] + 2 + d_e) >= 100:
                            p1 += 1
            cheat_dist = {(sr, sc): 0}
            Q = deque([(sr, sc)])
            while Q:
                r, c = Q.popleft()
                steps = cheat_dist[r, c]
                if steps == 20:
                    continue
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in cheat_dist:
                        cheat_dist[nr, nc] = steps + 1
                        Q.append((nr, nc))
            for r in range(R):
                for c in range(C):
                    steps = cheat_dist.get((r, c))
                    if steps is not None and is_open(r, c):
                        d_e = dist_to_E.get((r, c))
                        if d_e is not None:
                            if saved := time - (dist_from_S[sr, sc] + steps + d_e):
                                key = ((sr, sc), (r, c))
                                best_cheats[key] = max(best_cheats.get(key, 0), saved)
    return p1, sum(s >= 100 for s in best_cheats.values())

print(*solve())
