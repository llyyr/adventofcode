#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")
inp = open(filename).read().strip().splitlines()
target, start = ((r, c) for r, l in enumerate(inp) for c, ch in enumerate(l) if ch in "SE")
DIRS = [RIGHT, DOWN, LEFT, UP]

def solve():
    Q = [(0, (0, *start), (0, 0, 0))]
    visited = {}
    backtrack = {(0, *start): []}

    while Q:
        s, node, last = heapq.heappop(Q)
        if node not in visited:
            visited[node] = s
            if last != (0, 0, 0):
                backtrack[node] = [last]

            (d, r, c) = node
            if (r, c) == target:
                break

            dr, dc = DIRS[d]
            rr, cc = r + dr, c + dc
            if inp[rr][cc] != "#":
                heapq.heappush(Q, (s + 1, (d, rr, cc), node))

            for i in (-1, 1):
                heapq.heappush(Q, (s + 1000, ((d+i)%4, r, c), node))
        elif s == visited[node]:
            backtrack[node].append(last)

    points = set()
    nodes = [(d, r, c) for d, r, c in backtrack if (r, c) == target]
    while nodes:
        node = nodes.pop()
        points.add((node[1:]))
        nodes.extend(backtrack[node])
    return visited[(0, *target)], len(points)

print(*solve())
