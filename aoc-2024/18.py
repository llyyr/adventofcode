#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")
inp = [tuple(int(i) for i in l.split(",")) for l in open(filename)]

def find(B, S=70):
    r, c, seen = 0, 0, set()
    Q, dist = [(0, r, c)], defaultdict(lambda: (math.inf, (r, c)))
    while Q:
        d, r, c = heapq.heappop(Q)
        if r == c == S: break
        for dr, dc in DIRS:
            rr, cc = r + dr, c + dc
            if 0 <= rr <= S and 0 <= cc <= S and (rr, cc) not in B\
                and d+1 < dist[rr, cc][0]:
                    dist[rr, cc] = (d+1, (r, c))
                    heapq.heappush(Q, (d+1, rr, cc))
    while seen.add((r, c)) or (r and c): r, c = dist[r, c][1]
    return dist[S, S][0], seen

def solve():
    B = set(inp[:1024])
    d, seen = find(B)
    print(d)
    for r, c in inp[1024:]:
        B.add((r, c))
        if (r, c) in seen:
            d, seen = find(B)
            if d == math.inf: return print(r, c, sep=",")
solve()
