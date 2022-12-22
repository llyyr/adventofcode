#!/usr/bin/env python3.11

from aochelper import *

G, insts = open('22.txt').read().split('\n\n')
G = G.splitlines()
R = len(G)
C = lambda c: len(G[c])
insts = [''.join(v) for _, v in itertools.groupby(insts.strip(), str.isdigit)]

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
FACEMAP = {'L': -1, 'R': 1}

portal = {}
for i in range(50):
    portal[(0, 50 + i, 3)] = (150 + i, 0, 0)
    portal[(150 + i, 0, 2)] = (0, 50 + i, 1)

    portal[(150 - 1, 50 + i, 1)] = (150 + i, 50 - 1, 2)
    portal[(150 + i, 50 - 1, 0)] = (150 - 1, 50 + i, 3)

    portal[(0, 100 + i, 3)] = (200 - 1, 0 + i, 3)
    portal[(200 - 1, 0 + i, 1)] = (0, 100 + i, 1)

    portal[(50 - 1, 100 + i, 1)] = (50 + i, 100 - 1, 2)
    portal[(50 + i, 100 - 1, 0)] = (50 - 1, 100 + i, 3)

    portal[(0 + i, 150 - 1, 0)] = (150 - 1 - i, 100 - 1, 2)
    portal[(100 + i, 100 - 1, 0)] = (50 - 1 - i, 150 - 1, 2)

    portal[(50 + i, 50, 2)] = (100, 0 + i, 1)
    portal[(100, 0 + i, 3)] = (50 + i, 50, 0)

    portal[(0 + i, 50, 2)] = (150 - 1 - i, 0, 0)
    portal[(100 + i, 0, 2)] = (50 - 1 - i, 50, 0)

def solve(part):
    facing, r, c = 0, 0, 0
    while G[r][c] == ' ':
        c += 1
    for inst in insts:
        if inst in FACEMAP:
            facing = (facing + FACEMAP[inst]) % 4
        else:
            dr, dc = DIRS[facing]
            for _ in range(int(inst)):
                rr, cc = r + dr, c + dc
                if not 0 <= rr < R or not 0 <= cc < C(rr) or G[rr][cc] == ' ':
                    if part == 1:
                        rr, cc = r, c
                        drr, dcc = r - dr, c - dc
                        while 0 <= drr < R and 0 <= dcc < C(drr) and G[drr][dcc] != ' ':
                            rr, cc = drr, dcc
                            drr -= dr
                            dcc -= dc
                    elif part == 2:
                        rr, cc, newface = portal[(r, c, facing)]
                        if G[rr][cc] == '#':
                            break
                        facing = newface
                        dr, dc = DIRS[newface]
                if G[rr][cc] == '#':
                    break
                r, c = rr, cc
    return 1000 * (r + 1) + 4 * (c + 1) + facing

print(*map(solve, (1, 2)))

