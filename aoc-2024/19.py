#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")
Ps, Ds = map(str.split, open(filename).read().strip().split("\n\n"), [", ", "\n"])

@cache
def Bs(D): return not D or sum(Bs(D[len(P):]) for P in Ps if D.startswith(P))
print(sum(Bs(D) > 0 for D in Ds), sum(Bs(D) for D in Ds))

