#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace('py', 'txt')
Xs, Ys = (list(c) for c in zip(*(map(int, line.split()) for line in open(filename))))
Xs.sort()
Ys.sort()
print(sum(abs(x - y) for x, y in zip(Xs, Ys)))

C = Counter(Ys)
print(sum(x * C[x] for x in Xs))
