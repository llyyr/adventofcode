#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")
inp = open(filename).read().splitlines()
Cs = defaultdict(set)

for line in inp:
    a, b = line.split('-')
    Cs[a].add(b)
    Cs[b].add(a)

print(sum(any(x[0] == "t" for x in T) for T in
    {frozenset([x, y, z]) for x in Cs for y in Cs[x] for z in Cs[y] if z in Cs[x]}))

@cache
def C(n, s=frozenset()):
    O = Cs[n]
    if s <= O:
        s |= {n}
        return max((C(opt, s) for opt in O - s), key=len, default=s)
    return s

print(','.join(sorted(max((C(n) for n in Cs), key=len, default=frozenset()))))
