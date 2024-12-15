#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")
inp = open(filename).read().strip().split("\n\n")
DIR = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0), }

def parse(inp):
    G = []
    pos = (0, 0)
    for r, l in enumerate(inp[0].split("\n")):
        row = []
        for c, ch in enumerate(l):
            row.append(ch)
            if ch == "@":
                pos = (r, c)
        G.append(row)
    return G, pos, [m for l in inp[1].split("\n") for m in l]

def move_boxes(G, r, c, moves, DIR):
    for m in moves:
        if cur_boxes := get_boxes(G, m, (r, c), DIR):
            dr, dc = DIR[m]
            for pr, pc in cur_boxes[::-1]:
                if G[pr][pc] == "@":
                    r, c = (r + dr, c + dc)
                G[pr + dr][pc + dc] = G[pr][pc]
                G[pr][pc] = "."
    return G, r, c

def get_boxes(G, m, pos, DIR):
    Q = deque([pos])
    seen = set()
    cur_boxes = []
    dr, dc = DIR[m]
    while Q:
        r, c = Q.popleft()
        if (r, c) in seen:
            continue
        seen.add((r, c))
        if G[r][c] == ".":
            continue
        elif G[r][c] == "#":
            return
        cur_boxes.append((r, c))
        cur_ch = G[r][c]
        if cur_ch == "[" and (r, c + 1) not in seen and m != ">":
            Q.append((r, c + 1))
        elif cur_ch == "]" and (r, c - 1) not in seen and m != "<":
            Q.append((r, c - 1))
        Q.append((r + dr, c + dc))
    return cur_boxes

def solve(get="O"):
    for _ in range(2):
        G, (r, c), moves = parse(inp)
        G, r, c = move_boxes(G, r, c, moves, DIR)
        yield sum(100 * r + c for r, row in enumerate(G) for c, p in enumerate(row) if p == get)
        inp[0] = inp[0].replace('#', '##').replace('.', '..').replace('O', '[]').replace('@', '@.')
        get = "["

print(*solve())
