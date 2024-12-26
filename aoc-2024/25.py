#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")
Gs = open(filename).read().strip().split("\n\n")
Ks, Ls = [], []

for G in Gs:
    G, R, C = grid2dict(G.splitlines())
    K = G[(0, 0)] == '.'
    (Ks if K else Ls).append(
        [next(r for r in range(R)
            if G[((R - r - 1 if K else r), c)] == '.') for c in range(C)])

print(sum(all(k[i] + l[i] <= 7 for i in range(len(l))) for k in Ks for l in Ls))
