#!/usr/bin/env python3.11


from collections import deque


G, dist = [], []
for r, line in enumerate(open('12.txt')):
    row = []
    for c, char in enumerate(line):
        if char == 'S':
            char = 'a'
            start = (r, c)
        elif char == 'E':
            char = 'z'
            end = (r, c)
        row.append(ord(char) - ord('a'))
    G.append(row)
    dist.append([1e5 for _ in range(len(row))])

R = len(G)
C = len(G[0])

def solve(part2=False):
    Q = deque([start])
    dist[start[0]][start[1]] = 0
    if part2:
        for r in range(R):
            for c in range(C):
                if G[r][c] == 0:
                    Q.append((r, c))
                    dist[r][c] = 0
    while Q:
        r, c = Q.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            rr, cc = r + dr, c + dc
            if 0<=rr<R and 0<=cc<C and G[rr][cc]<=1+G[r][c]:
                if dist[r][c]+1 < dist[rr][cc]:
                    dist[rr][cc] = min(dist[rr][cc], dist[r][c]+1)
                    Q.append((rr, cc))

    return dist[end[0]][end[1]]

print(*map(solve, (False, True)))
