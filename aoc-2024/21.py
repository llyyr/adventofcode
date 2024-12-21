#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")
inp = open(filename).read().strip().split()
pad = {ch: (i % 3, i // 3) for i, ch in enumerate("789456123 0A")}
dir = {ch: (i % 3, i // 3) for i, ch in enumerate(" ^A<v>")}

def bfs(G, seq, inc):
    steps = {}
    (ax, ay), (bx, by) = G["A"], G[" "]
    for ch in seq:
        tx, ty = G[ch]
        blocked = (tx == bx and ay == by) or (ty == by and ax == bx)
        step = (tx - ax, ty - ay, blocked)
        steps[step] = steps.get(step, 0) + inc
        ax, ay = tx, ty
    return steps

def solve(iters):
    ret = 0
    for code in inp:
        paths = bfs(pad, code, 1)
        for _ in range(iters + 1):
            new_paths = {}
            for (dx, dy, blocked), cnt in paths.items():
                dirs = "<" * -dx + "v" * dy + "^" * -dy + ">" * dx
                dirs = dirs[::-1] if blocked else dirs
                dirs += "A"
                for step, cnt in bfs(dir, dirs, cnt).items():
                    new_paths[step] = new_paths.get(step, 0) + cnt
            paths = new_paths
        ret += sum(paths.values()) * int(code[:3])
    return ret

print(*map(solve, (2, 25)))
