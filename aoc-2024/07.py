#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")
inp = [ints(l) for l in open(filename)]

def is_valid(S, T, Vs, P):
    C = [S]
    for v in reversed(Vs):
        C2 = []
        for n in C:
            if (V := n - v) >= T:
                C2.append(V)
            if n % v == 0 and (V := n // v) >= T:
                C2.append(V)
            if P == 2 and n > v and n % (D := 10 ** len(str(v))) == v:
                C2.append(n // D)
        C = C2
    return T in C

print(*(sum(S * is_valid(S, T, Vs, P) for S, T, *Vs in inp) for P in (1, 2)))
