#!/usr/bin/env python3.10
import heapq as hq

def solve(risk, tiles):
    if tiles > 1:
        risk = [[0]*len(r)*tiles for r in inp*tiles]
        R = len(inp)
        C = len(inp[0])
        for r in range(len(risk)):
            for c in range(len(risk[r])):
                risk[r][c] = (inp[r%R][c%C] + r//R + c//C - 1) % 9 + 1
    Q = [(0, 0, 0)]
    visited = [[False]*len(r) for r in risk]
    while Q:
        cost, r, c = hq.heappop(Q)
        if visited[r][c]:
            continue
        if (r+1, c+1) == (len(risk), len(risk[r])):
            return cost
        visited[r][c] = True
        for rr, cc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if len(risk)>rr>=0<=cc<len(risk[0]) and not visited[rr][cc]:
                hq.heappush(Q, (cost + risk[rr][cc], rr, cc))

inp = [list(map(int, l.strip())) for l in open(0)]
print(solve(inp, 1))
print(solve(inp, 5))
