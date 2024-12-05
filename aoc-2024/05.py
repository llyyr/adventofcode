#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")
Rs, Ps = open(filename).read().split("\n\n")

ans = [0, 0]
R = {tuple(r.split("|")) for r in Rs.split()}
for p in [p.split(",") for p in Ps.split()]:
    np = sorted(p, key=cmp_to_key(lambda a, b: ((b, a) in R) - ((a, b) in R)))
    ans[p!=np] += int(np[len(p)//2])
print(*ans)
