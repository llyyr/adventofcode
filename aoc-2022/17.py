#!/usr/bin/env python3.11

from aochelper import *

inp = cycle(enumerate(({'>': 1, '<': -1}[c] for c in open('17.txt').read().strip())))
pieces = cycle(enumerate((
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((1, 0), (1, -1), (0, -1), (1, -2), (2, -1)),
    ((0, 0), (1, 0), (2, 0), (2, -1), (2, -2)),
    ((0, 0), (0, -1), (0, -2), (0, -3)),
    ((0, 0), (1, 0), (0, -1), (1, -1)),
    )))
L = int(1e12)
G = set((x, 0) for x in range(7))
H = 0
repeating = False
seen = {}
i = 0
while i < L:
    if i == 2022:
        print(-H)
    piece_idx, piece = next(pieces)
    inst_idx, inst = next(inp)
    W = max(x for x, _ in piece) + 1
    x, y = 2, H - 4
    while True:
        if all((x + dx + inst, y + dy) not in G for dx, dy in piece) and {1: x < 7 - W, -1: x > 0}[inst]:
            x += inst
        if any((x + dx, y + dy + 1) in G for dx, dy in piece):
            G |= {(x+dx, y+dy) for dx, dy in piece}
            break
        y += 1
        inst_idx, inst = next(inp)
    if not repeating:
        for bottom in range(H, -1):
            if all((x, bottom) in G for x in range(7)):
                if (piece_idx, inst_idx) in seen:
                    prev_i, prev_h = seen[(piece_idx, inst_idx)]
                    delta_i = i - prev_i
                    skipped_iters = (L - i) // delta_i
                    i += skipped_iters * delta_i
                    height_diff = prev_h - H
                    H -= skipped_iters * height_diff
                    G = set((x, y - skipped_iters * height_diff) for x, y in G)
                    repeating = True
                seen[(piece_idx, inst_idx)] = i, H
                break
    i += 1
    H = min(y for _, y in G)
print(-H)

