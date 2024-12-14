#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")
inp = [ints(x) for x in open(filename).read().splitlines()]
X, Y = 101, 103

def make_grid(inp, X, Y):
    G = [[" " for _ in range(X)] for _ in range(Y)]
    for px, py, *_ in inp:
        G[py][px] = BLOCK
    return "\n".join("".join(row) for row in G)

def update_positions(inp, step, X, Y):
    g = defaultdict(int)
    for i, (px, py, vx, vy) in enumerate(inp):
        px, py = (px + vx * step) % X, (py + vy * step) % Y
        inp[i] = (px, py, vx, vy)
        g[px, py] += 1
    return g

def quadrant_score(g, w, h):
    yield sum(g[x, y] for y in range(h) for x in range(w))
    yield sum(g[x, y] for y in range(h) for x in range(w + 1, X))
    yield sum(g[x, y] for y in range(h + 1, Y) for x in range(w))
    yield sum(g[x, y] for y in range(h + 1, Y) for x in range(w + 1, X))

def solve(inp):
    ITERS = 100
    g = update_positions(inp, ITERS, X, Y)
    print(math.prod(quadrant_score(g, X//2, Y//2)))
    while ITERS := ITERS + 1:
        update_positions(inp, 1, X, Y)
        ret = make_grid(inp, X, Y)
        if ret.count(BLOCK) == 500:
            print(ret)
            print(ITERS)
            break

solve(inp)
