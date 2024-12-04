#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")
inp = {(r, c): ch for r, l in enumerate(open(filename)) for c, ch in enumerate(l)}

def solve(r, c, part):
    Cs = []
    if part == 1:
        for i in range(4):
            Cs.append(((r+i, c), (r, c+i), (r+i, c+i), (r-i, c+i)))
    elif part == 2:
        for i in range(3):
            Cs.append(((r-1+i, c-1+i), (r+1-i, c-1+i)))
    return map(lambda C: "".join(inp.get(c, ".") for c in C), zip(*Cs))

print(sum(sum(ch in ("XMAS", "SAMX") for ch in solve(r, c, 1)) for r, c in inp))
print(sum(all(ch in ("MAS", "SAM") for ch in solve(r, c, 2)) for r, c in inp))
