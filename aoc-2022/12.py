#!/usr/bin/env python3.11

from collections import deque, defaultdict

inp = [l.rstrip() for l in open('12.txt')]
R, C = len(inp), len(inp[0])
starts, G, dist = [], {}, defaultdict(lambda: 1e5)

for r, line in enumerate(inp):
    for c, char in enumerate(line):
        if char == 'S':
            char = 'a'
            start = (r, c)
        elif char == 'E':
            char = 'z'
            end = (r, c)
        if char == 'a':
            dist[r, c] = 0
            starts.append((r, c))
        G[r, c] = ord(char) - ord('a')

def solve(start):
    Q = deque([l for l in start])
    while Q:
        r, c = Q.popleft()
        for nr, nc in ((r, c+1), (r, c-1), (r+1, c), (r-1, c)):
            if 0 <= nr < R and 0 <= nc < C and G[nr, nc] <= 1+G[r, c]:
                if dist[r, c]+1 < dist[nr, nc]:
                    dist[nr, nc] = min(dist[nr, nc], 1+dist[r, c])
                    Q.append((nr, nc))
    return dist[end]

print(*map(solve, ([start], starts)))
